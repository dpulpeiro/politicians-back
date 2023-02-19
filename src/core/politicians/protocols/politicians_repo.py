from typing import Iterable, Optional, Protocol

from core.politicians.entitites.politicians import (
    Politician,
    CreatePoliticianDto,
)
from shared.page import Page


class PoliticiansRepo(Protocol):
    async def bulk_insert(self, politicians: Iterable[CreatePoliticianDto]):
        ...

    async def fetch(self, politician_id: str) -> Optional[Politician]:
        ...

    async def list(self, search, political_party, gender, page) -> Page[Politician]:
        ...

    async def patch(
        self, politician_id, new_politician: Politician
    ) -> Optional[Politician]:
        ...

    async def delete(self, politician_id) -> bool:
        ...
