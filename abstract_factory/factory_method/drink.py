from abc import ABC, abstractmethod
from typing import AnyStr


class Drink(ABC):

    def __init__(self, volume: int, name: AnyStr) -> None:
        self.__volume: int = volume  # in milliliters
        self.__prepared: bool = False
        self.__name: AnyStr = name

    @abstractmethod
    def prepare(self) -> None:
        pass

    @property
    def volume(self) -> int:
        return self.__volume

    @property
    def prepared(self) -> bool:
        return self.__prepared

    @prepared.setter
    def prepared(self, value: bool) -> None:
        self.__prepared = value

    @property
    def name(self) -> AnyStr:
        return self.__name
