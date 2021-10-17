from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str
    manufacturer: str
    weight: float
    dimensions: str
    material: str
    barcode: str
    serial_number: str
    price: float

class Delete(BaseModel):
    part: int
    dealership: str
