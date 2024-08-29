from typing import NamedTuple

from application.dto.subscription_dto import SubscriptionDTO


class UserDTO(NamedTuple):
    id: int
    name: str
    email: str
    phone: str
    balance: int
    notification: str
    subscriptions: list[SubscriptionDTO] = []

class SaveUserDTO(NamedTuple):
    name: str
    email: str
    phone: str
    balance: int
    notification: str