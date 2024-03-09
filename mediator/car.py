from engine import Engine
from pedal import Pedal
from ignition import Ignition


class Car:

    def __init__(self, engine: Engine, pedal: Pedal, ignition: Ignition) -> None:
        self.__engine: Engine = engine
        self.__pedal: Pedal = pedal
        self.__ignition: Ignition = ignition

    def start(self) -> None:
        self.__ignition.on()

    def stop(self) -> None:
        self.__ignition.off()
