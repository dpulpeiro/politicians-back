from typing import Optional

from core.statistics.entitites.statistics import StatisticsSummary
from core.statistics.protocols.statistics_repo import StatisticsRepo


class StatisticsService:
    def __init__(self, statistics_repo: StatisticsRepo):
        self.statistics_repo = statistics_repo

    async def summary(self) -> Optional[StatisticsSummary]:
        return await self.statistics_repo.summary()
