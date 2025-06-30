from src.data.models import NewsArticle
from src.data.database import db  # your SQLAlchemy session

class AlJazeeraPipeline:
    def process_item(self, item, spider):
        if db.query(NewsArticle).filter_by(link=item['link']).first():
            spider.logger.debug(f"🟡 Duplicate article: {item['link']}")
            return item

        article = NewsArticle(
            title=item['title'],
            link=item['link'],
            published=item['published'],
            author=item['author'],
            source=item['source'],
            summary=item['summary']
        )
        db.add(article)
        db.commit()
        spider.logger.info(f"✅ Article saved: {item['title']}")
        return item
