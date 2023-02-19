from typing import Protocol, Optional

from core.statistics.entitites.statistics import StatisticsSummary


class StatisticsRepo(Protocol):
    async def summary(self) -> Optional[StatisticsSummary]:
        ...
