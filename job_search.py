import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

jobs = [
    "Assistant Manager – Supply Chain | Manufacturing | ₹12 LPA | Tata Group",
    "Assistant Manager – SCM | Oil & Gas | ₹14 LPA | Reliance",
    "Assistant Manager – Planning | Manufacturing | ₹13 LPA | Adani"
]

body = "\n".join(jobs)

msg = MIMEMultipart()
msg["From"] = GMAIL_USER
msg["To"] = GMAIL_USER
msg["Subject"] = "Daily Supply Chain Job Alerts (₹11.5 LPA+)"

msg.attach(MIMEText(body, "plain"))

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
server.send_message(msg)
server.quit()
