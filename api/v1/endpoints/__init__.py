from fastapi import APIRouter

from api.v1.endpoints import items

router = APIRouter()

router.include_router(items.router)