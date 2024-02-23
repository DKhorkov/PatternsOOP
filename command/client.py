from typing import Dict, AnyStr

from game_engine import GameEngine
from commands import MoveBackCommand, MoveForwardCommand, MoveRightCommand, MoveLeftCommand, \
    PrintPositionCommand, ExitCommand, UndoCommand, RedoCommand
from errors import InvalidButtonError
from game_app import GameApp
from history import History
from custom_types import CommandAndInfo


class Client:

    def __init__(self) -> None:
        self.__game_engine: GameEngine = GameEngine()
        self.__history: History = History()
        self.__keyboard: Dict[AnyStr, CommandAndInfo] = {
            'w': CommandAndInfo(
                command=MoveForwardCommand(game_engine=self.__game_engine),
                info='Move forward'
            ),
            's': CommandAndInfo(
                command=MoveBackCommand(game_engine=self.__game_engine),
                info='Move back'
            ),
            'a': CommandAndInfo(
                command=MoveLeftCommand(game_engine=self.__game_engine),
                info='Move left'
            ),
            'd': CommandAndInfo(
                command=MoveRightCommand(game_engine=self.__game_engine),
                info='Move right'
            ),
            'tab': CommandAndInfo(
                command=PrintPositionCommand(game_engine=self.__game_engine),
                info='Show position'
            ),
            'r': CommandAndInfo(
                command=RedoCommand(game_engine=self.__game_engine, history=self.__history),
                info='Redo move'
            ),
            'u': CommandAndInfo(
                command=UndoCommand(game_engine=self.__game_engine, history=self.__history),
                info='Undo last move'
            ),
            'esc': CommandAndInfo(
                command=ExitCommand(game_engine=self.__game_engine),
                info='Exit'
            ),

            'i': CommandAndInfo(
                command=MoveForwardCommand(game_engine=self.__game_engine),
                info='Alternative move forward'
            ),
            'k': CommandAndInfo(
                command=MoveBackCommand(game_engine=self.__game_engine),
                info='Alternative move back'
            ),
            'j': CommandAndInfo(
                command=MoveLeftCommand(game_engine=self.__game_engine),
                info='Alternative move left'
            ),
            'l': CommandAndInfo(
                command=MoveRightCommand(game_engine=self.__game_engine),
                info='Alternative move right'
            ),
        }

        self.__game_app: GameApp = GameApp(keyboard=self.__keyboard, history=self.__history)

    def run(self) -> None:
        self.__game_app.print_valid_buttons()
        while True:
            try:
                self.__game_app.execute_command(button=self.__get_button())
            except InvalidButtonError as e:
                print(e)
            except KeyboardInterrupt:
                pass

    @staticmethod
    def __get_button() -> AnyStr:
        button: AnyStr = input('Please, write the button to use command:\t').lower().strip(' ')
        return button
