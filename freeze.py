import warnings
from flask_frozen import Freezer, MissingURLGeneratorWarning
from main import app, KEYWORDS

warnings.filterwarnings("ignore", category=MissingURLGeneratorWarning)

app.config["STATIC_MODE"] = True

app.config["FREEZER_RELATIVE_URLS"] = True
app.config["FREEZER_DESTINATION"] = "build"

freezer = Freezer(app, with_no_argument_rules=False, log_url_for=True)


@freezer.register_generator
def home():
    yield {}


@freezer.register_generator
def search():
    for keyword in KEYWORDS:
        yield {"keyword": keyword}


if __name__ == "__main__":
    urls = freezer.freeze()
    print(f"\n{len(urls)}개 페이지 생성 완료 → build/")
