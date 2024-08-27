from application import UserDTO, UserService


class UpdateUserProfileUseCase:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def execute(self, user_id: int, user_dto: UserDTO):
        return self.user_service.update_profile(user_id, user_dto)