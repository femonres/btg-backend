from application.services.subscription_service import SubscriptionService
from application.mapper.transacction_mapper import TransactionMapper
from application.dto.transacction_dto import TransactionDTO


class GetTransactionHistoryUseCase:
    def __init__(self, subscription_service: 'SubscriptionService')  -> None:
        self.subscription_service = subscription_service

    def execute(self, user_id: str) -> list['TransactionDTO']:
        transactions = self.subscription_service.get_transaction_history(user_id)
        return [TransactionMapper.from_entity(t) for t in transactions]