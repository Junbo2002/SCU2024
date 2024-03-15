from .base_rec_model import BaseRecModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class ItemCFModel(BaseRecModel):
    def __init__(self):
        super(ItemCFModel, self).__init__()
        # self.base_path = "../" + self.base_path

        self.item_tags = self._get_item_tags()  # [138153, 3865]
        self.user_dict = self._get_user_dict()
        self.user_track_matrix = self._get_user_track_matrix()
        self.track_user_matrix = self.user_track_matrix.T

    def recall(self, user_id, top_n, filtered_tracks=None, neighbor_num=1000):
        """
        基于物品的协同过滤，返回top_n的推荐结果
        """
        if filtered_tracks is None:
            raise ValueError("filtered_tracks can not be None for ItemCFModel")

        user_idx = self.user_dict[user_id]
        track_user_matrix = self.track_user_matrix[filtered_tracks]  # [1000, 24184]
        user_track = self.user_track_matrix[user_idx, filtered_tracks]
        item_sim = cosine_similarity(track_user_matrix, dense_output=True)

        # 对角线置0
        np.fill_diagonal(item_sim, 0)
        # 矩阵转ndarray
        user_track = user_track.T.todense().A  # [1000, 1]
        item_sim = (user_track * item_sim).sum(0)  # [1000, 24184]
        top_n_idx = np.argpartition(item_sim, -top_n)[-top_n:]
        sims = np.zeros_like(item_sim)
        sims[top_n_idx] = item_sim[top_n_idx]
        return sims


if __name__ == '__main__':
    model = ItemCFModel()
    filtered_tracks = np.array([i for i in range(1000)])
    res = model.recall("10120", 10, filtered_tracks=filtered_tracks)
    print(res)
