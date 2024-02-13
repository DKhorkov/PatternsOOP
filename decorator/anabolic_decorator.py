from decorator import Decorator
from configs import DecoratorsMultipliers


class AnabolicDecorator(Decorator):
    """
    Increases powerlifter's strength by taking anabolic steroids.
    """

    def get_deadlift_weight(self) -> float:
        return self._context.get_deadlift_weight() * DecoratorsMultipliers.anabolic.value
