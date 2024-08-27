from abc import ABC, abstractmethod

from .domain_event import DomainEvent


class EventPublisher(ABC):

    @abstractmethod
    def publish(self, event: DomainEvent):
        pass