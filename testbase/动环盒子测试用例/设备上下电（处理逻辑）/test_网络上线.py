from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '设备上下电（处理逻辑）_网络上线_{time}.log',
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
@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_10():
    """
    - 用例标题：有线MQTT进行网络上线
    - 功能模块：/设备上下电（处理逻辑）/网络上线
    - 优先级：高
    - 前置条件：
    设置了有线MQTT地址，账号和密码
    - 步骤描述：
    1. 启用有线
    2.通过有线MQTT进行连接
    - 预期结果：
    1. 使用MQTT工具订阅MQTT地址进行监听，上报设备数据信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_11():
    """
    - 用例标题：重启/上电设备都会上报信息到MQTT
    - 功能模块：/设备上下电（处理逻辑）/网络上线
    - 优先级：中
    - 前置条件：
    设置了有线MQTT地址，账号和密码
    - 步骤描述：
    1. 启用有线
    2.重启/上电设置查看是否上报数据到MQTT
    - 预期结果：
    1. 使用MQTT工具订阅MQTT地址进行监听，上报设备数据信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
