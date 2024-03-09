from engine import Engine
from chain import Chain
from ignition import Ignition


class Chainsaw:

    def __init__(self, engine: Engine, chain: Chain, ignition: Ignition) -> None:
        self.__engine: Engine = engine
        self.__chain: Chain = chain
        self.__ignition: Ignition = ignition

    def start(self) -> None:
        self.__ignition.on()

    def stop(self) -> None:
        self.__ignition.off()
