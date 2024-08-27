import datetime
from typing import List

from domain.enums.prefer_notification import PreferNotification
from domain.enums.transaction_status import TransactionStatus
from domain.enums.transaction_type import TransactionType
from domain.exceptions import CanInvestException, InsufficientBalanceException, SubscriptionNotFoundException
from domain.models.fund import Fund
from domain.models.transaction import Transaction
from domain.value_objects.amount import Amount
from domain.value_objects.identifier import Identifier

class User:
    def __init__(self, id: int, name: str, email: str, phone: str, 
                 notification: PreferNotification, balance: Amount):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.notification = notification
        self.balance = balance
        self.transactions: List[Transaction] = []

    def subscribe_to_fund(self, fund: Fund, amount: Amount):
        # Validaciones
        if self.balance.value < amount.value:
            raise InsufficientBalanceException(fund.name)
        
        if fund.can_invest(amount):
            raise CanInvestException(fund.name, fund.min_amount)
        
        self.balance = self.balance - amount
        transaction = Transaction(
            transaction_id=Identifier.generate(),
            fund_id=fund.id,
            amount=amount,
            transaction_type=TransactionType.OPENING,
            status=TransactionStatus.COMPLETED
        )
        self.transactions.append(transaction)

    def cancel_fund_subscription(self, fund: Fund):
        self.transactions
        transaction = next((t for t in self.transactions if t.fund_id == fund.id and t.transaction_type == TransactionType.OPENING), None)
        if transaction:
            self.balance = self.balance + transaction.amount
            cancel_transaction = Transaction(
                transaction_id=Identifier.generate(),
                fund_id=fund.id,
                amount=transaction.amount,
                transaction_type=TransactionType.CANCELLATION,
                status=TransactionStatus.CANCELLED
            )
            self.transactions.append(cancel_transaction)
        else:
            raise SubscriptionNotFoundException(fund.name)
        