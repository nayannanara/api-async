from pydantic import BaseSettings


class Settings(BaseSettings):
    """
        Configuraçoes gerais usadas na aplicação
    """

    API_VERSION: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:123@localhost:5432/api-async-sqlmodel'


    class Config:
        case_sensitive = True


settings: Settings = Settings()