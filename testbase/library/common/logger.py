from __future__ import annotations
from typing import *
from loguru import logger
from datetime import datetime
from pathlib import Path
import traceback
import sys

# 配置屏幕输出的log格式
std_log_format = ('<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | '
                  '<level>{level: <8}</level> | '
                  '<level>{message}</level>')
logger.remove()
logger.add(sys.stderr, format=std_log_format, level='INFO')

# 配置log文件的格式
log_format = ('<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | '
              '<level>{level: <8}</level> | '
              '<cyan>{name}</cyan>:'
              '<cyan>{function}</cyan>:'
              '<cyan>{line}</cyan> - '
              '<level>{message}</level>')

log_path = Path.cwd().joinpath('testlog')
log_path /= str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
log_path.mkdir(exist_ok=True)
log_level = 'DEBUG'
log_rotation = '10 MB'
logger.add(log_path.joinpath('AT_{time}.log'),
           format=log_format,
           level=log_level,
           rotation=log_rotation,
           encoding='utf-8')


def logger_error_debug(message, *args, **kwargs):
    """
    同时生成error和debug日志，debug日志中为追踪信息
    :param message: error日志的信息
    """
    logger.error(message, *args, **kwargs)
    logger.debug(traceback.format_exc())


def logger_prompt(message, *args, **kwargs) -> bool:
    logger.info('请执行操作：' + message, *args, **kwargs)
    if input('是否完成？ (Yes/No)：') in ('Y', 'y', 'Yes', 'yes'):
        return True
    else:
        return False
