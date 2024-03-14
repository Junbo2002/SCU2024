from .base_rec_model import BaseRecModel
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class UserCFModel(BaseRecModel):
    def __init__(self):
        super(UserCFModel, self).__init__()
        # self.base_path = "../" + self.base_path

        # self.item_tags = self._get_item_tags()  # [138153, 3865]
        self.user_tags = self._get_user_tags()  # [24184, 3865]
        self.user_dict = self._get_user_dict()
        self.user_track_matrix = self._get_user_track_matrix()

    def recall(self, user_id, top_n, filtered_tracks=None, neighbor_num=1000):
        """
        基于用户的协同过滤，返回top_n的推荐结果
        """
        if filtered_tracks is None:
            raise ValueError("filtered_tracks can not be None for UserCFModel")
        # 1. 获取用户的tag向量
        user_idx = self.user_dict[user_id]
        user_tag_vector = self.user_tags[user_idx]  # [1, 3865]

        # 2. 计算用户与其他用户的相似度
        user_sim = cosine_similarity(user_tag_vector, self.user_tags, dense_output=True)
        user_sim = user_sim.squeeze(0)
        # 除去自己
        user_sim[user_idx] = 0.

        neighbor_idx = np.argpartition(user_sim, -neighbor_num)[-neighbor_num:]

        # 3. 获取neighbor_num用户的播放列表
        user_tracks = self.user_track_matrix[np.ix_(neighbor_idx, filtered_tracks)]  # [1000, 1000]
        user_sim = user_sim[neighbor_idx].reshape(-1,1)  # [1000, 1]
        # 加权求和
        # np.multiply(user_tracks.todense(), user_sim)
        user_tracks = np.multiply(user_sim, user_tracks.todense()).sum(0)  # [1000,]
        user_tracks = np.array(user_tracks).reshape(-1)
        top_n_idx = np.argpartition(user_tracks, -top_n)[-top_n:]
        sims = np.zeros_like(user_tracks)
        sims[top_n_idx] = user_tracks[top_n_idx]
        return sims


if __name__ == '__main__':
    model = UserCFModel()
    filtered_tracks = np.array([i for i in range(1000)])
    res = model.recall("10120", 10, filtered_tracks=filtered_tracks)
    print(res)