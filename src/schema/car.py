from pydantic import BaseModel

# Define class for a car (creating)
class Car(BaseModel):
    manufacturer: str
    model: str
    year: int
    price: float

# Define class for deleting a car
class Delete(BaseModel):
    vehicle: int
    dealership: str
