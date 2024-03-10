from tqdm import tqdm

from .base_rec_model import BaseRecModel
import pickle
from scipy import sparse
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class TagModel(BaseRecModel):
    def __init__(self):
        super(TagModel, self).__init__()
        # 假设B为大矩阵，S为小矩阵
        # 当CSR格式时，S×B速度较快，与B×S相比节约了一半时间。
        # 当CSC格式时，B×S速度较快，与S×B相比节约一半时间。
        # csr_matrix
        self.item_tags = self._get_item_tags()  # [138153, 3865]
        self.user_tags = self._get_user_tags()  # [24184, 3865]
        self.user_dict = self._get_user_dict()
        self.tag_dict = self._get_tag_dict()
        self.user_item_sim = cosine_similarity(self.user_tags, self.item_tags, dense_output=False)


    def recall(self, user_id, top_n):
        """
        根据用户喜欢的歌曲获得用户标签，然后计算用户标签与歌曲标签的相似度，返回top_n的歌曲
        """
        user_idx = self.user_dict[user_id]
        # sim = self.user_item_sim[user_idx].todense()
        # top_n_idx = np.argpartition(sim, -top_n)[0, -top_n:]
        # sims = sim[0, top_n_idx]

        # 提前存储相似度矩阵
        file = f"datasets/user_item_sim/{user_id}.npy"
        sim = np.load(file)
        top_n_idx = np.argpartition(sim, -top_n)[0, -top_n:]
        # sims = sim[0, top_n_idx]
        return self._get_top_n(sim, top_n)

    def _get_top_n(self, sim, top_n) -> list:
        raise NotImplementedError

    def _get_user_tag(self, user_id) -> sparse.csc_matrix:
        if user_id not in self.user_dict:
            Warning("User id not found in user_dict")
            return sparse.csc_matrix([0] * len(self.tag_dict))

        return self.user_tags[self.user_dict[user_id]]

    def _get_item_tags(self) -> list:
        data_path = "datasets/data/track_tag_vector.pkl"
        with open(data_path, 'rb') as f:
            item_tags = pickle.load(f)
        return item_tags

    def _get_user_tags(self) -> list:
        data_path = "datasets/data/user_tag_vector.pkl"
        with open(data_path, 'rb') as f:
            user_tags = pickle.load(f)
        return user_tags

    def _get_user_dict(self) -> dict:
        data_path = "datasets/data/user_dict.pkl"
        with open(data_path, 'rb') as f:
            user_dict = pickle.load(f)
        return user_dict

    def _get_tag_dict(self) -> dict:
        data_path = "datasets/data/tag_dict.pkl"
        with open(data_path, 'rb') as f:
            tag_dict = pickle.load(f)
        return tag_dict

    # def sparse_cosine_similarity(self, vector1, vector2):  # 将稀疏向量转换为稀疏矩阵(已优化)
    #     # sparse_matrix1 = sparse.csr_matrix(vector1)
    #     # sparse_matrix2 = sparse.csr_matrix(vector2)
    #
    #     norm1 = np.sqrt(vector1.multiply(vector1).sum())
    #     norm2 = np.sqrt(vector2.multiply(vector2).sum())
    #     # 计算内积
    #     dot_product = vector1.dot(vector2.T)
    #     # 计算余弦相似度
    #     similarity = dot_product / ((norm1 * norm2) + 1e-8)
    #
    #     return similarity.data[0] if similarity.nnz else 0.
