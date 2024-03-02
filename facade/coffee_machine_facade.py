from abc import ABC, abstractmethod

from coffee import Coffee
from water import Water


class CoffeeMachineFacade(ABC):

    @abstractmethod
    def make_americano(self) -> Coffee:
        raise NotImplementedError

    @abstractmethod
    def make_latte(self) -> Coffee:
        raise NotImplementedError

    @abstractmethod
    def make_cappuccino(self) -> Coffee:
        raise NotImplementedError

    @abstractmethod
    def make_boiling_water(self) -> Water:
        raise NotImplementedError
