import pytest
from unittest.mock import MagicMock

from domain import Amount, Fund, FundCategory
from application import GetFundsUsecase, FundService, FundDTO

@pytest.fixture
def fund_service():
    return MagicMock(spec=FundService)

@pytest.fixture
def get_funds_usecase(fund_service: FundService):
    return GetFundsUsecase(fund_service=fund_service)

@pytest.fixture
def funds():
    fund1 = Fund(id=1, name="FPV_BTG_PACTUAL_RECAUDADORA", min_amount=Amount(75000), category=FundCategory(category='FPV'))
    fund2 = Fund(id=2, name="FPV_BTG_PACTUAL_ECOPETROL", min_amount=Amount(125000), category=FundCategory(category='FPV'))
    funds_list: list[Fund] = []
    funds_list.append(fund1)
    funds_list.append(fund2)
    return funds_list

class TestGetFundsUsecase:
    
    def test_get_funds_usecase(self, get_funds_usecase: GetFundsUsecase, funds: list[Fund]):
        # Configura el mock para devolver una lista de fondos
        get_funds_usecase.fund_service.get_all_funds.return_value = funds
        
        result = get_funds_usecase.execute()
        
        assert len(result) == 2
        assert isinstance(result[0], FundDTO)
        get_funds_usecase.fund_service.get_all_funds.assert_called_once()