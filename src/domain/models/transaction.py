import datetime

from domain.enums.transaction_status import TransactionStatus
from domain.enums.transaction_type import TransactionType
from domain.models.fund import Fund
from domain.value_objects.identifier import Identifier
from domain.value_objects.money import Money


class Transaction:
    transaction_id: Identifier
    fund_id: int
    amount: Money
    timestamp: datetime
    transaction_type: TransactionType
    status: TransactionStatus