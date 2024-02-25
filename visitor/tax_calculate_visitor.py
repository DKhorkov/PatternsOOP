from person_visitor import PersonVisitor
from employee import Employee
from investor import Investor
from configs import TaxRates, MONTHS_PER_YEAR


class TaxCalculateVisitor(PersonVisitor):

    def __init__(self) -> None:
        self.__tax: float = 0

    def visit_employee(self, employee: Employee) -> None:
        employee_tax: float = employee.salary * TaxRates.employee.value * MONTHS_PER_YEAR
        self.__tax += employee_tax

    def visit_investor(self, investor: Investor) -> None:
        stonks_price_difference: float = investor.current_stonks_price - investor.previous_period_stonks_price

        # No tax if no stonks revenue:
        if stonks_price_difference > 0:
            investor_tax: float = stonks_price_difference * TaxRates.investor.value
            self.__tax += investor_tax

    @property
    def tax(self) -> float:
        return self.__tax
