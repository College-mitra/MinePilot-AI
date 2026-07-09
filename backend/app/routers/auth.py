from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/")
async def auth_status():
    return {
        "message": "Authentication service is ready."
    }