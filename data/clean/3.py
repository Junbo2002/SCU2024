import pickle
from scipy import sparse
from tqdm import tqdm
import numpy as np
file = "../minidata/data/user_tag_vector.pkl"
#
# with open(file, 'rb') as f:
#     user_tag_vector = pickle.load(f)
#
# res = []
# for vector in tqdm(user_tag_vector):
#     res.append(np.array(vector.todense()).squeeze(0))
# #
# res = np.array(res)
# print(res.shape)
# res = sparse.csr_matrix(res)
# file = "../minidata/data/user_tag_vector.pkl"
# with open(file, 'wb') as f:
#     pickle.dump(res, f)
# print(res)
# print(len(res))

# with open(file, 'rb') as f:
#     user_tag_vector = pickle.load(f)
#
# print(user_tag_vector)

# import mysql.connector
#
# db = mysql.connector.connect(
#     host="172.16.0.176",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="admin",  # 数据库密码
#     database="minidata"
# )
#
# cursor = db.cursor()
#
# sql = "SELECT id, playcount FROM track"
# cursor.execute(sql)
# res = cursor.fetchall()
# track_dict = {track_id: playcount for track_id, playcount in res}
# print(track_dict)
# with open("../minidata/data/trackid_playcount.pkl", 'wb') as f:
#     pickle.dump(track_dict, f)
# print(len(track_dict))

file = "../minidata/data/track_tag_vector.pkl"
with open(file, 'rb') as f:
    track_tag_vector = pickle.load(f)
print(len(track_tag_vector))