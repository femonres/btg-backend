import datetime
from src.domain.events.domain_event import DomainEvent
from src.domain.models.fund import Fund
from src.domain.models.user import User


class UserSubscribeEvent(DomainEvent):
    user_id: int
    fund_id: int
    notification: str

    @staticmethod
    def from_user(user: User, fund: Fund) -> 'UserSubscribeEvent':
        return UserSubscribeEvent(
            user_id=user.id,
            fund_id=fund.id,
            notification=user.notification.value,
            occurred_on=datetime.now()
        )

class UserUnsubscribeEvent(DomainEvent):
    user_id: int
    fund_id: int
    notification: str

    @staticmethod
    def from_user(user: User, fund: Fund) -> 'UserUnsubscribeEvent':
        return UserUnsubscribeEvent(
            user_id=user.id,
            fund_id=fund.id,
            notification=user.notification.value,
            occurred_on=datetime.now()
        )
