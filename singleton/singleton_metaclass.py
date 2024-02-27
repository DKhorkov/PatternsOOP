from typing import AnyStr

from hasher import Hasher


class SingletonMetaclass(type):

    _instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        """
        Checks if the class with provided args already exists.

        Uses hashed class with args for creating singletons with different __init__ arguments,
        but have same class scheme.
        """

        hashed_instance_key: AnyStr = Hasher.hash(cls, *args, **kwargs)
        if hashed_instance_key not in cls._instances:
            instance: object = super().__call__(*args, **kwargs)
            cls._instances[hashed_instance_key] = instance

        return cls._instances[hashed_instance_key]
