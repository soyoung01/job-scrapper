from flask import Flask, Response, redirect, render_template, request, url_for
from extractors import extract_all_jobs, SOURCES
from file import make_csv

app = Flask(__name__)

KEYWORDS = ["python", "javascript", "java"]

db = {}


def get_jobs(keyword):
    keyword = keyword.strip().lower()
    if keyword in db:
        return db[keyword]
    jobs = extract_all_jobs(keyword)
    if jobs:
        db[keyword] = jobs
    return jobs


@app.route("/")
def home():
    return render_template(
        "home.html",
        keywords=KEYWORDS,
        static_mode=app.config.get("STATIC_MODE", False),
    )


@app.route("/search/<keyword>/")
def search(keyword):
    jobs = get_jobs(keyword)
    counts = {source: 0 for source in SOURCES}
    for job in jobs:
        counts[job["source"]] += 1
    return render_template("search.html", keyword=keyword, jobs=jobs, counts=counts)


@app.route("/export/<keyword>.csv")
def export(keyword):
    return Response(make_csv(get_jobs(keyword)), mimetype="text/csv")


# Flask에서 사용 가능
@app.route("/search")
def search_query():
    keyword = request.args.get("keyword", "").strip()
    if not keyword:
        return redirect(url_for("home"))
    return redirect(url_for("search", keyword=keyword))


if __name__ == "__main__":
    app.run(debug=True)
