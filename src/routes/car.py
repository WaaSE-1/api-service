from fastapi import APIRouter
from src.modules.mysql.db import DBConnection
from src.schema import car

app = APIRouter()

# Get request for specific car
@app.get("/{car_id}", status_code=200)
async def register_user(car_id):
    db = DBConnection()
    return db.get_car_by_id(car_id)


# GET request to list all cars
@app.get("/", status_code=200)
async def register_user():
    db = DBConnection()
    return db.get_all_cars()


# Create a new car
@app.post("/", status_code=201)
async def create_car(car: car.Car):
    db = DBConnection()
    return db.create_new_car(car.dict())


# Remove a car
@app.delete("/", status_code=200)
async def remove_car(car: car.Delete):
    db = DBConnection()
    return db.remove_car(car.dict())
