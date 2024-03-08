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
        self.num_split = 10000
        self.primary_keys = set()
    
    def _sql_init(self) -> str:
        # "IGNORE"
        self.sql = f"""INSERT INTO {self.table_name} ({', '.join(self.columns)})
VALUES"""
    
    def _sql_close(self) -> str:
        self.sql = self.sql.strip(',') + ";"
    
    def _get_item(self, line) -> dict:
        raise NotImplementedError
    
    def _get_primary_key(self, line) -> str:
        raise NotImplementedError
    
    def load(self):
        lines = open(self.filepath, 'r').readlines()
        for line in tqdm(lines):
            line = line.strip().split('\t')

            # 检查是否有重复的主键
            primary_keys = self._get_primary_key(line)
            if primary_keys in self.primary_keys: continue
            self.primary_keys.add(primary_keys)

            self._concat(self._get_item(line))

        self._sql_close()
        self.write(self.savepath + f"_{self.sql_split}.sql")

    def _concat(self, item: list) -> str:
        values = '"' + '","'.join([item[k] for k in self.columns]) + '"'

        # 处理None值
        values = values.replace('"None"', 'null')

        self.sql += f"\n({values}),"
        self.sql_rows += 1

        if self.sql_rows >= self.num_split:
            self._sql_close()
            self.write(self.savepath + f"_{self.sql_split}.sql")
            self._sql_init()
            self.sql_rows = 0
            self.sql_split += 1

    def write(self, filepath: str):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.sql)
        f.close()