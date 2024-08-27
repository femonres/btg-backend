import datetime
from domain.events.domain_event import DomainEvent
from domain.models.fund import Fund
from domain.models.user import User


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
            occurred_on=datetime.now()
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
            occurred_on=datetime.now()
        )
