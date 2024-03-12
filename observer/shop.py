from typing import AnyStr, Dict

from publisher import Publisher


class Shop(Publisher):

    def __init__(self, name: AnyStr) -> None:
        super().__init__()
        self.__name: AnyStr = name
        self.__goods: Dict[AnyStr, float] = {}

    def get_info(self) -> Dict[AnyStr, float]:
        return self.__goods

    @property
    def name(self) -> str:
        return self.__name

    @property
    def goods(self) -> Dict[AnyStr, float]:
        return self.__goods

    @goods.setter
    def goods(self, value: Dict[AnyStr, float]) -> None:
        self.__goods = value
        self.notify()

    def __str__(self) -> AnyStr:
        return self.__name
