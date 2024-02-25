from enum import Enum


class TaxRates(Enum):
    employee: float = 0.13
    investor: float = 0.13


MONTHS_PER_YEAR: int = 12
