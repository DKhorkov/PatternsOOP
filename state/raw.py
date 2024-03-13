from abstract_state import State
from fried import Fried
from eaten import Eaten


class Raw(State):

    def eat(self) -> None:
        print(f'You ate {self.__class__.__name__} {self._food.__class__.__name__} and became infected with worms!')
        self._food.state = Eaten(food=self._food)

    def cook(self) -> None:
        self._food.state = Fried(food=self._food)
