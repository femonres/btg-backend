from typing import NamedTuple

from application.dto.subscription_dto import SubscriptionDTO


class UserDTO(NamedTuple):
    def __init__(self, id: int, name: str, email: str, phone: str, balance: int, notification: str, subscriptions: list[SubscriptionDTO]):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.balance = balance
        self.notification = notification
        self.subscriptions = subscriptions

class SaveUserDTO(NamedTuple):
    def __init__(self, name: str, email: str, phone: str, balance: int, notification: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.balance = balance
        self.notification = notification