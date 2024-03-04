from typing import AnyStr, Dict, List

from flyweight_factory import FlyweightFactory
from plant_flyweight import PlantFlyweight
from plant_context import PlantContext
from color import Color
from plant_type import PlantType
from configs import PlantSizes, PlantSpecies


class Client:

    def __init__(self) -> None:
        self.__flyweight_factory: FlyweightFactory = FlyweightFactory()
        self.__plants: List[PlantContext] = list()
        self.__colors: Dict[AnyStr, Color] = {
            'green': Color(r=0, g=255, b=0, name='green'),
            'yellow': Color(r=255, g=255, b=0, name='yellow')
        }
        self.__plant_types: Dict[AnyStr, PlantType] = {
            'poisonous': PlantType(name='poisonous'),
            'not poisonous': PlantType(name='not poisonous')
        }

    def run(self) -> None:
        self.__plant_plants()
        self.__describe_plants()

    def __plant_plants(self) -> None:
        self.__plant_a_plant()
        print(f'Flyweights count: {self.__flyweight_factory.count_flyweights()}')  # 1
        self.__plant_a_plant(color_name='yellow')
        print(f'Flyweights count: {self.__flyweight_factory.count_flyweights()}')  # 2
        self.__plant_a_plant(flowering=True, plant_size=PlantSizes.big.value, plant_species=PlantSpecies.rose.value)
        print(f'Flyweights count: {self.__flyweight_factory.count_flyweights()}')  # 2
        self.__plant_a_plant(plant_size=PlantSizes.medium.value, plant_species=PlantSpecies.philodendron.value)
        print(f'Flyweights count: {self.__flyweight_factory.count_flyweights()}')  # 2
        self.__plant_a_plant(
            plant_type_name='poisonous',
            flowering=True,
            plant_size=PlantSizes.big.value,
            plant_species=PlantSpecies.monstera.value
        )
        print(f'Flyweights count: {self.__flyweight_factory.count_flyweights()}')  # 3
        self.__plant_a_plant(
            plant_type_name='poisonous',
            color_name='yellow',
            plant_size=PlantSizes.small.value,
            plant_species=PlantSpecies.rose.value
        )
        print(f'Flyweights count: {self.__flyweight_factory.count_flyweights()}')  # 4

    def __plant_a_plant(
            self,
            color_name: AnyStr = 'green',
            plant_type_name: AnyStr = 'not poisonous',
            plant_size: AnyStr = PlantSizes.small.value,
            plant_species: AnyStr = PlantSpecies.ficus.value,
            flowering: bool = False
    ) -> None:

        color: Color = self.__colors.get(color_name)
        plant_type: PlantType = self.__plant_types.get(plant_type_name)
        plant_flyweight: PlantFlyweight = self.__flyweight_factory.get_plant_flyweight(
            color=color,
            plant_type=plant_type
        )

        plant: PlantContext = PlantContext(
            flowering=flowering,
            flyweight=plant_flyweight,
            species=plant_species,
            size=plant_size
        )

        self.__plants.append(plant)

    def __describe_plants(self) -> None:
        for plant in self.__plants:
            print(plant.describe_plant())
