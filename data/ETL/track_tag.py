import mysql.connector
import json
from tqdm import tqdm

mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="bigdata"
)

filepath = "C:/Users/80908/Desktop/entities/tracks.idomaar"

lines = open(filepath, "r").readlines()[4397307:]

# 数据有问题！！！ 主键

sql_ = "INSERT INTO track_tag (track_id, tag_id) VALUES"
cursor = mydb.cursor()
for line in tqdm(lines):
    line = line.split('\t')
    track_id = line[1]
    tag_ids = json.loads(line[-1])["tags"]

    if not tag_ids: continue
    for tag_id in tag_ids:
        tag_id = tag_id["id"]
        sql = f'{sql_} ("{track_id}", "{tag_id}");'

        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
            continue

    mydb.commit()