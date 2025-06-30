from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'news_articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    link = Column(String(500), nullable=False, unique=True)
    source = Column(String(100), nullable=False)
    published = Column(DateTime)
    author = Column(String(500))
    summary = Column(String(1000)) 
