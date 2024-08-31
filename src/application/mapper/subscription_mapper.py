from domain import Subscription, Subscription
from application.dto.subscription_dto import SubscriptionDTO


class SubscriptionMapper:
    @staticmethod
    def from_entity(subscription: 'Subscription') -> SubscriptionDTO:
        return SubscriptionDTO(
            id=subscription.subscription_id.id,
            fund_id=subscription.fund_id,
            fund_name=subscription.fund_name,
            amount=subscription.amount.value
        )
