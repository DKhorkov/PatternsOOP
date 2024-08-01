from typing import Dict, Type

from tabular_method.pets import Pet, Dog, Rat, Cat

PETS: Dict[str, Type[Pet]] = {
    'cat': Cat,
    'dog': Dog,
    'rat': Rat
}
