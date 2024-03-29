from typing import AnyStr

from plant_flyweight import PlantFlyweight


class PlantContext:

    def __init__(self, flowering: bool, species: AnyStr, size: AnyStr, flyweight: PlantFlyweight) -> None:
        self.__flowering: bool = flowering
        self.__species: AnyStr = species
        self.__size: AnyStr = size
        self.__flyweight: PlantFlyweight = flyweight

    def describe_plant(self) -> AnyStr:
        return self.__flyweight.describe_plant(plant_context=self)

    @property
    def flowering(self) -> bool:
        return self.__flowering

    @property
    def species(self) -> AnyStr:
        return self.__species

    @property
    def size(self) -> AnyStr:
        return self.__size
