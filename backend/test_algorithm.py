from algorithm import FinalModel
from tqdm import tqdm
import pickle

model = FinalModel()
user_ids = pickle.load(open("./algorithm/dataset/data/user_dict.pkl", "rb"))
s = set()
for user_id in tqdm(list(user_ids.keys())[:1000]):
    res = model.recall(user_id, 10)
    s.add(len(res))

print(s)