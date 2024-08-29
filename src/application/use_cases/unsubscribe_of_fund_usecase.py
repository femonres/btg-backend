from application.services.notification_service import NotificationService
from application.services.subscription_service import SubscriptionService
from application.mapper.transacction_mapper import TransactionMapper
from application.dto.subscription_dto import CancelSubscriptionDTO


class UnsubscribeOfFundUseCase:
    def __init__(self, subscription_service: 'SubscriptionService', notification_service: 'NotificationService'):
        self.subscription_service = subscription_service
        self.notification_service = notification_service

    def execute(self, dto: CancelSubscriptionDTO):
        transaction, user = self.subscription_service.unsubscribe_from_fund(dto.user_id, dto.fund_id)
        
        # Enviar notificación
        message = f"Cancelación exitosa de la suscripción al fondo {transaction.fund_name}."
        self.notification_service.send_notification(user, user.notification, message)
        
        
        return TransactionMapper.from_entity(transaction)