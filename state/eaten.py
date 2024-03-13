from abstract_state import State


class Eaten(State):

    def eat(self) -> None:
        print(f'How are you going to eat {self._food.__class__.__name__} you\'ve already eaten before?')

    def cook(self) -> None:
        print(f'How are you going to cook {self._food.__class__.__name__} you\'ve already eaten before?')
