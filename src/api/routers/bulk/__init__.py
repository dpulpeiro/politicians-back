from fastapi.routing import APIRouter

from . import bulk


def _build_router() -> APIRouter:
    rt = APIRouter()
    rt.include_router(bulk.router, prefix="/bulk", tags=["Bulk insert"])
    return rt


router = _build_router()
