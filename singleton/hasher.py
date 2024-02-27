from hashlib import sha256
from typing import AnyStr

from configs import ENCODING


class Hasher:

    __hash_algorithm = sha256()

    @classmethod
    def __reload(cls) -> None:
        """
        Reloading hash algorithm every usage due to update() method logic.
        """
        cls.__hash_algorithm = sha256()

    @classmethod
    def hash(cls, cls_to_hash: object, *args, **kwargs) -> AnyStr:
        """
        Hashes class, which should be singleton, with its params ot support different singletons with onw __init__ args.

        :param cls_to_hash: Class, that should be a singleton.
        :return: Hashed class with its params.
        """

        args_data: AnyStr = '_'.join(args)
        kwargs_data: AnyStr = '_'.join([f'{key}:{value}' for key, value in kwargs.items()])
        data_to_hash: AnyStr = f'{cls_to_hash.__class__.__name__}_{args_data}_{kwargs_data}'
        cls.__hash_algorithm.update(data_to_hash.encode(ENCODING))
        hashed_value: AnyStr = cls.__hash_algorithm.hexdigest()
        cls.__reload()
        return hashed_value
