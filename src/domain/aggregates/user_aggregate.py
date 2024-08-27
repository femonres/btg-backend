from domain.events.user_event import UserSubscribeEvent, UserUnsubscribeEvent
from domain.exceptions.exceptions import CanInvestException, InsufficientBalanceException
from domain.models.fund import Fund
from domain.models.user import User
from domain.value_objects.money import Money


class UserAggregate(User):
    def subscribe_to_fund(self, fund: Fund, amount: Money):
        # Validaciones
        if self.balance.amount < amount.amount:
            raise InsufficientBalanceException(fund.name)
        
        if fund.can_invest(amount):
            raise CanInvestException(fund.name, fund.min_amount)
        
        super().subscribe_to_fund(fund, amount)
        # Disparar evento
        UserSubscribeEvent.from_client(self, fund)

    def cancel_fund_subscription(self, fund: Fund):
        super().cancel_fund_subscription(fund)
        # Disparar evento
        UserUnsubscribeEvent.from_client(self, fund)
