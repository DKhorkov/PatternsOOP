from typing import AnyStr, Dict, List

from commands import Command
from errors import InvalidButtonError


class GameApp:
    """
    Game App is an invoker class, which executes Commands.
    """

    def __init__(self, keyboard: Dict[AnyStr, List[Command | AnyStr]]) -> None:
        self.__keyboard: Dict[AnyStr, List[Command | AnyStr]] = keyboard

    def execute_command(self, button: AnyStr) -> None:
        command_and_info: List[Command | AnyStr] = self.__keyboard.get(button, None)
        if not command_and_info:
            raise InvalidButtonError(f'Invalid button "{button}"')

        command: Command = command_and_info[0]
        command.execute()

    def print_valid_buttons(self) -> None:
        valid_buttons: AnyStr = '\n'.join(
            [f'{button} - {command_and_info[1]}' for button, command_and_info in self.__keyboard.items()]
        )

        print('\n\nAvailable buttons are presented below:\n\n' + valid_buttons, end='\n\n')
