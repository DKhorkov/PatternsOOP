from decorator import Decorator
from configs import DecoratorsMultipliers


class HungoverDecorator(Decorator):
    """
    Decreases powerlifter's strength due to the hangover effect after a “good” evening.
    """

    def get_deadlift_weight(self) -> float:
        return self._context.get_deadlift_weight() * DecoratorsMultipliers.anabolic.value
