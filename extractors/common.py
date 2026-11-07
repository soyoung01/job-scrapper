from requests import get
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def get_soup(url):
    try:
        response = get(url, headers=HEADERS, timeout=15)
    except Exception as error:
        print(f"[요청 실패] {url} : {error}")
        return None
    if response.status_code != 200:
        print(f"[응답 {response.status_code}] {url}")
        return None
    return BeautifulSoup(response.content, "html.parser")


def get_text(parent, selector):
    element = parent.select_one(selector)
    return element.get_text(" ", strip=True) if element else ""


def make_job(title, company, link, source):
    return {
        "title": title,
        "company": company,
        "link": link,
        "source": source,
    }
