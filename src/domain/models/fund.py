from domain.value_objects.fund_category import FundCategory
from domain.value_objects.money import Money


class Fund:
    id: int
    name: str
    min_amount: Money
    category: FundCategory

    def can_invest(self, amount: Money) -> bool:
            return amount >= self.min_amount