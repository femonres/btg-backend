from abc import ABC, abstractmethod
from typing import Optional

from domain.models.fund import Fund

class FundRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Fund]:
        pass

    @abstractmethod
    def get_by_id(self, fund_id: int) -> Optional[Fund]:
        pass
