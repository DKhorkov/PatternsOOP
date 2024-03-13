from abstract_state import State
from eaten import Eaten


class Overcooked(State):

    def eat(self) -> None:
        print(f'You ate {self.__class__.__name__} {self._food.__class__.__name__} and got poisoned!')
        self._food.state = Eaten(food=self._food)

    def cook(self) -> None:
        pass
