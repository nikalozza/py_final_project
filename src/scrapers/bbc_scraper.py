import requests
from bs4 import BeautifulSoup
from datetime import datetime
from sqlalchemy.orm import Session
from src.data.database import db
from src.data.models import NewsArticle

def scrape_bbc():
    url = "https://www.bbc.com/news"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    seen_links = set()

    for anchor in soup.find_all("a", attrs={"data-testid": "internal-link"}):
        href = anchor.get("href", "")
        headline_tag = anchor.find("h2", attrs={"data-testid": "card-headline"})
        if not headline_tag or not href.startswith("/news"):
            continue

        title = headline_tag.get_text(strip=True)
        link = "https://www.bbc.com" + href

        if link in seen_links:
            continue
        seen_links.add(link)

        print(f"Adding: {title} ({link})")

        news = NewsArticle(
            title=title,
            link=link,
            source="BBC",
            published=datetime.utcnow(),
            author=None,
            summary=None
        )
        existing = db.query(NewsArticle).filter_by(link=news.link).first()
        if existing:
            existing.title = news.title
            existing.source = news.source
            existing.published = news.published
            existing.author = news.author
            existing.summary = news.summary
        else:
            db.add(news)


    db.commit()
    db.close()
    print(f"✅ Scraped and saved {len(seen_links)} BBC articles.")
