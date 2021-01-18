"""
配置文件的相关操作
"""
from __future__ import annotations
from typing import *
from configparser import ConfigParser
from pathlib import Path
from .const_handler import CONST


class _IniConfigParser(ConfigParser):
    def as_dict(self) -> Dict:
        """
        将configparser.ConfigParser().read()读取到的数据转换成dict类型返回
        :return: 字典化后的ini文件信息
        """
        d = dict(self._sections)
        for k in d:
            d[k] = dict(d[k])
        return d


_conf_path = Path.cwd().joinpath('autotester/config/AutoTester.ini')
_conf = _IniConfigParser()
_conf.read(_conf_path, encoding='utf-8')
_conf = _conf.as_dict()

# 定义路径的常量
_tc_path = _conf['path']
PATH_TB_DIR = CONST.PATH_TB_DIR = Path(_tc_path['testbase_dir'])
PATH_LIB_DIR = PATH_TB_DIR.joinpath('library')
PATH_PLAN_DIR = PATH_TB_DIR.joinpath('testplan')
PATH_LOG_DIR = PATH_TB_DIR.joinpath('testlog')

# 定义测试用例模板元素的常量
_tc_tpl = _conf['testcase_template']
TC_SHEET = CONST.TC_SHEET = _tc_tpl['sheet']
TC_NUM = CONST.TC_NUM = _tc_tpl['num']
TC_TITLE = CONST.TC_TITLE = _tc_tpl['title']
TC_MODULES = CONST.TC_MODULES = _tc_tpl['modules']
TC_PRIORITY = CONST.TC_PRIORITY = _tc_tpl['priority']
TC_PRECONDITIONS = CONST.TC_PRECONDITIONS = _tc_tpl['preconditions']
TC_STEPS = CONST.TC_STEPS = _tc_tpl['steps']
TC_EXPECTED_RESULTS = CONST.TC_EXPECTED_RESULTS = _tc_tpl['expected_results']
TC_REMARK = CONST.TC_REMARK = _tc_tpl['remark']
TC_TAG = CONST.TC_TAG = _tc_tpl['tag']
TC_IS_AUTO = CONST.TC_IS_AUTO = _tc_tpl['is_auto']
TC_IS_AUTO_TRUE = CONST.TC_IS_AUTO_TRUE = _tc_tpl['is_auto_true']

# 定义测试用例日志的常量
_tc_log = _conf['testcase_log']
TC_LOG_CONSOLE_LEVEL = CONST.TC_LOG_CONSOLE_LEVEL = _tc_log['console_level']
TC_LOG_FILE_LEVEL = CONST.TC_LOG_FILE_LEVEL = _tc_log['file_level']
TC_LOG_MAXBYTES = CONST.TC_LOG_MAXBYTES = _tc_log['maxbytes']

# 定义测试工具本身日志的常量
_log = _conf['log']
LOG_CONSOLE_LEVEL = CONST.LOG_CONSOLE_LEVEL = _log['console_level']
LOG_FILE_LEVEL = CONST.LOG_FILE_LEVEL = _log['file_level']
LOG_MAXBYTES = CONST.LOG_MAXBYTES = _log['maxbytes']
