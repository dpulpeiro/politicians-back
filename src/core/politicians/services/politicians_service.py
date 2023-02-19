from typing import Iterable, Optional

from core.politicians.entitites.politicians import (
    Politician,
    CreatePoliticianDto,
    UpdatePoliticianDto,
)
from core.politicians.protocols.politicians_repo import PoliticiansRepo
from shared.page import Page


class PoliticiansService:
    def __init__(self, politicians_repo: PoliticiansRepo):
        self.politicians_repo = politicians_repo

    async def bulk_insert(self, politicians: Iterable[CreatePoliticianDto]):
        return await self.politicians_repo.bulk_insert(politicians)

    async def get(self, politician_id: str) -> Optional[Politician]:
        return await self.politicians_repo.fetch(politician_id)

    async def list(self, search, political_party, gender, page) -> Page[Politician]:
        politicians = await self.politicians_repo.list(
            search, political_party, gender, page
        )
        return politicians

    async def patch(
            self, politician_id, new_politician: UpdatePoliticianDto
    ) -> Optional[Politician]:
        current_politician = await self.politicians_repo.fetch(politician_id)
        if not current_politician:
            return None
        update_politician = current_politician.copy(update=new_politician.dict(exclude_unset=True), )
        politician = await self.politicians_repo.patch(politician_id, update_politician)
        return politician

    async def delete(self, politician_id) -> bool:
        return await self.politicians_repo.delete(politician_id)
