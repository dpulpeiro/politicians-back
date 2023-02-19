from fastapi.routing import APIRouter

from . import politicians


def _build_router() -> APIRouter:
    rt = APIRouter()
    rt.include_router(politicians.router, prefix="/politicians", tags=["Politicians"])
    return rt


router = _build_router()
