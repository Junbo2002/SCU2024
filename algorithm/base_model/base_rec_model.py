class BaseRecModel:
    def __init__(self):
        pass

    def recall(self, user_id, top_n):
        """
        Get top n recommendation result for user
        """
        raise NotImplementedError
    