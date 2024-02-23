import sys

from abc import ABC, abstractmethod

from game_engine import GameEngine
from configs import MOVE_STEP

from history import History


class Command(ABC):

    def __init__(self, game_engine: GameEngine) -> None:
        self._game_engine: GameEngine = game_engine

        self._undoable: bool = False

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError

    def cancel(self) -> None:
        raise NotImplementedError

    @property
    def undoable(self) -> bool:
        return self._undoable


class MoveLeftCommand(Command):

    def __init__(self, game_engine: GameEngine) -> None:
        super().__init__(game_engine)
        self._undoable: bool = True

    def execute(self) -> None:
        self._game_engine.x_pos -= MOVE_STEP

    def cancel(self) -> None:
        self._game_engine.x_pos += MOVE_STEP


class MoveRightCommand(Command):

    def __init__(self, game_engine: GameEngine) -> None:
        super().__init__(game_engine)
        self._undoable: bool = True

    def execute(self) -> None:
        self._game_engine.x_pos += MOVE_STEP

    def cancel(self) -> None:
        self._game_engine.x_pos -= MOVE_STEP


class MoveForwardCommand(Command):

    def __init__(self, game_engine: GameEngine) -> None:
        super().__init__(game_engine)
        self._undoable: bool = True

    def execute(self) -> None:
        self._game_engine.y_pos += MOVE_STEP

    def cancel(self) -> None:
        self._game_engine.y_pos -= MOVE_STEP


class MoveBackCommand(Command):

    def __init__(self, game_engine: GameEngine) -> None:
        super().__init__(game_engine)
        self._undoable: bool = True

    def execute(self) -> None:
        self._game_engine.y_pos -= MOVE_STEP

    def cancel(self) -> None:
        self._game_engine.y_pos += MOVE_STEP


class PrintPositionCommand(Command):

    def execute(self) -> None:
        print(f'Current position: x={self._game_engine.x_pos}, y={self._game_engine.y_pos}')


class UndoCommand(Command):

    def __init__(self, game_engine: GameEngine, history: History) -> None:
        super().__init__(game_engine)
        self._history: History = history

    def execute(self) -> None:
        self._history.undo()


class RedoCommand(Command):

    def __init__(self, game_engine: GameEngine, history: History) -> None:
        super().__init__(game_engine)
        self._history: History = history

    def execute(self) -> None:
        self._history.redo()


class ExitCommand(Command):

    def execute(self) -> None:
        sys.exit()
