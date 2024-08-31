from application.services.user_service import UserService
from application.dto.user_dto import UserDTO
from application.mapper.user_mapper import UserMapper


class FetchUsersUsecase:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def execute(self) -> list[UserDTO]:
        users = self.user_service.fetch_all()
        return [UserMapper.from_entity(f) for f in users]