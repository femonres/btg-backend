import unittest

from domain import User, Fund, Amount, FundCategory, TransactionType, NotificationType, ValidationStrategy, SubscriptionNotFoundException

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(
            id=1,
            name="John Doe",
            email="john.doe@example.com",
            phone="+573104567890",
            notification=NotificationType.EMAIL,
            balance=Amount(500000)
        )
        self.fund = Fund(
            id=1,
            name="FPV_BTG_PACTUAL_RECAUDADORA",
            min_amount=Amount(75000),
            category=FundCategory(category='FPV')
        )

    def test_subscribe_to_fund_success(self):
        # Suscribe al cliente al fondo
        invest_amount = Amount(80000)
        transaction = self.user.subscribe_to_fund(self.fund, invest_amount)
        
        # Verifica que el saldo se haya actualizado
        
        # Verifica que la transacción haya sido registrada
        self.assertEqual(len(self.user.subscriptions), 1)
        self.assertEqual(self.user.subscriptions[0].fund_id, self.fund.id)
        self.assertEqual(self.user.subscriptions[0].amount, invest_amount)
        self.assertEqual(self.user.balance.value, 420000)
        self.assertEqual(transaction.fund_id, 1)
        self.assertEqual(transaction.amount.value, 80000)
        self.assertEqual(transaction.transaction_type, TransactionType.OPENING)

    def test_unsubscribe_from_fund(self):
        # Se suscribe y luego cancela la suscripción
        invest_amount = Amount(80000)
        self.user.subscribe_to_fund(self.fund, invest_amount)
        transaction = self.user.cancel_fund_subscription(self.fund)
        
        # Verifica que el saldo se haya restablecido
        self.assertEqual(self.user.balance.value, 500000)
        
        # Verifica que la transacción de cancelación se haya registrado
        self.assertEqual(transaction.amount.value, 80000)
        self.assertEqual(transaction.transaction_type, TransactionType.CANCELLATION)

    def test_unsubscribe_fund_empty(self):
        # Intentar canelar un suscripcion que no esta registrada
        with self.assertRaises(SubscriptionNotFoundException):
            self.user.cancel_fund_subscription(self.fund)
