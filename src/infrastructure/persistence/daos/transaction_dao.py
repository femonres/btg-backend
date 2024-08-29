import datetime
from typing import Dict

from domain import TransactionType, Transaction, Amount, Identifier


class TransactionDAO:

    @staticmethod
    def to_dynamo_item(transaction: Transaction):
        return {
            'PK': f'CLIENT#{transaction.user_id}',
            'SK': f'TRANSACTION#{transaction.transaction_id}',
            'UserID': transaction.fund_id,
            'FundID': transaction.fund_id,
            'Amount': transaction.amount.value,
            'Timestamp': transaction.timestamp.time.isoformat(),
            'TransactionType': transaction.transaction_type.value,
        }

    @staticmethod
    def from_dynamo_item(item: Dict) -> Transaction:
        transaction = Transaction(
            user_id=int(item['FundID']),
            fund_id=int(item['FundID']),
            amount=Amount(item['Amount']),
            type=TransactionType[item['TransactionType']]
        )
        transaction.timestamp = datetime.time.fromisoformat(item['Timestamp'])
        
        return transaction