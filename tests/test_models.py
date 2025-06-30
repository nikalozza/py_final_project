import unittest
from datetime import datetime
from src.data.models import NewsArticle, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestNewsArticleModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Use in-memory SQLite for testing
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_article_creation(self):
        article = NewsArticle(
            title="Test Title",
            link="https://example.com/test",
            source="Test Source",
            published=datetime.utcnow(),
            author="Test Author",
            summary="This is a test summary."
        )
        self.session.add(article)
        self.session.commit()

        saved = self.session.query(NewsArticle).filter_by(link="https://example.com/test").first()
        self.assertIsNotNone(saved)
        self.assertEqual(saved.title, "Test Title")
        self.assertEqual(saved.source, "Test Source")
        self.assertEqual(saved.author, "Test Author")
        self.assertEqual(saved.summary, "This is a test summary.")

if __name__ == '__main__':
    unittest.main()
