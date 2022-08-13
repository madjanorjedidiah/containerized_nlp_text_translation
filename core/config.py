from fastapi import APIRouter
from api.v1.translate import router

"""
info: {title: "FastAPI", version: "0.1.0"}
"""

api_router = APIRouter()
api_router.include_router(router, prefix="/api/v1", tags=["api"])
