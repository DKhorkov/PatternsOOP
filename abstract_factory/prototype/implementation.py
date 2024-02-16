from typing import Optional

from prototype_factory import PrototypeFactory
from drink import Drink
from coffee import Coffee
from tea import Tea
from container import Container
from mug import Mug
from cup import Cup
from exceptions import InvalidDrinkError, ContainerOverflowError, UnegisteredPrototypeError


class Implementation:

    def __init__(self):
        self.__abstract_factory: PrototypeFactory = PrototypeFactory()
        self.__register_prototypes()

    def __register_prototypes(self) -> None:
        self.__abstract_factory.register(
            name='standard_coffee',
            prototype=Coffee(
                volume=350
            )
        )

        self.__abstract_factory.register(
            name='standard_mug',
            prototype=Mug(
                volume=500
            )
        )

        self.__abstract_factory.register(
            name='standard_tea',
            prototype=Tea(
                volume=350
            )
        )

        self.__abstract_factory.register(
            name='standard_cup',
            prototype=Cup(
                volume=500
            )
        )

        self.__abstract_factory.register(
            name='big_tea',
            prototype=Tea(
                volume=1000
            )
        )

        self.__abstract_factory.register(
            name='little_cup',
            prototype=Cup(
                volume=300
            )
        )


    def get_tea(self) -> Optional[Container]:
        """
        :return: Cup of tea.
        """

        tea: Tea = self.__abstract_factory.create('standard_tea')
        tea.prepare()
        cup: Cup = self.__abstract_factory.create('standard_cup')
        filled_drink: Container = self.__fill_drink(drink=tea, container=cup)
        return filled_drink

    def get_coffee(self) -> Optional[Container]:
        """
        :return: Mug of coffee.
        """

        coffee: Coffee = self.__abstract_factory.create('standard_coffee')
        coffee.prepare()
        mug: Mug = self.__abstract_factory.create('standard_mug')
        filled_drink: Container = self.__fill_drink(drink=coffee, container=mug)
        return filled_drink

    @staticmethod
    def __fill_drink(drink: Drink, container: Container) -> Optional[Container]:
        try:
            return container.fill(drink)
        except (InvalidDrinkError, ContainerOverflowError) as e:
            print(e)

    def fill_invalid_drink(self) -> None:
        drink: Drink = self.__abstract_factory.create('standard_coffee')
        container: Container = self.__abstract_factory.create('standard_cup')
        self.__fill_drink(drink=drink, container=container)

    def overflow_container(self) -> None:
        drink: Drink = self.__abstract_factory.create('big_tea')
        container: Container = self.__abstract_factory.create('little_cup')
        self.__fill_drink(drink=drink, container=container)

    def create_unregistered_exemplar(self) -> None:
        try:
            self.__abstract_factory.create('some_exemplar')
        except UnegisteredPrototypeError as e:
            print(e)

    def unregister_not_registered_exemplar(self) -> None:
        try:
            self.__abstract_factory.unregister('some_exemplar')
        except UnegisteredPrototypeError as e:
            print(e)


if __name__ == "__main__":
    implementation: Implementation = Implementation()
    tea: Container = implementation.get_tea()
    coffee: Container = implementation.get_coffee()
    implementation.fill_invalid_drink()
    implementation.overflow_container()
    implementation.create_unregistered_exemplar()
    implementation.unregister_not_registered_exemplar()
