import datetime

from domain.enums.transaction_status import TransactionStatus
from domain.enums.transaction_type import TransactionType
from domain.value_objects.amount import Amount
from domain.value_objects.identifier import Identifier


class Transaction:
    def __init__(self, transaction_id: Identifier, fund_id: int, amount: Amount,
                 transaction_type: TransactionType,  status: TransactionStatus):
        self.transaction_id = transaction_id
        self.fund_id = fund_id
        self.amount = amount
        self.timestamp :datetime = datetime.datetime.now()
        self.transaction_type = transaction_type
        self.status = status

    