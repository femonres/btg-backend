from domain.models.user import User
from domain.models.fund import Fund
from domain.value_objects.amount import Amount
from domain.value_objects.identifier import Identifier


class Subscription:
    def __init__(self, user: User, fund: Fund, amount: Amount):
        self.subscription_id = Identifier
        self.user = user
        self.fund = fund
        self.amount = amount