import pickle


class BaseRecModel:
    def __init__(self):
        # self.base_path = "dataset/data/"  # for algorithm
        self.base_path = "algorithm/dataset/data/"  # for backend
        pass

    def recall(self, user_id, top_n, filtered_tracks=None):
        """
        Get top n recommendation result for user
        """
        raise NotImplementedError

    # ====================
    # 下面是一些读取数据的方法
    # ====================

    def _get_item_tags(self) -> list:
        data_path = self.base_path + "track_tag_vector.pkl"
        with open(data_path, 'rb') as f:
            item_tags = pickle.load(f)
        return item_tags

    def _get_user_tags(self) -> list:
        data_path = self.base_path + "user_tag_vector.pkl"
        with open(data_path, 'rb') as f:
            user_tags = pickle.load(f)
        return user_tags

    def _get_user_dict(self) -> dict:
        data_path = self.base_path + "user_dict.pkl"
        with open(data_path, 'rb') as f:
            user_dict = pickle.load(f)
        return user_dict

    def _get_tag_dict(self) -> dict:
        data_path = self.base_path + "tag_dict.pkl"
        with open(data_path, 'rb') as f:
            tag_dict = pickle.load(f)
        return tag_dict

    def _get_user_track_matrix(self):
        data_path = self.base_path + "user_track_matrix.pkl"
        with open(data_path, 'rb') as f:
            user_track_matrix = pickle.load(f)
        return user_track_matrix

    def _get_track_time_vector(self):
        data_path = self.base_path + "track_time_vector.pkl"
        with open(data_path, 'rb') as f:
            track_time_vector = pickle.load(f)
        return track_time_vector

    def _get_user_skip_track(self):
        data_path = self.base_path + "user_skip_track.pkl"
        with open(data_path, 'rb') as f:
            user_skip_track = pickle.load(f)
        return user_skip_track

    def _get_user_track_prefer(self):
        data_path = self.base_path + "user_track_prefer.pkl"
        with open(data_path, 'rb') as f:
            user_track_prefer = pickle.load(f)
        return user_track_prefer
