import logging
from fastapi import FastAPI
from app.routers.v1 import router as v1_router
from app.config import settings

logger = logging.getLogger(__name__)

app = FastAPI(
    title="ALTEN Backend API",
    description="Backend API test",
    version="1.0.0",
)

app.include_router(v1_router.router, prefix=settings.API_V1_PREFIX, tags=["v1"])
app.include_router(v1_router.router, prefix=settings.API_LATEST_PREFIX, tags=["latest"])
