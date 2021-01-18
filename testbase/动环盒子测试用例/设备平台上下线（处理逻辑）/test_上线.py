from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '设备平台上下线（处理逻辑）_上线_{time}.log',
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
def test_动环盒子测试用例_14():
    """
    - 用例标题：MQTT重新上线上报全量数据
    - 功能模块：/设备平台上下线（处理逻辑）/上线
    - 优先级：高
    - 前置条件：
    设备连接的MQTT离线
    - 步骤描述：
    1. 重新连接MQTT
    2.查看数据上报
    - 预期结果：
    1. 上报当前的全量属性
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_15():
    """
    - 用例标题：MQTT重新上线上报缓存事件
    - 功能模块：/设备平台上下线（处理逻辑）/上线
    - 优先级：中
    - 前置条件：
    设备连接的MQTT离线
    - 步骤描述：
    1. 重新连接MQTT
    2.查看缓存中的告警事件是否上报
    - 预期结果：
    1. 上报最新的告警事件
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_16():
    """
    - 用例标题：MQTT重新上线上报遗愿信息
    - 功能模块：/设备平台上下线（处理逻辑）/上线
    - 优先级：中
    - 前置条件：
    设备连接的MQTT离线
    - 步骤描述：
    1.重新连接MQTT
    2.使用MQTT工具监测智能网关信息
    3.查看智能网关发送遗愿信息的方式
    - 预期结果：
    1.发送遗愿信息给MQTT服务器，后续间隔10S发送一次，总共发送三次遗愿信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
