from typing import List

from tax_calculate_visitor import TaxCalculateVisitor
from person import Person
from employee import Employee
from investor import Investor


class Example:

    def __init__(self) -> None:
        self.__persons: List[Person] = [
            Employee(
                name='John',
                surname='Smith',
                salary=10_500
            ),
            Employee(
                name='Jack',
                surname='Sparrow',
                salary=5_200
            ),
            Employee(
                name='Andrew',
                surname='Tate',
                salary=25_000
            ),
            Employee(
                name='Mark',
                surname='Godart',
                salary=15_700
            ),
            Investor(
                name='Donald',
                surname='Duck',
                current_stonks_price=320_000,
                previous_period_stonks_price=250_000
            ),
            Investor(
                name='Mickey',
                surname='Mouse',
                current_stonks_price=448_000,
                previous_period_stonks_price=350_000
            )
        ]

    def calculate_tax(self) -> float:
        person_visitor: TaxCalculateVisitor = TaxCalculateVisitor()
        for person in self.__persons:
            person.accept(person_visitor=person_visitor)

        tax: float = person_visitor.tax
        print(f'Tax for all persons, connected with company, is {tax:.2f}$.')
        return tax


if __name__ == '__main__':
    example = Example()
    example.calculate_tax()
