from abc import ABC, abstractmethod
from typing import List

from domain.models.fund import Fund

class FundRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Fund]:
        pass

    @abstractmethod
    def find_by_id(self, fund_id: int) -> Fund:
        pass

    @abstractmethod
    def find_by_name(self, fund_name: str) -> Fund:
        pass
