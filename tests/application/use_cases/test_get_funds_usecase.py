from typing import List
import pytest
from domain import Amount, Fund, FundCategory
from application import GetFundsUsecase

@pytest.fixture
def funds():
    fund1 = Fund(id=1, name="FPV_BTG_PACTUAL_RECAUDADORA", min_amount=Amount(75000), category=FundCategory(category='FPV'))
    fund2 = Fund(id=2, name="FPV_BTG_PACTUAL_ECOPETROL", min_amount=Amount(125000), category=FundCategory(category='FPV'))
    funds_list: List[Fund] = []
    funds_list.append(fund1)
    funds_list.append(fund2)
    return funds_list

def test_get_all_funds(mocker, funds):
    mock_fund_service = mocker.Mock()
    use_case = GetFundsUsecase(mock_fund_service)

    use_case.execute()
    
    assert len(funds) == 2