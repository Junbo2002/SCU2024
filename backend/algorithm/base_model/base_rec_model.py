class BaseRecModel:
    def __init__(self):
        # self.base_path = "dataset/data/"
        self.base_path = "algorithm/dataset/data/"
        pass

    def recall(self, user_id, top_n):
        """
        Get top n recommendation result for user
        """
        raise NotImplementedError
    