import smtplib
import os
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
EMAIL_TO = "vamsidevarapalli2002@gmail.com"


def fetch_jobs():
    search_urls = [
        "https://www.naukri.com/mechanical-engineer-supply-chain-jobs",
        "https://www.naukri.com/supply-chain-mechanical-jobs",
        "https://www.naukri.com/procurement-mechanical-jobs",
        "https://www.naukri.com/assistant-manager-supply-chain-jobs",
        "https://www.naukri.com/production-planning-mechanical-jobs"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    jobs = []

    for url in search_urls:
        try:
            response = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.text, "html.parser")

            for job in soup.select(".title"):
                title = job.text.strip()
                title_lower = title.lower()

                if any(keyword in title_lower for keyword in [
                    "mechanical",
                    "supply chain",
                    "procurement",
                    "planning",
                    "planner",
                    "assistant manager",
                    "engineer"
                ]):
                    jobs.append(title)

        except Exception as e:
            continue

    return list(set(jobs))[:30]  # top 30 unique jobs


def send_email(jobs):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = "Mechanical & Supply Chain Jobs (2+ Years Experience)"

    body = "Latest Mechanical / Supply Chain jobs (Experience > 2 years):\n\n"

    for idx, job in enumerate(jobs, 1):
        body += f"{idx}. {job}\n"

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASS)
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    job_list = fetch_jobs()

    if job_list:
        send_email(job_list)


