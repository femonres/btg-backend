from typing import Dict

from domain import User, Fund, Subscription, Amount, NotificationType, FundCategory


class UserDAO:

    @staticmethod
    def to_dynamo_item(user: User):
        return {
            'PK': f'CLIENT#{user.id}',
            'SK': f'#METADATA#{user.id}',
            'Name': user.name,
            'Email': user.email,
            'Phone': user.phone,
            'Notification': user.notification.value,
            'Balance': str(user.balance.value),
            'Subscriptions': [
                {
                    'FundID': str(subscription.fund.id),
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
            fund = Fund(id=int(sub['FundID']), name="", min_amount=Amount(0), category=FundCategory(category="FPV"))  # Mejorar
            user.subscriptions.append(Subscription(fund=fund, amount=Amount(sub['Amount'])))
        return user