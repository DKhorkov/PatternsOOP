from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

from exceptions import TaxLawsViolationsException

if TYPE_CHECKING:
    from employee import Employee


class TaxStrategy(ABC):

    @abstractmethod
    def calculate_annual_tax(self, context: 'Employee') -> Optional[float]:
        pass

    @staticmethod
    def _raise_tax_laws_violation_error() -> None:
        raise TaxLawsViolationsException('Tax laws were violated! Tax officer has already left with an inspection!')
