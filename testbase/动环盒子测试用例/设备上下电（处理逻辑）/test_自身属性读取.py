from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '设备上下电（处理逻辑）_自身属性读取_{time}.log',
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
def test_动环盒子测试用例_1():
    """
    - 用例标题：验证上电后进行全量数据上报
    - 功能模块：/设备上下电（处理逻辑）/自身属性读取
    - 优先级：高
    - 前置条件：
    设备可正常使用
    - 步骤描述：
    1. 设备通电
    2. 订阅主题接收上报数据
    - 预期结果：
    1. 重启后会上报一条全量数据信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_2():
    """
    - 用例标题：验证重启后进行全量数据上报
    - 功能模块：/设备上下电（处理逻辑）/自身属性读取
    - 优先级：高
    - 前置条件：
    设备可正常使用
    - 步骤描述：
    1. 对设备进行重启
    2.订阅主题接收重启后上报数据
    - 预期结果：
    1. 重启后会上报一条全量数据信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_3():
    """
    - 用例标题：完全读取全量数据上报包含信息
    - 功能模块：/设备上下电（处理逻辑）/自身属性读取
    - 优先级：中
    - 前置条件：
    设备通电并进行了一次全量上报
    - 步骤描述：
    1. 查看全量读取时的数据上报
    2. 验证报文中包含的字段信息
    - 预期结果：
    1. 报文包括设备型号、传感器数据、MQTT连接状态、固件版本
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_4():
    """
    - 用例标题：读取时间超过15s是否进行全量上报
    - 功能模块：/设备上下电（处理逻辑）/自身属性读取
    - 优先级：中
    - 前置条件：
    设备通电并进行了一次未完全读取
    - 步骤描述：
    1. 订阅主题接收上报数据
    2.当读取时间超过15s是否进行上报
    - 预期结果：
    1.当读取时间超过15s也会进行一次全量上报
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
