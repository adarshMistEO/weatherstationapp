from typing import List
from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGODB_URL: str = 'mongodb://localhost:27017'
    MONGODB_DB: str = 'weather_app'
    JWT_SECRET: str = 'mysecretkey'
    JWT_ALGORITHM: str = 'HS256'
    ALLOWED_HOSTS: List[str] = []
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
