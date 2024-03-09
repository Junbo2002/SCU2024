from base_rec_model import BaseRecModel


class PopularModel(BaseRecModel):
    def __init__(self):
        super(PopularModel, self).__init__()
        self.popular_items = self._get_popular_items()

    def recall(self, user_id, top_n):
        """
        与用户无关，返回热门的top_n个歌曲
        """
        return self.popular_items[:top_n]

    def _get_popular_items(self) -> list:
        raise NotImplementedError
