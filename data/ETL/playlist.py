import json
import mysql.connector
from tqdm import tqdm

mydb = mysql.connector.connect(
    host="172.16.0.176",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="admin",  # 数据库密码
    database="bigdata"
)
cursor = mydb.cursor()

file_path = "C:/Users/80908/Desktop/entities/playlist.idomaar"
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in tqdm(lines):
        line = line.replace("\\", "\\\\")
        data = line.split("\t")
        try:
            json1 = json.loads(data[3])
            json2 = json.loads(data[4])
        except:
            json2 = json.loads(data[4])
            line = data[3]
            first_q = line.find('Title":') + 7  # Title开始的双引号索引
            q1 = line.rfind('"')  # 倒数第一个双引号索引
            q2 = line.rfind('"', first_q, q1)
            q3 = line.rfind('"', first_q, q2)
            q4 = line.rfind('"', first_q, q3)
            last_q = line.rfind('"', first_q, q4)  # Title结束的双引号索引

            q = line.find('"', first_q + 1, last_q)  # 找第一个双引号
            if q != -1:  # 替换引号，会让引号索引往后移一位
                line = line[:q] + '\\"' + line[q + 1:]
            q += 1
            last_q += 1
            while q != -1:  # 还能找到双引号
                q = line.find('"', q + 1, last_q)  # 最后一次会返回-1
                if q != -1:  # 替换引号
                    line = line[:q] + '\\"' + line[q + 1:]
                    q += 1
                    last_q += 1
            # print(line)
            json1 = json.loads(line)

        sql = "INSERT INTO playlist (`id`, `title`, `numtrack`, `duration`, `creator_id`) VALUES (%s, %s, %s, %s, %s)"
        val = (data[1], json1["Title"], json1["numtracks"], json1["duration"], json2["subjects"][0]["id"])
        # print(sql, val)
        cursor.execute(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句
print("记录插入成功")
