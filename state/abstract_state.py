from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from food import Food


class State(ABC):

    def __init__(self, food: 'Food') -> None:
        self._food: Food = food

    @abstractmethod
    def cook(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def eat(self) -> None:
        raise NotImplementedError
