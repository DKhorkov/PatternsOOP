from dataclasses import dataclass, asdict
from typing import AnyStr

from configs import STR_SEPARATOR


@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int
    name: AnyStr

    def __str__(self) -> AnyStr:
        return STR_SEPARATOR.join(
            [value for key, value in asdict(self).items()]
        )
