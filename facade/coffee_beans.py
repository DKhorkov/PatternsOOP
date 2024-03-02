from dataclasses import dataclass
from typing import AnyStr

from configs import CoffeeBeansConditions


@dataclass
class CoffeeBeans:
    volume: float
    condition: AnyStr = CoffeeBeansConditions.corn.value
