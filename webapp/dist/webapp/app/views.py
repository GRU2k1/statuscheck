from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import schedule
import time
import requests
import smtplib
from email.mime.text import MIMEText
from .config import SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, SMTP_SERVER, SMTP_PORT, WEB_APP_URL,CC

# Create your views here.

def send_email(subject, body):
    # Email configuration
    sender_email = SENDER_EMAIL
    sender_password = SENDER_PASSWORD
    recipient_email = RECIPIENT_EMAIL
    cc_emails = CC.split(',') if CC else []  # Split CC addresses if provided, else empty list
    smtp_server = SMTP_SERVER
    smtp_port = SMTP_PORT
    
    # Create a MIMEText object
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Cc'] = ', '.join(cc_emails)  # Set the CC header
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email. Error: {str(e)}')
    finally:
        server.quit()

def check_web_app_status():
    # Example URL to check the status
    url = WEB_APP_URL
    response = requests.get(url)
    # Replace with the URL of your web application
    status_code = response.status_code
    if status_code >= 400:
        error_message = f'The web application returned an error (Status code: {status_code})' 
        #retrive the ip address
        #ip_address = request.META.get('REMOTE_ADDR')
        #modify the error msg
        #error_message += f'\n\nIP Address: {ip_address}'
        send_email('Web Application Error', error_message)

def schedule_task():
    # Schedule the task to run every 1 minute
    schedule.every(1).minutes.do(check_web_app_status)

    while True:
        # Run the scheduler
        schedule.run_pending()
        # Sleep for 1 second
        time.sleep(1)

def page(request):
    # Call the check_web_app_status function
    check_web_app_status()
    #schedule_task(request)
    ip_address = request.META.get('REMOTE_ADDR')
    # Render the page.html template
    return render(request, 'webapp/page.html', {'WEB_APP_URL': WEB_APP_URL})