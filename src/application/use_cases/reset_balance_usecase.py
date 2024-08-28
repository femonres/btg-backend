from application.services.user_service import UserService
from application.mapper.user_mapper import UserMapper
from application.dto.user_dto import UserDTO, SaveUserDTO


class ResetBalanceUseCase:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def execute(self, user_id: int) -> UserDTO:
        user = self.user_service.reset_balance(user_id)
        return UserMapper.from_entity(user)