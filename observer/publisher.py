from typing import Any, List, TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from subscriber import Subscriber


class Publisher(ABC):

    def __init__(self) -> None:
        self._subscribers: List['Subscriber'] = []

    def notify(self) -> None:
        for subscriber in self._subscribers:
            subscriber.update(self)

    @abstractmethod
    def get_info(self) -> Any:
        raise NotImplementedError

    def register(self, subscriber: 'Subscriber') -> None:
        self._subscribers.append(subscriber)

    def unregister(self, subscriber: 'Subscriber') -> None:
        self._subscribers.remove(subscriber)
