from enum import Enum
from typing import AnyStr


class StatusCodes(Enum):
    success: int = 200
    fail: int = 404


class AuthMessages(Enum):
    success: AnyStr = 'Authenticated'
    fail: AnyStr = 'Not authenticated'


class AuthTypes(Enum):
    basic: AnyStr = 'Basic'
    bearer: AnyStr = 'Bearer'
    cookies: AnyStr = 'Access-Token'


ENCODING: AnyStr = 'utf-8'
