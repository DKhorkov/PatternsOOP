class GameEngine:
    """
    GameEngine is a receiver class, which executes game logic via being invoked by Commands.
    """

    def __init__(self) -> None:
        self.__x_pos: int = 0
        self.__y_pos: int = 0

    @property
    def x_pos(self) -> int:
        return self.__x_pos

    @x_pos.setter
    def x_pos(self, value: int) -> None:
        self.__x_pos = value

    @property
    def y_pos(self) -> int:
        return self.__y_pos

    @y_pos.setter
    def y_pos(self, value: int) -> None:
        self.__y_pos = value
