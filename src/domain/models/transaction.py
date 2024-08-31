from datetime import datetime

from ..enums.transaction_type import TransactionType
from ..value_objects.amount import Amount
from ..value_objects.identifier import Identifier


class Transaction:
    def __init__(self, user_id: int, fund_id: int, fund_name: str,
                 amount: Amount, transaction_type: TransactionType):
        self.transaction_id = Identifier.generate()
        self.user_id = user_id
        self.fund_id = fund_id
        self.fund_name = fund_name
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    