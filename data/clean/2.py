# import json
# from tqdm import tqdm
#
# file = "C:/Users/HP/Desktop/音乐推荐/entities/mini_tracks.idomaar"
# res = []
# with open(file, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in tqdm(lines):
#         tags = json.loads(line.split('\t')[-1])["tags"]
#         for tag in tags:
#             res.append(tag["id"])
#
#
# from collections import Counter
# c = Counter(res)
# print(c)
# print(len(c))
# print(len(res))
#
# # count > 10
# c = [k for k, v in c.items() if v >= 10]
# c = {str(k): idx for idx, k in enumerate(c)}
#
# import pickle
# file = "../minidata/data/filtered_tags.pkl"
# with open(file, 'wb') as f:
#     pickle.dump(c, f)

import pickle
from scipy import sparse
from tqdm import tqdm
import json
file = "../minidata/data/filtered_tags.pkl"
with open(file, 'rb') as f:
    tag_dict = pickle.load(f)
#
# file = "C:/Users/HP/Desktop/音乐推荐/entities/mini_tracks.idomaar"
# res = []
# with open(file, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in tqdm(lines):
#         vector = [0] * len(tag_dict)
#         tags = json.loads(line.split('\t')[-1])["tags"]
#         for tag in tags:
#             tag_id = str(tag["id"])
#             if tag_id not in tag_dict: continue
#             vector[tag_dict[tag_id]] = 1
#         res.append(sparse.csr_matrix(vector))
#
# file = "../minidata/data/tag_vector.pkl"
# with open(file, 'wb') as f:
#     pickle.dump(res, f)

# file = "../minidata/data/tag_vector.pkl"
# with open(file, 'rb') as f:
#     tag_vector = pickle.load(f)
# # print(tag_vector)
# print(len(tag_vector))

file = "../minidata/data/track_ids.pkl"
with open(file, 'rb') as f:
    track_ids = set(pickle.load(f))

file = "../minidata/data/user_ids.pkl"
with open(file, 'rb') as f:
    user_ids = pickle.load(f)
user_dict = {user_id: idx for idx, user_id in enumerate(user_ids)}
file = "../minidata/data/user_dict.pkl"
with open(file, 'wb') as f:
    pickle.dump(user_dict, f)

file = "C:/Users/HP/Desktop/音乐推荐/entities/mini_tracks.idomaar"
track_dict = {track_id: [] for track_id in track_ids}
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in tqdm(lines):
        track_id = str(line.split('\t')[1])
        tags = json.loads(line.split('\t')[-1])["tags"]
        track_dict[track_id] = [tag["id"] for tag in tags if str(tag["id"]) in tag_dict]


file = "C:/Users/HP/Desktop/sql/preference.sql"
res = [[0] * len(tag_dict) for _ in range(len(user_dict))]
import re
pattern = re.compile(r"VALUES (.*);")
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in tqdm(lines):
        _, user_id, track_id = eval(pattern.findall(line)[0])
        if user_id not in user_dict or track_id not in track_ids: continue
        for tag_id in track_dict[track_id]:
            res[user_dict[user_id]][tag_dict[str(tag_id)]] += 1

# 存为稀疏矩阵
res = [sparse.csr_matrix(vector) for vector in res]
file = "../minidata/data/user_tag_vector.pkl"
with open(file, 'wb') as f:
    pickle.dump(res, f)
print(len(res))