from fastapi import FastAPI
import uvicorn
from src.routes import (
    user,
    employee,
    car,
    inventory,
    product,
    service,
    dealership,
    department,
)
from fastapi.middleware.cors import CORSMiddleware
from src.settings.envvariables import Settings

Settings().check_variables()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include/define our routes
app.include_router(user.app, prefix="/users", tags=["Users"])
app.include_router(employee.app, prefix="/employees", tags=["Employees"])
app.include_router(car.app, prefix="/cars", tags=["Cars"])
app.include_router(inventory.app, prefix="/inventory", tags=["Inventory"])
app.include_router(product.app, prefix="/products", tags=["Product"])
app.include_router(service.app, prefix="/services/requests", tags=["Service"])
app.include_router(dealership.app, prefix="/dealerships", tags=["Dealership"])
app.include_router(department.app, prefix="/departments", tags=["Department"])

# Launch the app with uvicorn and handle environment
if Settings().ENV == "prod":
    if __name__ == "__main__":
        print("Launching Production Environment")
        uvicorn.run("main:app", host="0.0.0.0", port=Settings().PORT, reload=False, workers=3)
else:
    if __name__ == "__main__":
        print("Launching Development Environment")
        uvicorn.run("main:app", host="0.0.0.0", port=Settings().PORT, reload=True, workers=1)
