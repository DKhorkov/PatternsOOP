from time import sleep

from drink import Drink
from configs import Timeouts


class Tea(Drink):

    def __init__(self, volume: int) -> None:
        super().__init__(volume=volume, name='tea')

    def prepare(self) -> None:
        print(f'Boiling water for {self.name}!')
        sleep(Timeouts.water_boiling.value)
        print(f'Brewing {self.name}!')
        self.prepared = True
        print(f'{self.name.capitalize()} is brewed!')
