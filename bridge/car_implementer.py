from abc import ABC, abstractmethod
from typing import Tuple


class CarImplementer(ABC):

    @staticmethod
    @abstractmethod
    def use_fuel_to_ride() -> Tuple[float, int]:
        raise NotImplementedError
