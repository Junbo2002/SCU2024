import json
import mysql.connector
from tqdm import tqdm
import pickle
from scipy import sparse

data_path = "dataset/data/"
track_map = pickle.load(open(data_path + "track_map.pkl", "rb"))
user_map = pickle.load(open(data_path + "user_dict.pkl", "rb"))
user_track = pickle.load(open(data_path + "user_track_lst.pkl", "rb"))

res = [[0] * len(track_map) for _ in range(len(user_map))]

for user in user_track:
    user_idx = user_map[user]
    for track in user_track[user]:
        track_idx = track_map[track]
        res[user_idx][track_idx] = 1

res = sparse.csr_matrix(res)
pickle.dump(res, open(data_path + "user_track_matrix.pkl", "wb"))