from fastapi import APIRouter
from src.modules.mysql.db import DBConnection
from src.schema import car


app = APIRouter()

# GET request to list all cars
@app.get("/", status_code=200)
async def register_user():
    db = DBConnection()
    return db.get_all_cars()

# Create a new car
@app.post("/", status_code=200)
async def create_car(car: car.Car):
    db = DBConnection()
    return db.create_new_car(car.dict())
