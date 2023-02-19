from typing import Optional

import elasticsearch8

from core.politicians.entitites.politicians import Politician
from core.statistics.entitites.statistics import StatisticsSummary
from core.statistics.protocols.statistics_repo import StatisticsRepo
from infra.database.elasticsearch import elasticsearch


class ElasticsearchStatisticsRepo(StatisticsRepo):
    index = "politicians_index"

    async def summary(self, top_n=10) -> Optional[StatisticsSummary]:
        try:
            elastic_result = elasticsearch.search(
                index=self.index,
                from_=0,
                size=top_n,
                sort=[{"retribucionanual": "desc"}],
                aggs={
                    "mean_salary": {"avg": {"field": "retribucionanual"}},
                    "median_salary": {
                        "percentiles": {"field": "retribucionanual", "percents": [50]}
                    },
                },
            ).body
            median_salary = elastic_result["aggregations"]["median_salary"]["values"][
                "50.0"
            ]
            mean_salary = elastic_result["aggregations"]["mean_salary"]["value"]
            politicians = []
            for hit in elastic_result["hits"]["hits"]:
                politicians.append(Politician(id=hit["_id"], **hit["_source"]))
            return StatisticsSummary(
                median_salary=median_salary,
                mean_salary=mean_salary,
                top_politicians=politicians,
            )
        except elasticsearch8.NotFoundError:
            return None
