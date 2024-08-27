import boto3

from domain import EventPublisher, PreferNotification, DomainEvent, UserSubscribeEvent, UserUnsubscribeEvent
from utils.error_utils import log_info

class EventPublisherImpl(EventPublisher):
    def __init__(self):
        self.sns_client = boto3.client('sns', region_name='us-east-1')
        self.sms_topic_arn = "arn:aws:sns:us-east-1:123456789012:sms-topic"
        self.email_topic_arn = "arn:aws:sns:us-east-1:123456789012:email-topic"


    def publish(self, event: DomainEvent):
        log_info(f"Evento publicado: {event}")
        if isinstance(event, UserSubscribeEvent):
            self.handle_subscription(event)
        elif isinstance(event, UserUnsubscribeEvent):
            self.handle_cancellation(event)

    def handle_subscription(self, event: UserSubscribeEvent):
        user = event.user
        if user.notification == PreferNotification.EMAIL:
            self._publish_to_sns(self.email_topic_arn, f"Gracias por suscribirte, {user.name}!")
        elif user.notification == PreferNotification.PHONE:
            self._publish_to_sns(self.sms_topic_arn, f"Gracias por suscribirte, {user.name}!")

    def handle_cancellation(self, event: UserUnsubscribeEvent):
        user = event.user
        if user.notification == PreferNotification.EMAIL:
            self._publish_to_sns(self.email_topic_arn, f"Lamentamos que te vayas, {user.name}.")
        elif user.notification == PreferNotification.SMS:
            self._publish_to_sns(self.sms_topic_arn, f"Lamentamos que te vayas, {user.name}.")

    def _publish_to_sns(self, topic_arn, message):
        self.sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject="Notificación de Evento",
        )
