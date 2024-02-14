from abc import ABC, abstractmethod

from drink import Drink
from container import Container


class AbstractFactory(ABC):

    @staticmethod
    @abstractmethod
    def create_drink(volume: int) -> Drink:
        pass

    @staticmethod
    @abstractmethod
    def create_container(volume: int) -> Container:
        pass
