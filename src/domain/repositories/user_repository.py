from abc import ABC, abstractmethod
from typing import List

from domain import User

class UserRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def update(self, user: User):
        pass
