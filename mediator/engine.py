from abstract_mediator import Mediator
from events import EngineEvents


class Engine:

    def __init__(self, mediator: Mediator) -> None:
        self.__mediator = mediator
        self.__is_working: bool = False

    def start(self) -> None:
        print('Engine started working')
        self.__is_working = True
        self.__mediator.notify(component=self, event=EngineEvents.start.value)

    def stop(self) -> None:
        print('Engine stopped working')
        self.__is_working = False
        self.__mediator.notify(component=self, event=EngineEvents.stop.value)

    @property
    def is_working(self) -> bool:
        return self.__is_working
