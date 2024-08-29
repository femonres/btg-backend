from application import GetProfileUseCase, GetTransactionHistoryUseCase, ResetBalanceUseCase, UpdateUserProfileUseCase
from interfaces.api.schemas.user_schemas import UserResponse, UserCreate
from interfaces.api.schemas.transaction_schemas import TransactionResponse


class UserController:
    def __init__(self, profile_usecase: GetProfileUseCase, update_profile_usecase: UpdateUserProfileUseCase, reset_balance_usecase: ResetBalanceUseCase, transaction_history_usecase: GetTransactionHistoryUseCase) -> None:
        self.profile_usecase = profile_usecase
        self.update_profile_usecase = update_profile_usecase
        self.reset_balance_usecase = reset_balance_usecase
        self.transaction_history_usecase = transaction_history_usecase

    def fetch_all(self) -> list[UserResponse]:
        user = self.profile_usecase.execute(1)
        return  [UserResponse.model_validate(user)]

    def get_profile(self, user_id: int) -> UserResponse:
        user = self.profile_usecase.execute(user_id)
        return  UserResponse.model_validate(user)
    
    def update_profile(self, user_id: int, user: UserCreate) -> UserResponse:
        user = self.update_profile_usecase.execute(user_id, user)
        return UserResponse.model_validate(user)
    
    def reset_balance(self, user_id: int) -> UserResponse:
        user = self.reset_balance_usecase.execute(user_id)
        return UserResponse.model_validate(user)

    def get_transaction_history(self, user_id: int) -> list[TransactionResponse]:
        transactions = self.transaction_history_usecase.execute(user_id)
        return [TransactionResponse.model_validate(tx) for tx in transactions]