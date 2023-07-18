import schedule
import time
import requests
import smtplib
from email.mime.text import MIMEText
#from flask import Flask, render_template

#app = Flask(__name__)

def send_email(subject, body):
    # Email configuration
    sender_email = 'pubgaccno9@gmail.com'
    sender_password = 'jswqgmwpcmfqsorc'
    recipient_email = 'gurucharan20182019@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a MIMEText object
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    # Connect to the SMTP server and send the email
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
    url = 'http://www.google.com'
    # Replace with the URL of your web application
    # Send a GET request to the URL
    response = requests.get(url)
    # Check the status code
    status_code = response.status_code
    # Check if the status code indicates an error
    if status_code >= 400:
        error_message = f'The web application returned an error (Status code: {status_code})'
        send_email('Web Application Error', error_message)

#@app.route("/status")
#def status():
    # Get the status of the web application
#    status = check_web_app_status()
    # Render the status page with the status code
#    return render_template('status.html', status=status)

if __name__ == "__main__":
    # Schedule the script to run every 1 minute
    schedule.every(1).minutes.do(check_web_app_status)
    #app.run(debug=True, port=8000)

    while True:
        # Run the scheduler
        schedule.run_pending()
        # Sleep for 1 second
        time.sleep(1)