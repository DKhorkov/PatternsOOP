from abc import ABC, abstractmethod
from typing import AnyStr

from person_visitor import PersonVisitor


class Person(ABC):

    def __init__(self, name: AnyStr, surname: AnyStr) -> None:
        self._name: AnyStr = name
        self._surname: AnyStr = surname

    @abstractmethod
    def accept(self, person_visitor: PersonVisitor) -> None:
        raise NotImplementedError

    @property
    def name(self) -> AnyStr:
        return self._name

    @property
    def surname(self) -> AnyStr:
        return self._surname
