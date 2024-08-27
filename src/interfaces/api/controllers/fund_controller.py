from typing import List

from domain import FundNotFoundException, InsufficientBalanceException
from application import GetFundsUsecase, SubscribeToFundUseCase, UnsubscribeOfFundUseCase
from interfaces.api.schemas.schemas import FundSchema, SubscriptionSchema, TransactionSchema
from utils.error_utils import handle_exception


class FundController:
    def __init__(self, get_funds_usecase: GetFundsUsecase, subscribe_usecase: SubscribeToFundUseCase, unsubscribe_usecase: UnsubscribeOfFundUseCase):
        self.all_funds_usecase = get_funds_usecase
        self.subscribe_usecase = subscribe_usecase
        self.unsubscribe_usecase = unsubscribe_usecase

    def get_all_funds(self) -> List[FundSchema]:
        funds = self.all_funds_usecase.execute()
        return [FundSchema.from_domain(tx) for tx in funds]

    def subscribe(self, subscription_schema: SubscriptionSchema) -> TransactionSchema:
        try:
            dto = subscription_schema.to_domain()
            transaction = self.subscribe_usecase.execute(dto)
            return TransactionSchema.from_domain(transaction)
        except FundNotFoundException as e:
            handle_exception(e)
            raise
        except InsufficientBalanceException as e:
            handle_exception(e)
            raise

    def unsubscribe(self, subscription_schema: SubscriptionSchema) -> TransactionSchema:
        try:
            dto = subscription_schema.to_domain()
            transaction = self.unsubscribe_usecase.execute(dto)
            return TransactionSchema.from_domain(transaction)
        except FundNotFoundException as e:
            handle_exception(e)
            raise
