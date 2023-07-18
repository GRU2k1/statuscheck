import psutil
import smtplib
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    # Check if the other application is running.
    if not psutil.process_exists("other_application_name"):
        # Send an email.
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("your_email@gmail.com", "your_password")
            smtp.sendmail("your_email@gmail.com", "recipient_email@gmail.com", "Subject: Other application not running\n\nOther application is not running.")
    # Display a message on the webpage.
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
