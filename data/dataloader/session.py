from baseloader import BaseLoader
import json

class Session(BaseLoader):
    def __init__(self, filepath: str, table_name: str, columns: list, savepath) -> None:
        super().__init__(filepath, table_name, columns, savepath)
    
    def _get_item(self, line) -> dict:
        # 这里不是用\t分割的???!!! 后面两个是空格 (而且不能split, 因为有的行里面有空格)
        js1, js2 = map(json.loads, line[-1].split())
        
        numtrack = js1["numtracks"]
        playtime = js1["playtime"]
        user_id = js2["subjects"][0]["id"]

        return {
            'id': str(line[1]),
            'user_id': str(user_id),
            'numtrack': str(numtrack),
            'playtime': str(playtime)
        }
    
    def _get_primary_key(self, line) -> str:
        return str(line[1])

file_path = 'C:/Users/HP/Desktop/音乐推荐/relations/sessions.idomaar'
savepath = 'C:/Users/HP/Desktop/音乐推荐/SQL/session/session'
table_name = 'session'
columns = ['id', 'numtrack', 'playtime', 'user_id']
session = Session(file_path, table_name, columns, savepath)
session.load()
print(len(set(session.primary_keys)))