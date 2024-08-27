import unittest

from domain import Fund, Amount, FundCategory


class TestFund(unittest.TestCase):
    def test_fund_creation(self):
        fund = Fund(
            id=1,
            name='FPV_BTG_PACTUAL_RECAUDADORA',
            min_amount=Amount(75000),
            category=FundCategory(category='FPV')
        )

        # Verifica que el fondo se haya creado correctamente
        self.assertEqual(fund.min_amount.value, 75000)
        self.assertEqual(fund.name, 'FPV_BTG_PACTUAL_RECAUDADORA')

    def test_invalid_fund_category(self):
        with self.assertRaises(ValueError):
            # Verifica que solo se pueda crear fondos con la categoria indicada
            Fund(
                id=1,
                name='FPV_BTG_PACTUAL_RECAUDADORA',
                min_amount=Amount(75000),
                category=FundCategory(category='TEST')
            )