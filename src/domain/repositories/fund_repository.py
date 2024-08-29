from abc import ABC, abstractmethod

from domain.models.fund import Fund

class FundRepository(ABC):

    @abstractmethod
    def get_all(self) -> list['Fund']:
        pass

    @abstractmethod
    def get_by_id(self, fund_id: int) -> 'Fund':
        pass
