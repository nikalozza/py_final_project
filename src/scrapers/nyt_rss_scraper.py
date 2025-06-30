import feedparser
from datetime import datetime
from src.data.models import NewsArticle
from src.data.database import db

def scrape_nyt_rss():
    rss_url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    feed = feedparser.parse(rss_url)

    count = 0
    for entry in feed.entries:
        title = entry.title.strip()
        link = entry.link
        published = datetime(*entry.published_parsed[:6]) if 'published_parsed' in entry else datetime.utcnow()
        summary = entry.summary if 'summary' in entry else None
        author = entry.get('author', None)

        article = NewsArticle(
            title=title,
            link=link,
            source="NYT",
            published=published,
            author=author,
            summary=summary
        )
        existing = db.query(NewsArticle).filter_by(link=article.link).first()
        if existing:
    # Optional: update fields (if needed)
            existing.title = article.title
            existing.source = article.source
            existing.published = article.published
            existing.author = article.author
            existing.summary = article.summary
        else:
            db.add(article)

        count += 1

    db.commit()
    print(f"📰 Scraped and saved {count} NYT articles from RSS.")
