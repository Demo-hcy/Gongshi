from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '设备上下电（处理逻辑）_下电_{time}.log',
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
def test_动环盒子测试用例_12():
    """
    - 用例标题：设备下电查看是否会上报数据
    - 功能模块：/设备上下电（处理逻辑）/下电
    - 优先级：中
    - 前置条件：
    设置了有线MQTT地址，账号和密码
    - 步骤描述：
    1. 设备下电
    2.使用MQTT工具订阅MQTT地址进行监听，查看设备下电上电会上报数据
    - 预期结果：
    1. 设备下电就不会上报数据
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_13():
    """
    - 用例标题：设备重启查看是否会上报之前遗留的数据
    - 功能模块：/设备上下电（处理逻辑）/下电
    - 优先级：中
    - 前置条件：
    设置了有线MQTT地址，账号和密码
    - 步骤描述：
    1. 设备下电后进行重启
    2.使用MQTT工具订阅MQTT地址进行监听，根据时间戳查看是否会上报之前遗留的数据
    - 预期结果：
    1. 设备重启后不会上报以前遗留的缓存数据数据
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
