from fastapi import APIRouter
from fastapi_cache import caches
import requests
from functools import lru_cache
from bs4 import BeautifulSoup
import json

router = APIRouter()
API_KEY = "b0d36553a3d96fb804b15692f31eaf63"
artist_url_img_map = json.load(open("assets/data/artist_url_map.json", "r"))

# @lru_cache(maxsize=128)

# 根据歌曲mbid获取歌曲信息  /tracks/mbid
@router.get("/request/track/{mbid}", tags=["tracks"])
async def get_track_by_id(mbid: str):
    url = f"https://ws.audioscrobbler.com/2.0/?method=track.getInfo&mbid={mbid}&api_key={API_KEY}&format=json"
    res = _request(url)
    return res.json()


# 根据用户名获取用户信息  /users/username
@router.get("/request/user/{username}", tags=["tracks"])
async def get_user_by_name(username: str):
    url = f"https://ws.audioscrobbler.com/2.0/?method=user.getInfo&user={username}&api_key={API_KEY}&format=json"
    res = _request(url)
    return res.json()

# top歌手列表
@router.get("/request/topartists", tags=["tracks"])
async def get_top_artists(limit: int = 5):
    url = f"https://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={API_KEY}&format=json&limit={limit}"
    res = _request(url).json()

    # 获取歌手图片
    artist_lst = res['artists']['artist']
    for artist in artist_lst:
        url = artist['url']
        if artist['url'] in artist_url_img_map:
            artist['img'] = artist_url_img_map[url]
        else:
            artist['img'] = _get_artist_img(url)
            artist_url_img_map[url] = artist['img']
    return res


@lru_cache(maxsize=256)
def _request(url: str):
    # proxies = {
    #     "http": "http://localhost:6666",
    #     "https": "http://localhost:6666"
    # }
    res = requests.get(url)
    # print(url)
    return res


@lru_cache(maxsize=32)
def _get_artist_img(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser') \
        .find("div", class_="header-new-background-image").get('content')


# if __name__ == '__main__':
#     @lru_cache(maxsize=128)
#     def get_track_by_id(mbid: str):
#         url = f"https://ws.audioscrobbler.com/2.0/?method=track.getInfo&mbid={mbid}&api_key={API_KEY}&format=json"
#         res = requests.get(url)
#         print(mbid)
#         return res.json()
#
#     from tqdm import tqdm
#     for i in tqdm(range(1000)):
#         res = get_track_by_id("887d4e5d-44db-4421-9a61-fc12c335eb89")
