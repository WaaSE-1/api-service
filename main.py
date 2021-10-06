from fastapi import FastAPI
from src.routes import user, cars
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.app, prefix="/users")
app.include_router(cars.app, prefix="/cars")
