from collections.abc import Iterable
from typing import List

from employee import Employee
from iterators import EmployeesIterator, NotFiredEmployeesIterator


class EmployeesCollection(Iterable):
    """
    Inherit from an existing Iterable interface so as not to create an abstract class.
    """

    def __init__(self, employees: List[Employee]) -> None:
        self.__employees: List[Employee] = employees

    def __getitem__(self, employee_index: int) -> Employee:
        """
        Current method purpose to get an employee by index without referring to the encapsulated
        @self.__employees attribute.

        :param employee_index: Index of employee to retrieve from employees collection.
        :return: Exemplar of Employee.
        """

        return self.__employees[employee_index]

    def __iter__(self) -> EmployeesIterator:
        """
        Current method returns iterator (pythonic way) instead of creating and call method get_iterator(self)
        for base scenario.

        :return: Iterator for iterate over current employees collection
        """

        return EmployeesIterator(self)

    def get_not_fired_employees_iterator(self) -> NotFiredEmployeesIterator:
        """
        Creating another method for getting iterator, because can not use @__iter__() method for multiple iterators.

        :return: Iterator to iter over only those Employees, who is not fired.
        """

        return NotFiredEmployeesIterator(self)
