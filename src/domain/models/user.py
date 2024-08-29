from abc import ABC, abstractmethod
from typing import List, Optional

from domain.enums.transaction_type import TransactionType
from domain.enums.notification_type import NotificationType
from domain.exceptions import SubscriptionNotFoundException
from domain.models.fund import Fund
from domain.models.transaction import Transaction
from domain.value_objects.amount import Amount
from domain.models.subscription import Subscription

class ValidationStrategy(ABC):
    @abstractmethod
    def can_subscribe(self, user: 'User', fund: 'Fund', amount: Amount):
        pass

class User:
    def __init__(self, id: int, name: str, email: str, phone: str, 
                 notification: NotificationType, balance: Amount,
                 validations: List[ValidationStrategy] = None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.notification = notification
        self.balance = balance
        self.subscriptions: List[Subscription] = []
        self.validations = validations

    def subscribe_to_fund(self, fund: 'Fund', amount: Amount):
        for validation in self.validations:
            validation.can_subscribe(self, fund, amount)

        subscription = Subscription(user=self, fund=fund, amount=amount)
        self.subscriptions.append(subscription)
        self.balance -= amount

        transaction = Transaction(fund_id=fund.id, amount=amount, transaction_type=TransactionType.OPENING)
        return transaction

    def cancel_fund_subscription(self, fund: 'Fund'):
        subscription = self.get_subscription(fund)
        if not subscription:
            raise SubscriptionNotFoundException(fund.name)
        
        self.balance += subscription.amount
        self.subscriptions.remove(subscription)

        transaction = Transaction(fund_id=fund.id, amount=subscription.amount, transaction_type=TransactionType.CANCELLATION)
        return transaction
        
    def is_subscribed(self, fund: 'Fund') -> bool:
        return any(sub.fund == fund for sub in self.subscriptions)
    
    def get_subscription(self, fund: 'Fund') -> Optional['Subscription']:
        for subscription in self.subscriptions:
            if subscription.fund == fund:
                return subscription
        return None
