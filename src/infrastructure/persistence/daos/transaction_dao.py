import datetime
from typing import Dict

from domain import TransactionStatus, TransactionType, Transaction, Amount, Identifier


class TransactionDAO:

    @staticmethod
    def to_dynamo_item(transaction: Transaction) -> Dict:
        return {
            'id': transaction.transaction_id.id,
            'fund_id': transaction.fund_id,
            'amount': transaction.amount,
            'timestamp': transaction.timestamp.isoformat(),
            'transaction_type': transaction.transaction_type.value,
            'status': transaction.status.value
        }

    @staticmethod
    def from_dynamo_item(item: Dict) -> Transaction:
        return Transaction(
            transaction_id=Identifier(item['id']),
            fund_id=item['fund_id'],
            amount=Amount(item['amount']),
            timestamp=datetime.fromisoformat(item['timestamp']),
            transaction_type=TransactionType(item['transaction_type']),
            status=TransactionStatus(item['status'])
        )