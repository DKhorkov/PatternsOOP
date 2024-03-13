from abc import ABC
from typing import Type

from abstract_state import State


class Food(ABC):

    def __init__(self, state: Type[State]) -> None:
        self._state: State = state(food=self)

    def eat(self) -> None:
        self._state.eat()

    def cook(self) -> None:
        self._state.cook()

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, state: State) -> None:
        self._state = state
