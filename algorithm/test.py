from base_model import BaseModelFactory

# model_name = "popular"
model_name = "tag"
model = BaseModelFactory().get_model(model_name)
print(model.recall(str(5590), 500))