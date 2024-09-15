import pytest

from application.dto.fund_dto import FundDTO
from application.mapper.fund_mapper import FundMapper
from domain import Fund, Amount, FundCategory

@pytest.fixture
def fund():
    return Fund(id=1, name="FPV_BTG_PACTUAL_RECAUDADORA", min_amount=Amount(75000), category=FundCategory('FPV'))

@pytest.fixture
def fund_dto():
    return FundDTO(id=1, name="FPV_BTG_PACTUAL_RECAUDADORA", min_amount=75000, category="FPV")

def test_fund_mapper_from_entity(fund: Fund):
    dto = FundMapper.from_entity(fund)
    
    assert isinstance(dto, FundDTO)
    assert dto.id == fund.id
    assert dto.name == fund.name
    assert dto.min_amount == fund.min_amount.value
    assert dto.category == fund.category.category

def test_fund_mapper_to_entity(fund_dto: FundDTO):
    fund = FundMapper.to_entity(fund_dto)
    
    assert isinstance(fund, Fund)
    assert fund.id == fund_dto.id
    assert fund.name == fund_dto.name
    assert fund.min_amount.value == fund_dto.min_amount
    assert fund.category.category == fund_dto.category