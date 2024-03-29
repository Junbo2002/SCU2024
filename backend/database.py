import json
import mysql.connector
import numpy as np

db = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="minidata"
)
cursor = db.cursor()

db_large = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="bigdata"
)
cursor_large = db_large.cursor()


# 定义一些常量
country_map = json.load(open("assets/data/country_map.json", 'r', encoding='utf-8'))

# ========================
# tracks
# ========================


def get_tracks_by_ids(track_ids: list):
    sql = "SELECT mbid FROM track WHERE id IN (%s)" % ("'" + "','".join(map(str, track_ids)) + "'")
    # print(sql)
    cursor.execute(sql)
    return cursor.fetchall()


# ========================
# 听歌排行榜, 按用户听歌次数排名
# ========================
def get_top_users(count=20):
    sql = f"SELECT lastfm_username, gender, age, country, playcount, subscribertype " \
          f"FROM `user` " \
          f"ORDER BY playcount DESC " \
          f"LIMIT 0, {count}"

    cursor_large.execute(sql)
    res = cursor_large.fetchall()
    keys = ["lastfm_username", "gender", "age", "country", "playcount", "subscribertype"]
    # 转为json格式 [{"lastfm_username": "xxx", "gender": "xxx", "age": ...}]
    objs = [dict(zip(keys, obj)) for obj in res]
    return objs

# ========================
# 歌曲排行榜, 按播放次数排名
# （这里用minidata查询）
# ========================
def get_top_tracks(count=20):
    sql = f'SELECT * FROM track ' \
          f'WHERE MBID != "" ' \
          f'ORDER BY playcount DESC ' \
          f'LIMIT 0, {count}'

    cursor.execute(sql)
    res = cursor.fetchall()
    keys = ["id", "person_id", "MBID", "name", "album_id", "duration", "playcount"]
    objs = [dict(zip(keys, obj)) for obj in res]
    return objs


# ========================
# 不同国籍用户播放量的平均值
# ========================
def get_avg_playcount_by_nationality():
    sql = f'SELECT country, AVG(playcount) AS avg_playcount ' \
          f'FROM `user` WHERE country != "" ' \
          f'GROUP BY country ' \
          f'ORDER BY avg_playcount DESC '

    cursor_large.execute(sql)
    res = cursor_large.fetchall()

    objs = []
    for abbr, cnt in res:
        if abbr not in country_map: continue
        objs.append({
            "name": country_map[abbr],
            "value": int(avgnationplaycount_map(int(cnt)) / 4) # 数据分布更加集中
        })
    return objs


# ========================
# 映射函数
# ========================
def avgnationplaycount_map(x):
    return -34285 + 2.426457764845094 * x - 5.511744175457289e-06 * x ** 2 + \
        5.310121419737438e+05 * x ** -1 + 3.796465649065208e+04 * x ** -2

# print(avgnationplaycount_map(10000))

# ========================
# 不同国籍用户数量
# ========================
def get_cnt_by_nationality():
    sql = f'SELECT country, COUNT(*) AS count ' \
          f'FROM `user` WHERE country != "" ' \
          f'GROUP BY country ' \
          f'ORDER BY count DESC '

    cursor_large.execute(sql)
    res = cursor_large.fetchall()
    objs = []
    for abbr, cnt in res:
        if abbr not in country_map: continue
        objs.append({
            "name": country_map[abbr],
            "value": int(np.log(cnt) * 10000)  # 数据分布更加集中

        })
    return objs




# ========================
# 听众年龄、订阅类型、用户数量的关系
# ========================
def get_age_info(ages: list = None):
    if ages is None:
        ages = [18, 35, 50]
    assert len(ages) == 3

    sql = f"SELECT \
        CASE \
            WHEN age BETWEEN 0 AND 15 THEN '{ages[0]}-' \
            WHEN age BETWEEN 15 AND 30 THEN '{ages[0]}-{ages[1]}' \
            WHEN age BETWEEN 30 AND 50 THEN '{ages[1]}-{ages[2]}' \
            ELSE '{ages[2]}+' \
        END AS age_group, \
        subscribertype, \
        COUNT(*) as user_count \
    FROM \
        user \
    GROUP BY \
        age_group, subscribertype \
    ORDER BY \
        MIN(age);"

    cursor_large.execute(sql)
    res = cursor_large.fetchall()

    seps = set([obj[0] for obj in res])
    keys = ["base", "premium"]
    data = {sep: {i: 0 for i in keys} for sep in seps}
    for obj in res:
        data[obj[0]][obj[1]] = int(obj[2])

    return data


# ========================
# 听众年龄、订阅类型、用户数量的关系
# 返回格式：
# {
#     "base": [0, 1, 10, 16, ...],
#     "premium":  [0, 1, 10, 16, ...]
# }
# ========================
def get_age_info_all():
    sql = f'SELECT age, COUNT(*) as user_count, subscribertype ' \
          f'FROM user ' \
          f'WHERE age != "" ' \
          f'GROUP BY age, subscribertype;'

    cursor_large.execute(sql)
    res = cursor_large.fetchall()
    max_age = max([int(i[0]) for i in res])

    base_cnt = [0] * (max_age + 1)
    premium_cnt = [0] * (max_age + 1)

    for age, cnt, subscribertype in res:
        if subscribertype == "base":
            base_cnt[int(age)] = int(cnt)
        else:
            premium_cnt[int(age)] = int(cnt)

    # 前缀和
    # base_cnt = np.cumsum(base_cnt).tolist()
    # premium_cnt = np.cumsum(premium_cnt).tolist()

    return {
        "base": base_cnt,
        "premium": premium_cnt
    }


# ========================
# 用户播放次数区间
# ========================
def get_playcount_range():
    sql = f'SELECT * FROM ' \
          f'(SELECT CONCAT(FLOOR(playcount / 10000) * 10000, "-", FLOOR(playcount / 10000) * 10000 + 10000) ' \
          f'AS `range`, COUNT(*) AS count FROM `user` ' \
          f'GROUP BY `range` ' \
          f'ORDER BY MIN(playcount) )as A ' \
          f'WHERE count > 100; '

    cursor_large.execute(sql)
    res = cursor_large.fetchall()
    objs = {obj[0]: int(obj[1]) for obj in res}
    return objs


# ========================
# 不同性别的用户数
# ========================
def get_gender_users():
    sql = f'SELECT gender, COUNT(*) AS count FROM `user` GROUP BY gender'

    cursor_large.execute(sql)
    res = cursor_large.fetchall()
    objs = {obj[0] if obj[0] else "unknown": int(obj[1]) for obj in res}
    return objs


# ========================
# 根据用户id获得用户名
# ========================
def get_username_by_id(uid):
    sql = f'SELECT lastfm_username FROM `user` WHERE id = "{uid}"'

    cursor_large.execute(sql)
    res = cursor_large.fetchall()

    return res[0][0] if res else None



if __name__ == '__main__':
    #  [18, 35, 50]
    pass
