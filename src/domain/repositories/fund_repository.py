from abc import ABC, abstractmethod

from src.domain.models.fund import Fund

class FundRepository(ABC):

    @abstractmethod
    def find_by_id(self, fund_id: int) -> Fund:
        pass

    @abstractmethod
    def find_by_name(self, fund_name: str) -> Fund:
        pass
