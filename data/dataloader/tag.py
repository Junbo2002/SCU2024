from baseloader import BaseLoader
import json
from utils import replace_quoto

class Tag(BaseLoader):
    def __init__(self, filepath: str, table_name: str, columns: list, savepath) -> None:
        super().__init__(filepath, table_name, columns, savepath)
    
    def _get_item(self, line) -> dict:
        try:
            js = json.loads(line[-2])
        except:
            s = replace_quoto(line[-2])
            js = eval(s)
            
        value = str(js['value']).replace('"', '\\"')
        return {
                "id": str(line[1]),
                "value": value
        }
    
file_path = 'C:/Users/HP/Desktop/音乐推荐/entities/tags.idomaar'
savepath = 'C:/Users/HP/Desktop/音乐推荐/SQL/tag/tag'
table_name = 'tag'
columns = ['id', 'value']
event = Tag(file_path, table_name, columns, savepath)
event.load()