from typing import AnyStr, Dict

from commands import Command
from errors import InvalidButtonError
from history import History
from custom_types import CommandAndInfo


class GameApp:
    """
    Game App is an invoker class, which executes Commands.
    """

    def __init__(self, keyboard: Dict[AnyStr, CommandAndInfo], history: History) -> None:
        self.__keyboard: Dict[AnyStr, CommandAndInfo] = keyboard
        self.__history: History = history

    def execute_command(self, button: AnyStr) -> None:
        command_and_info: CommandAndInfo = self.__keyboard.get(button, None)
        if not command_and_info:
            raise InvalidButtonError(f'Invalid button "{button}"')

        command: Command = command_and_info.command
        command.execute()

        if command.undoable:
            self.__history.add_command(command=command)

    def print_valid_buttons(self) -> None:
        valid_buttons: AnyStr = '\n'.join(
            [f'{button} - {command_and_info.info}' for button, command_and_info in self.__keyboard.items()]
        )

        print('\n\nAvailable buttons are presented below:\n\n' + valid_buttons, end='\n\n')
