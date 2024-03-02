from enum import Enum
from typing import AnyStr


class DrinkVolumes(Enum):
    # In milliliters:
    liter: float = 1000
    half_liter: float = 500
    quarter_liter: float = 250


class LiquidTemperatures(Enum):
    cold: float = 0.0
    hot: float = 50
    boiling: float = 100


class CoffeeBeansConditions(Enum):
    corn: AnyStr = 'corn'
    ground: AnyStr = 'ground'


class MilkConditions(Enum):
    regular: AnyStr = 'regular'
    frothed: AnyStr = 'frothed'
