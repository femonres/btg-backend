from typing import Dict

from domain import User, Identifier, Subscription, Amount, NotificationType, FundCategory


class UserDAO:

    @staticmethod
    def to_dynamo_item(user: User):
        return {
            'PK': f'CLIENT#{user.id}',
            'Name': user.name,
            'Email': user.email,
            'Phone': user.phone,
            'Notification': user.notification.value,
            'Balance': user.balance.value,
            'Subscriptions': [
                {
                    'ID': str(subscription.subscription_id.id),
                    'FundID': str(subscription.fund_id),
                    'FundName': str(subscription.fund_name),
                    'Amount': str(subscription.amount.value)
                }
                for subscription in user.subscriptions
            ]
        }
        
    @staticmethod
    def from_dynamo_item(item: Dict) -> User:
        user = User(
            id=int(item['PK'].split('#')[1]),
            name=item['Name'],
            email=item['Email'],
            phone=item['Phone'],
            notification=NotificationType(item['Notification']),
            balance=Amount(item['Balance'])
        )
        for sub in item.get('Subscriptions', []):
            subscription = Subscription(fund_id=int(sub['FundID']), fund_name=sub['FundName'], amount=Amount(int(sub['Amount'])))
            subscription.subscription_id = Identifier(sub['ID'])
            user.subscriptions.append(subscription)

        return user