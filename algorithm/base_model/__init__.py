from .popular_model import PopularModel
from .multi_road_recall import MultiRoadRecallModel
from .user_cf import UserCFModel
from .item_cf import ItemCFModel
from .tag_model import TagModel


class BaseModelFactory:
    def __init__(self):
        self.model_map = {
            "popular": PopularModel,
            "user_cf": UserCFModel,
            "item_cf": ItemCFModel,
            "tag": TagModel,
            "multi_road_recall": MultiRoadRecallModel
        }

    def get_model(self, model_name):
        return self.model_map[model_name]()