from sqlalchemy import Engine
from sqlmodel import Session
from typing import Generator, Any
from app.config import DatabaseConfig
from sqlmodel import create_engine


class PostgresDatabaseStorage:
    def __init__(self, config: DatabaseConfig) -> None:
        self.config = config
        self._engine = self.create_engine()

    def create_engine(self) -> Engine:
        engine = create_engine(
            url="postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
                host=self.config.HOST,
                port=self.config.PORT,
                database=self.config.DATABASE,
                user=self.config.USER,
                password=self.config.PASSWORD,
            ),
        )
        return engine

    def get_engine(self) -> Engine:
        return self._engine

    def get_session(self) -> Generator[Session, Any, None]:
        with Session(self.get_engine()) as session:
            yield session
