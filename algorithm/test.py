from base_model import BaseModelFactory


def get_recommendation_model():
    model_names = ["popular", "tag"]
    model_factory = BaseModelFactory()
    model_lst = [model_factory.get_model(model_name) for model_name in model_names]
    model = model_factory.get_model("multi_road_recall")
    model.add_model(model_lst)
    return model

if __name__ == '__main__':
    model = get_recommendation_model()
    res = model.recall("10120", 10)
    print(res)