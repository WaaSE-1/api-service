from pydantic import BaseModel


class Inventory(BaseModel):
    vehicle: str
    dealership: str
    inventory: int
