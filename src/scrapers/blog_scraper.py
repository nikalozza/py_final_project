from datetime import datetime
from dateutil import parser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sqlalchemy.exc import IntegrityError
from src.data.models import NewsArticle
from src.data.database import db
import time

def scrape_blog():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.promptcloud.com/blog/")
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = soup.find_all("div", id=lambda x: x and x.startswith("post-"))
    print(f"🔍 Found {len(articles)} articles")

    article_count = 0

    for post in articles:
        try:
            title_tag = post.find("h3", class_="title")
            if not title_tag or not title_tag.a:
                continue
            title = title_tag.get_text(strip=True)
            link = title_tag.a["href"]

            # Check for duplicates
            existing = db.query(NewsArticle).filter_by(link=link).first()
            if existing:
                continue  # Skip duplicates

            author_tag = post.find("span", attrs={"data-text": True})
            author = author_tag["data-text"].strip() if author_tag else None

            date_tag = post.find("li", class_="post-meta-date")
            date_str = date_tag.get_text(strip=True) if date_tag else None
            published = parser.parse(date_str) if date_str else datetime.utcnow()

            summary_tag = post.find("div", class_="post-thumbnail")
            summary = summary_tag.p.get_text(strip=True) if summary_tag and summary_tag.p else None

            news = NewsArticle(
                title=title,
                link=link,
                source="PromptCloud",
                published=published,
                author=author,
                summary=summary
            )

            db.add(news)
            db.flush()  # Try inserting to catch integrity errors early
            article_count += 1

        except IntegrityError:
            db.rollback()  # Roll back on duplicate error
        except Exception as e:
            db.rollback()
            print(f"⚠️ Error scraping post: {e}")

    try:
        db.commit()
    except Exception as e:
        print(f"❌ Commit failed: {e}")
        db.rollback()

    print(f"✅ PromptCloud scraping completed. Articles added: {article_count}")

if __name__ == "__main__":
    scrape_blog()
