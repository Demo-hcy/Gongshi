"""
封装的公共类或方法
"""
from __future__ import annotations
from typing import *
import datetime
import time
import inspect
import string
import random
import traceback
from pathlib import Path


def get_time(is_now: bool = True,
             layout: str = '%Y-%m-%d %H:%M:%S',
             delta_sec: int = 0,
             delta_min: int = 0,
             delta_hour: int = 0,
             delta_day: int = 0,
             delta_week: int = 0) -> datetime:
    """
    获取时间

    python中时间日期格式化符号：
    ------------------------------------
    - %y 两位数的年份表示（00-99）
    - %Y 四位数的年份表示（000-9999）
    - %m 月份（01-12）
    - %d 月内中的一天（0-31）
    - %H 24小时制小时数（0-23）
    - %I 12小时制小时数（01-12）
    - %M 分钟数（00=59）
    - %S 秒（00-59）
    - %a 本地简化星期名称
    - %A 本地完整星期名称
    - %b 本地简化的月份名称
    - %B 本地完整的月份名称
    - %c 本地相应的日期表示和时间表示
    - %j 年内的一天（001-366）
    - %p 本地A.M.或P.M.的等价符
    - %U 一年中的星期数（00-53）星期天为星期的开始
    - %w 星期（0-6），星期天为星期的开始
    - %W 一年中的星期数（00-53）星期一为星期的开始
    - %x 本地相应的日期表示
    - %X 本地相应的时间表示
    - %Z 当前时区的名称  # 乱码
    - %% %号本身
    - datetime.timedelta 代表两个时间之间的时间差
    - time.strftime(fmt[,tupletime]) 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定
    - time.strptime(str,fmt='%a %b %d %H:%M:%S %Y') 根据fmt的格式把一个时间字符串解析为时间元组
    - time.mktime(tupletime) 接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）

    :param is_now: 是否当前时间
    :param layout: 10timestamp or 13timestamp or 时间格式
    :param delta_sec: 间隔时间，秒
    :param delta_min: 间隔时间，分
    :param delta_hour: 间隔时间，时
    :param delta_day: 间隔时间，天
    :param delta_week: 间隔时间，周
    :return:
    """
    ti = datetime.datetime.now()
    if not is_now:
        ti = ti + datetime.timedelta(seconds=delta_sec,
                                     minutes=delta_min,
                                     hours=delta_hour,
                                     days=delta_day,
                                     weeks=delta_week)
    if layout == '10timestamp':
        ti = int(time.mktime(ti.timetuple()))
        return ti
    elif layout == '13timestamp':
        ti = int(round(time.mktime(ti.timetuple()) * 1000))
        return ti
    else:
        ti = ti.strftime(layout)
        return ti


def get_function_name():
    """
    获取正在运行函数(或方法)的名称
    """
    return inspect.stack()[1][3]


def create_name(head="", length=15):
    """
    创建随机的名称,数字 + 小写字母
    :param head: 名称前缀
    :param length: 名称长度（包含head的长度）
    :return:返回str
    """
    char_set = string.ascii_lowercase + string.digits * 2
    name_str = ""
    length = length - len(head)
    if length <= 0:
        raise ValueError("param is error,length >= len(head)")
    for _ in range(length):
        name_str += random.sample(char_set, 1)[0]
    return str(head) + name_str


def find_file(abspath, expr="*"):
    """
    查找指定文件夹下面的文件
    :param abspath: 文件的绝对路径
    :param expr: 文件名的linux下的正则表达式 : 默认返回所有文件，eg: *.py,test[1-9]{1,2}.log
    :return: 返回文件的绝对路径列表
    """
    path_list = []

    def _find_fun(path, expr):
        p = Path(path)
        if p.is_file():
            if p.match(expr):
                path_list.append(str(p))
        elif p.is_dir():
            dir_list = p.iterdir()
            for _path in dir_list:
                _find_fun(_path, expr)

    _find_fun(abspath, expr)
    return path_list


def to_import_str(abspath: str):
    """
    moudle的绝对路径，转化为可以用__import__方法导入的字符串
    eg G:\work\auto_qjzh\testcase\test_1.py to auto_qjzh.testcase.test_1
    :param abspath:
    :return: str
    """
    index = abspath.find('测试用例')
    new_str = abspath[index + 5:-3]
    new_path = new_str.replace("\\", ".")
    return new_path


def asbool(val: str) -> bool:
    """
    将真值的字符串表示形式转换为True或False
    - 真值是'y'、'yes'、't'、'true'、'on'、'1'
    - 假值是'n'、'no'、'f'、'false'、'off'、'0'
    - 如果'val'是其他值，则引发ValueError
    :param val: 待转换的字符串
    :return: 转换后的布尔值
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    else:
        raise ValueError("无效的真值：%r" % val)


def cmp_dict(expr_dict, data_dict, cmp_type=True):
    """
    判断data_dict是否包含expr_dict中的键值对
    expr_dict中的k,v都是data_dict中对应k,v的子集
    :param expr_dict: 表达式字典
    :param data_dict: 数据字典
    :param cmp_type: 比较类型，如果为True时，比较list和元组时，判断是否为子集，为False时做值判断;
    :return: 满足所有条件返回True，反之返回False
    """
    result = False
    for k, v in expr_dict.items():
        # 为字典时递归调用
        if isinstance(v, dict):
            res = cmp_dict(v, data_dict.get(k))
            if res is False:
                break
        # 为list时，转为集合比较
        elif isinstance(v, list) and isinstance(data_dict.get(k),
                                                list) and cmp_type:
            if set(v) < set(data_dict.get(k)):  # 是否为子集
                continue
            else:
                break
        else:
            if v == data_dict.get(k):
                continue
            else:
                break
    else:
        result = True
    return result


def align_line(s: str, space_num: int = 4) -> str:
    """
    在字符串每行前添加空格，使每行对齐缩进

    :param s: 源字符串
    :param space_num: 对齐空格数量
    :return: 对齐后的字符串
    """
    new_s = ' ' * space_num + s
    new_s = new_s.replace('\n', '\n' + ' ' * space_num)
    return new_s


def str_find_all(sub, src_str):
    """
    查找字符串中sub的所有索引位置
    :param sub: 子字符串
    :param src_str: 源字符串
    :return: 字符串索引list，未找到时返回空list
    """
    index_list = []
    index = src_str.find(sub)
    while index != -1:
        index_list.append(index)
        index = src_str.find(sub, index + 1)

    return index_list


def get_var_name(v):
    (fn, ln, fn, text) = traceback.extract_stack()[-2]
    begin = text.find('get_var_name(') + len('get_var_name(')
    end = text.find(')', begin)
    return text[begin:end]


def copy_dir(src_path: Path,
             target_path: Path,
             only_dir: bool = False,
             is_python_dir: bool = False):
    if src_path.is_dir() and target_path.is_dir():
        filelist_src = src_path.iterdir()
        for file in filelist_src:
            if file.is_dir():
                path1 = target_path.joinpath(file.name)
                path1.mkdir(exist_ok=True)
                if is_python_dir:
                    path1.joinpath('__init__.py').touch(exist_ok=True)
                copy_dir(file, path1, only_dir, is_python_dir)
            else:
                if not only_dir:
                    with open(file, 'rb') as read_stream:
                        contents = read_stream.read()
                        path1 = target_path.joinpath(file.name)
                        with open(path1, 'wb') as write_stream:
                            write_stream.write(contents)
        return True
    else:
        return False


if __name__ == '__main__':
    # print(get_time(True, '13timestamp'))
    # print(get_time(False, '%Y-%m-%d %H:%M:%S', 0, 0, 0, 5, 0))
    # copy_dir(Path(r'D:\test2'), Path(r'D:\test1'), only_dir=True)
    Path('')
