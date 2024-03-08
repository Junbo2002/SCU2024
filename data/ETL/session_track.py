import mysql.connector
import json
from tqdm import tqdm

mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="bigdata"
)

filepath = "C:/Users/80908/Desktop/relations/sessions.idomaar"

lines = open(filepath, "r").readlines()

sql_ = "INSERT INTO session_track (session_id, track_id, playstart, playtime, playratio, action) VALUES"
cursor = mydb.cursor()
for line in tqdm(lines):
    line = line.split('\t')
    session_id = line[1]
    tracks = json.loads(line[-1].split()[1])["objects"]
    # print(tracks)

    for track in tracks:
        track_id = str(track["id"])
        playstart = str(track["playstart"])
        playtime = str(track["playtime"])
        playratio = str(track["playratio"])
        action = str(track["action"])

        sql = f'{sql_} ("{session_id}", "{track_id}", "{playstart}", "{playtime}", "{playratio}", "{action}");'
        sql = sql.replace('"None"', 'null')
        # print(sql)
        # break
        try:
            cursor.execute(sql)
        except Exception as e:
            # print(sql)
            print(e)
            continue
    # break
    mydb.commit()