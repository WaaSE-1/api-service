from pydantic import BaseModel


class Product(BaseModel):
    manufacturer: str
    weight: float
    dimensions: str
    material: str
    barcode: str
    serial_number: str
    price: float