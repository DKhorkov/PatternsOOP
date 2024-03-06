from typing import AnyStr, Optional
from pydantic import BaseModel
from configs import StatusCodes, AuthMessages


class Response(BaseModel):
    username: Optional[AnyStr] = None
    message: AnyStr = AuthMessages.fail.value
    status_code: int = StatusCodes.fail.value

    def __str__(self) -> AnyStr:
        return (
            f'Response for user with username={self.username}.\n'
            f'Status_code={self.status_code}\n'
            f'Message={self.message}\n'
        )
