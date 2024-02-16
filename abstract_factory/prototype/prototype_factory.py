from typing import Dict, Hashable, Union, Type

from abstract_prototype import AbstractPrototype
from exceptions import UnegisteredPrototypeError


class PrototypeFactory:

    prototypes: Dict[Hashable, AbstractPrototype] = {}

    @classmethod
    def create(cls, name: Hashable) -> object:
        cls.__check_type(object_to_check=name, allowed_type=Hashable)

        prototype = PrototypeFactory.prototypes.get(name)
        if prototype:
            return prototype.clone()

        raise UnegisteredPrototypeError(f'Prototype for {name} is not registered!')

    @classmethod
    def register(cls, name: Hashable, prototype: AbstractPrototype) -> None:
        cls.__check_type(object_to_check=name, allowed_type=Hashable)
        cls.__check_type(object_to_check=prototype, allowed_type=AbstractPrototype)
        cls.prototypes[name] = prototype

    @classmethod
    def unregister(cls, name: Hashable) -> None:
        cls.__check_type(object_to_check=name, allowed_type=Hashable)

        try:
            del cls.prototypes[name]
        except KeyError:
            raise UnegisteredPrototypeError(f'Prototype for {name} was not registered!')

    @staticmethod
    def __check_type(object_to_check: Hashable, allowed_type: Union[Type[Hashable] | Type[AbstractPrototype]]) -> None:
        if not isinstance(object_to_check, allowed_type):
            raise TypeError(f'{object_to_check}\'s type is not {allowed_type}!')


