from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from datetime import datetime
from sqlalchemy.orm import Session
from src.data.database import db
from src.data.models import NewsArticle
import time

# ... same imports and setup as before ...

def scrape_cnn():
    url = "https://edition.cnn.com/world/europe"  # you're now using the Europe section

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("user-agent=Mozilla/5.0")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        seen_links = set()
        

        for container in soup.find_all("span", class_="container__headline-text"):
            title = container.get_text(strip=True)
            anchor = container.find_parent("a")
            if not anchor or not anchor.get("href"):
                continue

            href = anchor.get("href")
            if not href.startswith("/"):
                continue

            full_url = "https://edition.cnn.com" + href
            if full_url in seen_links:
                continue
            seen_links.add(full_url)

            print(f"Adding: {title} ({full_url})")

            news = NewsArticle(
                title=title,
                link=full_url,
                source="CNN",
                published=datetime.utcnow(),
                author=None,
                summary=None
            )
            existing = db.query(NewsArticle).filter_by(link=news.link).first()
            if existing:
    # Optional: update fields (if needed)
                existing.title = news.title
                existing.source = news.source
                existing.published = news.published
                existing.author = news.author
                existing.summary = news.summary
            else:
                db.add(news)


        db.commit()
        db.close()
        print(f"✅ Scraped and saved {len(seen_links)} CNN articles.")

    except TimeoutException:
        print("❌ Timeout while loading CNN")
    finally:
        driver.quit()

