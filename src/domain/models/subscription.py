from ..value_objects.amount import Amount
from ..value_objects.identifier import Identifier


class Subscription:
    def __init__(self, fund_id: int, amount: Amount):
        self.subscription_id = Identifier
        self.fund_id = fund_id
        self.amount = amount