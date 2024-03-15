from baseloader import BaseLoader
import json
from utils import replace_quoto

class PlayList(BaseLoader):
    def __init__(self, filepath: str, table_name: str, columns: list, savepath) -> None:
        super().__init__(filepath, table_name, columns, savepath)
    
    def _get_item(self, line) -> dict:
        # 这里不是用\t分割的???!!! 后面两个是空格 (而且不能split, 因为有的行里面有空格)

        try:
            js1 = json.loads(line[-2])
        except:
            s = replace_quoto(line[-2])
            js1 = json.loads(s)

        js2 = json.loads(line[-1])
        
        title = str(js1["Title"]).replace('"', '\\"')
        numtrack = js1["numtracks"]
        duration = js1["duration"]
        creator_id = js2["subjects"][0]["id"]

        return {
            'id': str(line[1]),
            'title': str(title),
            'numtrack': str(numtrack),
            'duration': str(duration),
            'creator_id': str(creator_id)
        }
    
    def _get_primary_key(self, line) -> str:
        return str(line[1])

file_path = 'C:/Users/HP/Desktop/音乐推荐/entities/playlist.idomaar'
savepath = 'C:/Users/HP/Desktop/音乐推荐/SQL/playlist/playlist'
table_name = 'playlist'
columns = ['id', 'title', 'numtrack', 'duration', 'creator_id']
playlist = PlayList(file_path, table_name, columns, savepath)
playlist.load()
print(len(set(playlist.primary_keys)))