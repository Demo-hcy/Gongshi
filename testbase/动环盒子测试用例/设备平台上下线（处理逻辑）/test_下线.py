from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '设备平台上下线（处理逻辑）_下线_{time}.log',
                       format=log_format,
                       level=log_level,
                       rotation=log_rotation,
                       encoding='utf-8')


def teardown_moudle():
    """
    本文件结束前执行一次
    """
    logger.remove(trace)


def setup_function():
    """
    每个测试用例开始前执行一次
    """
    pass


def teardown_function():
    """
    每个测试用例结束后执行一次
    """
    # 在此处添加内容

    logs = log_path.glob('*.log')
    for log in logs:
        allure.attach.file(log, str(log).split('\\')[-1])


# 此后为测试用例脚本
@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_17():
    """
    - 用例标题：设备下线查看是否会上报遗愿信息
    - 功能模块：/设备平台上下线（处理逻辑）/下线
    - 优先级：中
    - 前置条件：
    平台对接了设备
    - 步骤描述：
    1. 设备下线
    2.监听是否上报离线遗愿消息
    - 预期结果：
    1. 设备离线会上报一次
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
