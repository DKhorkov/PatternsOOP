from typing import Protocol, runtime_checkable


@runtime_checkable
class Animal(Protocol):

    def make_voice(self) -> None:
        pass
