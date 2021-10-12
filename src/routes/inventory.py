from fastapi import APIRouter
from src.modules.mysql.db import DBConnection
from src.schema import inventory

app = APIRouter()

# Post request to update inventory
@app.post("/", status_code=200)
async def update_inventory(inventory: inventory.Inventory):
    db = DBConnection()
    return db.update_vehicle_inventory(inventory.dict())

# Post request to add car part to the stock
@app.post("/carpart", status_code=200)
async def update_car_part_inventory(inventory: inventory.CarPartInventory):
    db = DBConnection()
    return db.update_car_part_inventory(inventory.dict())
