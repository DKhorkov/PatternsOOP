from abc import ABC
from typing import Self, List, Optional


class Component(ABC):
    """
    Base class for implementing composite pattern.

    Component is an abstract class so that it SHOULD only be implemented,
    but not instantiated from it.
    """

    def __init__(self, price: float) -> None:
        self.__price: float = price

        # Should be overriden only in composite:
        self._children: Optional[List[Self]] = None

    def price(self) -> float:
        return self.__price

    @staticmethod
    def is_composite() -> bool:
        return False

    def add(self, component: Self) -> None:
        """
        Should be overriden in composite class and used only by composites.

        :param component: Another component, which will be a child of composite.
        """

        raise NotImplementedError

    def remove(self, component: Self) -> None:
        """
        Should be overriden in composite class and used only by composites.

        :param component: Another component, which will be a child of composite.
        """

        raise NotImplementedError

    def get_child(self, index: int):
        """
        Should be overriden in composite class and used only by composites.

        :param index: Index of composite's child to retrieve.
        """

        raise NotImplementedError
