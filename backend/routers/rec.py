from fastapi import APIRouter
from ..algorithm import get_recommendation_model

router = APIRouter()
model = get_recommendation_model()


@router.get("/rec/{userid}", tags=["rec"])
async def read_user(userid: str):
    res = model.recall(userid, 10)
    # print(res)
    return {"userid": userid, "rec": res[1].tolist()}