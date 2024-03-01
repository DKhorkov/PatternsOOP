from pc_interface import PCInterface
from game_app import GameApp
from custom_types import Position


class Emulator(PCInterface, GameApp):
    """
    Emulator is an Adapter for launch mobile game on PC.

    In this case, a class adapter is used.
    If it were necessary to work with different GameApp-s, then it would be worth using an object adapter,
    which would use aggregation rather than inheritance, and the adapter constructor would accept an GameApp instance.
    """

    def w(self) -> None:
        self.swipe_up()

    def s(self) -> None:
        self.swipe_down()

    def d(self) -> None:
        self.swipe_right()

    def a(self) -> None:
        self.swipe_left()

    def tab(self) -> Position:
        position: Position = self.double_tap()
        print(f'Current position: x={position.x}; y={position.y}')
        return position
