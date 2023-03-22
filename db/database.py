from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.settings import *

SQLALCHEMY_DATABASE_URL = "mysql://{0}:{1}@{2}:{3}/{4}".format(settings.DB_USERNAME,
  settings.DB_PASSWORD,
  settings.DB_URL,
  settings.DB_PORT,
  settings.DB_NAME)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
