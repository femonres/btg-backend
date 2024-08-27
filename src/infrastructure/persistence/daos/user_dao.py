from typing import Dict

from domain import User, PreferNotification, Amount
from .transaction_dao import TransactionDAO


class UserDAO:

    @staticmethod
    def to_dynamo_item(user: User) -> Dict:
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'notification': user.notification.value,
            'balance': user.balance,
            'transactions': [TransactionDAO.to_dynamo_item(tx) for tx in user.transactions]
        }
    
    @staticmethod
    def from_dynamo_item(item: Dict) -> User:
        return User(
            id=item['id'],
            name=item['name'],
            email=item['email'],
            phone=item['phone'],
            notification=PreferNotification(item['notification']),
            balance=Amount(item['balance']),
            transactions=[TransactionDAO.from_dynamo_item(tx) for tx in item['transactions']]
        )