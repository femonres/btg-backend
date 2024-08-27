from application import UserService


class GetProfileUseCase:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def execute(self, user_id: int):
        return self.user_service.get_user_profile(user_id)