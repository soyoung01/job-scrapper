from urllib.parse import quote
from extractors.common import get_soup, get_text, make_job

SOURCE = "Berlin Startup Jobs"


def extract_berlin_jobs(keyword):
    url = f"https://berlinstartupjobs.com/skill-areas/{quote(keyword, safe='')}/"
    soup = get_soup(url)
    if soup is None:
        return []

    jobs = []
    for job in soup.select("li.bjs-jlid"):
        title_tag = job.select_one("h4.bjs-jlid__h a")
        if not title_tag:
            continue
        jobs.append(
            make_job(
                title=title_tag.get_text(strip=True),
                company=get_text(job, "a.bjs-jlid__b"),
                link=title_tag.get("href", ""),
                source=SOURCE,
            )
        )
    print(f"{SOURCE}: {len(jobs)}개")
    return jobs


if __name__ == "__main__":
    for job in extract_berlin_jobs("python"):
        print(job)
