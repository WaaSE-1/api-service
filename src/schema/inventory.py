from pydantic import BaseModel

class Inventory(BaseModel):
    vehicle: int
    dealership: str
    inventory: int

class CarPartInventory(BaseModel):
    car_part_id: int
    dealership: str
    inventory: int
