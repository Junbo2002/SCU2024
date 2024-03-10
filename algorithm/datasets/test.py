import pickle

trackid_playcount = {"111": 123, "222": 456, "333": 789}

with open('./data/trackid_playcount.pkl', 'wb') as f:
    pickle.dump(trackid_playcount, f)

print(len(trackid_playcount))