import pytest

from domain import Fund, Amount, FundCategory


class TestFund:

    def test_fund_initialization(self):
        fund = Fund(id=1, name="FPV_BTG_PACTUAL_RECAUDADORA", min_amount=Amount(1000), category=FundCategory("FPV"))

        # Verifica que el constructor inicialize correctamente los atributos.
        assert fund.id == 1
        assert fund.name == "FPV_BTG_PACTUAL_RECAUDADORA"
        assert fund.min_amount.value == 1000
        assert fund.category.category == "FPV"

    def test_invalid_category(self):
        with pytest.raises(ValueError):
            # Verifica que solo se pueda crear fondos con la categoria indicada
            Fund(id=1, name='FPV_BTG_PACTUAL_RECAUDADORA', min_amount=Amount(1000), category=FundCategory('TEST'))

    def test_can_invest_with_sufficient_amount(self):
        fund = Fund(id=1, name="FPV_BTG_PACTUAL_RECAUDADORA", min_amount=Amount(1000), category=FundCategory("FPV"))
        # Verifica que la cantidad invertida es mayor o igual al monto mínimo requerido.
        assert fund.can_invest(Amount(1500)) is True

    def test_can_invest_with_insufficient_amount(self):
        fund = Fund(id=1, name="FPV_BTG_PACTUAL_RECAUDADORA", min_amount=Amount(1000), category=FundCategory("FPV"))
        # Verifica que la cantidad invertida es menor que el monto mínimo requerido.
        assert fund.can_invest(Amount(500)) is False
