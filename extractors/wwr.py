from urllib.parse import quote
from extractors.common import get_soup, get_text, make_job

SOURCE = "We Work Remotely"
BASE_URL = "https://weworkremotely.com"


def extract_wwr_jobs(keyword):
    url = f"{BASE_URL}/remote-jobs/search?utf8=%E2%9C%93&term={quote(keyword)}"
    soup = get_soup(url)
    if soup is None:
        return []

    jobs = []
    for job in soup.select("section.jobs li"):
        title = get_text(job, "span.new-listing__header__title__text") or get_text(
            job, "span.title"
        )
        if not title:
            continue

        link_tag = job.select_one('a[href^="/remote-jobs/"]')
        link = BASE_URL + link_tag["href"] if link_tag else ""

        company = get_text(job, "p.new-listing__company-name") or get_text(
            job, "span.company"
        )

        jobs.append(make_job(title, company, link, SOURCE))

    print(f"{SOURCE}: {len(jobs)}개")
    return jobs


if __name__ == "__main__":
    for job in extract_wwr_jobs("python"):
        print(job)
