from typing import AnyStr, Any

from observer.publisher import Publisher
from subscriber import Subscriber


class Customer(Subscriber):

    def __init__(self, name: AnyStr) -> None:
        super().__init__()
        self.__name: AnyStr = name

    def update(self, publisher: Publisher) -> None:
        print(f'{self.__name} received update from {str(publisher)}...')
        info: Any = publisher.get_info()
        print(
            f'{self.__name} requested information on the subscription from {str(publisher)} and '
            f'received the following response {info}...'
        )

    @property
    def name(self) -> AnyStr:
        return self.__name
