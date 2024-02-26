from enum import Enum
from pathlib import Path


class TaxRates(Enum):
    employee: float = 0.13
    investor: float = 0.13


MONTHS_PER_YEAR: int = 12

EXPORTED_DATA_FOLDER: Path = Path('exported_data')
