from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from m import send_email

app = Flask(__name__)
website_status = "unknown"

def check_website_status():
    global website_status
    website_url = "http://127.0.0.1:5000/app"  # Replace with the URL you want to check
    try:
        response = requests.get(website_url)
        if response.status_code == 200:
            website_status = "up"
        else:
            website_status = "down"
            subject = "Website Down"
            message = "The website is down. Please check."
            send_email("pubgaccno9@gmail.com", "jswqgmwpcmfqsorc", "akasshkrishnan1811@gmail.com", subject, message)
    except requests.exceptions.RequestException:
        website_status = "error"
        subject = "Website Check Error"
        message = "An error occurred while checking the website."
        send_email("pubgaccno9@gmail.com", "jswqgmwpcmfqsorc", "akasshkrishnan1811@gmail.com", subject, message)

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(check_website_status, 'interval', minutes=1)
scheduler.start()

@app.route("/", methods=["GET"])
def index():
    global website_status
    website_status_text = ""

    if website_status == "up":
        website_status_text = "Website is up and running"
    elif website_status == "down":
        website_status_text = "Website is down"
    elif website_status == "error":
        website_status_text = "An error occurred while checking the website"
    else:
        website_status_text = "Website status is unknown"

    return render_template("index.html", website_status_text=website_status_text)

if __name__ == "_main_":
    app.run(debug=True)



#send_email("pubgaccno9@gmail.com", "jswqgmwpcmfqsorc", "akasshkrishnan1811@gmail.com", subject, message)