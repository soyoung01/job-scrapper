from extractors.berlin import extract_berlin_jobs, SOURCE as BERLIN_SOURCE
from extractors.wwr import extract_wwr_jobs, SOURCE as WWR_SOURCE
from extractors.web3 import extract_web3_jobs, SOURCE as WEB3_SOURCE

SCRAPPERS = [extract_berlin_jobs, extract_wwr_jobs, extract_web3_jobs]
SOURCES = [BERLIN_SOURCE, WWR_SOURCE, WEB3_SOURCE]


def extract_all_jobs(keyword):
    all_jobs = []
    for scrapper in SCRAPPERS:
        try:
            all_jobs += scrapper(keyword)
        except Exception as error:
            print(f"[{scrapper.__name__} 실패] {error}")
    return all_jobs
