from fastapi import FastAPI

app = FastAPI(
    title="MinePilot AI Backend",
    version="1.0.0",
    description="Backend API for MinePilot AI"
)

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