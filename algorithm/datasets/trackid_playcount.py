import mysql.connector
import pickle

db = mysql.connector.connect(
    host="",
    user="root",
    password="admin",
    database="minidata"
)

cursor = db.cursor()

sql = "SELECT id, playcount FROM track"

cursor.execute(sql)
res = cursor.fetchall()

# 保存为字典
trackid_playcount = {}
for r in res:
    trackid_playcount[r[0]] = r[1]

with open('./data/trackid_playcount.pkl', 'wb') as f:
    pickle.dump(trackid_playcount, f)

print(len(trackid_playcount))