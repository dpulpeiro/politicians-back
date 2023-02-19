from typing import List

from pydantic import BaseModel

from core.politicians.entitites.politicians import Politician


class StatisticsSummary(BaseModel):
    mean_salary: float
    median_salary: float
    top_politicians: List[Politician]
