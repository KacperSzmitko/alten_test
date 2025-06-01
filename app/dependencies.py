from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from app.storage.postgres import PostgresDatabaseStorage
from app.config import settings

db = PostgresDatabaseStorage(settings.DB_CONFIG)
DbSessionDep = Annotated[Session, Depends(db.get_session)]
