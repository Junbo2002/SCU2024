import json
import os

import mysql.connector
from tqdm import tqdm

base_path = "C:/Users/80908/Desktop/session/"

mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="bigdata"
)
cursor = mydb.cursor()
for idx, file_path in enumerate(os.listdir(base_path)):
    print(f"file {idx}")
    file_path = os.path.join(base_path, file_path)
    with open(file_path, "r") as file:
        lines = file.readlines()
        sql = lines[0].strip() + " " + lines[1].strip() + " "
        for line in tqdm(lines[2:]):
            line = sql + line.strip().strip(',') + ";"

            try:
                cursor.execute(line)
            except:
                continue


mydb.commit()  # 数据表内容有更新，必须使用到该语句