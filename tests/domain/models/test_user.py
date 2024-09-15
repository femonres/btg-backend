import pytest

from domain import User, Fund, Amount, FundCategory, TransactionType, NotificationType, ValidationStrategy, SubscriptionNotFoundException

@pytest.fixture
def user():
    return User(
        id=1,
        name="John Doe",
        email="john.doe@example.com",
        phone="+573104567890",
        notification=NotificationType.EMAIL,
        balance=Amount(500000))
    
@pytest.fixture
def fund():
    return Fund(
        id=1,
        name="FPV_BTG_PACTUAL_RECAUDADORA",
        min_amount=Amount(75000),
        category=FundCategory(category='FPV'))

class TestUser:

    def test_subscribe_to_fund(self, user: User, fund: Fund):
        # Suscribe al cliente al fondo
        transaction = user.subscribe_to_fund(fund, Amount(80000))
        
        # Verifica que el saldo se haya actualizado
        assert user.balance.value == 420000
        
        # Verifica que la transacción haya sido registrada
        assert len(user.subscriptions) == 1
        assert user.subscriptions[0].fund_id == fund.id
        assert user.subscriptions[0].amount.value == 80000

        # Verifica que la transacción haya sido registrada
        assert transaction.fund_id == fund.id
        assert transaction.amount.value == 80000
        assert transaction.transaction_type == TransactionType.OPENING

    def test_unsubscribe_from_fund(self, user: User, fund: Fund):
        # Se suscribe y luego cancela la suscripción
        user.subscribe_to_fund(fund, Amount(80000))
        transaction = user.cancel_fund_subscription(fund)
        
        # Verifica que la suscripción se haya cancelado
        assert len(user.subscriptions) == 0

        # Verifica que el saldo se haya restablecido
        assert user.balance.value == 500000
        
        # Verifica que la transacción de cancelación se haya registrado
        assert transaction.amount.value == 80000
        assert transaction.transaction_type == TransactionType.CANCELLATION

    def test_cancel_non_existent_subscription(self, user: User, fund: Fund):
        # Intentar canelar un suscripcion que no esta registrada
        with pytest.raises(SubscriptionNotFoundException):
            user.cancel_fund_subscription(fund)

    def test_is_subscribed(self, user: User, fund: Fund):
        amount = Amount(80000)
        user.subscribe_to_fund(fund, amount)
        assert user.is_subscribed(fund) is True

    def test_get_subscription(self, user: User, fund: Fund):
        amount = Amount(80000)
        user.subscribe_to_fund(fund, amount)
        subscription = user.get_subscription(fund)
        assert subscription is not None
        assert subscription.fund_id == fund.id