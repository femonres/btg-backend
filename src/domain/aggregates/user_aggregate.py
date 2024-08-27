from domain.models.fund import Fund
from domain.models.user import User
from domain.value_objects.amount import Amount
from domain.exceptions import CanInvestException, InsufficientBalanceException
from domain.events.user_event import UserSubscribeEvent, UserUnsubscribeEvent


class UserAggregate(User):
    def subscribe_to_fund(self, fund: Fund, amount: Amount):    
        super().subscribe_to_fund(fund, amount)
        # Disparar evento
        UserSubscribeEvent.from_user(self, fund)

    def cancel_fund_subscription(self, fund: Fund):
        super().cancel_fund_subscription(fund)
        # Disparar evento
        UserUnsubscribeEvent.from_user(self, fund)
