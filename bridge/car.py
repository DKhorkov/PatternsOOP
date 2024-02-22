from abc import ABC, abstractmethod

from car_implementer import CarImplementer


class Car(ABC):

    def __init__(
            self,
            fuel: float,  # In percents
            implementer: CarImplementer
    ) -> None:

        self._fuel: float = fuel
        self._implementer: CarImplementer = implementer

        self._is_riding: bool = False
        self._mileage: int = 0

    @abstractmethod
    def ride(self) -> None:
        raise NotImplementedError

    def _emergency_stop(self) -> None:
        self._is_riding = False
        print(f'{self.__class__.__name__} is out of fuel! Emergency stop!')

    def stop(self) -> None:
        self._is_riding = False

    @property
    def fuel(self) -> float:
        return self._fuel

    @property
    def is_riding(self) -> bool:
        return self._is_riding

    @property
    def mileage(self) -> int:
        return self._mileage
