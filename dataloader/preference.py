from baseloader import BaseLoader
import json

class Preference(BaseLoader):
    def __init__(self, filepath: str, table_name: str, columns: list, savepath) -> None:
        super().__init__(filepath, table_name, columns, savepath)
    
    def _get_item(self, line) -> dict:
        # 这里不是用\t分割的???!!! 后面两个是空格 (而且不能split, 因为有的行里面有空格)
        js = json.loads(line[-1][20:])
        user_id = js["subjects"][0]["id"]
        track_id = js["objects"][0]["id"]

        return {
            'id': str(line[1]),
            'user_id': str(user_id),
            'track_id': str(track_id)
        }
    
    def _get_primary_key(self, line) -> str:
        return str(line[1])

file_path = 'C:/Users/HP/Desktop/音乐推荐/relations/love.idomaar'
savepath = 'C:/Users/HP/Desktop/音乐推荐/SQL/preference/preference'
table_name = 'preference'
columns = ['id', 'user_id', 'track_id']
preference = Preference(file_path, table_name, columns, savepath)
preference.load()
print(len(set(preference.primary_keys)))