from fastapi import FastAPI
from src.routes import user


app = FastAPI()

app.include_router(user.app, prefix="/users")
