from typing import List

from application import TransactionDTO, UserDTO
from domain import Amount, UserRepository, UserNotFoundException
from utils.error_utils import handle_exception


class UserService:
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    def get_user_profile(self, user_id: int) -> UserDTO:
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise UserNotFoundException(user_id)
        
        #TODO: Hacer el Mappeo del Dominio al DTO
        return user


    def update_profile(self, user_id: int, user_dto: UserDTO) -> UserDTO:
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise UserNotFoundException(user_id)
        
        user.name = user_dto.name
        user.email = user_dto.email
        user.phone = user_dto.phone
        user.notification = user_dto.notification
        self.user_repo.update(user)

        #TODO: Hacer el Mappeo del Dominio al DTO
        return user
    
    def reset_balance(self, user_id: int) -> UserDTO:
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise UserNotFoundException(user_id)
        
        user.balance = Amount(500000)
        user.transactions.clear()
        self.user_repo.update(user)

        #TODO: Hacer el Mappeo del Dominio al DTO
        return user

    def get_transaction_history(self, user_id: int) -> List[TransactionDTO]:
        # Obtener el historial de transacciones del usuario
        try:
            #TODO: Hacer el Mappeo del Dominio al DTO
            return self.user_repo.get_by_id(user_id).transactions
        except UserNotFoundException as e:
            handle_exception(e)
            raise e