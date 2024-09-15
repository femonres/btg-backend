import pytest

from domain import Amount

class TestAmountValueObject():

    def test_amount_creation(self):
        amount = Amount(100)
        
        # Verifica que el valor se haya establecido correctamente
        assert amount.value == 100

    def test_amount_negative_value(self):
        with pytest.raises(ValueError, match="El monto no puede ser negativo"):
            # Verifica que no se pueda crear un Amount con valor negativo
            Amount(-50)

    def test_amount_equality(self):
        amount1 = Amount(100)
        amount2 = Amount(100)
        amount3 = Amount(200)
        assert amount1 == amount2
        assert amount1 != amount3

    def test_amount_addition(self):
        amount1 = Amount(100)
        amount2 = Amount(50)
        result = amount1 + amount2
        assert result == Amount(150)

    def test_amount_addition_invalid_type(self):
        amount1 = Amount(100)
        with pytest.raises(ValueError, match="Operación inválida"):
            amount1 + 50

    def test_amount_subtraction(self):
        amount1 = Amount(100)
        amount2 = Amount(50)
        result = amount1 - amount2
        assert result == Amount(50)

    def test_amount_subtraction_invalid_type(self):
        amount1 = Amount(100)
        with pytest.raises(ValueError, match="Operación inválida"):
            amount1 - 50

    def test_amount_repr(self):
        amount = Amount(100)
        assert repr(amount) == "Amount(100)"
