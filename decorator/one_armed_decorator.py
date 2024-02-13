from decorator import Decorator
from configs import DecoratorsMultipliers


class OneArmedDecorator(Decorator):
    """
    Decreases powerlifter's strength via reduced stability due to having only one hand.
    """

    def get_deadlift_weight(self) -> float:
        return self._context.get_deadlift_weight() * DecoratorsMultipliers.one_armed.value
