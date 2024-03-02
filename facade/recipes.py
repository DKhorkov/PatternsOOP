from abc import ABC, abstractmethod


class Recipe(ABC):

    @abstractmethod
    def __init__(self) -> None:
        self._water: float = 0.0
        self._milk: float = 0.0
        self._coffee_beans: float = 0.0

    @property
    def water(self) -> float:
        return self._water

    @property
    def coffee_beans(self) -> float:
        return self._coffee_beans

    @property
    def milk(self) -> float:
        return self._milk


class AmericanoRecipe(Recipe):

    def __init__(self):
        self._water: float = 0.8
        self._milk: float = 0.0
        self._coffee_beans: float = 0.2


class LatteRecipe(Recipe):

    def __init__(self):
        self._water: float = 0.4
        self._milk: float = 0.4
        self._coffee_beans: float = 0.2


class CapuccinoRecipe(Recipe):

    def __init__(self):
        self._water: float = 0.6
        self._milk: float = 0.2
        self._coffee_beans: float = 0.2
