from abc import ABC, abstractmethod


class Pet(ABC):

    def __init__(self, name: str) -> None:
        self._name: str = name

    @abstractmethod
    def make_voice(self) -> None:
        raise NotImplementedError


class Dog(Pet):

    def make_voice(self) -> None:
        print(f"{self._name} says woof")


class Cat(Pet):

    def make_voice(self) -> None:
        print(f"{self._name} says meow")


class Rat(Pet):

    def make_voice(self) -> None:
        print(f"{self._name} says peee")
