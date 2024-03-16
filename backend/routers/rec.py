from fastapi import APIRouter
from ..algorithm import FinalModel
from ..database import get_tracks_by_ids

router = APIRouter()
model = FinalModel()


@router.get("/rec", tags=["rec"])
async def get_rec_by_uid(userid: str, count: int = 10):
    """
    根据用户id获取推荐歌曲
    :param userid: 用户id
    :param count: 推荐数量
    :return: {
        "userid": "6007",
        "rec": [
            "3c52dc03-f169-464e-83ab-0f26888799db",
            "d20ada7a-b028-4cf6-9e85-48b7712c1932",
            ...
        ]
    }
    """
    # 获得推荐歌曲的ids
    res = model.recall(userid, count)
    # 根据歌曲ids获取歌曲mbid
    track_mbids = get_tracks_by_ids(res)
    return {"userid": userid, "rec": [i[0] for i in track_mbids]}