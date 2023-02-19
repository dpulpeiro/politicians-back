from typing import Iterable, Optional

import elasticsearch8
from elasticsearch8 import helpers

from config import settings
from core.politicians.entitites.politicians import (
    Politician,
    CreatePoliticianDto,
)
from core.politicians.protocols.politicians_repo import PoliticiansRepo
from infra.database.elasticsearch import elasticsearch
from shared.page import Page


class ElasticsearchPoliticiansRepo(PoliticiansRepo):
    INDEX = "politicians_index"

    async def bulk_insert(self, politicians: Iterable[CreatePoliticianDto]):
        helpers.bulk(
            elasticsearch,
            [politician.dict() for politician in politicians],
            index=self.INDEX,
        )

    async def fetch(self, politician_id: str) -> Optional[Politician]:
        try:
            politician_json = elasticsearch.get(index=self.INDEX, id=politician_id)
            data = politician_json.body["_source"]
            data["id"] = politician_id
            return Politician(**data)
        except elasticsearch8.NotFoundError:
            return None

    async def list(self, search, political_party, gender, page) -> Page[Politician]:
        # Build query
        query = {"bool": {}}
        if search:
            query["bool"]["must"] = [
                {
                    "match": {
                        "nombre": {
                            "query": search,
                            "fuzziness": "AUTO",
                            "operator": "and",
                        }
                    }
                },
            ]
        terms = []
        if political_party:
            terms.append({"term": {"partido_para_filtro.keyword": political_party}})
        if gender:
            terms.append({"term": {"genero.keyword": gender}})
        if terms:
            query["bool"]["filter"] = terms
        # Execute query
        politicians = []
        total = 0
        try:

            elastic_result = elasticsearch.search(
                from_=page * settings.PAGE_SIZE,
                size=settings.PAGE_SIZE,
                index=self.INDEX,
                query=query,
            ).body
            total = elastic_result["hits"]["total"]["value"]
            for hit in elastic_result["hits"]["hits"]:
                politicians.append(Politician(id=hit["_id"], **hit["_source"]))
        except elasticsearch8.NotFoundError:
            pass
        finally:
            return Page(items=politicians, page=page, size=settings.PAGE_SIZE, total=total)

    async def patch(
            self, politician_id, new_politician: Politician
    ) -> Optional[Politician]:
        try:
            elasticsearch.update(
                index=self.INDEX,
                id=politician_id,
                doc=new_politician.dict(exclude={"id"}),
            )
            return new_politician
        except elasticsearch8.NotFoundError:
            return None

    async def delete(self, politician_id) -> bool:
        try:
            elasticsearch.delete(index=self.INDEX, id=politician_id)
            return True
        except elasticsearch8.NotFoundError:
            return False
