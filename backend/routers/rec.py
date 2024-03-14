from fastapi import APIRouter
from ..algorithm import FinalModel
from ..database import get_tracks_by_ids

router = APIRouter()
model = FinalModel()


@router.get("/rec", tags=["rec"])
async def read_user(userid: str, count: int = 10):
    res = model.recall(userid, count)
    # print(res, type(res))
    track_mbids = get_tracks_by_ids(res)
    # print(track_mbids, type(track_mbids))
    # print(track_mbids, type(track_mbids))
    return {"userid": userid, "rec": [i[0] for i in track_mbids]}