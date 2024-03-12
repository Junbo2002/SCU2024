import mysql.connector

# db = mysql.connector.connect(
#     host="172.16.0.176",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="admin",  # 数据库密码
#     database="minidata"
# )
# cursor = db.cursor()

# ========================
# tracks
# ========================

def get_tracks_by_ids(track_ids: list):
    sql = "SELECT mbid FROM track WHERE id IN (%s)" % ("'" + "','".join(map(str, track_ids)) + "'")
    # print(sql)
    cursor.execute(sql)
    return cursor.fetchall()