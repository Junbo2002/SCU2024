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

with open(file, 'rb') as f:
    user_tag_vector = pickle.load(f)

print(user_tag_vector)


