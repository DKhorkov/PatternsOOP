from time import sleep

from tea import Tea
from container import Container
from configs import Timeouts


class Cup(Container):

    def __init__(self, volume: int) -> None:
        super().__init__(volume=volume, name='cup')

    def fill(self, drink: Tea) -> None:
        self._check_drink_type(drink=drink, allowable_drink=Tea)
        self._check_drink_volume(drink=drink)

        print(f'Pouring a {self.name} of {drink.name}!')
        sleep(Timeouts.filling_container.value)
        self.filled = True
        print(f'Enjoy your {drink.name}!')
