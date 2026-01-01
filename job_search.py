import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

queries = [
    "Assistant Manager Supply Chain Manufacturing 2-3 years India",
    "Supply Chain Planner SAP MM 2-3 years India",
    "Procurement P2P SAP 2-3 years Manufacturing India",
    "Operations Planning Utilities 2-3 years India"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

jobs = []

for query in queries:
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&ibp=htl;jobs"
    response = requests.get(url, headers=HEADERS, timeout=20)
    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.select("a"):
        link = a.get("href", "")
        text = a.get_text(strip=True)

        if any(site in link for site in ["naukri.com", "linkedin.com/jobs", "indeed.com"]):
            jobs.append(
                f"""
{text}
Apply 👉 {link}
----------------------------------
"""
            )

if not jobs:
    jobs.append("No matching Supply Chain jobs found today for 2–3 years experience.")

body = "\n".join(jobs)

msg = MIMEText(body)
msg["Subject"] = "Daily Supply Chain Jobs (2–3 yrs | Resume-Matched)"
msg["From"] = GMAIL_USER
msg["To"] = GMAIL_USER

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
server.sendmail(GMAIL_USER, GMAIL_USER, msg.as_string())
server.quit()
