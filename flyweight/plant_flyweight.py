from typing import AnyStr

from color import Color
from plant_type import PlantType
from plant_context import PlantContext


class PlantFlyweight:

    def __init__(self, color: Color, plant_type: PlantType) -> None:
        self.__color: Color = color
        self.__plant_type: PlantType = plant_type

    def describe_plant(self, plant_context: PlantContext) -> AnyStr:
        flowering_info: AnyStr = 'flowering' if plant_context.flowering else 'not flowering'
        plant_description: AnyStr = f'A {self.__plant_type.name} plant of {plant_context.species} species, ' \
                                    f'with {self.__color.name} color, {plant_context.size} size, ' \
                                    f'which is {flowering_info} now.'

        return plant_description
