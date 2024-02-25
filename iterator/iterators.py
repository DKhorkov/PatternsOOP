from collections.abc import Iterator
from typing import TYPE_CHECKING

from employee import Employee

if TYPE_CHECKING:
    from employees_collection import EmployeesCollection


class EmployeesIterator(Iterator):
    """
    Inherit from an existing Iterator interface so as not to create an abstract class.
    """

    def __init__(self, employee_collection: 'EmployeesCollection') -> None:
        self._employee_collection = employee_collection
        self._current_employee_index = 0

    def __next__(self) -> Employee:
        """
        Current method allows to retrieve the next Employee from Employees collection in pythonic way,
        combining a method for retrieving an element from the collection - @get_current_element() and a method,
        that checks that the index of the current element does not exceed the length
        of the collection itself - @is_done().

        :return: Exemplar of Employee.
        """

        employee: Employee = self._get_current_employee()
        self._increment_current_employee_index()
        return employee

    def _get_current_employee(self) -> Employee:
        try:
            employee: Employee = self._employee_collection[self._current_employee_index]
        except IndexError:
            raise StopIteration

        return employee

    def _increment_current_employee_index(self) -> None:
        self._current_employee_index += 1


class NotFiredEmployeesIterator(EmployeesIterator):

    def __next__(self) -> Employee:
        while self._get_current_employee().fired:
            self._increment_current_employee_index()

        employee: Employee = self._get_current_employee()
        self._increment_current_employee_index()
        return employee
