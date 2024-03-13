from abstract_state import State
from overcooked import Overcooked
from eaten import Eaten


class Fried(State):

    def eat(self) -> None:
        print(f'You ate {self.__class__.__name__} {self._food.__class__.__name__} and experienced bliss!')
        self._food.state = Eaten(food=self._food)

    def cook(self) -> None:
        self._food.state = Overcooked(food=self._food)
