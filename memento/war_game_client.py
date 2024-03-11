from typing import List, AnyStr

from abstract_memento import AbstractMemento
from war_game import WarGame
from exceptions import NotEnoughMoneyError, NoUnitsToSellError


class WarGameClient:

    def __init__(self) -> None:
        self.__game: WarGame = WarGame()
        self.__saves: List[AbstractMemento] = []

    def save_game(self, save_name: AnyStr) -> None:
        save: AbstractMemento = self.__game.save(save_name=save_name)
        self.__saves.append(save)

    def load_game(self, save_index: int) -> None:
        save: AbstractMemento = self.__saves[save_index - 1]  # due to enumerate from 1
        self.__game.load(save=save)

    def view_saves(self) -> None:
        print(f'\nThere are {len(self.__saves)} saves now:')
        for index, save in enumerate(self.__saves, start=1):
            print(f'{index}) - {save.save_name} {save.save_datetime}')

    def delete_save(self, save_index: int) -> None:
        try:
            self.__saves.pop(save_index - 1)  # due to enumerate from 1
        except IndexError:
            print(f'No save with index {save_index}!')

    def buy_soldier(self) -> None:
        try:
            self.__game.buy_soldier()
        except NotEnoughMoneyError as e:
            print(e)

    def sell_soldier(self) -> None:
        try:
            self.__game.sell_soldier()
        except NoUnitsToSellError as e:
            print(e)

    def buy_tank(self) -> None:
        try:
            self.__game.buy_tank()
        except NotEnoughMoneyError as e:
            print(e)

    def sell_tank(self) -> None:
        try:
            self.__game.sell_tank()
        except NoUnitsToSellError as e:
            print(e)

    def fight_enemy(self) -> None:
        fight_status: AnyStr = self.__game.fight_enemy()
        print(fight_status)
