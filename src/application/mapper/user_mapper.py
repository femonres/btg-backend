from domain import User, Amount, NotificationType
from application.dto.user_dto import UserDTO
from application.mapper.subscription_mapper import SubscriptionMapper


class UserMapper:
    @staticmethod
    def from_entity(user: 'User') -> UserDTO:
        subscriptions = [SubscriptionMapper.from_entity(sub) for sub in user.subscriptions]
        return UserDTO(
            id=user.id,
            name=user.name,
            email=user.email,
            phone=user.phone,
            balance=user.balance.value,
            notification=user.notification.value,
            subscriptions=subscriptions
        )

    @staticmethod
    def to_entity(dto: UserDTO) -> User:
        return User(
            id=dto.id,
            name=dto.name,
            email=dto.email,
            phone=dto.phone,
            balance=Amount(dto.balance),
            notification=NotificationType(dto.notification)
        )