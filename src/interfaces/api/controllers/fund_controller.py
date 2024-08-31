from domain import UserNotFoundException, FundNotFoundException, InsufficientBalanceException
from application import GetFundsUsecase, SubscribeToFundUseCase, UnsubscribeOfFundUseCase, CreateSubscriptionDTO, CancelSubscriptionDTO
from interfaces.api.schemas.fund_schemas import FundResponse
from interfaces.api.schemas.transaction_schemas import TransactionResponse, CreateSubscription, CancelSubscription
from utils.error_utils import handle_exception


class FundController:
    def __init__(self, get_funds_usecase: GetFundsUsecase, subscribe_usecase: SubscribeToFundUseCase, unsubscribe_usecase: UnsubscribeOfFundUseCase):
        self.get_funds_usecase = get_funds_usecase
        self.subscribe_usecase = subscribe_usecase
        self.unsubscribe_usecase = unsubscribe_usecase

    def get_all_funds(self) -> list[FundResponse]:
        funds = self.get_funds_usecase.execute()
        return [FundResponse.model_validate(tx) for tx in funds]

    def subscribe(self, fund_id: int, subscription: CreateSubscription) -> TransactionResponse:
        dto = CreateSubscriptionDTO(subscription.user_id, fund_id, subscription.amount)
        transaction = self.subscribe_usecase.execute(dto)
        return TransactionResponse.model_validate(transaction)

    def unsubscribe(self, fund_id: int, cancel: CancelSubscription) -> TransactionResponse:
        dto = CancelSubscriptionDTO(cancel.user_id, fund_id)
        transaction = self.unsubscribe_usecase.execute(dto)
        return TransactionResponse.model_validate(transaction)
