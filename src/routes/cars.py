from fastapi import APIRouter
from src.modules.mysql.db import DBConnection


app = APIRouter()

# GET request to list all cars
@app.get("/", status_code=200)
async def register_user():
    db = DBConnection()
    return db.get_all_cars()

