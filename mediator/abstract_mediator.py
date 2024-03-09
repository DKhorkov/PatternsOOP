from abc import ABC, abstractmethod
from typing import AnyStr


class Mediator(ABC):

    @abstractmethod
    def notify(self, component: object, event: AnyStr) -> None:
        raise NotImplementedError
