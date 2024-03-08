from baseloader import BaseLoader
import json

class Track(BaseLoader):
    def __init__(self, filepath: str, table_name: str, columns: list, savepath) -> None:
        super().__init__(filepath, table_name, columns, savepath)
    
    def _get_item(self, line) -> dict:
        # {"duration":274000,"playcount":917,"MBID":"0f4857e4-7f73-4ae1-93fe-c08bf4d5ce4d","name":"009+Sound+System/_/Number+Two"}	
        
        # {"artists":[{"type":"person","id":53}],"albums":[{"type":"album","id":2}],"tags":[{"type":"tag","id":254186},{"type":"tag","id":70618}]}

        j1 = json.loads(line[-2])
        j2 = json.loads(line[-1])

        return {**{k: str(j1[k]) for k in j1}, 
                'id': str(line[1]),
                'person_id': str(j2['artists'][0]['id']) if j2['artists'] else "None",
                'album_id': str(j2['albums'][0]['id']) if j2['albums'] else "None",
            }

    def _get_primary_key(self, line) -> str:
        return str(line[1])


file_path = 'C:/Users/HP/Desktop/音乐推荐/entities/tracks.idomaar'
savepath = 'C:/Users/HP/Desktop/音乐推荐/SQL/track/track'
table_name = 'track'
columns = ['id', 'person_id', 'MBID', 'name', 'album_id', 'duration', 'playcount']
track = Track(file_path, table_name, columns, savepath)
track.load()
print(len(set(track.primary_keys)))