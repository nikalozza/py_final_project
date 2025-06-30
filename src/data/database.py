from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.data.models import Base
import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.yaml')

with open(CONFIG_PATH, 'r') as f:
    config = yaml.safe_load(f)

engine = create_engine(config['database']['url'])
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
db = Session()
