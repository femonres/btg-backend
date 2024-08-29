from domain import Transaction, Amount
from application.dto.transacction_dto import TransactionDTO

class TransactionMapper:
    @staticmethod
    def from_entity(transaction: 'Transaction') -> TransactionDTO:
        return TransactionDTO(
            transaction_id=transaction.transaction_id,
            fund_id=transaction.fund_id,
            amount=transaction.amount.value,
            timestamp=transaction.timestamp.time.isoformat()
        )