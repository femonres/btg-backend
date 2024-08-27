from dataclasses import dataclass
from domain.value_objects.amount import Amount
from domain.value_objects.fund_category import FundCategory

class Fund:
    def __init__(self, id: int, name: str, min_amount: Amount, category: FundCategory):
        self.id = id
        self.name = name
        self.min_amount = min_amount
        self.category = category

    def can_invest(self, amount: Amount) -> bool:
            return self.min_amount.value >= amount.value