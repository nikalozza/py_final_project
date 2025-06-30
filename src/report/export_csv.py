import csv
import os
from src.data.database import db
from src.data.models import NewsArticle

EXPORT_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'articles_export.csv')

def export_articles_to_csv():
    articles = db.query(NewsArticle).all()

    if not articles:
        print("⚠️ No articles found in the database.")
        return

    with open(EXPORT_PATH, mode='w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['ID', 'Title', 'Link', 'Source', 'Published', 'Author', 'Summary'])

        for article in articles:
            writer.writerow([
                article.id,
                article.title,
                article.link,
                article.source,
                article.published,
                article.author,
                article.summary
            ])

    print(f"✅ Exported {len(articles)} articles to {EXPORT_PATH}")

if __name__ == "__main__":
    export_articles_to_csv()
