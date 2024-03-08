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

file_path = "C:/Users/80908/Desktop/entities/albums.idomaar"
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in tqdm(lines):
        line = line.replace("\\", "\\\\")
        try:
            data = line.split("\t")
            items = json.loads(data[3])
        except:
            data = line.split("\t")
            line = data[3]
            first_q = line.rfind(':"') + 1  # json自带的第一个双引号索引
            last_q = line.rfind('"')  # json自带的最后一个双引号索引

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
            items = json.loads(line)

        sql = "INSERT INTO album (`id`, `MBID`, `title`) VALUES (%s, %s, %s)"
        val = (data[1], items["MBID"], items["title"])
        cursor.execute(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句
print("记录插入成功")
