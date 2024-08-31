from typing import NamedTuple
from pydantic import BaseModel


class SubscriptionDTO(BaseModel):
    id: str
    fund_id: int
    fund_name: str
    amount: int

class CreateSubscriptionDTO(NamedTuple):
    user_id: int
    fund_id: int
    amount: int

class CancelSubscriptionDTO(NamedTuple):
    user_id: int
    fund_id: int