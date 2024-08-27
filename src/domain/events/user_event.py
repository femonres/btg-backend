import datetime

from .domain_event import DomainEvent
from domain import Fund, User

class UserSubscribeEvent(DomainEvent):
    user: User
    fund: Fund
    notification: str

    @staticmethod
    def from_user(user: User, fund: Fund) -> 'UserSubscribeEvent':
        return UserSubscribeEvent(
            user=user,
            fund=fund,
            notification=user.notification.value,
            occurred_on=datetime.datetime.now()
        )

class UserUnsubscribeEvent(DomainEvent):
    user: User
    fund: Fund
    notification: str

    @staticmethod
    def from_user(user: User, fund: Fund) -> 'UserUnsubscribeEvent':
        return UserUnsubscribeEvent(
            user=user,
            fund=fund,
            notification=user.notification.value,
            occurred_on=datetime.datetime.now()
        )
