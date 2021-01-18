"""
常量处理器，对修改常量抛出异常
"""
from __future__ import annotations
from typing import *


class _CONST:
    """
    该类定义了一个方法__setattr()__，和一个异常ConstError，
    ConstError类继承自类TypeError。
    通过调用类自带的字典__dict__, 判断定义的常量是否包含在字典中。
    如果字典中包含此变量，将抛出异常，否则，给新创建的常量赋值。
    """
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError(f'不能重新设置常量 ({name})')
        self.__dict__[name] = value


CONST = _CONST()
