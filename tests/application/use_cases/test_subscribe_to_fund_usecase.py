import pytest
from datetime import datetime
from unittest.mock import MagicMock, patch

from domain import Amount, Transaction, TransactionType
from application import SubscribeToFundUseCase, CreateSubscriptionDTO, TransactionDTO, SubscriptionAlreadyValidation, InsufficientBalanceValidation, MinimumAmountValidation
from utils.formatters import format_currency


@pytest.fixture
def setup_mocks():
    subscription_service = MagicMock()
    notification_service = MagicMock()
    transaction_mapper = MagicMock()

    transaction = Transaction(user_id=1, fund_id=1, fund_name='FPV_BTG_PACTUAL_RECAUDADORA', amount=Amount(50000), transaction_type=TransactionType.OPENING)
    user = MagicMock()

    subscription_service.subscribe_to_fund.return_value = (transaction, user)
    transaction_mapper.from_entity.return_value = transaction

    return {
        'subscription_service': subscription_service,
        'notification_service': notification_service,
        'transaction_mapper': transaction_mapper,
        'transaction': transaction,
        'user': user
    }

def test_subscribe_to_fund_success(setup_mocks):
    subscription_service = setup_mocks['subscription_service']
    notification_service = setup_mocks['notification_service']
    transaction_mapper = setup_mocks['transaction_mapper']
    transaction = setup_mocks['transaction']
    user = setup_mocks['user']

    use_case = SubscribeToFundUseCase(subscription_service, notification_service)
    
    dto = CreateSubscriptionDTO(user_id=1, fund_id=1, amount=50000)
    result = use_case.execute(dto)

    validate_polices = [SubscriptionAlreadyValidation(), InsufficientBalanceValidation(), MinimumAmountValidation()]
    subscription_service.subscribe_to_fund.assert_called_once_with(dto.user_id, dto.fund_id, dto.amount, validate_polices)

    # Verificar que la notificación fue enviada correctamente
    message = f"Suscripción exitosa al fondo {dto.fund_id} por un monto de {format_currency(dto.amount)}."
    notification_service.send_notification.assert_called_once_with(user, user.notification, message)
    
    # Verificar que el mapper transformó correctamente el objeto de transacción
    transaction_mapper.from_entity.assert_called_once_with(transaction)
    assert result == transaction_mapper.from_entity.return_value

@patch('application.mapper.transacction_mapper.TransactionMapper')
def test_subscribe_to_fund_use_case_mapping(mock_transaction_mapper, setup_mocks):
    subscription_service = setup_mocks['subscription_service']
    notification_service = setup_mocks['notification_service']
    
    mock_transaction_mapper.from_entity.return_value = TransactionDTO(transaction_id="12345", user_id=1, fund_id=1, fund_name='FPV_BTG_PACTUAL_RECAUDADORA', amount=50000, timestamp=datetime.now().isoformat(), transaction_type=TransactionType.OPENING)
    
    use_case = SubscribeToFundUseCase(subscription_service, notification_service)
    
    dto = CreateSubscriptionDTO(user_id=1, fund_id=1, amount=Amount(50000))
    
    result = use_case.execute(dto)
    
    # Verificar que el mapper es llamado y el resultado es como se espera
    mock_transaction_mapper.from_entity.assert_called_once()
    assert result == mock_transaction_mapper.from_entity.return_value
