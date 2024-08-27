import unittest

from domain import FundCategory

class TestFundCategory(unittest.TestCase):

    def test_category_creation(self):
        category = FundCategory(category="FPV")
        # Verifica que el valor sea una categoría válida
        self.assertEqual(category.category, 'FPV')

    def test_category_invalid(self):
        with self.assertRaises(ValueError):
            FundCategory(category="PRUEBA")
