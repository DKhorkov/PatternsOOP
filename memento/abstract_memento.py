import datetime

from typing import AnyStr
from abc import ABC, abstractmethod


class AbstractMemento(ABC):

    def __init__(self, save_name: AnyStr, save_datetime: datetime.datetime) -> None:
        self.__save_name: AnyStr = save_name
        self.__save_datetime: datetime.datetime = save_datetime

    @abstractmethod
    def _get_game_state(self) -> None:
        raise NotImplementedError

    @property
    def save_name(self) -> AnyStr:
        return self.__save_name

    @property
    def save_datetime(self) -> datetime.datetime:
        return self.__save_datetime
