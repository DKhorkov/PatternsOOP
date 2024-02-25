from typing import AnyStr

from person import Person
from person_visitor import PersonVisitor


class Employee(Person):

    def __init__(self, name: AnyStr, surname: AnyStr, salary: float) -> None:
        super().__init__(name=name, surname=surname)
        self.__salary: float = salary

    def accept(self, person_visitor: PersonVisitor) -> None:
        person_visitor.visit_employee(self)

    @property
    def salary(self) -> float:
        return self.__salary
