from application.services.subscription_service import SubscriptionService
from application.services.notification_service import NotificationService
from application.dto.subscription_dto import CreateSubscriptionDTO
from application.mapper.transacction_mapper import TransactionMapper
from application.services.strategies.subscription_strategies import InsufficientBalanceValidation, MinimumAmountValidation, SubscriptionAlreadyValidation
from utils.formatters import format_currency
    
class SubscribeToFundUseCase:
    def __init__(self, subscription_service: 'SubscriptionService', notification_service: 'NotificationService'):
        self.subscription_service = subscription_service
        self.notification_service = notification_service

    def execute(self, dto: CreateSubscriptionDTO):
        validations_policies = [SubscriptionAlreadyValidation(), InsufficientBalanceValidation(), MinimumAmountValidation()]

        transaction, user = self.subscription_service.subscribe_to_fund(dto.user_id, dto.fund_id, dto.amount, validations_policies)

        # Enviar notificación
        message = f"Suscripción exitosa al fondo {transaction.fund_name} por un monto de {format_currency(transaction.amount.value)}."
        self.notification_service.send_notification(user, user.notification, message)
        
        return TransactionMapper.from_entity(transaction)
        