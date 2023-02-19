from typing import List

from fastapi.routing import APIRouter
from starlette.responses import JSONResponse

from api.container import get_services
from core.politicians.entitites.politicians import Politician, UpdatePoliticianDto
from shared.page import Page

router = APIRouter()

politicians_service = get_services().politicians_service


@router.get(
    "",
    response_class=JSONResponse,
    response_model=Page[Politician],
    status_code=200,
    responses={
        200: {"description": "Politicians found"},
    },
)
async def list_politicians(
    search: str = "", political_party: str = None, gender: str = None, page: int = 0
):
    return list(await politicians_service.list(search, political_party, gender, page))


@router.get(
    "/{politician_id}",
    response_class=JSONResponse,
    response_model=Politician,
    status_code=200,
    responses={
        200: {"description": "Politician found"},
        404: {"description": "Politician not found"},
    },
)
async def get(politician_id: str):
    politician = await politicians_service.get(politician_id)
    if not politician:
        return JSONResponse(
            status_code=404,
            content={"description": f"Politician '{politician_id}' not found"},
        )
    return politician


@router.patch(
    "/{politician_id}",
    response_class=JSONResponse,
    response_model=Politician,
    status_code=200,
    responses={
        200: {"description": "Politicians found"},
        404: {"description": "Politicians not found"},
    },
)
async def patch(politician_id: str, politician: UpdatePoliticianDto):
    politician = await politicians_service.patch(politician_id, politician)
    if not politician:
        return JSONResponse(
            status_code=404,
            content={"description": f"Politician '{politician_id}' not found"},
        )
    return politician


@router.delete(
    "/{politician_id}",
    status_code=204,
    responses={
        204: {"description": "Politician deleted if exists"},
    },
)
async def delete(politician_id: str):
    result = await politicians_service.delete(politician_id)
    if not result:
        return JSONResponse(
            status_code=404,
            content={"description": f"Politician '{politician_id}' not found"},
        )
