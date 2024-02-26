from typing import List

from tax_calculate_visitor import TaxCalculateVisitor
from json_export_visitor import JsonExportVisitor
from person import Person
from employee import Employee
from investor import Investor
from configs import EXPORTED_DATA_FOLDER


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

    def export_to_json(self) -> None:
        person_visitor: JsonExportVisitor = JsonExportVisitor()
        for person in self.__persons:
            person.accept(person_visitor=person_visitor)

        print(f'All persons, connected with company, were exported to JSON and stored to {EXPORTED_DATA_FOLDER} folder.')


if __name__ == '__main__':
    example = Example()
    example.export_to_json()
    example.calculate_tax()
