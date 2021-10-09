from pydantic import BaseModel


class Car(BaseModel):
    manufacturer: str
    model: str
    year: int
    price: float
    