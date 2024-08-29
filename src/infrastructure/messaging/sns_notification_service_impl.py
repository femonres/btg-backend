import boto3

from domain import User, NotificationType
from application import NotificationService
from utils.error_utils import log_info

class SNSNotificationServiceImpl(NotificationService):
    def __init__(self):
        self.sns_client = boto3.client('sns', region_name='us-east-1')
        self.sms_topic_arn = "arn:aws:sns:us-east-1:123456789012:sms-topic" #Remplazar por el AccountID de AWS
        self.email_topic_arn = "arn:aws:sns:us-east-1:123456789012:email-topic"

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
        self._publish_to_sns(self.email_topic_arn, attributes, user_name=username, message=message)
        

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
        self._publish_to_sns(self.sms_topic_arn, attributes, user_name=username, message=message)
        
        
    def _publish_to_sns(self, topic_arn, attributes, user_name: str, message: str):
        self.sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=f"Notificación para {user_name}",
            MessageAttributes=attributes
        )
