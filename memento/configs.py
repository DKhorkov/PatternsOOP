from enum import Enum
from typing import AnyStr


class GameSettings(Enum):
    start_money: int = 5_000
    solder_cost: int = 100
    solder_power: int = 5
    tank_cost: int = 1_500
    tank_power: int = 60
    sales_ratio: float = 0.9
    enemy_power: int = 220


class GameStatuses(Enum):
    victory: AnyStr = 'Victory'
    defeat: AnyStr = 'Defeat'
    draw: AnyStr = 'Draw'
