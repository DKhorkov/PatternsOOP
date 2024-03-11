from typing import AnyStr

from configs import GameSettings, GameStatuses
from game_memento import GameMemento
from abstract_memento import AbstractMemento
from game import Game


class WarGame(Game):

    def __init__(
            self,
            money: int = GameSettings.start_money.value,
            army_power: int = 0,
            enemy_power: int = GameSettings.enemy_power.value,
            solders_count: int = 0,
            tanks_count: int = 0
    ) -> None:

        self.__money: int = money
        self.__army_power: int = army_power
        self.__enemy_power: int = enemy_power
        self.__solders_count: int = solders_count
        self.__tanks_count: int = tanks_count

    def buy_soldier(self) -> None:
        if self.__money >= GameSettings.solder_cost.value:
            self.__solders_count += 1
            self.__money -= GameSettings.solder_cost.value
            self.__army_power += GameSettings.solder_power.value
        else:
            print(f'Not enough money to buy soldier!')

    def sell_soldier(self) -> None:
        if self.__solders_count > 0:
            self.__solders_count -= 1
            self.__money += GameSettings.solder_cost.value * GameSettings.sales_ratio.value
            self.__army_power -= GameSettings.solder_power.value
        else:
            print(f'No soldiers to sell!')

    def buy_tank(self) -> None:
        if self.__money >= GameSettings.tank_cost.value:
            self.__tanks_count += 1
            self.__money -= GameSettings.tank_cost.value
            self.__army_power += GameSettings.tank_power.value
        else:
            print(f'Not enough money to buy tank!')

    def sell_tank(self) -> None:
        if self.__tanks_count > 0:
            self.__tanks_count -= 1
            self.__money += GameSettings.tank_cost.value * GameSettings.sales_ratio.value
            self.__army_power -= GameSettings.tank_power.value
        else:
            print(f'No tanks to sell!')

    def fight_enemy(self) -> AnyStr:
        if self.__army_power > self.__enemy_power:
            return GameStatuses.victory.value
        elif self.__army_power == self.__enemy_power:
            return GameStatuses.draw.value
        else:
            return GameStatuses.defeat.value

    def save(self, save_name: AnyStr) -> AbstractMemento:
        return GameMemento(
            save_name=save_name,
            **{
                attr.split('__')[-1]: value for attr, value in self.__dict__.items()
            }
        )

    def load(self, save: AbstractMemento) -> None:
        """
        Evading the impossibility of creating two different interfaces in Python: external (for all caretakers)
        and internal (for the owner class).
        """

        self.__init__(**save._get_game_state())
