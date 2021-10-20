from fastapi import APIRouter
from src.modules.mysql.db import DBConnection
from src.schema import car

app = APIRouter()

# Get a list of departments.
@app.get("/", status_code=200)
async def get_all_departments():
    db = DBConnection()
    return db.get_all_departments()
