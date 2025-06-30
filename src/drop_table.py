import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data.database import Base, engine
from src.data.models import NewsArticle

# Drop the news_articles table
NewsArticle.__table__.drop(engine)
print("table dropped successfully!!!")
