from fastapi import APIRouter
from src.modules.mysql.db import DBConnection
from src.schema import car

app = APIRouter()

# Get a list of dealerships.
@app.get("/", status_code=200)
async def get_all_dealerships():
    db = DBConnection()
    return db.get_all_dealerships()
