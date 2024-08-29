from domain import Amount, Transaction, UserRepository, FundRepository, TransactionRepository, ValidationStrategy
from domain import FundNotFoundException, UserNotFoundException

class SubscriptionService:
    def __init__(self, user_repository: 'UserRepository', fund_repository: 'FundRepository', transaction_repository: 'TransactionRepository'):
        self.user_repository = user_repository
        self.fund_repository = fund_repository
        self.transaction_repository = transaction_repository

    def subscribe_to_fund(self, user_id: int, fund_id: int, amount: int, validations: list[ValidationStrategy]):
        user = self.user_repository.get_by_id(user_id)
        fund = self.fund_repository.get_by_id(fund_id)

        print("==========================================")
        print(user.name)
        print("==========================================")
        print(fund.name)
        print("==========================================")

        if not user:
            raise UserNotFoundException(user_id)
        
        if not fund:
            raise FundNotFoundException(fund_id)
        
        user.validations = validations
        transaction = user.subscribe_to_fund(fund, Amount(amount))
        
        self.user_repository.save(user)
        self.transaction_repository.save(transaction)
        
        return transaction, user

    def unsubscribe_from_fund(self, user_id: int, fund_id: int):
        user = self.user_repository.get_by_id(user_id)
        fund = self.fund_repository.get_by_id(fund_id)
        
        transaction = user.cancel_fund_subscription(fund)
        
        self.user_repository.save(user)
        self.transaction_repository.save(transaction)
        
        return transaction, user

    def get_transaction_history(self, user_id: int) -> list['Transaction']:
        return self.transaction_repository.find_by_user_id(user_id)