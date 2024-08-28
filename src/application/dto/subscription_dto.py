from typing import NamedTuple


class SubscriptionDTO(NamedTuple):
    def __init__(self, fund_id: int, amount: int):
        self.fund_id = fund_id
        self.amount = amount

class CreateSubscriptionDTO(NamedTuple):
    def __init__(self, user_id: int, fund_id: int, amount: int):
        self.user_id = user_id
        self.fund_id = fund_id
        self.amount = amount

class CancelSubscriptionDTO(NamedTuple):
    def __init__(self, user_id: int, fund_id: int):
        self.user_id = user_id
        self.fund_id = fund_id