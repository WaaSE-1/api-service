from pydantic import BaseModel

# Define classes for a car and deleting a car
class Car(BaseModel):
    manufacturer: str
    model: str
    year: int
    price: float


class Delete(BaseModel):
    vehicle: int
    dealership: str
