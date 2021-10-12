from pydantic import BaseModel

class Service(BaseModel):
    VIN: str
    service: int
    mechanic: int
    date: str
