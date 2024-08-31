from domain import Transaction
from application.dto.transacction_dto import TransactionDTO

class TransactionMapper:
    @staticmethod
    def from_entity(transaction: 'Transaction') -> TransactionDTO:
        return TransactionDTO(
            transaction_id=transaction.transaction_id.id,
            user_id=transaction.user_id,
            fund_id=transaction.fund_id,
            fund_name=transaction.fund_name,
            amount=transaction.amount.value,
            timestamp=transaction.timestamp.isoformat(),
            transaction_type=transaction.transaction_type.value
        )