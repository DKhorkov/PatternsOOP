from coffee_machine_facade import CoffeeMachineFacade
from half_liter_coffee_machine import HalfLiterCoffeeMachine
from coffee import Coffee
from water import Water


if __name__ == '__main__':
    coffee_machine: CoffeeMachineFacade = HalfLiterCoffeeMachine()
    latte: Coffee = coffee_machine.make_latte()
    americano: Coffee = coffee_machine.make_americano()
    cappuccino: Coffee = coffee_machine.make_cappuccino()
    boiling_water: Water = coffee_machine.make_boiling_water()

    print(f'Americano is a {americano}')
    print(f'Capuccino is a {cappuccino}')
    print(f'Latte is a {latte}')
    print(f'Boiling water is {boiling_water}')
