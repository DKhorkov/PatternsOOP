from typing import AnyStr
from abc import ABC, abstractmethod

from abstract_memento import AbstractMemento


class Game(ABC):

    @abstractmethod
    def save(self, save_name: AnyStr) -> AbstractMemento:
        raise NotImplementedError

    @abstractmethod
    def load(self, save: AbstractMemento) -> None:
        raise NotImplementedError
