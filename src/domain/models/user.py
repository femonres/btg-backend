import datetime
from typing import List
from pydantic import BaseModel

from src.domain.enums.prefer_notification import PreferNotification
from src.domain.enums.transaction_status import TransactionStatus
from src.domain.enums.transaction_type import TransactionType
from src.domain.models.fund import Fund
from src.domain.models.transaction import Transaction
from src.domain.value_objects.identifier import Identifier
from src.domain.value_objects.money import Money


class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    notification: PreferNotification
    balance: Money
    transactions: List[Transaction] = []

    def subscribe_to_fund(self, fund: Fund, amount: Money):
        self.balance = self.balance.subtract(amount)
        transaction = Transaction(
            transaction_id=Identifier.generate(),
            user=self,
            fund=fund,
            amount=amount,
            timestamp=datetime.now(),
            transaction_type=TransactionType.OPENING,
            status=TransactionStatus.COMPLETED
        )
        self.transactions.append(transaction)

    def cancel_fund_subscription(self, fund: Fund):
        transaction = next((t for t in self.transactions if t.fund == fund and t.transaction_type == TransactionType.OPENING), None)
        if transaction:
            self.balance = self.balance.add(transaction.amount)
            cancel_transaction = Transaction(
                transaction_id=Identifier.generate(),
                user=self,
                fund=fund,
                amount=transaction.amount,
                timestamp=datetime.now(),
                transaction_type=TransactionType.CANCELLATION,
                status=TransactionStatus.CANCELLED
            )
            self.transactions.append(cancel_transaction)
        else:
            raise ValueError("No hay suscripción activa para este fondo.")