from pathlib import Path

html = Path("_site/index.html").read_text(encoding="utf-8")
start = html.find('<h2 id="news">')
if start < 0:
    start = html.find("id=\"news\"")
print("start", start)
print(html[start : start + 4500])
