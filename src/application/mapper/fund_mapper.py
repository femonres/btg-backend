from domain import Fund, Amount, FundCategory
from application.dto.fund_dto import FundDTO


class FundMapper:
    @staticmethod
    def from_entity(fund: 'Fund') -> FundDTO:
        return FundDTO(
            id=fund.id,
            name=fund.name,
            min_amount=fund.min_amount.value,
            category=fund.category.category
        )

    @staticmethod
    def to_entity(dto: FundDTO) -> Fund:
        return Fund(
            id=dto.id,
            name=dto.name,
            min_amount=Amount(dto.min_amount),
            category=FundCategory(dto.category)
        )