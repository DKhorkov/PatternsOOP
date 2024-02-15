from field import Field
from area_mixin import AreaMixin


class PotatoField(AreaMixin, Field):
    """
    In Python, the class hierarchy is defined from right to left, so in this case the
    class Figure() is the base class and is extended by AreaMixin().

    Better to inherit in such way, but not the opposite, because in many cases mixin classes do not override
    each other's or the base class's methods. But if a method or property is overridden in mixins,
    this can lead to unexpected results, since the priority of resolving methods is from left to right.
    """

    def __init__(self, length: float, width: float, name: str = 'Potato field') -> None:
        self.__name = name
        self.__length = length
        self.__width = width

    def plow(self) -> None:
        print(
            f'Plowing {self.__name} with an area of '
            f'{self.calculate_area(length=self.__length, width=self.__width):.2f} square meters!'
        )

