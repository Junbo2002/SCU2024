"""
整合所有模型：召回、粗排、精排
"""

from .base_rec_model import BaseRecModel
import pickle
import numpy as np


class FinalModel(BaseRecModel):
    def __init__(self, models):
        super(FinalModel, self).__init__()
        self.models = models

        track_map = pickle.load(open(self.base_path + "track_map.pkl", "rb"))
        self.track_map = {v: k for k, v in track_map.items()}

    def recall(self, user_id, top_n, filtered_tracks=None):
        pass

