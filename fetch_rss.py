import feedparser
from rss_feeds import RSS_FEEDS
from datetime import datetime
import os

OUTPUT_FILE = "output/index.html"
TEMPLATE_FILE = "templates/index_template.html"

def fetch_articles():
    all_articles = {}
    for category, urls in RSS_FEEDS.items():
        all_articles[category] = []
        for url in urls:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:  # récupérer les 5 derniers articles
                all_articles[category].append({
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.get("published", ""),
                    "summary": entry.get("summary", "")
                })
    return all_articles

def generate_html(articles):
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    content = ""
    for category, items in articles.items():
        content += f"<h2>{category.capitalize()}</h2>\n<ul>\n"
        for item in items:
            content += f'<li><a href="{item["link"]}" target="_blank">{item["title"]}</a> - {item["published"]}</li>\n'
        content += "</ul>\n"

    html_output = template.replace("{{CONTENT}}", content)
    html_output = html_output.replace("{{LAST_UPDATE}}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_output)

if __name__ == "__main__":
    articles = fetch_articles()
    generate_html(articles)
    print("Page générée avec succès !")
