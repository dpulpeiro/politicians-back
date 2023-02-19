from fastapi import APIRouter
from starlette.responses import JSONResponse

from api.container import get_services
from core.statistics.entitites.statistics import StatisticsSummary

router = APIRouter()

statistics_service = get_services().statistics_service


@router.get(
    "",
    response_class=JSONResponse,
    response_model=StatisticsSummary,
    status_code=200,
    responses={
        200: {"description": "Statistics"},
        503: {"description": "Statistics service unavailable"},
    },
)
async def summary():
    statistics = await statistics_service.summary()
    if statistics is None:
        return JSONResponse(status_code=503, content="Statistics service unavailable, maybe there aren't politicians")
    return statistics
