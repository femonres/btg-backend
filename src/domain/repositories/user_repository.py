from abc import ABC, abstractmethod

from src.domain.models.user import User

class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def update(self, user: User):
        pass
