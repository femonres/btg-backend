from typing import NamedTuple


class SubscriptionDTO(NamedTuple):
    id: str
    fund_id: int
    amount: int

class CreateSubscriptionDTO(NamedTuple):
    user_id: int
    fund_id: int
    amount: int

class CancelSubscriptionDTO(NamedTuple):
    user_id: int
    fund_id: int