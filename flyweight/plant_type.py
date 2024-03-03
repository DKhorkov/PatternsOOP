from dataclasses import dataclass
from typing import AnyStr


@dataclass(frozen=True)
class PlantType:
    name: AnyStr

    def __str__(self) -> AnyStr:
        return self.name
