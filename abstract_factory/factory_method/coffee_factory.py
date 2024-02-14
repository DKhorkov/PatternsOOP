from abstract_factory import AbstractFactory
from coffee import Coffee
from mug import Mug


class CoffeeFactory(AbstractFactory):

    @staticmethod
    def create_drink(volume: int) -> Coffee:
        return Coffee(volume=volume)

    @staticmethod
    def create_container(volume: int) -> Mug:
        return Mug(volume=volume)
