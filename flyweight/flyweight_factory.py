from typing import Dict, Hashable

from plant_flyweight import PlantFlyweight
from color import Color
from plant_type import PlantType
from configs import STR_SEPARATOR


class FlyweightFactory:

    def __init__(self) -> None:
        self.__plant_flyweights: Dict[Hashable, PlantFlyweight] = {}

    def get_plant_flyweight(self, color: Color, plant_type: PlantType) -> PlantFlyweight:
        plant_flyweight_hash: Hashable = self.__get_plant_flyweight_hash(color=color, plant_type=plant_type)
        if plant_flyweight_hash not in self.__plant_flyweights:
            self.__plant_flyweights[plant_flyweight_hash] = PlantFlyweight(color=color, plant_type=plant_type)

        plant_flyweight: PlantFlyweight = self.__plant_flyweights.get(plant_flyweight_hash)
        return plant_flyweight

    @staticmethod
    def __get_plant_flyweight_hash(color: Color, plant_type: PlantType) -> Hashable:
        """
        Since there is no need the hash of an object to be the same between different runs
        (objects will be generated anew per each run), but to be the same for the same instances via each run,
        the built-in hash function will be used.
        """

        plant_flyweight_hash: Hashable = hash(
            STR_SEPARATOR.join([str(color), str(plant_type)])
        )

        return plant_flyweight_hash
