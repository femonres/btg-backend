from domain import NotificationType, User


class NotificationService:
    def send_notification(self, user: 'User', notification_type: NotificationType, message: str):
        if notification_type == NotificationType.EMAIL:
            self._send_email(user.email, message)
        elif notification_type == NotificationType.SMS:
            self._send_sms(user.phone, message)

    def _send_email(self, email: str, message: str):
        # Lógica para enviar un email
        pass

    def _send_sms(self, phone: str, message: str):
        # Lógica para enviar un SMS
        pass