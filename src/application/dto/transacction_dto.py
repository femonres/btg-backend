from typing import NamedTuple


class TransactionDTO(NamedTuple):
    def __init__(self, transaction_id: str, fund_id: int, fund_name: int, amount: int, timestamp: str, transaction_type: str):
        self.transaction_id = transaction_id
        self.fund_id = fund_id
        self.fund_name = fund_name
        self.amount = amount
        self.timestamp = timestamp
        self.transaction_type = transaction_type