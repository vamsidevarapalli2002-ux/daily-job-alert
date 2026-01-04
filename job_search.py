import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

print("Job search script started")

EMAIL = os.environ.get("EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

msg = MIMEMultipart()
msg["From"] = EMAIL
msg["To"] = EMAIL
msg["Subject"] = "TEST EMAIL – Job Alert Working"

body = """
Hello Vamsi,

✅ Your GitHub Actions job automation is now WORKING.

Next steps:
- Add real job search logic
- Filter mechanical + supply chain roles
- Experience > 2 years
- Daily 12 PM IST emails

Regards,
Job Alert Bot
"""

msg.attach(MIMEText(body, "plain"))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)

print("Email sent successfully")
