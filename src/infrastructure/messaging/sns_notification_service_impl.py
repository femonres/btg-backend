import os
import boto3

from domain import User, NotificationType
from application import NotificationService
from utils.singleton import singleton
from utils.error_utils import log_info

@singleton
class SNSNotificationServiceImpl(NotificationService):
    def __init__(self):
        self.sns_client = boto3.client('sns', region_name='us-west-2')
        self.email_topic_arn = os.getenv('EMAIL_TOPIC_ARN')
        self.sms_topic_arn = os.getenv('SMS_TOPIC_ARN')

    def send_notification(self, user: 'User', notification_type: NotificationType, message: str):
        if notification_type == NotificationType.EMAIL:
            self._send_email(user.name, user.email, message)
        elif notification_type == NotificationType.PHONE:
            self._send_sms(user.name, user.phone, message)

    def _send_email(self, username: str, email: str, message: str):
        attributes = {
            'email': {
                'DataType': 'String',
                'StringValue': email
            }
        }
        self._publish_to_sns(self.email_topic_arn, attributes, subject=email, message=message)
        

    def _send_sms(self, username: str, phone: str, message: str):
        attributes = {
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String',
                'StringValue': 'Transactional'
            },
            'phone': {
                'DataType': 'String',
                'StringValue': phone
            }
        }
        self._publish_to_sns(self.sms_topic_arn, attributes, subject=phone, message=message)
        
        
    def _publish_to_sns(self, topic_arn, attributes, subject: User, message: str):
        try:
            self.sns_client.publish(
                TopicArn=topic_arn,
                Message=message,
                Subject=subject,
                MessageAttributes=attributes)
        except Exception as e:
            print(f"Error al publicar el mensaje en SNS: {e}")
