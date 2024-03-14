from tqdm import tqdm

class BaseLoader:

    def __init__(self, filepath: str, table_name: str, columns: list, savepath: str='') -> None:
        self.filepath = filepath
        self.savepath = savepath
        self.table_name = table_name
        self.columns = columns
        self._sql_init()

        self.sql_rows = 0
        self.sql_split = 0
        self.num_split = 30000
        self.cnt = 0
    
    def _sql_init(self) -> str:
        self.sql = f"""INSERT INTO {self.table_name} ({', '.join(self.columns)})
VALUES"""
    
    def _sql_close(self) -> str:
        self.sql = self.sql.strip(',') + ";"
    
    def _get_item(self, line) -> dict:
        raise NotImplementedError
    
    def load(self):
        lines = open(self.filepath, 'r').readlines()
        for line in tqdm(lines):
            self.cnt += 1
            if 1 > 1000:
                break
            line = line.strip().split('\t')
            self._concat(self._get_item(line))

        self._sql_close()
        self.write(self.savepath + f"_{self.sql_split}.sql")

    def _concat(self, item: list) -> str:
        values = '"' + '","'.join([item[k] for k in self.columns]) + '"'
        self.sql += f"\n({values}),"
        self.sql_rows += 1

        if self.sql_rows >= self.num_split:
            self._sql_close()
            self.write(self.savepath + f"_{self.sql_split}.sql")
            self._sql_init()
            self.sql_rows = 0
            self.sql_split += 1

    def write(self, filepath: str):
        with open(filepath, 'w') as f:
            f.write(self.sql)
        f.close()