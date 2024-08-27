from typing import List

from application import CancellationDTO, FundDTO, SubscriptionDTO
from domain import UserSubscribeEvent, FundNotFoundException, UserNotFoundException, EventPublisher, FundRepository, UserRepository

class FundService:
    def __init__(self, user_repo: UserRepository, fund_repo: FundRepository, event_publisher: EventPublisher):
        self.user_repo = user_repo
        self.fund_repo = fund_repo
        self.event_publisher = event_publisher

    def subscribe_to_fund(self, subscription_dto: SubscriptionDTO):
        user = self.user_repo.get_by_id(subscription_dto.user_id)
        fund = self.fund_repo.find_by_id(subscription_dto.fund_id)

        if not user:
            raise UserNotFoundException(subscription_dto.fund_id)
        if not fund:
            raise FundNotFoundException(subscription_dto.fund_id)

        user.subscribe_to_fund(fund, subscription_dto.amount)
        self.user_repo.update(user)

        # enviar notificacion
        event = UserSubscribeEvent.from_user(user, fund)
        self.event_publisher.publish(event)

    def unsubscribe_from_fund(self, cancellation_dto: CancellationDTO):
        user = self.user_repo.get_by_id(cancellation_dto.user_id)
        fund = self.fund_repo.find_by_id(cancellation_dto.fund_id)

        if not user:
            raise UserNotFoundException(cancellation_dto.fund_id)
        if not fund:
            raise FundNotFoundException(cancellation_dto.fund_id)

        user.cancel_fund_subscription(fund)
        self.user_repo.update(user)
        
        # enviar notificacion
        event = UserSubscribeEvent.from_user(user, fund)
        self.event_publisher.publish(event)

    def get_all_funds(self) -> List[FundDTO]:
        #TODO: Hacer el Mappeo del Dominio al DTO
        return self.fund_repo.get_all()