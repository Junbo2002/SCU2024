import pickle
from tqdm import tqdm
import json
import mysql.connector

mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="minidata"
)
cursor = mydb.cursor()

tag_set = set()
filepath = "C:/Users/HP/Desktop/音乐推荐/entities/mini_tracks.idomaar"
primary_key = set()
with open(filepath, "r") as file:
    lines = file.readlines()
    for line in tqdm(lines):
        tags = json.loads(line.split("\t")[-1])["tags"]
        track_id = line.split("\t")[1]
        for tag in tags:
            key = f"{track_id}-{tag['id']}"
            if key in primary_key: continue
            primary_key.add(key)

            sql = "INSERT INTO track_tag (track_id, tag_id) VALUES (%s, %s)"
            val = (track_id, tag["id"])
            try:
                cursor.execute(sql, val)
            except Exception as e:
                print(e)
    mydb.commit()