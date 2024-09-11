from fastapi import APIRouter # type: ignore

router = APIRouter()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}