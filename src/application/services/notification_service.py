from abc import abstractmethod
from domain import NotificationType, User


class NotificationService:

    @abstractmethod
    def send_notification(self, user: 'User', notification_type: NotificationType, message: str):
        pass
