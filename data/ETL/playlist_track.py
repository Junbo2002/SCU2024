import mysql.connector
import json
from tqdm import tqdm

mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="bigdata"
)

filepath = "C:/Users/80908/Desktop/entities/playlist.idomaar"

lines = open(filepath, "r").readlines()

sql_ = "INSERT INTO playlist_track (playlist_id, track_id) VALUES"
cursor = mydb.cursor()
for line in tqdm(lines):
    line = line.split('\t')
    playlist_id = line[1]
    track_ids = json.loads(line[-1])["objects"]

    for track_id in track_ids:
        if not track_id: break
        track_id = track_id["id"]
        sql = f'{sql_} ("{playlist_id}", "{track_id}");'

        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
            continue

    mydb.commit()