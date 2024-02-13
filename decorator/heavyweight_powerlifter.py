from powerlifter import PowerLifter
from configs import WeightCategoriesLimits, WeightCategoriesDeadliftCoefficients


class HeavyWeightPowerLifter(PowerLifter):

    def _check_weight_class(self) -> None:
        if (self._weight < WeightCategoriesLimits.light_heavyweight.value or
                self._weight > WeightCategoriesLimits.heavyweight.value):

            self._raise_weight_class_error()

    def get_deadlift_weight(self) -> float:
        return self._weight * WeightCategoriesDeadliftCoefficients.heavyweight.value
