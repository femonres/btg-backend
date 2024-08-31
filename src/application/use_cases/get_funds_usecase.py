from application.dto.fund_dto import FundDTO
from application.services.fund_service import FundService
from application.mapper.fund_mapper import FundMapper

class GetFundsUsecase:
    def __init__(self, fund_service: FundService) -> None:
        self.fund_service = fund_service

    def execute(self) -> list[FundDTO]:
        funds = self.fund_service.get_all_funds()
        return [FundMapper.from_entity(f) for f in funds]