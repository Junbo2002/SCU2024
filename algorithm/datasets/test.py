import pickle

# 读取数据
with open('playlist_track_sentences.pkl', 'rb') as f:
    sentences = pickle.load(f)

print(sentences)
print(len(sentences))

