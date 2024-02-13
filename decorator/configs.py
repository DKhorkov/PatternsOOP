from enum import Enum
from math import inf


class WeightCategoriesLimits(Enum):
    """
    All categories presented in kilograms.
    """

    flyweight: float = 53.00
    bantamweight: float = 59.00
    featherweight: float = 66.00
    lightweight: float = 74.00
    welterweight: float = 83.00
    middleweight: float = 93.00
    light_heavyweight: float = 105.00
    heavyweight: float = 120.00
    super_heavyweight: float = inf


class WeightCategoriesDeadliftCoefficients(Enum):
    flyweight: float = 2.93
    bantamweight: float = 2.91
    featherweight: float = 2.89
    lightweight: float = 2.77
    welterweight: float = 2.67
    middleweight: float = 2.56
    light_heavyweight: float = 2.4
    heavyweight: float = 2.25
    super_heavyweight: float = 1.93


class DecoratorsMultipliers(Enum):
    anabolic: float = 1.5
    hungover: float = 0.7
    one_armed: float = 0.55
