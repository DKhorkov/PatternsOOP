from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from commands import Command


class History:

    def __init__(self) -> None:
        self.__commands: List['Command'] = list()
        self.__current_command_index: int = len(self.__commands) - 1

    def add_command(self, command: 'Command') -> None:
        """
        If command is already in history and needs to be redone, just increases current command index.

        Elif multiple commands were executed and some of them were undid,
        deletes undid commands from history and adds new one.

        In base case just adds new command to history.

        :param command: New command, that was executed.
        """

        if self.__commands and self.__check_current_command_index() and self.__get_redo_command() == command:
            self.__current_command_index += 1
            return

        elif self.__check_current_command_index():
            self.__commands = self.__commands[: self.__current_command_index + 1]

        self.__commands.append(command)
        self.__current_command_index += 1

    def undo(self) -> None:
        if self.__current_command_index >= 0:
            command = self.__commands[self.__current_command_index]
            command.cancel()
            self.__current_command_index -= 1

    def redo(self) -> None:
        if self.__check_current_command_index():
            command = self.__get_redo_command()
            command.execute()

    def __check_current_command_index(self) -> bool:
        """
        Checks, if current command index in less than len of history not to raise IndexError in other methods.

        :return: Flag, signaling whether current command index is appropriate or not.
        """

        if self.__current_command_index < (len(self.__commands) - 1):
            return True

        return False

    def __get_redo_command(self) -> 'Command':
        """
        Command to redo is next to current executed command.

        :return: Command to redo.
        """

        command: Command = self.__commands[self.__current_command_index + 1]
        return command
