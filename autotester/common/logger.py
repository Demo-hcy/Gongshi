"""
全局日志
"""
from __future__ import annotations
from typing import *
from loguru import logger
from pathlib import Path
import sys
import traceback
from .load_conf import LOG_CONSOLE_LEVEL, LOG_FILE_LEVEL, LOG_MAXBYTES

log_format = ('<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | '
              '<level>{level: <8}</level> | '
              '<cyan>{file}</cyan>:'
              '<cyan>{name}</cyan>:'
              '<cyan>{function}</cyan>:'
              '<cyan>{line}</cyan> - '
              '<level>{message}</level>')

logger.remove()
logger.add(sys.stderr, format=log_format, level=LOG_CONSOLE_LEVEL)
logger.add(Path.cwd().joinpath('log/AT_{time}.log'),
           format=log_format,
           level=LOG_FILE_LEVEL,
           rotation=LOG_MAXBYTES,
           encoding='utf-8')


def logger_error_debug(message: Any, *args: Any, **kwargs: Any):
    """
    同时生成error和debug日志，debug日志中为追踪信息
    :param message: error日志的信息
    """
    logger.error(message, *args, **kwargs)
    logger.debug(traceback.format_exc())