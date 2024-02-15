from abc import ABC, abstractmethod


class Field(ABC):

    @abstractmethod
    def plow(self) -> None:
        pass
