import unittest

from domain import TransactionStatus, TransactionType, Transaction, Amount, Identifier


class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        transaction = Transaction(
            transaction_id=Identifier.generate(),
            fund_id=1,
            amount=Amount(75000),
            transaction_type=TransactionType.OPENING,
            status=TransactionStatus.COMPLETED
        )
        
        # Verifica que la transacción se haya creado correctamente
        self.assertEqual(transaction.amount.value, 75000)
        self.assertEqual(transaction.status, TransactionStatus.COMPLETED)

    def test_invalid_transaction_amount(self):
        with self.assertRaises(ValueError):
            # Verifica que no se puede crear una transacción con un monto negativo
            Transaction(
                transaction_id=Identifier.generate(),
                fund_id=1,
                amount=Amount(-100),
                transaction_type=TransactionType.OPENING,
                status=TransactionStatus.COMPLETED
            )