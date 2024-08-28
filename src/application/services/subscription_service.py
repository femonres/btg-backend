from typing import List
from domain import Amount, Transaction, UserRepository, FundRepository, TransactionRepository, ValidationStrategy

class SubscriptionService:
    def __init__(self, user_repository: 'UserRepository', fund_repository: 'FundRepository', transaction_repository: 'TransactionRepository'):
        self.user_repository = user_repository
        self.fund_repository = fund_repository
        self.transaction_repository = transaction_repository

    def subscribe_to_fund(self, user_id: int, fund_id: int, amount: int, validations: List[ValidationStrategy]) -> 'Transaction':
        user = self.user_repository.get_by_id(user_id)
        fund = self.fund_repository.get_by_id(fund_id)
        
        user.validations = validations
        transaction = user.subscribe_to_fund(fund, Amount(amount))
        
        self.user_repository.save(user)
        self.transaction_repository.save(transaction)
        
        return transaction

    def unsubscribe_from_fund(self, user_id: int, fund_id: int) -> 'Transaction':
        user = self.user_repository.get_by_id(user_id)
        fund = self.fund_repository.get_by_id(fund_id)
        
        transaction = user.cancel_fund_subscription(fund)
        
        self.user_repository.save(user)
        self.transaction_repository.save(transaction)
        
        return transaction

    def get_transaction_history(self, user_id: int) -> list['Transaction']:
        return self.transaction_repository.get_by_user_id(user_id)