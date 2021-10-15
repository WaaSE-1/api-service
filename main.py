from fastapi import FastAPI
import uvicorn
from src.routes import user, car, inventory, product, service
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
app.include_router(car.app, prefix="/cars")
app.include_router(inventory.app, prefix="/inventory")
app.include_router(product.app, prefix="/products")
app.include_router(service.app, prefix="/services/requests")

# Launch the app with uvicorn and handle environment
if Settings().ENV == 'prod':
    if __name__ == '__main__':
        print('Launching Production Environment')
        uvicorn.run('main:app', host='0.0.0.0', port=80, reload=False, workers=3)
else:
    if __name__ == '__main__':
        print('Launching Development Environment')
        uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=1)
