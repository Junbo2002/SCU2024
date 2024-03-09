import json
import mysql.connector
from tqdm import tqdm
import pickle

mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="bigdata"
)
cursor = mydb.cursor()

file = "data/user_ids.pkl"
with open(file, "rb") as f:
    user_ids = pickle.load(f)

user_ids = set(user_ids)

sql = "select distinct creator_id from playlist"
cursor.execute(sql)
creators = cursor.fetchall()
creators = [creator[0] for creator in creators]

users = set(creators) & user_ids
print(len(users))
print(len(creators))
print(len(user_ids))