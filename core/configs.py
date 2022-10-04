from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
        Configuraçoes gerais usadas na aplicação
    """

    API_VERSION: str = '/api/v0'
    DB_URL: str = 'postgresql+asyncpg://postgres:postgres@localhost:5432/api-async'
    DBBaseModel = declarative_base()


    class Config:
        case_sensitive = True


settings = Settings()