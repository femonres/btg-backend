from application import UserService


class ResetBalanceUseCase:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def execute(self, user_id: int):
        return self.user_service.reset_balance(user_id)