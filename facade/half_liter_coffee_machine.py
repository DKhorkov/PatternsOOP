from coffee_machine_facade import CoffeeMachineFacade
from boiler import Boiler
from mixer import Mixer
from grinder import Grinder
from coffee import Coffee
from water import Water
from milk import Milk
from coffee_beans import CoffeeBeans
from recipes import Recipe, AmericanoRecipe, CapuccinoRecipe, LatteRecipe
from configs import DrinkVolumes


class HalfLiterCoffeeMachine(CoffeeMachineFacade):

    def __init__(self) -> None:
        self.__drink_volume: float = DrinkVolumes.half_liter.value
        self.__boiler: Boiler = Boiler()
        self.__grinder: Grinder = Grinder()
        self.__mixer: Mixer = Mixer()

    def make_americano(self) -> Coffee:
        return self.__make_coffee(recipe=AmericanoRecipe())

    def make_latte(self) -> Coffee:
        return self.__make_coffee(recipe=LatteRecipe())

    def make_cappuccino(self) -> Coffee:
        return self.__make_coffee(recipe=CapuccinoRecipe())

    def __make_coffee(self, recipe: Recipe) -> Coffee:
        water: Water = self.__boiler.boil_water(
            Water(self.__drink_volume * recipe.water)
        )

        coffee_beans: CoffeeBeans = self.__grinder.grind_coffee_beans(
            CoffeeBeans(self.__drink_volume * recipe.coffee_beans)
        )

        milk: Milk = self.__mixer.froth_milk(
            Milk(self.__drink_volume * recipe.milk)
        )

        return Coffee(
            water=water,
            coffee_beans=coffee_beans,
            milk=milk
        )

    def make_boiling_water(self) -> Water:
        return self.__boiler.boil_water(
            Water(self.__drink_volume)
        )
