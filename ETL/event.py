from baseloader import BaseLoader
import json

class Event(BaseLoader):
    def __init__(self, filepath: str, table_name: str, columns: list, savepath) -> None:
        super().__init__(filepath, table_name, columns, savepath)
    
    def _get_item(self, line) -> dict:
        playtime = json.loads(line[-2])["playtime"]
        j2 = json.loads(line[-1])
        user_id = j2["subjects"][0]["id"]
        track_id = j2["objects"][0]["id"]

        return {
            'id': str(line[1]),
            'user_id': str(user_id),
            'track_id': str(track_id),
            'playtime': str(playtime)
        }
    


file_path = 'C:/Users/HP/Desktop/音乐推荐/relations/events.idomaar'
savepath = 'C:/Users/HP/Desktop/音乐推荐/SQL/event/event'
table_name = 'event'
columns = ['id', 'user_id', 'track_id', 'playtime']
event = Event(file_path, table_name, columns, savepath)
event.load()