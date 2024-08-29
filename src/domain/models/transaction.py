import datetime

from domain.enums.transaction_type import TransactionType
from domain.value_objects.amount import Amount
from domain.value_objects.identifier import Identifier


class Transaction:
    def __init__(self, user_id: int, fund_id: int, amount: Amount,
                 transaction_type: TransactionType):
        self.transaction_id = Identifier
        self.user_id = user_id
        self.fund_id = fund_id
        self.amount = amount
        self.timestamp :datetime = datetime.datetime.now(datetime.UTC)
        self.transaction_type = transaction_type

    