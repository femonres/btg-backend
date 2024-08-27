from typing import List

from application import GetProfileUseCase, GetTransactionHistoryUseCase, ResetBalanceUseCase, UpdateUserProfileUseCase
from interfaces.api.schemas.schemas import TransactionSchema, UserSchema


class UserController:
    def __init__(self, profile_usecase: GetProfileUseCase, update_profile_usecase: UpdateUserProfileUseCase, reset_balance_usecase: ResetBalanceUseCase, transaction_history_usecase: GetTransactionHistoryUseCase) -> None:
        self.profile_usecase = profile_usecase
        self.update_profile_usecase = update_profile_usecase
        self.reset_balance_usecase = reset_balance_usecase
        self.transaction_history_usecase = transaction_history_usecase

    def get_profile(self, user_id: int) -> UserSchema:
        user = self.profile_usecase.execute(user_id)
        return UserSchema.from_domain(user)
    
    def update_profile(self, user_id: int, user_schema: UserSchema) -> UserSchema:
        user = self.update_profile_usecase.execute(user_id, user_schema.to_domain())
        return UserSchema.from_domain(user)
    
    def reset_balance(self, user_id: int) -> UserSchema:
        user = self.reset_balance_usecase.execute(user_id)
        return UserSchema.from_domain(user)

    def get_transaction_history(self, user_id: int) -> List[TransactionSchema]:
        transactions = self.transaction_history_usecase(user_id)
        return [TransactionSchema.from_domain(tx) for tx in transactions]