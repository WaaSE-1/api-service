from fastapi import APIRouter  # , Response
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
    # Establishes connection to the database
    db = DBConnection()
    return db.create_service_request(service.dict())
