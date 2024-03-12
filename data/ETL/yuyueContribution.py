import pickle
import json
import mysql.connector
from tqdm import tqdm

mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="minidata"
)
cursor = mydb.cursor()

with open("E:/Code/sxflights/user_dict.pkl", 'rb') as f:
    user_dict = pickle.load(f)

with open("E:/Code/sxflights/track_map.pkl", 'rb') as f:
    track_map = pickle.load(f)

file = "C:/Users/Lenovo/Desktop/relations/events.idomaar"
with open(file, "r") as f:
    lines = f.readlines()
    for line in tqdm(lines):
        line = line.split("\t")
        data = line
        playtime = json.loads(data[3])
        items = json.loads(data[4])
        user_id = items["subjects"][0]["id"]
        track_id = items["objects"][0]["id"]

        user_id, track_id = str(user_id), str(track_id)
        if user_id not in user_dict or track_id not in track_id:
            continue

        sql = "INSERT INTO event (`id`, `user_id`, `track_id`, `playtime`, `timestamp`) VALUES (%s, %s, %s, %s, %s)"

        val = (data[1], items["subjects"][0]["id"], items["objects"][0]["id"], playtime["playtime"] , data[2])
        cursor.execute(sql,val)

mydb.commit()
print("记录插入成功")
