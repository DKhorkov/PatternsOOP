from game_engine import GameEngine
from custom_types import Position


class GameApp:
    """
    Mobile touch screen based app.
    """

    def __init__(self) -> None:
        self.__game_engine: GameEngine = GameEngine()

    def swipe_up(self) -> None:
        self.__game_engine.move_forward()

    def swipe_down(self) -> None:
        self.__game_engine.move_back()

    def swipe_right(self) -> None:
        self.__game_engine.move_right()

    def swipe_left(self) -> None:
        self.__game_engine.move_left()

    def double_tap(self) -> Position:
        return self.__game_engine.get_current_position()
