from dataclasses import dataclass
from typing import AnyStr

from configs import MilkConditions


@dataclass
class Milk:
    volume: float
    condition: AnyStr = MilkConditions.regular.value
