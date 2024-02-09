from typing import List

from component import Component
from configs import DEFAULT_BUILD_PRICE, DEFAULT_COMPONENT_PRICE


class Composite(Component):

    def __init__(
            self,
            price: float = DEFAULT_COMPONENT_PRICE,
            build_price: float = DEFAULT_BUILD_PRICE
    ) -> None:

        """
        Leave the constructor identical to the Component's, so that the client
        would be able to work in the same way with both Detail and Composite.
        """

        super().__init__(price=price)
        self.__build_price = build_price

        self._children: List[Component] = list()

    def price(self) -> float:
        price_sum: float = 0.00
        for child in self._children:
            price_sum += child.price()

        return price_sum + self.__build_price

    @staticmethod
    def is_composite() -> bool:
        return True

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def get_child(self, index: int) -> Component:
        return self._children[index]
