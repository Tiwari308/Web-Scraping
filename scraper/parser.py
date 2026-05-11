from bs4 import BeautifulSoup

def parse_jobs(html):
    soup = BeautifulSoup(html, "html.parser")
    jobs = []

    for job in soup.select(".job-card"):
        jobs.append({
            "title": job.select_one(".job-title").get_text(strip=True),
            "company": job.select_one(".company").get_text(strip=True),
            "location": job.select_one(".location").get_text(strip=True),
            "posted_date": job.select_one(".date").get_text(strip=True)
        })

    return jobs

