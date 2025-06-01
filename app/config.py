from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import Literal


class DatabaseConfig(BaseModel):
    HOST: str = "localhost"
    PORT: str = "5432"
    DATABASE: str = "mydatabase"
    USER: str = "user"
    PASSWORD: str = "password"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"


class Settings(BaseSettings):
    ENV: Literal["dev", "qa", "stage", "prod"] = "dev"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DB_CONFIG: DatabaseConfig = DatabaseConfig()
    API_V1_PREFIX: str = "/api/v1"
    API_LATEST_PREFIX: str = "/api/latest"


settings = Settings()
