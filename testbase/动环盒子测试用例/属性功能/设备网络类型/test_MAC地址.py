from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_设备网络类型_MAC地址_{time}.log',
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
def test_动环盒子测试用例_86():
    """
    - 用例标题：全量属性上报中包含MAC地址字段和属性值
    - 功能模块：/属性功能/设备网络类型/MAC地址
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性
    - 步骤描述：
    1.等待MQTT上线查看属性上报的字段 是否包含MAC地址
    - 预期结果：
    1.上报的属性中包含MAC地址及属性值
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_87():
    """
    - 用例标题：重启智能网关MAC地址不会改变
    - 功能模块：/属性功能/设备网络类型/MAC地址
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，当前MAC地址为：08:00:27:00:01:92
    - 步骤描述：
    1.重启智能网关，等待属性上报查看MAC地址是否改变
    - 预期结果：
    1.重启网关之后的MAC地址还是为：08:00:27:00:01:92
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_88():
    """
    - 用例标题：智能网关上下电MAC地址不会改变
    - 功能模块：/属性功能/设备网络类型/MAC地址
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，当前MAC地址为：08:00:27:00:01:92
    - 步骤描述：
    1.智能网关上下电，等待属性上报查看MAC地址是否改变
    - 预期结果：
    1.网关上下电之后的MAC地址还是为：08:00:27:00:01:92
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_89():
    """
    - 用例标题：智能网关升级后MAC地址不会改变
    - 功能模块：/属性功能/设备网络类型/MAC地址
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，当前MAC地址为：08:00:27:00:01:92
    - 步骤描述：
    1.对智能网关进行升级，等待属性上报查看MAC地址是否改变
    - 预期结果：
    1.对网关进行升级之后的MAC地址还是为：08:00:27:00:01:92
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
