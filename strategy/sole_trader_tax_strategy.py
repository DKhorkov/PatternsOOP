from typing import Optional, TYPE_CHECKING

from tax_strategy import TaxStrategy
from configs import TaxRates, SalaryAmountLimits, SalaryAmountRestrictions, TaxRatesAfterRestrictionsBreakdown

if TYPE_CHECKING:
    from employee import Employee


class SoleTraderTaxStrategy(TaxStrategy):

    def calculate_annual_tax(self, context: 'Employee') -> Optional[float]:
        """
        https://www.b-kontur.ru/enquiry/489-limity-po-usn#header_24461_1
        """

        if context.salary >= SalaryAmountLimits.solo_trader.value:
            return self._raise_tax_laws_violation_error()
        elif context.salary <= SalaryAmountRestrictions.solo_trader.value:
            return context.salary * TaxRates.solo_trader.value
        else:
            return context.salary * TaxRatesAfterRestrictionsBreakdown.solo_trader.value
