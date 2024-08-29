from typing import NamedTuple


class TransactionDTO(NamedTuple):
    transaction_id: str
    fund_id: int
    amount: int
    timestamp: str
    transaction_type: str