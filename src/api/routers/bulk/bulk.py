import csv
import io

from fastapi import APIRouter, UploadFile
from starlette.responses import JSONResponse

from api.container import get_services
from core.politicians.entitites.create_politician_dto_from_json import (
    create_politician_dto_from_json,
)

router = APIRouter()
politicians_service = get_services().politicians_service


@router.post(
    "",
    response_class=JSONResponse,
    status_code=201,
    responses={
        204: {"description": "Bulk inserted"},
    },
)
async def bulk(csv_file: UploadFile):
    contents = (await csv_file.read()).decode("utf-8-sig")
    politicians_json_list = csv.DictReader(io.StringIO(contents), delimiter=";")
    politicians = [
        create_politician_dto_from_json(politician_json)
        for politician_json in politicians_json_list
    ]
    await politicians_service.bulk_insert(politicians)
