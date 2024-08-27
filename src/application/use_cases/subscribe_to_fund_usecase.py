from application import SubscriptionDTO, FundService
from domain import FundNotFoundException, InsufficientBalanceException
from utils.error_utils import handle_exception
    
class SubscribeToFundUseCase:
    def __init__(self, fund_service: FundService)  -> None:
        self.fund_service = fund_service

    def execute(self, subscription_dto: SubscriptionDTO):
        try:
            self.fund_service.subscribe_to_fund(subscription_dto)
        except InsufficientBalanceException as e:
            handle_exception(e)
            raise e
        except FundNotFoundException as e:
            handle_exception(e)
            raise e