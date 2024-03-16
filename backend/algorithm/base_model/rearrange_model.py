from .base_rec_model import BaseRecModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class RearrangeModel(BaseRecModel):
    def __init__(self):
        super(RearrangeModel, self).__init__()
        # self.base_path = "../" + self.base_path

        self.user_skip_track = self._get_user_skip_track()  # [138153, 3865]
        self.user_prefer_track = self._get_user_track_prefer()
        self.user_track_matrix = self._get_user_track_matrix()
        self.user_dict = self._get_user_dict()

    def recall(self, user_id, top_n, filtered_tracks=None):
        """
        :param filtered_tracks: 歌曲的原始idx（区别于cf模型）
        """
        if filtered_tracks is None:
            raise ValueError("filtered_tracks can not be None for **RearrangeModel**")

        # user_idx = self.user_dict[user_id]

        user_skip_track_set = self.user_skip_track[user_id]  # 用户跳过的歌曲
        user_prefer_track_set = self.user_prefer_track[user_id]  # 用户喜欢的歌曲
        filtered_tracks_set = set(filtered_tracks)

        to_filter = user_skip_track_set | user_prefer_track_set
        filtered = list(filtered_tracks_set - to_filter)

        if len(filtered) >= top_n:
            # 过滤后的歌曲数足够，随机选择top_n个
            res = np.random.choice(filtered, top_n, replace=False)
            return list(res)
        elif len(filtered_tracks_set | user_prefer_track_set) >= top_n:
            # 过滤后的歌曲数不够，从用户喜欢的歌曲中补充
            num = top_n - len(filtered)
            return list(set(filtered) | user_prefer_track_set)[:num]
        else:
            # 用户喜欢的歌曲数也不够，从所有歌曲中补充
            res = np.random.choice(filtered, top_n, replace=False)
            return list(res)