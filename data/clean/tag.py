# tag表标签很散，初始有27w个标签

import json
import mysql.connector
from tqdm import tqdm
import difflib

mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="bigdata"
)
cursor = mydb.cursor()
sql = "SELECT value FROM tag"
cursor.execute(sql)
tags = cursor.fetchall()
tags = [tag[0] for tag in tags]
tag_set = []
tag_dict = {}

max_step = 10
threshold = 0.6

# 27w 双重循环复杂度太高
# 优化后从 3h+ -> 24s
# 首先对value预处理。去掉”空格、-、'等“
# tags = list(map(lambda x: x.replace(' ', '').replace('-', '').replace('\'', ''), tags))
# 然后进行排序
# tags = list(map(lambda x: x.lower(), tags))
# 循环时比较最近的max_step个元素即可

for i in tqdm(range(len(tags))):
    flag = True

    for tag in tag_set[-max_step:]:
        if difflib.SequenceMatcher(None, tags[i], tag).quick_ratio() >= threshold:
            flag = False
            tag_dict[tags[i]] = tag
            break

    if flag:
        tag_set.append(tags[i])
        tag_dict[tags[i]] = tags[i]

print(len(tag_set))
import pickle
with open('tag_set.pkl', 'wb') as f:
    pickle.dump(tag_set, f)
with open('tag_dict.pkl', 'wb') as f:
    pickle.dump(tag_dict, f)


# print(len(tags))
# print('\n'.join(tags))
