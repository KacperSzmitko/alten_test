from fastapi import APIRouter, HTTPException, Query
import logging
from app.dependencies import DbSessionDep
from app.storage.models.user import User
from sqlmodel import select, or_
from app.types.user import UserInputModel

# Set up logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/users", tags=["Users"])
async def get_users(
    db: DbSessionDep,
    username: str = Query(None, description="Filter users by name"),
) -> list[User]:
    stmt = select(User)

    if username:
        logger.info(f"Fetching users with username: {username}")
        stmt = stmt.where(or_(User.username.ilike(f"%{username}%")))
    db_users = db.exec(stmt).all()
    return db_users


@router.get("/users/{user_id}", tags=["Users"])
async def get_user(
    user_id: int,
    db: DbSessionDep,
) -> User:
    if user_id <= 0:
        logger.error(f"Invalid user_id: {user_id}")
        raise HTTPException(status_code=400, detail="Invalid user ID")
    stmt = select(User).where(User.id == user_id)
    db_user = db.exec(stmt).first()
    if not db_user:
        logger.error(f"User with id {user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users", tags=["Users"])
async def create_user(
    user: UserInputModel,
    db: DbSessionDep,
) -> User:
    created_user = User(
        username=user.username, email=user.email, hashed_password=user.hashed_password, is_superuser=user.is_superuser
    )
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user
