from time import sleep
from copy import deepcopy
from typing import Self

from tea import Tea
from container import Container
from configs import Timeouts
from abstract_prototype import AbstractPrototype


class Cup(Container, AbstractPrototype):

    def __init__(self, volume: int) -> None:
        super().__init__(volume=volume, name='cup')

    def fill(self, drink: Tea) -> None:
        self._check_drink_type(drink=drink, allowable_drink=Tea)
        self._check_drink_volume(drink=drink)

        print(f'Pouring a {self.name} of {drink.name}!')
        sleep(Timeouts.filling_container.value)
        self.filled = True
        print(f'Enjoy your {drink.name}!')

    def clone(self) -> Self:
        return deepcopy(self)
