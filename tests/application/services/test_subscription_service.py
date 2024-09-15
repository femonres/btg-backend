import pytest
from unittest.mock import MagicMock

from application import SubscriptionService
from domain import (
    Fund, User, Transaction, ValidationStrategy,
    FundRepository,
    TransactionRepository,
    UserRepository,
    Amount, FundCategory, TransactionType)


@pytest.fixture
def setup_mocks():
    # Crear los mocks para los reposiories
    user_repo = MagicMock(UserRepository)
    fund_repo = MagicMock(FundRepository)
    transaction_repo = MagicMock(TransactionRepository)
    
    # Crear objetos de dominio para pruebas
    user = MagicMock(User)
    fund = Fund(id=1, name="FPV_BTG_PACTUAL_RECAUDADORA", min_amount=Amount(75000), category=FundCategory('FPV'))
    
    transaction = Transaction(
        user_id=1,
        fund_id=1,
        fund_name="FPV_BTG_PACTUAL_RECAUDADORA",
        amount=Amount(80000),
        transaction_type=TransactionType.OPENING
    )
    
    # Configurar los mocks
    user_repo.get_by_id.return_value = user
    fund_repo.get_by_id.return_value = fund
    user.subscribe_to_fund.return_value = transaction
    user.cancel_fund_subscription.return_value = transaction
    transaction_repo.find_by_user_id.return_value = [transaction]
    
    # Crear instancia del servicio con los mocks
    subscription_service = SubscriptionService(user_repo, fund_repo, transaction_repo)
    
    return {
        'subscription_service': subscription_service,
        'user_repo': user_repo,
        'fund_repo': fund_repo,
        'transaction_repo': transaction_repo,
        'user': user,
        'fund': fund,
        'transaction': transaction
    }

def test_subscribe_to_fund(setup_mocks):
    service = setup_mocks['subscription_service']
    user_repo = setup_mocks['user_repo']
    fund_repo = setup_mocks['fund_repo']
    transaction_repo = setup_mocks['transaction_repo']
    user = setup_mocks['user']
    fund = setup_mocks['fund']
    transaction = setup_mocks['transaction']

    validations = [MagicMock(ValidationStrategy)]
    
    result_transaction, result_user = service.subscribe_to_fund(
        user_id=1,
        fund_id=1,
        amount=50,
        validations=validations
    )
    
    user_repo.get_by_id.assert_called_once_with(1)
    fund_repo.get_by_id.assert_called_once_with(1)
    user.subscribe_to_fund.assert_called_once_with(fund, Amount(50))
    user_repo.save.assert_called_once_with(user)
    transaction_repo.save.assert_called_once_with(transaction)
    
    assert result_transaction == transaction
    assert result_user == user

def test_unsubscribe_from_fund(setup_mocks):
    service = setup_mocks['subscription_service']
    user_repo = setup_mocks['user_repo']
    fund_repo = setup_mocks['fund_repo']
    transaction_repo = setup_mocks['transaction_repo']
    user = setup_mocks['user']
    fund = setup_mocks['fund']
    transaction = setup_mocks['transaction']

    result_transaction, result_user = service.unsubscribe_from_fund(
        user_id=1,
        fund_id=1
    )
    
    user_repo.get_by_id.assert_called_once_with(1)
    fund_repo.get_by_id.assert_called_once_with(1)
    user.cancel_fund_subscription.assert_called_once_with(fund)
    user_repo.save.assert_called_once_with(user)
    transaction_repo.save.assert_called_once_with(transaction)
    
    assert result_transaction == transaction
    assert result_user == user

def test_get_transaction_history(setup_mocks):
    service = setup_mocks['subscription_service']
    transaction_repo = setup_mocks['transaction_repo']
    transaction = setup_mocks['transaction']

    result = service.get_transaction_history(user_id=1)

    transaction_repo.find_by_user_id.assert_called_once_with(1)
    assert result == [transaction]