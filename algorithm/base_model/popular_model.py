from .base_rec_model import BaseRecModel
import pickle
import numpy as np


class PopularModel(BaseRecModel):
    def __init__(self):
        super(PopularModel, self).__init__()
        self.track_ids, self.track_probs = self._get_popular_items()

    def recall(self, user_id, top_n):
        """
        与用户无关，返回热门的top_n个歌曲
        """
        return self._random_select(top_n)

    def _get_popular_items(self):
        data_path = "datasets/data/trackid_playcount.pkl"
        with open(data_path, 'rb') as f:
            trackid_playcount = pickle.load(f)

        track_ids = list(trackid_playcount.keys())
        track_playcounts = [trackid_playcount[track_id] for track_id in track_ids]
        track_probs = [playcount / sum(track_playcounts) for playcount in track_playcounts]
        return np.array(track_ids), np.array(track_probs)

    def _random_select(self, top_n):
        # {"111": 123, "222": 456, "333": 789}  id: playcount
        # 根据playcount的大小作为概率，随机选择top_n个
        size = min(top_n, len(self.track_ids))
        index = np.random.choice(self.track_ids, size=size, replace=False, p=self.track_probs.ravel())
        return index


