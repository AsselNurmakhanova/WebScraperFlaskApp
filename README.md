# WebScraper Flask App
## Project implementation stages
### Stages
1. Provide URL address of article webpage
2. Send the request to provided URL address
3. If status code is OK, fetch article name
4. If status code is OK, fetch all opinions from requested webpage
5. For all fetched opinions, parse them to extract relevant data
6. Check if there is next page with opinions
7. For all remaining pages repeat steps 2-5
8. Save obtained opinions
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
|publication date|pub-date|#Blog1 > div > div > div > meta:nth-child(4)|
|modification date|mod-date|#Blog1 > div > div > div > meta:nth-child(5)|
|tags|tags|#app > div > div.postmeta > span.p-tags|
|body|body|#articlebody|
