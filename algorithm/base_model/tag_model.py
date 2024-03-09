from base_rec_model import BaseRecModel


class TagModel(BaseRecModel):
    def __init__(self):
        super(TagModel, self).__init__()
        self.item_tags = self._get_item_tags()

    def recall(self, user_id, top_n):
        """
        根据用户喜欢的歌曲获得用户标签，然后计算用户标签与歌曲标签的相似度，返回top_n的歌曲
        """
        user_tag = self._get_user_tag(user_id)
        sim = self._cal_cosine_similarity(user_tag, self.item_tags)
        return self._get_top_n(sim, top_n)

    def _get_top_n(self, sim, top_n) -> list:
        raise NotImplementedError

    def _get_user_tag(self, user_id) -> list:
        raise NotImplementedError

    def _get_item_tags(self) -> list:
        # [[]]
        raise NotImplementedError

    def _cal_cosine_similarity(self, user_tag, item_tags) -> list:
        raise NotImplementedError
