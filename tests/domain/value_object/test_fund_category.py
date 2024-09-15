import pytest

from domain import FundCategory

class TestFundCategory:

    def test_category_initialization(self):
        category = FundCategory(category="FPV")
        # Verifica que el valor sea una categoría válida
        assert category.category == 'FPV'

    def test_category_invalid(self):
        with pytest.raises(ValueError):
            FundCategory(category="PRUEBA")
