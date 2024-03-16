from fastapi import APIRouter
from fastapi_cache import caches
import requests
from functools import lru_cache
from bs4 import BeautifulSoup
import json

router = APIRouter()
API_KEY = "b0d36553a3d96fb804b15692f31eaf63"
artist_url_img_map = json.load(open("assets/data/artist_url_map.json", "r"))


@router.get("/request/track/{mbid}", tags=["requests"])
async def get_track_by_id(mbid: str):
    """
    根据歌曲 mbid 获取歌曲信息
    :param mbid: lastfm官方对歌曲的唯一标识
    :return: {"track": {"name": "song name", ...}}
    """
    url = f"https://ws.audioscrobbler.com/2.0/?method=track" \
          f".getInfo&mbid={mbid}&api_key={API_KEY}&format=json"
    res = _request(url)
    return res.json()


@router.get("/request/user/{username}", tags=["requests"])
async def get_user_by_name(username: str):
    """
    根据用户名获取用户信息
    :param username: 用户名
    :return: {"user": {"name": "elchode", ...}}
    """
    url = f"https://ws.audioscrobbler.com/2.0/?method=user.getInfo&user={username}&api_key={API_KEY}&format=json"
    res = _request(url)
    return res.json()


@router.get("/request/topartists", tags=["requests"])
async def get_top_artists(limit: int = 5):
    """
    获取top歌手列表
    :param limit: top歌手数量
    :return: {
        "artists": {
            "artist": [
                {
                    "name": "The Weeknd",
                    "playcount": "621398803",
                    "mbid": "c8b03190-306c-4120-bb0b-6f2ebfc06ea9",
                    "url": "https://www.last.fm/music/The+Weeknd",
                    "image": "https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png",
                    "img": "https://lastfm.freetls.fastly.net/i/u/ar0/725cbf01f1b2b49bf17b3cb6e956283b.jpg"
                    ...
                },
                ...
    ]}}
    """
    url = f"https://ws.audioscrobbler.com/2.0/?method=chart" \
          f".gettopartists&api_key={API_KEY}&format=json&limit={limit}"
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


@lru_cache(maxsize=512)
def _request(url: str):
    """
    请求封装,方便使用 LRU 缓存
    :param url: 请求地址
    :return: 请求结果
    """

    # 添加代理
    proxies = {
        "http": "http://localhost:6666",
        "https": "http://localhost:6666"
    }
    res = requests.get(url, proxies=proxies)
    return res


@lru_cache(maxsize=128)
def _get_artist_img(url):
    """
    获取歌手图片
    :param url: 歌手链接地址
    :return: 歌手图片地址
    """
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
