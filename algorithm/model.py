from base_model import BaseModelFactory

# model_name = "popular"
model_names = ["popular", "tag"]
model_factory = BaseModelFactory()
model_lst = [model_factory.get_model(model_name) for model_name in model_names]
model = model_factory.get_model("multi_road_recall")
model.add_model(model_lst)

print(model.recall(str(5590), 20))
