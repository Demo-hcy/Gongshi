from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_设备网络类型_有线IP地址_{time}.log',
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
def test_动环盒子测试用例_90():
    """
    - 用例标题：MQTT连接成功进行属性上报中包含IP地址字段及属性
    - 功能模块：/属性功能/设备网络类型/有线IP地址
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性
    - 步骤描述：
    1.等待MQTT上线进行一次属性上报，查看上报属性字段中是否 包含IP地址字段和属性值
    - 预期结果：
    1.MQTT上报属性中，包含IP字段和属性值，默认IP：192.168.53.200
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_91():
    """
    - 用例标题：修改IP并在属性中可以观察到IP发生改变
    - 功能模块：/属性功能/设备网络类型/有线IP地址
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，当前默认IP：192.168.53.200
    - 步骤描述：
    1.修改IP为192.168.54.211，重启智能网关，等待属性上报
    2.查看IP是否修改成功
    - 预期结果：
    1.上报属性中的IP变为：192.168.54.211
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_92():
    """
    - 用例标题：重启智能网关不会改变设置的IP
    - 功能模块：/属性功能/设备网络类型/有线IP地址
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，当前IP：192.168.54.211
    - 步骤描述：
    1.重启智能网关，查看重启后上报的属性中IP是否发生变化
    - 预期结果：
    1.上报属性中的IP还是为设置的IP：192.168.54.211
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_93():
    """
    - 用例标题：智能网关上下电不会改变设置的IP
    - 功能模块：/属性功能/设备网络类型/有线IP地址
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，当前IP：192.168.54.211
    - 步骤描述：
    1.智能网关上下电，查看重启后上报的属性中IP是否发生变化
    - 预期结果：
    1.上报属性中的IP还是为设置的IP：192.168.54.211
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_94():
    """
    - 用例标题：智能网关升级不会改变设置的IP
    - 功能模块：/属性功能/设备网络类型/有线IP地址
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，当前IP：192.168.54.211
    - 步骤描述：
    1.对智能网关进行升级，查看重启后上报的属性中IP是否发生变化
    - 预期结果：
    1.上报属性中的IP还是为设置的IP：192.168.54.211
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
