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

with open('./data/tag_map.pkl', 'rb') as f:
    tag_map = pickle.load(f)

for k, v in tqdm(tag_map.items()):
    sql = "INSERT INTO tag (id, value) VALUES (%s, %s)"
    val = (k, v)
    cursor.execute(sql, val)


mydb.commit()