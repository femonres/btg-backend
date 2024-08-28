import datetime

from domain.enums.transaction_type import TransactionType
from domain.value_objects.amount import Amount
from domain.value_objects.identifier import Identifier
from domain.models.fund import Fund
from domain.models.user import User


class Transaction:
    def __init__(self, user: User, fund: Fund, amount: Amount,
                 transaction_type: TransactionType):
        self.transaction_id = Identifier
        self.user = user
        self.fund = fund
        self.amount = amount
        self.timestamp :datetime = datetime.datetime.now(datetime.UTC)
        self.transaction_type = transaction_type

    