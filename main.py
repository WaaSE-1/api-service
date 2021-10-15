from fastapi import FastAPI
from src.routes import user, employee, car, inventory, product, service
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
app.include_router(user.app, prefix="/users")
app.include_router(employee.app, prefix="/employees")
app.include_router(car.app, prefix="/cars")
app.include_router(inventory.app, prefix="/inventory")
app.include_router(product.app, prefix="/products")
app.include_router(service.app, prefix="/services/requests")