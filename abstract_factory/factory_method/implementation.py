from typing import Optional

from abstract_factory import AbstractFactory
from tea_factory import TeaFactory
from coffee_factory import CoffeeFactory
from drink import Drink
from container import Container
from exceptions import InvalidDrinkError, ContainerOverflowError


class Implementation:

    def __init__(self):
        self.__abstract_factory: Optional[AbstractFactory] = None

    def get_tea(self) -> Optional[Container]:
        """
        :return: Cup of tea.
        """

        self.__abstract_factory = TeaFactory()
        return self.__make_served_drink()

    def get_coffee(self) -> Optional[Container]:
        """
        :return: Mug of coffee.
        """

        self.__abstract_factory = CoffeeFactory()
        return self.__make_served_drink()

    def __make_served_drink(self, drink_volume: int = 350, container_volume: int = 500) -> Optional[Container]:
        drink: Drink = self.__abstract_factory.create_drink(drink_volume)
        drink.prepare()
        if drink.prepared:
            container: Container = self.__abstract_factory.create_container(container_volume)
            container.fill(drink)
            if container.filled:
                return container

    def fill_invalid_drink(self) -> None:
        self.__abstract_factory = TeaFactory()
        drink: Drink = self.__abstract_factory.create_drink(200)
        self.__abstract_factory = CoffeeFactory()
        container: Container = self.__abstract_factory.create_container(300)
        try:
            container.fill(drink)
        except InvalidDrinkError as e:
            print(e)

    def overflow_container(self) -> None:
        self.__abstract_factory = TeaFactory()
        try:
            self.__make_served_drink(container_volume=200)
        except ContainerOverflowError as e:
            print(e)


if __name__ == "__main__":
    implementation: Implementation = Implementation()
    tea: Container = implementation.get_tea()
    coffee: Container = implementation.get_coffee()
    implementation.fill_invalid_drink()
    implementation.overflow_container()
