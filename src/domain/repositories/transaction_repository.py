from abc import ABC, abstractmethod

from domain.models.transaction import Transaction

class TransactionRepository(ABC):

    @abstractmethod
    def find_by_user_id(self, user_id: int) -> list['Transaction']:
        pass

    @abstractmethod
    def save(self, transaction: 'Transaction'):
        pass