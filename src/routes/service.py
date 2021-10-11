from fastapi import APIRouter  # , Response
from src.modules.mysql.db import DBConnection
from src.schema import service

app = APIRouter()

# Create service request
@app.post("/", status_code=201)
async def create_service_request(service: service.Service):
    # Establishes connection to the database
    db = DBConnection()
    return db.create_service_request(service.dict())

