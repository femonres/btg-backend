from pydantic import BaseModel

from src.domain.value_objects.fund_category import FundCategory
from src.domain.value_objects.money import Money


class Fund(BaseModel):
    id: int
    name: str
    min_amount: Money
    category: FundCategory

    def can_invest(self, amount: Money) -> bool:
            return amount >= self.min_amount