from fastapi import FastAPI
from app.routers import entity

app = FastAPI(title="Orion-LD Adapter Service")

app.include_router(entity.router, prefix="/orion/entity", tags=["Entity"])
