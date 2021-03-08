"""
工具类或函数
"""
from __future__ import annotations
from typing import *
from enum import Enum
from threading import Thread
import traceback


class ResultData:
    def __init__(self, result: bool = False, data: Union[Dict, str] = ''):
        self.result = result
        if isinstance(result, str):
            self.data_str: str = data
            self.data_dict: Dict = []
        else:
            self.data_str: str = str(data)
            self.data_dict: Dict = data


class ThreadWithReturnValue(Thread):
    def __init__(self, *init_args, **init_kwargs):
        """
        带返回值的线程对象
        thread1 = ThreadWithReturnValue(target=DataFrame2Matrix, args=(n_users, n_items, train_data))
        thread1.start()
        train_data_matrix = thread1.join()  # 获取返回值
        """
        super().__init__(*init_args, **init_kwargs)
        self._return = None

    def run(self):
        self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return


class _Const():
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key, value):
        if key in vars(self).keys():
            # 存在性验证
            raise self.ConstError("Can't change a const variable: '%s'" % key)
        if not key.isupper():
            # 语法规范验证
            raise self.ConstCaseError("Const variable must be combined with upper letters:'%s'" % key)
        vars(self)[key] = value


const = _Const()


class DictToObject(dict):
    def __init__(self, *args, **kwargs):
        """
        字典转对象，通过对象属性方式访问，实际还是字典
        """
        super().__init__(*args, **kwargs)
        # 先调用父类的构造方法,因为传进来的是一个字典，dict这个类会把你传入的{k:v}这样的变成一个dict的类

    def __getattr__(self, item):
        # __getattr__的作用是通过x.xx的时候它会自动调用__getattr__这个方法，把你要获取的属性的key传过来
        # 比如说 user.name ,它就是调用了__getattr__，把name传给__getattr__函数，然后返回这个name的值
        value = self[item]
        if isinstance(value, dict):
            value = DictToObject(value)  # 如果是字典类型，直接返回DictToObject这个类的对象

        elif isinstance(value, list) or isinstance(value, tuple):
            # 如果是list，循环list判断里面的元素，如果里面的元素是字典，那么就把字典转成DictToObject的对象
            value = list(value)
            for index, obj in enumerate(value):
                if isinstance(obj, dict):
                    value[index] = DictToObject(obj)
        return value


def asbool(val: str) -> bool:
    """
    将真值的字符串表示形式转换为True或False
    - 真值是'y'、'yes'、't'、'true'、'on'、'1'
    - 假值是'n'、'no'、'f'、'false'、'off'、'0'
    - 如果'val'是其他值，则引发ValueError
    :param val: 待转换的字符串
    :return: 返回转换后的布尔值
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    else:
        raise ValueError("无效的真值：%r" % val)


def first_upper(val: str) -> str:
    """
    将字符串的首字母大写，其余字母不变
    :param val: 待处理的字符串
    :return: 返回处理后的字符串
    """
    for i, s in enumerate(val):
        if s.isalpha():
            return val[0:i] + s.upper() + val[i + 1:]
        else:
            continue


def remove(old: str, to_be_removed: Tuple(str)) -> str:
    """
    移除字符串中符合的子字符串
    :param old: 需处理的字符串
    :param to_be_removed: 需移除的一系列子字符串
    :return: 返回生成的新字符串
    """
    for s in to_be_removed:
        old = old.replace(s, '')
    return old


def str_format(val: str, is_first_upper: bool = True) -> str:
    """
    去除首尾空格，将-转为_
    :param val: 待处理的字符串
    :param is_first_upper: 是否首字母大写
    :return: 返回处理后的字符串
    """
    s = val.strip()
    if is_first_upper:
        s = first_upper(s)
    import keyword
    for x in keyword.kwlist:
        if s == x:
            s = x + '_'
    s = s.replace('-', '_')
    s = s.replace('.', '_')
    s = s.replace(' ', '')
    s = s.replace('7G', 'QG')
    # s = remove(s, ('7G-', '7G_'))
    # s = s.replace(' ', '_')
    return s


def get_ends(s: str, ends: Tuple) -> str:
    """
    如果s是以ends中的任一字符串结尾的则返回改结尾字符串，否则返回None
    :param s: 需判断的字符串
    :param ends: 结尾字符串清单
    :return: 返回符合的结尾字符串
    """
    for end in ends:
        max_len = max([len(x) for x in ends])
        end_str = s[-max_len:]
        if end in end_str:
            return end


def get_var_name(v):
    """
    将括号内的值转换为字符串
    - 输入：get_var_name(inforscreen.services.setBrightness)
    - 返回：'inforscreen.services.setBrightness'
    :param v: 需转换为字符串的值
    :return: 返回转换后的字符串
    """
    (fn, ln, fn, text) = traceback.extract_stack()[-2]
    begin = text.find('get_var_name(') + len('get_var_name(')
    end = text.find(')', begin)
    return text[begin:end]


def enum_to_dict(enum_cls: Enum) -> Dict:
    """
    将枚举对象转化为字典
    :param enum_cls: 枚举的类
    :return: 返回转化后的字典
    """
    if not issubclass(enum_cls, Enum):
        return []
    result_dict = dict()
    for itme in enum_cls:
        result_dict[itme.name] = itme.value
    return result_dict
