import pytest
from unittest.mock import MagicMock

from domain import Fund, Amount, FundCategory, FundRepository
from application import FundService



@pytest.fixture
def setup_mocks():
    fund_repo = MagicMock(FundRepository)
    
    fund1 = Fund(id=1, name="FPV_BTG_PACTUAL_RECAUDADORA", min_amount=Amount(75000), category=FundCategory('FPV'))
    fund2 = Fund(id=2, name="FPV_BTG_PACTUAL_ECOPETROL", min_amount=Amount(125000), category=FundCategory('FPV'))
    fund_repo.get_all.return_value = [fund1, fund2]

    fund_service = FundService(fund_repo)
    
    return {
        'fund_service': fund_service,
        'fund_repo': fund_repo,
        'funds': [fund1, fund2]
    }

def test_get_all_funds(setup_mocks):
    fund_service = setup_mocks['fund_service']
    fund_repo = setup_mocks['fund_repo']
    expected_funds = setup_mocks['funds']

    # Ejecutar
    actual_funds = fund_service.get_all_funds()
    
    fund_repo.get_all.assert_called_once()
    
    # Verificar
    assert actual_funds == expected_funds