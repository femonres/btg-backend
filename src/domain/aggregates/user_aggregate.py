from src.domain.events.user_event import UserSubscribeEvent, UserUnsubscribeEvent
from src.domain.models.fund import Fund
from src.domain.models.user import User
from src.domain.value_objects.money import Money


class UserAggregate(User):
    def subscribe_to_fund(self, fund: Fund, amount: Money):
        # Validaciones
        if self.balance.amount < amount.amount:
            raise ValueError(f"No tiene saldo disponible para vincularse al fondo: {fund.name}")
        
        if fund.can_invest(amount):
            raise ValueError(f"El monto con el cual desea vincularse al: {fund.name}, es inferior el minimo requerido: {fund.min_amount}")
        
        super().subscribe_to_fund(fund, amount)
        # Disparar evento
        UserSubscribeEvent.from_client(self, fund)

    def cancel_fund_subscription(self, fund: Fund):
        super().cancel_fund_subscription(fund)
        # Disparar evento
        UserUnsubscribeEvent.from_client(self, fund)
