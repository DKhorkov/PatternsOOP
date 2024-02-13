from powerlifter import PowerLifter


class Decorator(PowerLifter):
    """
    Decorator must have an identical interface to the object being decorated
    in order to be a transparent wrapper for the client usage.
    """

    def __init__(self, context: PowerLifter) -> None:
        self._context: PowerLifter = context

    def get_deadlift_weight(self) -> float:
        return self._context.get_deadlift_weight()

    def _check_weight_class(self) -> None:
        return self._context._check_weight_class()
