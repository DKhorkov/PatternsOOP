from dataclasses import dataclass, asdict
from typing import AnyStr, Optional, Dict, Any
from datetime import datetime


@dataclass
class Employee:
    # Personal data:
    name: AnyStr
    surname: AnyStr
    birthday: datetime
    address: AnyStr
    email: AnyStr
    phone: AnyStr

    # Job data:
    job_title: AnyStr
    hire_date: datetime
    salary: float
    fired: bool = False
    dismissal_date: Optional[datetime] = None

    def dict(self) -> Dict[AnyStr, Any]:
        return asdict(self)
