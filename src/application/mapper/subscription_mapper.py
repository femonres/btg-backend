from domain import Subscription, Amount, Subscription
from application.dto.subscription_dto import SubscriptionDTO


class SubscriptionMapper:
    @staticmethod
    def from_entity(subscription: 'Subscription') -> SubscriptionDTO:
        return SubscriptionDTO(
            fund_id=subscription.fund.id,
            amount=subscription.amount.value
        )
