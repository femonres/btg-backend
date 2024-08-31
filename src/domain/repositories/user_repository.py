from abc import ABC, abstractmethod
from typing import Optional

from domain.models.user import User

class UserRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: 'User'):
        pass
