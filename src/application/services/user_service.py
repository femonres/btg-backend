from typing import List
from domain import Amount, User, UserRepository, UserNotFoundException


class UserService:
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    def fetch_all(self) -> List[User]:
        return self.user_repo.get_all()

    def get_user_profile(self, user_id: int) -> 'User':
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise UserNotFoundException(user_id)
        
        return user

    def update_profile(self, user_id: int, user: 'User') -> 'User':
        current_user = self.user_repo.get_by_id(user_id)

        if not current_user:
            raise UserNotFoundException(user_id)
        
        current_user.name = user.name
        current_user.email = user.email
        current_user.phone = user.phone
        current_user.notification = user.notification
        self.user_repo.save(current_user)

        return current_user
    
    def reset_balance(self, user_id: int) -> 'User':
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise UserNotFoundException(user_id)
        
        user.balance = Amount(500000)
        user.subscriptions.clear()
        self.user_repo.save(user)

        return user
