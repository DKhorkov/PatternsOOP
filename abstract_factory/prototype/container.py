from abc import ABC, abstractmethod
from typing import AnyStr, Type

from drink import Drink
from exceptions import InvalidDrinkError, ContainerOverflowError


class Container(ABC):

    def __init__(self, volume: int, name: AnyStr) -> None:
        self.__volume: int = volume  # in milliliters
        self.__filled: bool = False
        self.__name: str = name

    @abstractmethod
    def fill(self, drink: Drink) -> None:
        pass

    @property
    def volume(self) -> int:
        return self.__volume

    @property
    def filled(self) -> bool:
        return self.__filled

    @filled.setter
    def filled(self, value: bool) -> None:
        self.__filled = value

    @property
    def name(self) -> AnyStr:
        return self.__name
    
    def _check_drink_type(self, drink: Drink, allowable_drink: Type[Drink]) -> None:
        if not isinstance(drink, allowable_drink):
            raise InvalidDrinkError(f'{self.name.capitalize()} can not be used for filling {drink.name}!')

    def _check_drink_volume(self, drink: Drink) -> None:
        if drink.volume > self.volume:
            raise ContainerOverflowError(
                f'{drink.volume} ml of {drink.name} can not be filled in {self.volume} ml {self.name}!'
            )
