import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_appspassword, receiver_email, subject, message):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"  # For Gmail
    smtp_port = 587  # For Gmail

    try:
        # Create a multipart message
        email_message = MIMEMultipart()
        email_message["From"] = sender_email
        email_message["To"] = receiver_email
        email_message["Subject"] = subject

        # Add the message body
        email_message.attach(MIMEText(message, "plain"))

        # Create SMTP session for sending the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS for security
            server.starttls()
            # Log in to your email account
            server.login(sender_email, sender_appspassword)
            # Send email
            server.sendmail(sender_email, receiver_email, email_message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))


# details
sender_email = "pubgaccno9@gmail.com"
sender_appspassword = "jswqgmwpcmfqsorc" #use app password here to connect to gmail
receiver_email = "gurucharan20182019@gmail.com"
subject = "Application error"
message = "An error has occured in the application Error code:"

send_email(sender_email, sender_appspassword, receiver_email, subject, message)

