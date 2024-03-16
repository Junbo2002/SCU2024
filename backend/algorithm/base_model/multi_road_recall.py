from .base_rec_model import BaseRecModel
import numpy as np
import pickle


class MultiRoadRecallModel(BaseRecModel):
    def __init__(self):
        super(MultiRoadRecallModel, self).__init__()
        track_map = pickle.load(open(self.base_path + "track_map.pkl", "rb"))
        self.track_map = {v: k for k, v in track_map.items()}
        self.models = []

    def recall(self, user_id, top_n, p="mean", filtered_tracks=None):
        """
        多路召回，返回top_n的推荐结果
        暂时使用平均召回
        """
        recall_lst = []
        for model in self.models:
            if not isinstance(model, BaseRecModel):
                raise TypeError("model must be an instance of BaseRecModel")

            recall_res = model.recall(user_id, top_n, filtered_tracks=filtered_tracks)
            # 特征归一化（平等考虑每个子模型权重）
            recall_res = recall_res / (recall_res.sum() + 1e-5)  # 防止除0
            # 其他归一化方法
            # recall_res = \
            #     (recall_res - recall_res.mean()) / recall_res.std()
            recall_lst.append(recall_res)

        if p == "mean":
            res = np.array(recall_lst).mean(axis=0)
            top_n_idx = np.argpartition(res, -top_n)[-top_n:]
            # track_ids = [self.track_map[i] for i in top_n_idx]
            return res[top_n_idx].tolist(), top_n_idx
        else:
            raise NotImplementedError

    def add_model(self, model):
        if isinstance(model, list):
            for m in model:
                self.add_model(m)
        elif isinstance(model, BaseRecModel):
            self.models.append(model)
        else:
            raise TypeError("model must be an instance of BaseRecModel")