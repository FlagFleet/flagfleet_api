from pydantic_settings import BaseSettings
from functools import lru_cache
from sqlalchemy.engine.url import URL
import os


class Settings(BaseSettings):
    # Database settings
    DATABASE_USERNAME: str = os.getenv("DATABASE_USERNAME", "user")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "password")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "db")
    DATABASE_PORT: int = int(os.getenv("DATABASE_PORT", 5432))
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "db_name")
    DATABASE_DRIVER: str = os.getenv("DATABASE_DRIVER", "postgresql+pg8000")

    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI SQLModel App"

    class Config:
        case_sensitive = True

    @property
    def DATABASE_URL(self) -> str:
        """Construit l'URL de connexion à partir des composants."""
        return str(f"{self.DATABASE_DRIVER}://{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}/{self.DATABASE_NAME}")


def get_settings() -> Settings:
    return Settings()
