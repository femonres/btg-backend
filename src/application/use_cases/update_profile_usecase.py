from application.services.user_service import UserService
from application.mapper.user_mapper import UserMapper
from application.dto.user_dto import UserDTO, SaveUserDTO


class UpdateUserProfileUseCase:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def execute(self, user_id: int, user_dto: SaveUserDTO) -> UserDTO:
        user = self.user_service.update_profile(user_id, user_dto)
        return UserMapper.from_entity(user)