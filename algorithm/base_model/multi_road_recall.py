from base_rec_model import BaseRecModel
import numpy as np


class MultiRoadRecallModel(BaseRecModel):
    def __init__(self):
        super(MultiRoadRecallModel, self).__init__()

    def recall(self, recall_list, top_n):
        """
        多路召回，返回top_n的推荐结果
        暂时使用平均召回
        """
        recall_list = np.array(recall_list)
        recall_list = np.mean(recall_list, axis=0)
        return recall_list[:top_n]
