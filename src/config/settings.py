import os
from pydantic import BaseSettings
from dotenv import load_dotenv
from typing import Optional
from functools import lru_cache

load_dotenv(dotenv_path=".env")

class Settings(BaseSettings):
  ENV: str = os.getenv("ENV")

  DB_URL: str = os.getenv("DB_URL")
  DB_PORT: str = os.getenv("DB_PORT")
  DB_NAME: str = os.getenv("DB_NAME")
  DB_USERNAME: str = os.getenv("DB_USERNAME")
  DB_PASSWORD: str = os.getenv("DB_PASSWORD")

@lru_cache()
def get_settings():
  return Settings()

settings = get_settings()
