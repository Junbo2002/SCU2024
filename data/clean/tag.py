# tag表标签很散，初始有27w个标签

import json
import mysql.connector
from tqdm import tqdm
import difflib
import pickle

mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="bigdata"
)
cursor = mydb.cursor()
sql = "SELECT id, value FROM tag"
cursor.execute(sql)
tags = cursor.fetchall()
tag_map = {tag[0]: tag[1] for tag in tags}

ids = [tag[0] for tag in tags]

tags = [tag[1] for tag in tags]

tag_lst = []
tag_dict = {}

max_step = 10000
threshold = 0.8

with open('../minidata/data/tag_set.pkl', 'rb') as f:
    tag_set = pickle.load(f)
tags = list(tag_set)
tag_map = {i: tag_map[i] for i in tag_set}
with open('../minidata/data/tag_map.pkl', 'wb') as f:
    pickle.dump(tag_map, f)
print(len(tags))
# 27w 双重循环复杂度太高
# 优化后从 3h+ -> 24s
# 首先对value预处理。去掉”空格、-、'等“
# tags = list(map(lambda x: x.replace(' ', '').replace('-', '').replace('\'', ''), tags))
# 然后进行排序
tags = list(map(lambda x: x.lower(), tags))
# 循环时比较最近的max_step个元素即可

cnt = 0
for i in tqdm(range(len(tags))):
    flag = True
    x = tag_map[tags[i]]
    for tag in tag_lst[-max_step:]:
        # if ids[i] not in tag_set:
        #     continue
        # else:
        #     cnt += 1

        if difflib.SequenceMatcher(None, x, tag).quick_ratio() >= threshold:
            flag = False
            tag_dict[x] = tag
            break

    if flag:
        tag_lst.append(x)
        tag_dict[x] = x

print(len(tag_lst))
print(len(set(tag_dict.values())))
import pickle

with open('tag_dict.pkl', 'wb') as f:
    pickle.dump(tag_dict, f)


# print(len(tags))
# print('\n'.join(tags))
print(cnt)