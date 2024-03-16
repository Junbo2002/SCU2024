# from algorithm import FinalModel
# from database import get_all_users
# from tqdm import tqdm
#
#
# model = FinalModel()
# users = get_all_users()
#
# # 测试推荐算法效率
# for user_id in tqdm(users):
#     res = model.recall(user_id, 10)
#     # print(res)


import requests
url = "http://localhost:6666"

# 测试代理是否可用
res = requests.get(url, timeout=0.5)
print(res.text)