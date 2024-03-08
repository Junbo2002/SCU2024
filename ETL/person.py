from baseloader import BaseLoader
import json

class Person(BaseLoader):
    def __init__(self, filepath: str, table_name: str, columns: list, savepath) -> None:
        super().__init__(filepath, table_name, columns, savepath)
    
    def _get_item(self, line) -> dict:
        j1 = json.loads(line[-2])

        return {**{k: str(j1[k]) for k in j1}, 'id': str(line[1])}


file_path = 'C:/Users/HP/Desktop/音乐推荐/entities/persons.idomaar'
savepath = 'C:/Users/HP/Desktop/音乐推荐/SQL/person/person'
table_name = 'person'
columns = ['id', 'MBID', 'name']
person = Person(file_path, table_name, columns, savepath)
person.load()