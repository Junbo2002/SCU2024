from fastapi import APIRouter
from ..algorithm import get_recommendation_model
from ..database import get_tracks_by_ids

router = APIRouter()
model = get_recommendation_model()


@router.get("/rec/{userid}", tags=["rec"])
async def read_user(userid: str):
    res = model.recall(userid, 5)
    track_ids = res[1]
    track_mbids = get_tracks_by_ids(track_ids)
    # print(track_mbids, type(track_mbids))
    return {"userid": userid, "rec": [i[0] for i in track_mbids]}