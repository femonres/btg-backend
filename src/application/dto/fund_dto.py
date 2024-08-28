from typing import NamedTuple


class FundDTO(NamedTuple):
    def __init__(self, id: int, name: str, min_amount: int, category: str):
        self.id = id
        self.name = name
        self.min_amount = min_amount
        self.category = category