from typing import Tuple

from car_implementer import CarImplementer
from configs import FuelConsumptions, KILOMETERS_PER_ITERATION


class GasolineCarImplementer(CarImplementer):

    @staticmethod
    def use_fuel_to_ride() -> Tuple[float, int]:
        return FuelConsumptions.gasoline.value, KILOMETERS_PER_ITERATION
