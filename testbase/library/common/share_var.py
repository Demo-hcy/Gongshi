from __future__ import annotations
from typing import *
from pathlib import Path
import json
from .logger import logger


class ShareVar:
    data_path = Path.cwd().joinpath(r'public_var\share_var')

    @classmethod
    def sava(cls, data_dict):
        """
        将数据保存为json文件，覆盖原有数据
        :param data_dict: 数据字典
        :return: 成功返回True，失败返回False
        """
        if not isinstance(data_dict, dict):
            logger_error_debug(f'保存的的数据必须是字典格式：{str(data_dict)}')
            return False
        with open(cls.data_path, 'w+') as data:
            json.dump(data_dict, data)
            logger.info(f'数据保存成功：{json.dumps(data_dict)}')
        return True

    @classmethod
    def load(cls):
        """
        加载共享数据
        :return: 成功返回字典，失败返回False
        """
        if not cls.data_path.exists():
            logger_error_debug('共享数据文件不存在，已被删除或者未调用share_var中的创建方法')
            return False
        with open(cls.data_path, 'r+') as data:
            data_dict = json.load(data)

        return data_dict

    @classmethod
    def update(cls, data_dict):
        """
        更新共享数据
        :param data_dict
        :return: 成功返回True,失败返回False
        """
        if not cls.data_path.exists():
            logger_error_debug('共享数据文件不存在，已被删除或者未调用share_var中的创建方法')
            return False
        if not isinstance(data_dict, dict):
            logger_error_debug('保存的的数据必须是字典格式：%s' % str(data_dict))
            return False
        with open(cls.data_path, 'r+') as data:
            old_dict = json.load(data)
            old_dict.update(data_dict)
            data.seek(0)
            data.truncate()
            data.flush()
            json.dump(old_dict, data)
            logger.info('更新共享数据成功')
        return True

    @classmethod
    def clear_share_data(cls):
        """
        清除共享数据，不删除文件
        :return: 成功返回True，失败返回False
        """
        if not cls.data_path.exists():
            logger_error_debug('共享数据文件不存在，已被删除或者未调用share_var中的创建方法')
            return False
        with open(cls.data_path, 'w+') as data:
            json.dump({}, data)
            logger.info('共享数据清除成功')
        return True