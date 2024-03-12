from abc import abstractmethod, ABC

from publisher import Publisher
from typing import List


class Subscriber(ABC):

    def __init__(self) -> None:
        self._publishers: List[Publisher] = []

    @abstractmethod
    def update(self, publisher: Publisher) -> None:
        raise NotImplementedError

    def subscribe(self, publisher: Publisher) -> None:
        self._publishers.append(publisher)
        publisher.register(self)

    def unsubscribe(self, publisher: Publisher) -> None:
        self._publishers.remove(publisher)
        publisher.unregister(self)

    @property
    def publishers(self) -> List[Publisher]:
        return self._publishers
