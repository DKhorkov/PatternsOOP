from typing import List, Dict, AnyStr

from game_engine import GameEngine
from commands import Command, MoveBackCommand, MoveForwardCommand, MoveRightCommand, MoveLeftCommand, \
    PrintPositionCommand, ExitCommand, UndoCommand, RedoCommand
from errors import InvalidButtonError
from game_app import GameApp
from history import History


class Client:

    def __init__(self) -> None:
        self.__game_engine: GameEngine = GameEngine()
        self.__history: History = History()
        self.__keyboard: Dict[AnyStr, List[Command | AnyStr]] = {
            'w': [MoveForwardCommand(game_engine=self.__game_engine, history=self.__history), 'Move forward'],
            's': [MoveBackCommand(game_engine=self.__game_engine, history=self.__history), 'Move back'],
            'a': [MoveLeftCommand(game_engine=self.__game_engine, history=self.__history), 'Move left'],
            'd': [MoveRightCommand(game_engine=self.__game_engine, history=self.__history), 'Move right'],
            'tab': [PrintPositionCommand(game_engine=self.__game_engine, history=self.__history), 'Show position'],
            'r': [RedoCommand(game_engine=self.__game_engine, history=self.__history), 'Redo move'],
            'u': [UndoCommand(game_engine=self.__game_engine, history=self.__history), 'Undo last move'],
            'esc': [ExitCommand(game_engine=self.__game_engine, history=self.__history), 'Exit'],

            'i': [MoveForwardCommand(game_engine=self.__game_engine, history=self.__history), 'Alternative move forward'],
            'k': [MoveBackCommand(game_engine=self.__game_engine, history=self.__history), 'Alternative move back'],
            'j': [MoveLeftCommand(game_engine=self.__game_engine, history=self.__history), 'Alternative move left'],
            'l': [MoveRightCommand(game_engine=self.__game_engine, history=self.__history), 'Alternative move right'],
        }

        self.__game_app: GameApp = GameApp(keyboard=self.__keyboard)

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
