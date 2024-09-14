from datetime import datetime
from typing import Dict

from domain import TransactionType, Transaction, Amount, Identifier


class TransactionDAO:

    @staticmethod
    def to_dynamo_item(transaction: Transaction):
        return {
            'PK': str(transaction.transaction_id.id),
            'ClientID': str(transaction.user_id),
            'FundID': str(transaction.fund_id),
            'FundName': transaction.fund_name,
            'Amount': transaction.amount.value,
            'Timestamp': transaction.timestamp.isoformat(),
            'TransactionType': transaction.transaction_type.value,
        }

    @staticmethod
    def from_dynamo_item(item: Dict) -> Transaction:
        transaction = Transaction(
            user_id=int(item['ClientID']),
            fund_id=int(item['FundID']),
            fund_name=str(item['FundName']),
            amount=Amount(int(item['Amount'])),
            transaction_type=TransactionType[item['TransactionType']]
        )
        transaction.transaction_id = Identifier(item['PK'])
        transaction.timestamp = datetime.fromisoformat(item['Timestamp'])
        
        return transaction