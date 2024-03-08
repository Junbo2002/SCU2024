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

# 查询playlist表中所有id
sql = "SELECT id FROM playlist"
cursor.execute(sql)
playlist_ids = cursor.fetchall()
playlist_ids = [i[0] for i in playlist_ids]  # [...] 57559

sentences = []
for playlist_id in tqdm(playlist_ids):
    # 查询该歌单中所有的歌曲id
    sql = "SELECT track_id FROM playlist_track WHERE playlist_id = {}".format(playlist_id)
    cursor.execute(sql)
    track_ids = cursor.fetchall()
    # track_ids = [i[0] for i in track_ids]  # [...] 57559

    sentences.append(track_ids)

# 保存sentences
with open('playlist_track_sentences.pkl', 'wb') as f:
    pickle.dump(sentences, f)
