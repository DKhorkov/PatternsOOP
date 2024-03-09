from enum import Enum
from typing import AnyStr


class EngineEvents(Enum):
    start: AnyStr = 'start'
    stop: AnyStr = 'stop'


class PedalEvents(Enum):
    block: AnyStr = 'block'
    unblock: AnyStr = 'unblock'


class IgnitionEvents(Enum):
    on: AnyStr = 'on'
    off: AnyStr = 'off'


class ChainEvents(Enum):
    spins: AnyStr = 'spins'
    stays: AnyStr = 'stays'
