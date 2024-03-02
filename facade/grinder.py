from coffee_beans import CoffeeBeans

from configs import CoffeeBeansConditions


class Grinder:

    @staticmethod
    def grind_coffee_beans(coffee_beans: CoffeeBeans) -> CoffeeBeans:
        coffee_beans.condition = CoffeeBeansConditions.ground.value
        return coffee_beans
