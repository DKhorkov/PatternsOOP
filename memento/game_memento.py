import datetime

from typing import AnyStr, Dict, Any

from abstract_memento import AbstractMemento


class GameMemento(AbstractMemento):

    def __init__(
            self,
            save_name: AnyStr,
            money: int,
            army_power: int,
            enemy_power: int,
            solders_count: int,
            tanks_count: int
    ) -> None:

        super().__init__(save_name=save_name, save_datetime=datetime.datetime.now())
        self.__money: int = money
        self.__army_power: int = army_power
        self.__enemy_power: int = enemy_power
        self.__solders_count: int = solders_count
        self.__tanks_count: int = tanks_count

    def _get_game_state(self) -> Dict[AnyStr, Any]:
        return {
            'money': self.__money,
            'army_power': self.__army_power,
            'enemy_power': self.__enemy_power,
            'solders_count': self.__solders_count,
            'tanks_count': self.__tanks_count
        }
