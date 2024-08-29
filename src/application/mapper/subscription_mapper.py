from domain import Subscription, Amount, Subscription
from application.dto.subscription_dto import SubscriptionDTO


class SubscriptionMapper:
    @staticmethod
    def from_entity(subscription: 'Subscription') -> SubscriptionDTO:
        return SubscriptionDTO(
            id=subscription.subscription_id,
            fund_id=subscription.fund_id,
            amount=subscription.amount.value
        )
