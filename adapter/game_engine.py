from custom_types import Position
from configs import STEP_RANGE


class GameEngine:

    def __init__(self) -> None:
        self.__x = 0
        self.__y = 0

    def move_forward(self) -> None:
        self.__x += STEP_RANGE

    def move_back(self) -> None:
        self.__x -= STEP_RANGE

    def move_right(self) -> None:
        self.__y += STEP_RANGE

    def move_left(self) -> None:
        self.__y -= STEP_RANGE

    def get_current_position(self) -> Position:
        return Position(x=self.__x, y=self.__y)
