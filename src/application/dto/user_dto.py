from typing import List, NamedTuple
from pydantic import BaseModel

from application.dto.subscription_dto import SubscriptionDTO


class UserDTO(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    balance: int
    notification: str
    subscriptions: List[SubscriptionDTO] = []

class SaveUserDTO(NamedTuple):
    name: str
    email: str
    phone: str
    balance: int
    notification: str