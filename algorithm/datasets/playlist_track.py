from tqdm import tqdm
import pickle
import json

filepath = "C:/Users/HP/Desktop/音乐推荐/entities/playlist.idomaar"

lines = open(filepath, 'r', encoding='utf-8').readlines()

sentences = []
for line in tqdm(lines):
    line = line.strip().split("\t")
    tracks = json.loads(line[-1])["objects"]

    # 如果是空列表，跳过 （数据存在 []  [[]] 两种情况）
    if not tracks or not tracks[0]:
        continue

    track_ids = [str(track["id"]) for track in tracks]

    sentences.append(track_ids)

# 保存sentences
with open('playlist_track_sentences.pkl', 'wb') as f:
    pickle.dump(sentences, f)