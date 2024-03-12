from tqdm import tqdm

from .base_rec_model import BaseRecModel
import pickle
import numpy as np


class PopularModel(BaseRecModel):
    def __init__(self):
        super(PopularModel, self).__init__()
        self.track_ids, self.track_probs = self._get_popular_items()

    def recall(self, user_id, top_n, filtered_tracks=None):
        """
        与用户无关，返回热门的top_n个歌曲
        """
        sims = np.zeros(len(self.track_ids))
        index = self._random_select(top_n)
        sims[index] = self.track_probs[index]
        return sims

    def _get_popular_items(self):
        import os
        print(os.getcwd())
        data_path = self.base_path + "trackid_playcount.pkl"
        with open(data_path, 'rb') as f:
            trackid_playcount = pickle.load(f)

        track_ids = list(trackid_playcount.keys())
        track_playcounts = [int(trackid_playcount[track_id]) for track_id in track_ids]
        track_playcounts = np.array(track_playcounts)
        track_probs = track_playcounts / track_playcounts.sum()
        return np.array(track_ids), np.array(track_probs)

    def _random_select(self, top_n):
        # {"111": 123, "222": 456, "333": 789}  id: playcount
        # 根据playcount的大小作为概率，随机选择top_n个
        size = min(top_n, len(self.track_ids))
        index = np.random.choice(len(self.track_probs), size=size, replace=False, p=self.track_probs.ravel())
        return index


