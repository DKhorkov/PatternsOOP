from typing import AnyStr

from abstract_mediator import Mediator
from engine import Engine
from pedal import Pedal
from ignition import Ignition
from car import Car
from events import EngineEvents, PedalEvents, IgnitionEvents


class CarMediator(Mediator):

    def __init__(self) -> None:
        self.__engine: Engine = Engine(self)
        self.__pedal: Pedal = Pedal(self)
        self.__ignition: Ignition = Ignition(self)
        self.__car: Car = Car(
            engine=self.__engine,
            pedal=self.__pedal,
            ignition=self.__ignition
        )

    def notify(self, component: object, event: AnyStr) -> None:
        if isinstance(component, Ignition) and event == IgnitionEvents.on.value:
            self.__engine.start()
            self.__pedal.unblock()
        elif isinstance(component, Ignition) and event == IgnitionEvents.off.value:
            self.__engine.stop()
            self.__pedal.block()
        elif isinstance(component, Engine) and event == EngineEvents.start.value:
            pass
        elif isinstance(component, Engine) and event == EngineEvents.stop.value:
            pass
        elif isinstance(component, Pedal) and event == PedalEvents.unblock.value:
            pass
        elif isinstance(component, Pedal) and event == PedalEvents.block.value:
            pass

    @property
    def car(self) -> Car:
        return self.__car
