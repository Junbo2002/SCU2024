from .base_model import BaseModelFactory


def get_model(model_name_lst):
    model_factory = BaseModelFactory()
    model_lst = [model_factory.get_model(model_name) for model_name in model_name_lst]
    model = model_factory.get_model("multi_road_recall")
    model.add_model(model_lst)
    return model


class FinalModel:
    def __init__(self):
        self.recall_model = get_model(["popular", "tag"])
        self.pre_ranking_model = get_model(["user_cf", "item_cf", "time_cf"])

        self.track_map = self.recall_model.track_map

    def recall(self, user_id, top_n):
        probs, tracks = self.recall_model.recall(user_id, 1000)  # 召回
        track_map = {idx: v for idx, v in enumerate(tracks)}  # {0: "track_id", 1: "track_id", ...}
        probs, tracks = self.pre_ranking_model.recall(user_id, top_n, filtered_tracks=tracks)  # 粗排

        track_ids = [track_map[i] for i in tracks]  # 返回的是下标id
        track_ids = [self.track_map[i] for i in track_ids]
        return track_ids


if __name__ == '__main__':
    model = FinalModel()
    import tqdm
    for i in tqdm.tqdm(range(100000)):
        res = model.recall("10120", top_n=10)
    # print(res)