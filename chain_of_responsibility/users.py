from typing import Dict, Hashable, AnyStr

from hasher import Hasher


# Used as database. Getting username by token:
ALLOWED_USERS: Dict[Hashable, AnyStr] = {
    Hasher.hash('basic'): 'basic',
    Hasher.hash('bearer'): 'bearer',
    Hasher.hash('cookies'): 'cookies'
}
