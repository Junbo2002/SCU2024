import json
from fastapi import APIRouter
from ..database import *

router = APIRouter()


@router.get("/visualize/userrank", tags=["visualize"])
async def get_user_rank(count: int = 20):
    """
    获取用户排行榜(根据听歌数量排序)
    :param count: 返回用户数量
    :return: [
        {
            "lastfm_username": "Lukinx",
            "gender": "",
            "age": "",
            "country": "SE",
            "playcount": 1000017,
            "subscribertype": "base"
        },
        ...
    ]
    """
    res = get_top_users(count)
    return res


@router.get("/visualize/trackrank", tags=["visualize"])
async def get_track_rank(count: int = 20):
    """
    获取歌曲排行榜(根据播放次数排序)
    :param count: 返回歌曲数量
    :return: [
        {
            "id": "2369978",
            "person_id": "296242",
            "MBID": "34678368-3745-4930-b3df-a05f156e8d78",
            "name": "Riton/_/Put+That+on+My+Momma",
            "album_id": "136388",
            "duration": "314000",
            "playcount": 1285338
        },
        ...
    ]
    """
    res = get_top_tracks(count)
    return res


@router.get("/visualize/avgnationplaycount", tags=["visualize"])
async def get_avg_nation_playcount():
    """
    获取不同国籍用户播放量的平均值
    :return: [
        {
            "name": "Switzerland",
            "value": 30475
        },
        ...
    ]
    """
    res = get_avg_playcount_by_nationality()
    return res


@router.get("/visualize/nationusers", tags=["visualize"])
async def get_nation_users():
    """
    获取不同国籍用户数量
    :return: [
        {
            "name": "United States",
            "value": 91534
        },
        ...
    ]
    """
    res = get_cnt_by_nationality()
    return res


@router.get("/visualize/age", tags=["visualize"])
async def get_ages(age1: int = 18, age2: int = 35, age3: int = 55):
    """
    获取不同年龄段用户数量
    :param [age1, age2, age3]: 年龄段
    :return: {
        "18-35": {
            "base": 21875,
            "premium": 215
        },
        ...
    }
    """
    res = get_age_info(sorted([age1, age2, age3]))
    return res


@router.get("/visualize/ageall", tags=["visualize"])
async def get_ages():
    """
    获取所有年龄段用户数量
    :return: {
        "base": [15, 10, 6, 6, 19, ...]
        "premium": [2, 1, 0, 2, 1, ...]
    }
    """
    res = get_age_info_all()
    return res


@router.get("/visualize/playcountrange", tags=["visualize"])
async def get_play_count_range():
    """
    获取不同播放量区间用户数量
    :return: {
        "0-10000": 6321,
        "10000-20000": 6058,
        "20000-30000": 5557,
        ...
    }
    """
    res = get_playcount_range()
    return res


@router.get("/visualize/gender", tags=["visualize"])
async def get_gender():
    """
    获取不同性别用户数量
    :return: {
        "unknown": 120,
        "f": 13490,
        "m": 26377,
        "n": 5180
    }
    """
    res = get_gender_users()
    return res


@router.get("/request/user", tags=["visualize"])
async def get_user_by_name(uid: str):
    """
    根据用户id获取用户名
    :param uid: 用户id
    :return: "elcorazon33"
    """
    res = get_username_by_id(uid)
    return res
