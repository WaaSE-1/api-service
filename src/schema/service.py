from pydantic import BaseModel
from typing import Optional


class Service(BaseModel):
    VIN: str
    service: int
    mechanic: Optional[int] = None
    date: str
