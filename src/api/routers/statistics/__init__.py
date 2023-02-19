from fastapi.routing import APIRouter

from . import statistics


def _build_router() -> APIRouter:
    rt = APIRouter()
    rt.include_router(statistics.router, prefix="/statistics", tags=["Statistics"])
    return rt


router = _build_router()
