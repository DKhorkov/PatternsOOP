from value_object.figure import Figure


class Square(Figure):

    def __init__(self, side: float) -> None:
        self._side: float = side

    def square(self) -> float:
        return self._side * self._side

    def expand(self, times: float) -> Figure:
        return Square(self._side * times)
