import os

from pydantic import Field
from pydantic_settings import BaseSettings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class PojectSettings(BaseSettings):
    APP_NAME: str = "Ecom API"
    # PostgresDB
    POSTGRES_URL: str = Field(
        'postgresql://postgres:postgres@localhost:5432/postgres',
        env='POSTGRES_URL'
    )
    

settings = PojectSettings()
