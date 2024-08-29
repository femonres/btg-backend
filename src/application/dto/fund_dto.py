from typing import NamedTuple


class FundDTO(NamedTuple):
    id: int
    name: str
    min_amount: int
    category: str