from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from employee import Employee
    from investor import Investor


class PersonVisitor(ABC):

    @abstractmethod
    def visit_employee(self, employee: 'Employee') -> None:
        raise NotImplementedError

    @abstractmethod
    def visit_investor(self, investor: 'Investor') -> None:
        raise NotImplementedError
