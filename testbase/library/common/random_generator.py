"""
随机获取各类数据
"""
from __future__ import annotations
from typing import *
import random
import hashlib
import string


def random_data(data: List):
    """
    数组中随机选取数据
    :param data: 范围数组
    :return: 随机选取的数据
    """
    num = random.choice(data)
    return num


def random_float(start: float, end: float, accuracy: int) -> float:
    """
    获取随机浮点数据
    :param start: 起始数
    :param end: 结束数
    :param accuracy: 精度
    :return: 随机浮点数据
    """
    if start <= end:
        num = random.uniform(start, end)
    else:
        num = random.uniform(end, start)
    num = round(num, accuracy)
    return num


def random_int(start: int, end: int) -> int:
    """
    获取随机整型数据
    :param start: 起始数
    :param end: 结束数
    :return: 随机整形数据
    """
    if start <= end:
        num = random.randint(start, end)
    else:
        num = random.randint(end, start)
    return num


def random_hash_md5(data: str) -> str:
    """
    md5加密
    :param data: 待加密的字符串
    :return: 加密后的字符串
    """
    m1 = hashlib.md5()
    m1.update(data.encode('utf-8'))
    data = m1.hexdigest()
    return data


def random_str(num_len: int) -> str:
    """
    从a-z,A-Z,0-9生成指定数量的随机字符串
    :param num_len: 字符串长度
    :return: 随机字符串
    """
    strings = ''.join(random.sample(string.hexdigits, num_len))
    return strings


if __name__ == '__main__':
    print(random_data([1, 2, 3, 4]))
    print(random_float(1, 200, 2))
    print(random_int(222, 333))
    print(random_hash_md5('33332323423'))
    print(random_str(16))
