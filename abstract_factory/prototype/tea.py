from time import sleep
from typing import Self
from copy import deepcopy

from drink import Drink
from configs import Timeouts
from abstract_prototype import AbstractPrototype


class Tea(Drink, AbstractPrototype):

    def __init__(self, volume: int) -> None:
        super().__init__(volume=volume, name='tea')

    def prepare(self) -> None:
        print(f'Boiling water for {self.name}!')
        sleep(Timeouts.water_boiling.value)
        print(f'Brewing {self.name}!')
        self.prepared = True
        print(f'{self.name.capitalize()} is brewed!')

    def clone(self) -> Self:
        return deepcopy(self)
