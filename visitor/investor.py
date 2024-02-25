from typing import AnyStr

from person import Person
from person_visitor import PersonVisitor


class Investor(Person):

    def __init__(
            self,
            name: AnyStr,
            surname: AnyStr,
            current_stonks_price: float,
            previous_period_stonks_price: float
    ) -> None:

        super().__init__(name=name, surname=surname)
        self.__current_stonks_price: float = current_stonks_price
        self.__previous_period_stonks_price: float = previous_period_stonks_price

    def accept(self, person_visitor: PersonVisitor) -> None:
        person_visitor.visit_investor(self)

    @property
    def current_stonks_price(self) -> float:
        return self.__current_stonks_price

    @property
    def previous_period_stonks_price(self) -> float:
        return self.__previous_period_stonks_price
