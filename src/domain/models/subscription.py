from ..value_objects.amount import Amount
from ..value_objects.identifier import Identifier


class Subscription:
    def __init__(self, fund_id: int, fund_name: str, amount: Amount):
        self.subscription_id = Identifier.generate()
        self.fund_id = fund_id
        self.fund_name = fund_name
        self.amount = amount