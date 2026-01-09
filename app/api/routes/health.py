from fastapi import APIRouter

router = APIRouter()


@router.get("/version")
def get_version() -> dict:
    return {
        "service": "online-reservation-auth",
        "version": "0.1.0",
        "status": "ok",
    }
