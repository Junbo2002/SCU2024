from fastapi import APIRouter

router = APIRouter()


@router.get("/rec/{userid}", tags=["rec"])
async def read_user(userid: str):
    return {"userid": userid}