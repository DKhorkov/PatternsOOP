from abc import ABC, abstractmethod
from typing import Self


class AbstractPrototype(ABC):

    @abstractmethod
    def clone(self) -> Self:
        pass
