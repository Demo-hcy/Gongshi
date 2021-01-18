from ..common import *


class SqlClient:
    def __init__(self) -> None:
        self.connect_status = False

    def query(self, sql: str) -> Optional[Tuple]:
        pass

    def change(self, sql: str) -> bool:
        pass

    def mulit_change(self, sql_list: List[str]) -> bool:
        pass

    def close(self) -> None:
        """
        关闭数据库连接
        """
        self.cursor.close()
        self.connect_status = False
