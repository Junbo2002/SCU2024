# import pickle
#
# file = '../minidata/data/tag_map.pkl'
# with open(file, 'rb') as f:
#     tag_dict = pickle.load(f)
# print(tag_dict)
# print(len(tag_dict))
import json

import numpy as np
from scipy import sparse
from tqdm import tqdm
import pickle

file = "../minidata/data/track_ids.pkl"
with open(file, 'rb') as f:
    track_ids = set(pickle.load(f))
print(len(track_ids))
file = "../minidata/data/user_ids.pkl"
with open(file, 'rb') as f:
    user_ids = set(pickle.load(f))

track_dict = {track_id: 0 for track_id in track_ids}
file = "C:/Users/HP/Desktop/音乐推荐/entities/mini_tracks.idomaar"
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in tqdm(lines):
        track_id = str(line.split('\t')[1])
        tags = json.loads(line.split('\t')[-1])["tags"]
        track_dict[track_id] += len(tags)


file = "C:/Users/HP/Desktop/sql/preference.sql"
user_dict = {user_id: 0 for user_id in user_ids}
import re
pattern = re.compile(r"VALUES (.*);")
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in tqdm(lines):
        _, user_id, track_id = eval(pattern.findall(line)[0])
        if user_id not in user_ids or track_id not in track_ids: continue
        user_dict[user_id] += track_dict[track_id]

# 按value排序
user_dict = sorted(user_dict.items(), key=lambda x: x[1], reverse=True)
user_dict = {user_id: idx for idx, (user_id, _) in enumerate(user_dict)}
print(user_dict)