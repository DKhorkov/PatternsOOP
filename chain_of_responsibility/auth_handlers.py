import base64

from typing import AnyStr
from abc import ABC, abstractmethod

from request import Request
from response import Response
from configs import AuthTypes, StatusCodes, AuthMessages, ENCODING
from users import ALLOWED_USERS


class AuthHandler(ABC):

    @abstractmethod
    def authenticate(self, request: Request) -> Response:
        raise NotImplementedError


class NotAuthenticatedAuthHandler(AuthHandler):

    def authenticate(self, request: Request) -> Response:
        return Response()


class BasicAuthHandler(AuthHandler):

    def __init__(self, parent: AuthHandler):
        self.__parent: AuthHandler = parent

    def authenticate(self, request: Request) -> Response:
        if request.authorization and request.authorization.startswith(AuthTypes.basic.value):
            username: AnyStr = base64.b64decode(
                request.authorization.split(' ')[-1]
            ).decode(ENCODING)

            if username:
                return Response(
                    username=username,
                    status_code=StatusCodes.success.value,
                    message=AuthMessages.success.value
                )

        return self.__parent.authenticate(request=request)


class BearerAuthHandler(AuthHandler):

    def __init__(self, parent: AuthHandler):
        self.__parent: AuthHandler = parent

    def authenticate(self, request: Request) -> Response:
        if request.authorization and request.authorization.startswith(AuthTypes.bearer.value):
            username: AnyStr = ALLOWED_USERS.get(
                request.authorization.split(' ')[-1]
            )

            if username:
                return Response(
                    username=username,
                    status_code=StatusCodes.success.value,
                    message=AuthMessages.success.value
                )

        return self.__parent.authenticate(request=request)


class CookiesAuthHandler(AuthHandler):

    def __init__(self, parent: AuthHandler):
        self.__parent: AuthHandler = parent

    def authenticate(self, request: Request) -> Response:
        if request.cookies and request.cookies.get(AuthTypes.cookies.value):
            username: AnyStr = ALLOWED_USERS.get(
                request.cookies.get(
                    AuthTypes.cookies.value
                )
            )

            if username:
                return Response(
                    username=username,
                    status_code=StatusCodes.success.value,
                    message=AuthMessages.success.value
                )

        return self.__parent.authenticate(request=request)
