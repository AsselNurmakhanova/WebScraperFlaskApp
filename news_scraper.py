import os
import re
import json
import requests
from dateutil.parser import isoparse
from datetime import timezone
from bs4 import BeautifulSoup
article_code = "2026/06/cybersecurity-stars-awards-2026-winners.html"
url = f"https://thehackernews.com/{article_code}"
response = requests.get(url)
print(response.status_code)
page_dom = BeautifulSoup(response.text, 'html.parser')
print(type(page_dom))
article_name = page_dom.select_one("#app > div > h1 > a").get_text()
print(article_name)
article = page_dom.select("#app > div")
print(type(article))
print(len(article))
whole_article = []
for ar in article:
    single_article = {
        'title': ar.select_one('h1 > a').text.strip(),
        'author': ar.select_one("div.postmeta > span.p-author > span:nth-child(2)").text.strip(),
        'pub_date': isoparse(ar.select_one('meta[itemprop="datePublished"]')["content"]).astimezone(timezone.utc).isoformat(),
        'mod_date': isoparse(ar.select_one('meta[itemprop="dateModified"]')["content"]).astimezone(timezone.utc).isoformat(),
        'tags': ar.select_one("div.postmeta > span.p-tags").text.strip(), 
        'body': ar.select_one("#articlebody").text.strip()
    }
    whole_article.append(single_article)
if not os.path.exists("./articles"):
    os.mkdir("./articles")
safe_name = re.sub(r'[\\/*?:"<>|]', '', article_name).strip().replace(' ', '_')
fname = os.path.join("articles", f"{safe_name}.json")
json_text = json.dumps(whole_article, indent=4, ensure_ascii=False)
with open(fname, "w", encoding="utf-8") as jf:
    jf.write(json_text)