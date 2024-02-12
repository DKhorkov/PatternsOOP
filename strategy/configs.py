from enum import Enum
from math import inf


class TaxRates(Enum):
    self_employed: float = 4.00 / 100
    solo_trader: float = 6.00 / 100
    regular: float = 13.00 / 100


class SalaryAmountRestrictions(Enum):
    self_employed: float = 2_400_000
    solo_trader: float = 199_350_000
    regular: float = 5_000_000


class TaxRatesAfterRestrictionsBreakdown(Enum):
    self_employed: float = 0.00 / 100  # Restriction == Limit to self-employed
    solo_trader: float = 8.00 / 100
    regular: float = 15.00 / 100


class SalaryAmountLimits(Enum):
    self_employed: float = 2_400_000  # Restriction == Limit to self-employed
    solo_trader: float = 265_800_000
    regular: float = inf


DEFAULT_TAX: float = 0.00
