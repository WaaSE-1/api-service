from fastapi import APIRouter  # , Response
from src.modules.mysql.db import DBConnection
from src.schema import product

app = APIRouter()

# Get all products
@app.get("/", status_code=200)
async def get_all_products():
    db = DBConnection()
    return db.get_all_products()


@app.post("/", status_code=201)
async def create_a_product(product: product.Product):
    db = DBConnection()
    return db.create_new_product(product.dict())


# TODO Assign a product to a dealership
