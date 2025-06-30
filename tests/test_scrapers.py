import unittest
from src.data.database import db
from src.data.models import NewsArticle
from src.scrapers import cnn_scraper, bbc_scraper, nyt_rss_scraper, blog_scraper

class TestScrapers(unittest.TestCase):

    def setUp(self):
        # Count existing articles to detect increase
        self.initial_count = db.query(NewsArticle).count()

    def test_cnn_scraper(self):
        cnn_scraper.scrape_cnn()
        articles = db.query(NewsArticle).filter_by(source="CNN").all()
        self.assertTrue(len(articles) > 0)
        for article in articles:
            self.assertIsNotNone(article.title)
            self.assertIsNotNone(article.link)
            self.assertEqual(article.source, "CNN")

    def test_bbc_scraper(self):
        bbc_scraper.scrape_bbc()
        articles = db.query(NewsArticle).filter_by(source="BBC").all()
        self.assertTrue(len(articles) > 0)
        for article in articles:
            self.assertIsNotNone(article.title)
            self.assertIsNotNone(article.link)
            self.assertEqual(article.source, "BBC")

    def test_nyt_scraper(self):
        nyt_rss_scraper.scrape_nyt_rss()
        articles = db.query(NewsArticle).filter_by(source="NYT").all()
        self.assertTrue(len(articles) > 0)
        for article in articles:
            self.assertIsNotNone(article.title)
            self.assertIsNotNone(article.link)
            self.assertEqual(article.source, "NYT")

    def test_promptcloud_scraper(self):
        blog_scraper.scrape_blog()
        articles = db.query(NewsArticle).filter_by(source="PromptCloud").all()
        self.assertTrue(len(articles) > 0)
        for article in articles:
            self.assertIsNotNone(article.title)
            self.assertIsNotNone(article.link)
            self.assertEqual(article.source, "PromptCloud")

if __name__ == '__main__':
    unittest.main()
