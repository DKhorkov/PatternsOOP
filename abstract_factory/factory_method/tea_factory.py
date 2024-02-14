from abstract_factory import AbstractFactory
from tea import Tea
from cup import Cup


class TeaFactory(AbstractFactory):

    @staticmethod
    def create_drink(volume: int) -> Tea:
        return Tea(volume=volume)

    @staticmethod
    def create_container(volume: int) -> Cup:
        return Cup(volume=volume)
