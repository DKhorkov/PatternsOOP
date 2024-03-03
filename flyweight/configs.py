from typing import AnyStr
from enum import Enum


class PlantSpecies(Enum):
    monstera: AnyStr = 'monstera'
    philodendron: AnyStr = 'philodendron'
    ficus: AnyStr = 'ficus'
    rose: AnyStr = 'rose'


class PlantSizes(Enum):
    big: AnyStr = 'big'
    medium: AnyStr = 'medium'
    small: AnyStr = 'small'


STR_SEPARATOR: AnyStr = '_'
