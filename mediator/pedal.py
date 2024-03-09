from abstract_mediator import Mediator
from events import PedalEvents


class Pedal:

    def __init__(self, mediator: Mediator) -> None:
        self.__mediator = mediator
        self.__is_blocked: bool = True

    def unblock(self) -> None:
        print('Pedal is unblocked')
        self.__is_blocked = False
        self.__mediator.notify(component=self, event=PedalEvents.unblock.value)

    def block(self) -> None:
        print('Pedal is blocked')
        self.__is_blocked = True
        self.__mediator.notify(component=self, event=PedalEvents.block.value)

    @property
    def is_blocked(self) -> bool:
        return self.__is_blocked
