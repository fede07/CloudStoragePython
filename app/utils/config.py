import os

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.environ.get("DATABASE_URL")
    JWT_SECRET: str = os.environ.get("JWT_SECRET")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM")
    JWT_EXPIRATION_MINUTES: int = os.environ.get("JWT_EXPIRATION_MINUTES")
    STORAGE_LIMIT: int = 5 * 1024 * 1024 * 1024

    AWS_ACCESS_KEY_ID: str = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET_NAME: str = os.environ.get("AWS_S3_BUCKET_NAME")
    AWS_S3_REGION: str = os.environ.get("AWS_S3_REGION")

settings = Settings()
