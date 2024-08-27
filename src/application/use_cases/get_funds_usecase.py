from application import FundService


class GetFundsUsecase:
    def __init__(self, fund_service: FundService) -> None:
        self.fund_service = fund_service

    def execute(self):
        return self.fund_service.get_all_funds()