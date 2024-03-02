from dataclasses import dataclass
from typing import AnyStr

from configs import LiquidTemperatures


@dataclass
class Water:
    volume: float
    temperature: float = LiquidTemperatures.cold.value

    def __str__(self) -> AnyStr:
        return f'{self.volume} ml of {self.temperature}° C Water.'
