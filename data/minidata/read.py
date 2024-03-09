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

track_ids = pickle.load(open("data/track_ids.pkl", "rb"))

sql = f'SELECT DISTINCT user_id FROM preference WHERE track_id IN ({",".join(track_ids)})'
# print(sql)
cursor.execute(sql)
user_ids = cursor.fetchall()
user_ids = [user_ids[0] for user_ids in user_ids]


with open('data/user_ids.pkl', 'wb') as f:
    pickle.dump(user_ids, f)