from fastapi import FastAPI
from app.routes import devices
from app.database import engine
from app import models
from app.mqtt_client import start_mqtt

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
def startup_event():
    start_mqtt()

app.include_router(devices.router)

@app.get("/")
def root():
    return {"message": "ScreenSync backend running"}