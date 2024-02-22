from enum import Enum


class FuelCoefficients(Enum):
    large_vehicle_weight: float = 1.6
    all_wheel_drive: float = 1.3


class FuelConsumptions(Enum):
    # Consumptions in liters per 100km:
    diesel: float = 12.3
    gasoline: float = 9.8


KILOMETERS_PER_ITERATION: int = 100
EMPTY_FUEL_THRESHOLD: float = 0.0
ITERATION_TIMEOUT_SECONDS: float = 1.0
