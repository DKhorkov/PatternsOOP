from typing import AnyStr, Optional

from strategy import TaxStrategy
from configs import DEFAULT_TAX


class Employee:

    def __init__(
            self,
            name: AnyStr,
            surname: AnyStr,
            salary: float,
            tax_strategy: Optional[TaxStrategy] = None
    ) -> None:

        self.__name = name
        self.__surname = surname
        self.__salary = salary
        self.__tax_strategy = tax_strategy

    @property
    def tax_strategy(self) -> TaxStrategy:
        return self.__tax_strategy

    @tax_strategy.setter
    def tax_strategy(self, tax_strategy: TaxStrategy) -> None:
        self.__tax_strategy = tax_strategy

    @property
    def salary(self) -> float:
        return self.__salary

    def calculate_annual_tax(self) -> Optional[float]:
        if not self.tax_strategy:
            return DEFAULT_TAX

        return self.__tax_strategy.calculate_annual_tax(context=self)
