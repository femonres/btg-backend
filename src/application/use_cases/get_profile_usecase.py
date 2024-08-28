from application.services.user_service import UserService
from application.mapper.user_mapper import UserMapper
from application.dto.user_dto import UserDTO


class GetProfileUseCase:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def execute(self, user_id: int) -> UserDTO:
        return UserMapper.from_entity(self.user_service.get_user_profile(user_id))