from typing import Dict, AnyStr, Callable

from pc_interface import PCInterface
from emulator import Emulator


class Client:

    def __init__(self) -> None:
        self.__interface: PCInterface = Emulator()

        # Should be a Command pattern in real app:
        self.__commands: Dict[AnyStr, Callable] = {
            'w': self.__interface.w,
            's': self.__interface.s,
            'd': self.__interface.d,
            'a': self.__interface.a,
            'tab': self.__interface.tab,
            'esc': self.__interface.esc,
        }

    def run(self) -> None:
        self.__print_commands_info()
        while True:
            command: AnyStr = input('\nPlease, enter a game command:\t')
            if command not in self.__commands:
                print('Invalid command, please, try again!')
                continue

            self.__commands[command]()

    @staticmethod
    def __print_commands_info() -> None:
        commands_info: AnyStr = f'w - move forward;\n' \
                                f's - move back;\n' \
                                f'd - move right;\n' \
                                f's - move left;\n' \
                                f'tab - print current position;\n' \
                                f'esc - exit.'

        print(commands_info, end='\n\n')
