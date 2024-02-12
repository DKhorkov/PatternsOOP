from typing import Optional, TYPE_CHECKING

from tax_strategy import TaxStrategy
from configs import TaxRates, SalaryAmountLimits, SalaryAmountRestrictions, TaxRatesAfterRestrictionsBreakdown

if TYPE_CHECKING:
    from employee import Employee


class RegularTaxStrategy(TaxStrategy):

    def calculate_annual_tax(self, context: 'Employee') -> Optional[float]:
        """
        https://www.moedelo.org/club/buhgalterskij-uchet/podohodnyj-nalog-s-zarplaty
        """

        if context.salary >= SalaryAmountLimits.regular.value:
            return self._raise_tax_laws_violation_error()
        elif context.salary <= SalaryAmountRestrictions.regular.value:
            return context.salary * TaxRates.regular.value
        else:
            base_tax: float = SalaryAmountRestrictions.regular.value * TaxRates.regular.value
            excess_tax_base: float = context.salary - SalaryAmountRestrictions.regular.value
            excess_tax: float = excess_tax_base * TaxRatesAfterRestrictionsBreakdown.regular.value
            return base_tax + excess_tax
