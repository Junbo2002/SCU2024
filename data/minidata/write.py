import mysql.connector
import re
import pickle
from tqdm import tqdm


mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="minidata"
)
cursor = mydb.cursor()

file = "data/track_ids.pkl"
with open(file, "rb") as f:
    track_ids = pickle.load(f)
file = "data/user_ids.pkl"
with open(file, "rb") as f:
    user_ids = pickle.load(f)

track_ids = set(track_ids)
user_ids = set(user_ids)

filepath = "C:/Users/HP/Desktop/sql/preference.sql"
pattern = re.compile(r"VALUES \('(\d+)', '(\d+)', '(\d+)'\);")
with open(filepath, "r") as f:
    lines = f.readlines()
    for line in tqdm(lines):
        _, user_id, track_id = pattern.findall(line)[0]
        if track_id not in track_ids or user_id not in user_ids: continue

        sql = line
        cursor.execute(sql)

mydb.commit()