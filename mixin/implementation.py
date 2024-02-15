from potato_field import PotatoField
from rectangle import Rectangle


class Implementation:
    """
    Since both the potato field and the rectangle were inherited from AreaMixin,
    they can use the area calculation method.

    Thus, a mixin makes it possible to dynamically expand the behavior of objects
    without creating connectivity between them.
    """

    def __init__(self):
        self.__potato_filed: PotatoField = PotatoField(20.5, 36.7)
        self.__rectangle: Rectangle = Rectangle(15, 10)

    @property
    def potato_filed(self) -> PotatoField:
        return self.__potato_filed

    @property
    def rectangle(self) -> Rectangle:
        return self.__rectangle


if __name__ == '__main__':
    implementation = Implementation()
    implementation.rectangle.draw()
    implementation.potato_filed.plow()
