from time import sleep
from copy import deepcopy
from typing import Self

from coffee import Coffee
from container import Container
from configs import Timeouts
from abstract_prototype import AbstractPrototype


class Mug(Container, AbstractPrototype):

    def __init__(self, volume: int) -> None:
        super().__init__(volume=volume, name='mug')

    def fill(self, drink: Coffee) -> None:
        self._check_drink_type(drink=drink, allowable_drink=Coffee)
        self._check_drink_volume(drink=drink)

        print(f'Pouring a {self.name} of {drink.name}!')
        sleep(Timeouts.filling_container.value)
        self.filled = True
        print(f'Enjoy your {drink.name}!')

    def clone(self) -> Self:
        return deepcopy(self)
