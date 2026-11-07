# Job Scrapper

Flask로 만든 잡 스크래퍼.

- [berlinstartupjobs.com](https://berlinstartupjobs.com)
- [weworkremotely.com](https://weworkremotely.com)
- [web3.career](https://web3.career)

## 구조

```
main.py            Flask 앱 (/, /search/<keyword>/)
freeze.py          Frozen-Flask로 정적 HTML 생성 → build/
extractors/        사이트별 스크래퍼 (모두 같은 형태의 dict 반환)
templates/         home.html, search.html
```

## 실행

```bash
pip install -r requirements.txt

# 1) 로컬 Flask 서버
python main.py                      # http://localhost:5000

# 2) 정적 사이트 생성
python freeze.py
python -m http.server -d build      # http://localhost:8000

# 3) GitHub Pages 배포
ghp-import -n -p -f build
```
