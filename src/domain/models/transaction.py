import datetime
from pydantic import BaseModel

from src.domain.enums.transaction_status import TransactionStatus
from src.domain.enums.transaction_type import TransactionType
from src.domain.models.fund import Fund
from src.domain.models.user import User
from src.domain.value_objects.identifier import Identifier
from src.domain.value_objects.money import Money


class Transaction(BaseModel):
    transaction_id: Identifier
    user: 'User'
    fund: Fund
    amount: Money
    timestamp: datetime
    transaction_type: TransactionType
    status: TransactionStatus