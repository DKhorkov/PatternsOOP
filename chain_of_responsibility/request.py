from typing import AnyStr, Optional, Dict
from pydantic import BaseModel


class Request(BaseModel):
    cookies: Optional[Dict[AnyStr, AnyStr]] = None
    authorization: Optional[AnyStr] = None
