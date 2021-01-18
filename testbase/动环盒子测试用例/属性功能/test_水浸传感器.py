from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_水浸传感器_{time}.log',
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
def test_动环盒子测试用例_177():
    """
    - 用例标题：MQTT上报属性中包含水浸传感器属性
    - 功能模块：/属性功能/水浸传感器
    - 优先级：高
    - 前置条件：
    水浸传感器在线，可正常上报属性消息
    - 步骤描述：
    1.等待MQTT上线
    2.检查MQTT上报属性消息中是否包含水浸在线状态、水浸状态
    - 预期结果：
    1.MQTT上线会上报一下属性消息
    2.MQTT上报属性消息中包含水浸在线状态、水浸状态
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_178():
    """
    - 用例标题：定时上报属性中包含水浸传感器属性
    - 功能模块：/属性功能/水浸传感器
    - 优先级：高
    - 前置条件：
    水浸传感器在线，可正常上报属性消息，默认定时上报间隔为180s
    - 步骤描述：
    1.检查是否每隔180s进行一次属性上报，上报属性消息中是否包含水浸在线状态、水浸状态
    - 预期结果：
    1.每隔180s进行一次属性上报
    2.上报属性消息中包含水浸在线状态、水浸状态
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_179():
    """
    - 用例标题：当触发水浸时进行属性上报
    - 功能模块：/属性功能/水浸传感器
    - 优先级：中
    - 前置条件：
    水浸传感器在线，可正常上报属性消息，当前水浸状态为False
    - 步骤描述：
    1.当触发水浸时，查看是否进行属性上报，并检查属性中水浸状态
    - 预期结果：
    1.触发水浸进行一次全量属性上报，并且水浸状态为False
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
