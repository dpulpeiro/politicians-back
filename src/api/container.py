from dataclasses import dataclass
from typing import Callable

from core.politicians.protocols.politicians_repo import PoliticiansRepo
from core.politicians.services.politicians_service import PoliticiansService
from core.statistics.protocols.statistics_repo import StatisticsRepo
from core.statistics.services.statistics_service import StatisticsService
from infra.database.repositories.elasticsearch_politicians_repo import (
    ElasticsearchPoliticiansRepo,
)
from infra.database.repositories.elasticsearch_statistics_repo import (
    ElasticsearchStatisticsRepo,
)


@dataclass(frozen=True)
class Repositories:
    politicians_repo: PoliticiansRepo
    statistics_repo: StatisticsRepo


@dataclass(frozen=True)
class Services:
    politicians_service: PoliticiansService
    statistics_service: StatisticsService


def _build_repositories() -> Callable[[], Repositories]:
    repositories = Repositories(
        politicians_repo=ElasticsearchPoliticiansRepo(),
        statistics_repo=ElasticsearchStatisticsRepo(),
    )

    def fn() -> Repositories:
        return repositories

    return fn


get_repositories = _build_repositories()


def _build_services() -> Callable[[], Services]:
    repositories = get_repositories()
    services = Services(
        politicians_service=PoliticiansService(
            politicians_repo=repositories.politicians_repo
        ),
        statistics_service=StatisticsService(
            statistics_repo=repositories.statistics_repo
        ),
    )

    def fn() -> Services:
        return services

    return fn


get_services = _build_services()
