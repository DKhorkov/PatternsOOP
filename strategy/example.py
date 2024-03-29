from typing import AnyStr

from employee import Employee
from self_employed_tax_strategy import SelfEmployedTaxStrategy
from sole_trader_tax_strategy import SoleTraderTaxStrategy
from regular_tax_strategy import RegularTaxStrategy
from exceptions import TaxLawsViolationsException


class Example:

    def __init__(self, salary: float, name: AnyStr = 'John', surname: AnyStr = 'Smith') -> None:
        self.__employee = Employee(name=name, surname=surname, salary=salary)

    def regular_tax(self) -> float:
        self.__employee.tax_strategy = RegularTaxStrategy()
        regular_tax: float = self.__employee.calculate_annual_tax()
        print(f'Regular tax = {regular_tax}')
        return regular_tax

    def self_employed_tax(self) -> float:
        self.__employee.tax_strategy = SelfEmployedTaxStrategy()
        self_employed_tax: float = self.__employee.calculate_annual_tax()
        print(f'Self-employed tax = {self_employed_tax}')
        return self_employed_tax

    def solo_trader_tax(self) -> float:
        self.__employee.tax_strategy = SoleTraderTaxStrategy()
        solo_trader_tax: float = self.__employee.calculate_annual_tax()
        print(f'Solo-trader tax = {solo_trader_tax}')
        return solo_trader_tax


if __name__ == '__main__':
    example = Example(salary=1_000_000)
    example.regular_tax()
    example.self_employed_tax()
    example.solo_trader_tax()

    # Excess tax_calculations:
    example = Example(salary=200_000_000)
    example.solo_trader_tax()
    example = Example(salary=10_000_000)
    example.regular_tax()

    # Tax after restrictions breakdown:
    example = Example(salary=280_000_000)
    try:
        example.self_employed_tax()
    except TaxLawsViolationsException as e:
        print(e)

    try:
        example.solo_trader_tax()
    except TaxLawsViolationsException as e:
        print(e)
