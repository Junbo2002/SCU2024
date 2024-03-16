import pickle


class BaseRecModel:
    # 统一管理数据文件路径映射
    file_map = {
        "item_tags": "track_tag_vector.pkl",
        "user_tags": "user_tag_vector.pkl",
        "user_dict": "user_dict.pkl",
        "tag_dict": "tag_dict.pkl",
        "user_track_matrix": "user_track_matrix.pkl",
        "track_time_vector": "track_time_vector.pkl",
        "user_skip_track": "user_skip_track.pkl",
        "user_track_prefer": "user_track_prefer.pkl"
    }

    def __init__(self):
        # self.base_path = "dataset/data/"  # for algorithm
        self.base_path = "algorithm/dataset/data/"  # for backend

    def recall(self, user_id, top_n, filtered_tracks=None):
        """
        Get top n recommendation result for user
        """
        raise NotImplementedError

    # ====================
    # 下面是一些读取数据的方法
    # ====================

    def _get_item_tags(self) -> list:
        data_path = self.base_path + self.file_map["item_tags"]
        data = self._load_pickle(data_path)
        return data

    def _get_user_tags(self) -> list:
        data_path = self.base_path + self.file_map["user_tags"]
        data = self._load_pickle(data_path)
        return data

    def _get_user_dict(self) -> dict:
        data_path = self.base_path + self.file_map["user_dict"]
        data = self._load_pickle(data_path)
        return data

    def _get_tag_dict(self):
        data_path = self.base_path + self.file_map["tag_dict"]
        data = self._load_pickle(data_path)
        return data

    def _get_user_track_matrix(self):
        data_path = self.base_path + self.file_map["user_track_matrix"]
        data = self._load_pickle(data_path)
        return data

    def _get_track_time_vector(self):
        data_path = self.base_path + self.file_map["track_time_vector"]
        data = self._load_pickle(data_path)
        return data

    def _get_user_skip_track(self):
        data_path = self.base_path + self.file_map["user_skip_track"]
        data = self._load_pickle(data_path)
        return data

    def _get_user_track_prefer(self):
        data_path = self.base_path + self.file_map["user_track_prefer"]
        data = self._load_pickle(data_path)
        return data

    def _load_pickle(self, data_path):
        with open(data_path, 'rb') as f:
            data = pickle.load(f)
        return data