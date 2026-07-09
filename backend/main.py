from fastapi import FastAPI
from app.core.firebase import db
from app.routers.auth import router as auth_router

app = FastAPI(
    title="MinePilot AI Backend",
    version="1.0.0",
    description="Backend API for MinePilot AI"
)

app.include_router(auth_router)

@app.get("/")
async def root():
    return {
        "app": "MinePilot AI",
        "message": "Backend is running 🚀"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }