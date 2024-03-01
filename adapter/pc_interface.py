import sys

from abc import ABC, abstractmethod

from custom_types import Position


class PCInterface(ABC):
    """
    Interface for each adapter so that they can be easily replaced if necessary.
    """

    @abstractmethod
    def w(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def a(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def d(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def s(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def tab(self) -> Position:
        raise NotImplementedError

    @staticmethod
    def esc() -> None:
        sys.exit()
