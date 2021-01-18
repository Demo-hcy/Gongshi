from ..common import *
from .sql_client import SqlClient
import pymysql


class MysqlClient(SqlClient):
    def __init__(self,
                 user: str,
                 password: str,
                 host: str,
                 port: int,
                 dbname: str,
                 resp_is_dict: bool = False) -> None:
        """
        MySQL数据库客户端
        :param user: 用户名
        :param password: 密码
        :param host: 地址
        :param port: 端口
        :param dbname: 数据库名称
        :param resp_is_dict: 结果是否以字典返回，默认返回元组
        """
        super().__init__()
        db = pymysql.connect
        try:
            if resp_is_dict:
                self.dbconnect = db(host, user, password, dbname, port, cursorclass=pymysql.cursors.DictCursor)
            else:
                self.dbconnect = db(host, user, password, dbname, port)
            self.cursor = self.dbconnect.cursor()
            self.connect_status = True
        except Exception as e:
            logger_error_debug(f'数据库连接失败：{e}')
            raise

    def query(self, sql: str) -> Optional[Tuple]:
        """
        查询操作
        :param sql: 单条sql以分号结尾
        :return: 返回查询出错返回None，否则返回查询结果
        """
        try:
            self.cursor.execute(sql)
        except Exception as e:
            logger_error_debug(f'查询错误：{sql} {e}')
            raise
        r = self.cursor.fetchall()
        return r

    def change(self, sql: str) -> bool:
        """
        增加删除修改操作
        :param sql: 单条sql以分号结尾
        :return: 返回执行成功返回True，否则返回False
        """
        try:
            self.cursor.execute(sql)
            self.dbcon.commit()
        except Exception as e:
            logger_error_debug(f'修改错误：{sql} {e}')
            self.dbconnect.rollback()
            raise
        return True

    def mulit_change(self, sql_list: List[str]) -> bool:
        """
        批量增加删除修改操作
        :param sql_list: 多条sql，每条以分号结尾
        :return: 返回执行成功返回True，否则返回False
        """
        try:
            for sql in sql_list:
                self.cursor.execute(sql)
            self.dbconnect.commit()
        except Exception as e:
            logger_error_debug(f'批量修改错误：{sql_list} {e}')
            self.dbconnect.rollback()
            raise
        return True
