from typing import AnyStr

from abstract_mediator import Mediator
from engine import Engine
from chain import Chain
from ignition import Ignition
from chainsaw import Chainsaw
from events import EngineEvents, ChainEvents, IgnitionEvents


class ChainsawMediator(Mediator):

    def __init__(self) -> None:
        self.__engine: Engine = Engine(self)
        self.__chain: Chain = Chain(self)
        self.__ignition: Ignition = Ignition(self)
        self.__chainsaw: Chainsaw = Chainsaw(
            engine=self.__engine,
            chain=self.__chain,
            ignition=self.__ignition
        )

    def notify(self, component: object, event: AnyStr) -> None:
        if isinstance(component, Ignition) and event == IgnitionEvents.on.value:
            self.__engine.start()
            self.__chain.spin()
        elif isinstance(component, Ignition) and event == IgnitionEvents.off.value:
            self.__engine.stop()
            self.__chain.stop()
        elif isinstance(component, Engine) and event == EngineEvents.start.value:
            pass
        elif isinstance(component, Engine) and event == EngineEvents.stop.value:
            pass
        elif isinstance(component, Chain) and event == ChainEvents.spins.value:
            pass
        elif isinstance(component, Chain) and event == ChainEvents.stays.value:
            pass

    @property
    def chainsaw(self) -> Chainsaw:
        return self.__chainsaw
