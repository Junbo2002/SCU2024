import json
from fastapi import APIRouter
from ..database import *

router = APIRouter()


@router.get("/visualize/userrank", tags=["visualize"])
async def get_user_rank(count: int = 20):
    res = get_top_users(count)
    return res


@router.get("/visualize/trackrank", tags=["visualize"])
async def get_track_rank(count: int =20):
    res = get_top_tracks(count)
    return res


@router.get("/visualize/avgnationplaycount", tags=["visualize"])
async def get_avg_nation_playcount():
    res = get_avg_playcount_by_nationality()
    return res


@router.get("/visualize/nationusers", tags=["visualize"])
async def get_nation_users():
    res = get_cnt_by_nationality()
    return res


@router.get("/visualize/age", tags=["visualize"])
async def get_ages(age1: int = 18, age2: int = 35, age3: int = 55):
    res = get_age_info([age1, age2, age3])
    return res


@router.get("/visualize/playcountrange", tags=["visualize"])
async def get_play_count_range():
    res = get_playcount_range()
    return res


@router.get("/visualize/gender", tags=["visualize"])
async def get_gender():
    res = get_gender_users()
    return res
