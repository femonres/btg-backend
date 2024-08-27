import datetime
from typing import List

from domain.enums.prefer_notification import PreferNotification
from domain.enums.transaction_status import TransactionStatus
from domain.enums.transaction_type import TransactionType
from domain.exceptions.exceptions import SubscriptionNotFoundException
from domain.models.fund import Fund
from domain.models.transaction import Transaction
from domain.value_objects.identifier import Identifier
from domain.value_objects.money import Money


class User:
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
            fund_id=fund.id,
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
                fund_id=fund.id,
                amount=transaction.amount,
                timestamp=datetime.now(),
                transaction_type=TransactionType.CANCELLATION,
                status=TransactionStatus.CANCELLED
            )
            self.transactions.append(cancel_transaction)
        else:
            raise SubscriptionNotFoundException(fund.name)
        