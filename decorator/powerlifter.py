from abc import ABC, abstractmethod

from exceptions import WeightClassError


class PowerLifter(ABC):

    def __init__(self, weight: float) -> None:
        self._weight = weight
        self._check_weight_class()

    @abstractmethod
    def get_deadlift_weight(self) -> float:
        pass

    @abstractmethod
    def _check_weight_class(self) -> None:
        pass

    def _raise_weight_class_error(self) -> None:
        raise WeightClassError(
            f'The powerlifter with weight of {self._weight} kg was disqualified for violation of weight category!'
        )
