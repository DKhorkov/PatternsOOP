from dataclasses import dataclass
from typing import AnyStr


@dataclass
class Car:
    """
    Creating car with default values to ensure there will be no broken car during building.
    For example, without engine.
    """

    # Base car parts:
    wheels: int = 4
    engine: AnyStr = 'V2'
    seats: int = 4
    transmission: AnyStr = 'mechanic'
    breaks: AnyStr = 'disc'

    # Optional benefits:
    gps: bool = False
    conditioner: bool = False
    hatch: bool = False  # автомобильный люк
    spoiler: bool = False

    def __str__(self) -> AnyStr:
        car_info: AnyStr = (
            f'A {self.seats} seats and {self.wheels} wheels car with a {self.engine} engine, '
            f'{self.transmission} transmission and {self.breaks} breaks.\n'
            f'Additional info about this car:\n\n'
            f'GPS: {self.gps};'
            f'Conditioner: {self.conditioner};'
            f'Hatch: {self.hatch};'
            f'Spoiler: {self}'
        )

        return car_info
