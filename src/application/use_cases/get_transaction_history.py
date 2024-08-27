from application import UserService
from domain import UserNotFoundException
from utils.error_utils import handle_exception


class GetTransactionHistoryUseCase:
    def __init__(self, user_service: UserService)  -> None:
        self.user_service = user_service

    def execute(self, user_id: str):
        try:
            return self.user_service.get_transaction_history(user_id)
        except UserNotFoundException as e:
            handle_exception(e)
            raise