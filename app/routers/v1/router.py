from fastapi import APIRouter
from app.routers.v1 import users

router = APIRouter()

router.include_router(
    router=users.router,
)
