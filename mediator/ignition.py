from abstract_mediator import Mediator
from events import IgnitionEvents


class Ignition:

    def __init__(self, mediator: Mediator) -> None:
        self.__mediator = mediator

    def on(self) -> None:
        print('Turned on the ignition')
        self.__mediator.notify(component=self, event=IgnitionEvents.on.value)

    def off(self) -> None:
        print('Turned off the ignition')
        self.__mediator.notify(component=self, event=IgnitionEvents.off.value)
