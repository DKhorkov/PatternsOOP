from abstract_mediator import Mediator
from events import ChainEvents


class Chain:

    def __init__(self, mediator: Mediator) -> None:
        self.__mediator = mediator
        self.__is_spinning: bool = False

    def spin(self) -> None:
        print('Chain is spinning now')
        self.__is_spinning = True
        self.__mediator.notify(component=self, event=ChainEvents.spins.value)

    def stop(self) -> None:
        print('Chain stopped spinning')
        self.__is_spinning = False
        self.__mediator.notify(component=self, event=ChainEvents.stays.value)

    @property
    def is_spinning(self) -> bool:
        return self.__is_spinning
