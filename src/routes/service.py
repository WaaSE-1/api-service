from fastapi import APIRouter, Response, Depends
import random
from src.modules.auth.core import Auth
from src.modules.mysql.db import DBConnection
from src.schema import service

app = APIRouter()

# Get all avaiable services
@app.get("/", status_code=200)
async def get_available_services():
    db = DBConnection()
    return db.get_all_services()


# Create service request
@app.post("/", status_code=201)
async def create_service_request(service: service.Service):
    service = service.dict()
    # Establishes connection to the database
    db = DBConnection()
    # Check if service with given ID exists
    if not db.valid_service(service["service"]):
        return {"error": "Service with specified ID was not found!"}

    # Check if the provided VIN number is valid.
    # In future we should also check if this VIN is owned by the request init.
    if db.valid_vin(service["VIN"]):
        return {"error": "Vehicle with the provided VIN number was not found!"}

    # Fetch a list of all active employees
    employees = db.get_all_employees()

    # Set employee ID to be random number if one was not specified
    if not service["mechanic"]:
        service["mechanic"] = random.choice(employees)["id"]

    return db.create_service_request(service)


# Get service history for a given user.
@app.get("/history", status_code=200)
async def get_service_history(
    response: Response, token: str = Depends(Auth.validate_token)
):
    db = DBConnection()
    return db.get_service_history(token["id"])
