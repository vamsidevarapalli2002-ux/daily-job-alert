import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

raw_jobs = [
    "Assistant Manager – Supply Chain | Manufacturing | 2-3 years | ₹12 LPA | Tata Group",
    "Assistant Manager – SCM | Oil & Gas | 5 years | ₹14 LPA | Reliance",
    "Assistant Manager – Planning | Manufacturing | 2+ years | ₹13 LPA | Adani",
    "Assistant Manager – Logistics | Manufacturing | 1 year | ₹10 LPA | ABC Ltd"
]

experience_keywords = [
    "2 years", "3 years", "2-3 years", "2+ years", "3+ years"
]

jobs = []
for job in raw_jobs:
    if any(exp in job.lower() for exp in experience_keywords):
        jobs.append(job)

if not jobs:
    jobs.append("No matching jobs found for 2–3 years experience today.")

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
