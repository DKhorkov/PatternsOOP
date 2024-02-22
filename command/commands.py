import sys

from abc import ABC, abstractmethod

from game_engine import GameEngine
from configs import MOVE_STEP

from history import History


class Command(ABC):

    def __init__(self, game_engine: GameEngine, history: History) -> None:
        self._game_engine: GameEngine = game_engine
        self._history: History = history

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError

    def cancel(self) -> None:
        raise NotImplementedError


class MoveLeftCommand(Command):

    def execute(self) -> None:
        self._history.add_command(self)
        self._game_engine.x_pos -= MOVE_STEP

    def cancel(self) -> None:
        self._game_engine.x_pos += MOVE_STEP


class MoveRightCommand(Command):

    def execute(self) -> None:
        self._history.add_command(self)
        self._game_engine.x_pos += MOVE_STEP

    def cancel(self) -> None:
        self._game_engine.x_pos -= MOVE_STEP


class MoveForwardCommand(Command):

    def execute(self) -> None:
        self._history.add_command(self)
        self._game_engine.y_pos += MOVE_STEP

    def cancel(self) -> None:
        self._game_engine.y_pos -= MOVE_STEP


class MoveBackCommand(Command):

    def execute(self) -> None:
        self._history.add_command(self)
        self._game_engine.y_pos -= MOVE_STEP

    def cancel(self) -> None:
        self._game_engine.y_pos += MOVE_STEP


class PrintPositionCommand(Command):

    def execute(self) -> None:
        print(f'Current position: x={self._game_engine.x_pos}, y={self._game_engine.y_pos}')


class UndoCommand(Command):

    def execute(self) -> None:
        self._history.undo()


class RedoCommand(Command):

    def execute(self) -> None:
        self._history.redo()


class ExitCommand(Command):

    def execute(self) -> None:
        sys.exit()
