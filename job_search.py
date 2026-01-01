import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

QUERY = "Assistant Manager Supply Chain Manufacturing 2-3 years India"
URL = f"https://www.google.com/search?q={QUERY.replace(' ', '+')}&ibp=htl;jobs"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []

for a in soup.select("a"):
    link = a.get("href", "")
    text = a.get_text(strip=True)

    if ("naukri.com" in link or "linkedin.com/jobs" in link or "indeed.com" in link):
        jobs.append(f"{text}\nApply 👉 {link}\n----------------------")

if not jobs:
    jobs.append("No matching jobs found today.")

body = "\n".join(jobs)

msg = MIMEText(body)
msg["Subject"] = "Daily Supply Chain Jobs (2–3 yrs) – Apply Links"
msg["From"] = GMAIL_USER
msg["To"] = GMAIL_USER

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
server.sendmail(GMAIL_USER, GMAIL_USER, msg.as_string())
server.quit()

