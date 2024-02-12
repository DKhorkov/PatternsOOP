from typing import Optional, TYPE_CHECKING

from strategy import TaxStrategy
from configs import TaxRates, SalaryAmountLimits

if TYPE_CHECKING:
    from employee import Employee


class SelfEmployedTaxStrategy(TaxStrategy):

    def calculate_annual_tax(self, context: 'Employee') -> Optional[float]:
        """
        https://kontur.ru/articles/4818
        """

        if context.salary >= SalaryAmountLimits.self_employed.value:
            return self._raise_tax_laws_violation_error()
        else:
            return context.salary * TaxRates.self_employed.value
