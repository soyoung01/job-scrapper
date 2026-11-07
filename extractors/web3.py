from urllib.parse import quote
from extractors.common import get_soup, get_text, make_job

SOURCE = "web3.career"
BASE_URL = "https://web3.career"


def extract_web3_jobs(keyword):
    url = f"{BASE_URL}/{quote(keyword, safe='')}-jobs"
    soup = get_soup(url)
    if soup is None:
        return []

    jobs = []
    for row in soup.select("tbody tr"):
        title_tag = row.select_one("h2")
        if not title_tag:
            continue

        link_tag = title_tag.find_parent("a") or row.select_one("a[href]")
        href = link_tag.get("href", "") if link_tag else ""
        link = href if href.startswith("http") else BASE_URL + href

        jobs.append(
            make_job(
                title=title_tag.get_text(strip=True),
                company=get_text(row, "h3"),
                link=link,
                source=SOURCE,
            )
        )

    print(f"{SOURCE}: {len(jobs)}개")
    return jobs


if __name__ == "__main__":
    for job in extract_web3_jobs("python"):
        print(job)
