from baseloader import BaseLoader
import json

class User(BaseLoader):
    def __init__(self, filepath: str, table_name: str, columns: list, savepath) -> None:
        super().__init__(filepath, table_name, columns, savepath)
    
    def _get_item(self, line) -> dict:
        # age 字段如果没数据，会出现 "age":, 的情况，需要处理
        line[-1] = line[-1].replace('"age":,', '"age":"",')
        j1 = json.loads(line[-1])

        return {**{k: str(j1[k]) for k in j1}, 'id': str(line[1])}


file_path = 'C:/Users/HP/Desktop/音乐推荐/entities/users.idomaar'
savepath = 'C:/Users/HP/Desktop/音乐推荐/SQL/user/user'
table_name = 'user'
columns = ['id', 'lastfm_username', 'gender', 'age', 'country', 'playcount', 'playlists', 'subscribertype']
event = User(file_path, table_name, columns, savepath)
event.load()