import os
import json
from flask import Flask, render_template
from datetime import datetime
from news_scraper import safe_name
app = Flask(__name__)
def load_articles():
    path = os.path.join("articles", f"{safe_name}.json")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
@app.route("/")
def home():
    article = load_articles()
    return render_template("index.html", articles=article)
@app.template_filter("pretty_date") # I wanted to prettify dates
def pretty_date(value):
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return dt.strftime("%d %B %Y, %H:%M")
if __name__ == "__main__":
    app.run()