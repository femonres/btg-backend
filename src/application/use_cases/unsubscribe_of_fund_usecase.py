from application import CancellationDTO, FundService
from domain import FundNotFoundException
from utils.error_utils import handle_exception


class UnsubscribeOfFundUseCase:
    def __init__(self, fund_service: FundService)  -> None:
        self.fund_service = fund_service

    def execute(self, cancellation_dto: CancellationDTO):
        try:
            self.fund_service.unsubscribe_from_fund(cancellation_dto)
        except FundNotFoundException as e:
            handle_exception(e)
            raise