from .base_rec_model import BaseRecModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime


class TimeCFModel(BaseRecModel):
    def __init__(self):
        super(TimeCFModel, self).__init__()
        # self.base_path = "../../" + self.base_path

        # self.track_map = self._ge()  # [24184, 50]
        self.track_time_vector = np.array(self._get_track_time_vector())  # [122598, 12+24]

    def recall(self, user_id, top_n, filtered_tracks=None):
        """
        过滤符合当前时间特征的歌曲
        """
        if filtered_tracks is None:
            # raise ValueError("filtered_tracks can not be None for **TimeCFModel**")
            track_time_vector = self.track_time_vector
        else:
            track_time_vector = self.track_time_vector[filtered_tracks]  # [1000, 36]

        # 获取当前时间特征：月份 & 小时
        now = datetime.now()
        month, hour = now.month, now.hour
        time_vector = [0] * len(self.track_time_vector[0])
        time_vector[month - 1] = 1
        time_vector[hour + 12] = 1

        time_vector = np.array(time_vector).reshape(1, -1)
        time_sim = cosine_similarity(time_vector, track_time_vector)[0]

        top_n_idx = np.argpartition(time_sim, -top_n)[-top_n:]
        # print("time_cf:", top_n_idx)
        sims = np.zeros_like(time_sim)
        sims[top_n_idx] = time_sim[top_n_idx]
        return sims


if __name__ == '__main__':
    model = TimeCFModel()
    filtered_tracks = np.array([i for i in range(1000)])
    res = model.recall("10120", 10, filtered_tracks=filtered_tracks)
    print(res)
