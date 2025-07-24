import os

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.environ.get("DATABASE_URL")
    JWT_SECRET: str = os.environ.get("JWT_SECRET")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM")
    JWT_EXPIRATION_MINUTES: int = os.environ.get("JWT_EXPIRATION_MINUTES")

settings = Settings()
