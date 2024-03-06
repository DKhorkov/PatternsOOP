import base64

from typing import List

from request import Request
from response import Response
from hasher import Hasher
from auth_handlers import (AuthHandler, NotAuthenticatedAuthHandler, BasicAuthHandler, BearerAuthHandler,
                           CookiesAuthHandler)
from configs import AuthTypes, ENCODING


class Example:

    def __init__(self) -> None:
        self.__requests: List[Request] = [
            Request(
                authorization=f'{AuthTypes.basic.value} {base64.b64encode('basic'.encode(ENCODING)).decode(ENCODING)}'
            ),
            Request(
                authorization=f'{AuthTypes.bearer.value} {Hasher.hash(username='bearer')}'
            ),
            Request(
                cookies={AuthTypes.cookies.value: Hasher.hash(username='cookies')}
            ),
            Request()
        ]

        self.__not_authenticated_auth_handler: AuthHandler = NotAuthenticatedAuthHandler()
        self.__basic_auth_handler: AuthHandler = BasicAuthHandler(parent=self.__not_authenticated_auth_handler)
        self.__bearer_auth_handler: AuthHandler = BearerAuthHandler(parent=self.__basic_auth_handler)
        self.__cookies_auth_handler: AuthHandler = CookiesAuthHandler(parent=self.__bearer_auth_handler)

    def process_requests(self) -> None:
        for request in self.__requests:
            response: Response = self.__cookies_auth_handler.authenticate(request=request)
            print(response)


if __name__ == '__main__':
    example = Example()
    example.process_requests()
