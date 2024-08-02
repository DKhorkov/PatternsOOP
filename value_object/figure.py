from __future__ import annotations
from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def square(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def expand(self, times: float) -> Figure:
        raise NotImplementedError
