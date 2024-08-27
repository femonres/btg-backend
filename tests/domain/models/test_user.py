import unittest

from domain import Fund, User, Amount, FundCategory, PreferNotification, TransactionStatus, CanInvestException, InsufficientBalanceException, SubscriptionNotFoundException


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(
            id=1,
            name="John Doe",
            email="john.doe@example.com",
            phone="+573104567890",
            notification=PreferNotification.EMAIL,
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
        self.user.subscribe_to_fund(self.fund, Amount(80000))
        
        # Verifica que el saldo se haya actualizado
        self.assertEqual(self.user.balance.value, 420000)
        
        # Verifica que la transacción haya sido registrada
        self.assertEqual(len(self.user.transactions), 1)
        transaction = self.user.transactions[0]
        self.assertEqual(transaction.amount.value, 80000)
        self.assertEqual(transaction.status, TransactionStatus.COMPLETED)

    def test_unsubscribe_from_fund(self):
        # Se suscribe y luego cancela la suscripción
        self.user.subscribe_to_fund(self.fund, Amount(80000))
        self.user.cancel_fund_subscription(self.fund)
        
        # Verifica que el saldo se haya restablecido
        self.assertEqual(self.user.balance.value, 500000)
        
        # Verifica que la transacción de cancelación se haya registrado
        self.assertEqual(len(self.user.transactions), 2)
        transaction = self.user.transactions[1]
        self.assertEqual(transaction.amount.value, 80000)
        self.assertEqual(transaction.status, TransactionStatus.CANCELLED)

    def test_subscribe_to_fund_insufficient_balance(self):
        # Intenta suscribir un fondo con un monto mayor al saldo disponible
        expensive_fund = Fund(
            id=2,
            name="FPV_BTG_PACTUAL_ECOPETROL",
            min_amount=Amount(125000),
            category=FundCategory(category='FPV')
        )
        
        with self.assertRaises(InsufficientBalanceException):
            self.user.subscribe_to_fund(expensive_fund, Amount(600000))
    
    def test_subscribe_to_fund_amount_less_than_allowed(self):
        # Intenta suscribir un fondo con un monto menor al permitido
        less_allowed = Fund(
            id=4,
            name="FDO-ACCIONES",
            min_amount=Amount(250000),
            category=FundCategory(category='FIC')
        )
        
        with self.assertRaises(CanInvestException):
            self.user.subscribe_to_fund(less_allowed, Amount(35000))

    def test_unsubscribe_fund_empty(self):
        # Intentar canelar un suscripcion que no esta registrada
        with self.assertRaises(SubscriptionNotFoundException):
            self.user.cancel_fund_subscription(self.fund)
        