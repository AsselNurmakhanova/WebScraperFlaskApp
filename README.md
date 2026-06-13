# WebScraper Flask App
## Project implementation stages
### Stages
1. Provide URL address of article webpage
2. Send the request to provided URL address
3. If status code is OK, fetch article name
4. If status code is OK, fetch article from requested webpage
5. For all fetched articles, parse them to extract relevant data
6. Save obtained article
7. Create a Flask application
8. Load saved JSON data in Flask application
9. Create a route to display fetched articles
10. Render article data using HTML template
11. Run Flask server and verify that scraped data is displayed correctly
## Project inputs
### Product codes
- 2026/06/cybersecurity-stars-awards-2026-winners.html
- 2026/06/threatsday-bulletin-worm-code-leaked-ai.html
- 2026/05/before-whistle-ctm360-reveals-how.html
- 2026/05/kimsuky-deploys-httpspy-expands-arsenal.html
- 2026/05/3-soc-steps-that-shut-down-incident.html

### Article structure
|component|name|selector|
|---------|----|--------|
|title|title|#app > div > h1 > a|
|author|author|#app > div > div.postmeta > span.p-author > span:nth-child(2)|
|publication date|pub-date|'(meta[itemprop="datePublished"]')["content"]'|
|modification date|mod-date|'(meta[itemprop="dateModified"]')["content"]'|
|tags|tags|#app > div > div.postmeta > span.p-tags|
|body|body|#articlebody|
