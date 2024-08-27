import unittest

from domain import Amount

class TestAmountValueObject(unittest.TestCase):

    def test_amount_creation(self):
        amount = Amount(100)
        
        # Verifica que el valor se haya establecido correctamente
        self.assertEqual(amount.value, 100)

    def test_amount_negative_value(self):
        with self.assertRaises(ValueError):
            # Verifica que no se puede crear un Amount con valor negativo
            Amount(-50)

    def test_amount_addition(self):
        amount1 = Amount(50)
        amount2 = Amount(25)
        total = amount1 + amount2
        
        # Verifica la suma de dos Amounts
        self.assertEqual(total.value, 75)

    def test_amount_subtraction(self):
        amount1 = Amount(50)
        amount2 = Amount(25)
        difference = amount1 - amount2
        
        # Verifica la resta de dos Amounts
        self.assertEqual(difference.value, 25)

    def test_amount_equality(self):
        amount1 = Amount(50)
        amount2 = Amount(50)
        amount3 = Amount(25)
        
        # Verifica la igualdad de Amounts
        self.assertEqual(amount1, amount2)
        self.assertNotEqual(amount1, amount3)
