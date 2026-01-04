def fetch_jobs():
    search_urls = [
        "https://www.naukri.com/mechanical-engineer-supply-chain-jobs",
        "https://www.naukri.com/supply-chain-mechanical-jobs",
        "https://www.naukri.com/procurement-mechanical-jobs",
        "https://www.naukri.com/production-planning-mechanical-jobs"
    ]

    headers = {"User-Agent": "Mozilla/5.0"}
    jobs = []

    for url in search_urls:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        for job in soup.select(".title"):
            title = job.text.strip().lower()

            # keyword filter
            if any(k in title for k in [
                "supply chain",
                "procurement",
                "planner",
                "planning",
                "assistant manager",
                "engineer",
                "mechanical"
            ]):
                jobs.append(job.text.strip())

    return list(set(jobs))[:20]  # top 20 unique jobs

