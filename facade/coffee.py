from dataclasses import dataclass
from typing import AnyStr

from water import Water
from coffee_beans import CoffeeBeans
from milk import Milk


@dataclass(frozen=True)
class Coffee:
    water: Water
    coffee_beans: CoffeeBeans
    milk: Milk

    def __str__(self) -> AnyStr:
        return f'Coffee with {self.water.volume} ml of boiling water, ' \
               f'{self.coffee_beans.volume} ml of {self.coffee_beans.condition} coffee and ' \
               f'{self.milk.volume} ml of {self.milk.condition} milk.'
