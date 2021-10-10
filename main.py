from fastapi import FastAPI
from src.routes import user, car, inventory, product
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

app.include_router(user.app, prefix="/users")
app.include_router(car.app, prefix="/cars")
app.include_router(inventory.app, prefix="/inventory")
app.include_router(product.app, prefix="/products")
