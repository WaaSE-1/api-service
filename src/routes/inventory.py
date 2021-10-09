from fastapi import APIRouter
from src.modules.mysql.db import DBConnection
from src.schema import inventory 

app = APIRouter()

#Post request to update inventory
@app.post("/", status_code=200) 
async def update_inventory(inventory: inventory.Inventory):
    print(inventory.dict())
    db = DBConnection()
    return db.update_vehicle_inventory(inventory.dict()) 

