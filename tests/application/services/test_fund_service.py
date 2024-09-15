import pytest
from unittest.mock import MagicMock

from domain import Fund, Amount, FundCategory, FundRepository
from application import FundService

@pytest.fixture
def fund_service():
    fund_repo = MagicMock(FundRepository)
    return FundService(fund_repo)

@pytest.fixture
def funds():
    fund1 = Fund(id=1, name="FPV_BTG_PACTUAL_RECAUDADORA", min_amount=Amount(75000), category=FundCategory('FPV'))
    fund2 = Fund(id=2, name="FPV_BTG_PACTUAL_ECOPETROL", min_amount=Amount(125000), category=FundCategory('FPV'))
    return [fund1, fund2]

class TestFundService:
    def test_get_all_funds(self, fund_service: FundService, funds: list[Fund]):
        fund_service.fund_repo.get_all.return_value = funds

        # Ejecutar
        actual_funds = fund_service.get_all_funds()

        # Verificar
        fund_service.fund_repo.get_all.assert_called_once()
        assert actual_funds == funds