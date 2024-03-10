from .base_rec_model import BaseRecModel


class ItemCFModel(BaseRecModel):
    def __init__(self):
        super(ItemCFModel, self).__init__()
        self.item_sim = self._get_item_sim()
        self.rec_items = self._get_rec_items()

    def recall(self, user_id, top_n):
        """
        基于物品的协同过滤，返回top_n的推荐结果
        """
        rec_items = self._get_rec_items_for_user(user_id)
        return rec_items[:top_n]

    def _get_item_sim(self) -> list:
        raise NotImplementedError

    def _get_rec_items(self):
        raise NotImplementedError

    def _get_rec_items_for_user(self, user_id):
        raise NotImplementedError

