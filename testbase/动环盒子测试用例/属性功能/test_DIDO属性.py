from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_DIDO属性_{time}.log',
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
def test_动环盒子测试用例_134():
    """
    - 用例标题：查看属性上报中DO属性值
    - 功能模块：/属性功能/DIDO属性
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，未设置过DO属性
    - 步骤描述：
    1.等待MQTT上报属性
    2.检查Do属性
    - 预期结果：
    1.当MQTT上线后上报一次属性，上报属性中包含Do1和DO2的默认状态
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_135():
    """
    - 用例标题：配置DO1状态为长点动开
    - 功能模块：/属性功能/DIDO属性
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True）
    - 步骤描述：
    1.Do1口对接灯控
    2.配置DO1状态为True，点动时间为0
    3.查看灯控是否一直开
    - 预期结果：
    1.当设置长点动True，灯控一直开
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_136():
    """
    - 用例标题：配置DO1状态为长点动关
    - 功能模块：/属性功能/DIDO属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True）
    - 步骤描述：
    1.Do1口对接灯控
    2.配置DO1状态为False，点动时间为0
    3.查看灯控是否一直关
    - 预期结果：
    1.当设置长点动False，灯控一直关
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_137():
    """
    - 用例标题：配置DO2状态为长点动开
    - 功能模块：/属性功能/DIDO属性
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True）
    - 步骤描述：
    1.DO2口对接灯控
    2.配置DO2状态为True，点动时间为0
    3.查看灯控是否一直开
    - 预期结果：
    1.当设置长点动True，灯控一直开
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_138():
    """
    - 用例标题：配置DO2状态为长点动关
    - 功能模块：/属性功能/DIDO属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True）
    - 步骤描述：
    1.DO2口对接灯控
    2.配置DO2状态为False，点动时间为0
    3.查看灯控是否一直关
    - 预期结果：
    1.当设置长点动False，灯控一直关
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_139():
    """
    - 用例标题：验证DO1点动功能（开）
    - 功能模块：/属性功能/DIDO属性
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True），当前DO1为False
    - 步骤描述：
    1.Do1口对接灯控
    2.配置DO1状态为True，点动时间为6000
    3.查看灯控是否开6s
    - 预期结果：
    1.当设置点动时间为6000s时，灯控只开6s，然后保持关
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_140():
    """
    - 用例标题：验证DO1点动功能（关）
    - 功能模块：/属性功能/DIDO属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True），当前DO1为True
    - 步骤描述：
    1.Do1口对接灯控
    2.配置DO1状态为False，点动时间为6000
    3.查看灯控是否关6s
    - 预期结果：
    1.当设置点动时间为6000s时，灯控只关6s，然后保持开
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_141():
    """
    - 用例标题：验证DO2点动功能（开）
    - 功能模块：/属性功能/DIDO属性
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True），当前DO2为False
    - 步骤描述：
    1.DO2口对接灯控
    2.配置DO2状态为True，点动时间为6000
    3.查看灯控是否开6s
    - 预期结果：
    1.当设置点动时间为6000s时，灯控只开6s，然后保持关
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_142():
    """
    - 用例标题：验证DO2点动功能（关）
    - 功能模块：/属性功能/DIDO属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True），当前DO2为True
    - 步骤描述：
    1.DO2口对接灯控
    2.配置DO2状态为False，点动时间为6000
    3.查看灯控是否关6s
    - 预期结果：
    1.当设置点动时间为6000s时，灯控只关6s，然后保持开
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_143():
    """
    - 用例标题：DI1电平状态变化由低变高
    - 功能模块：/属性功能/DIDO属性
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True），当前DI1为低电平
    - 步骤描述：
    1.给DI1口接入高电平
    2.检查DI1状态
    - 预期结果：
    1.DI1状态为true
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_144():
    """
    - 用例标题：DI1电平状态变化由高变低
    - 功能模块：/属性功能/DIDO属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True），当前DI1为高电平
    - 步骤描述：
    1.给DI1口接入低电平
    2.检查DI1状态
    - 预期结果：
    1.DI1状态为false
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_145():
    """
    - 用例标题：DI2电平状态变化由低变高
    - 功能模块：/属性功能/DIDO属性
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True），当前DI2为低电平
    - 步骤描述：
    1.给DI2口接入高电平
    2.检查DI2状态
    - 预期结果：
    1.DI2状态为true
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_146():
    """
    - 用例标题：DI2电平状态变化由高变低
    - 功能模块：/属性功能/DIDO属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True），当前DI2为高电平
    - 步骤描述：
    1.给DI2口接入低电平
    2.检查DI2状态
    - 预期结果：
    1.DI2状态为false
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_147():
    """
    - 用例标题：DI1.DI2电平同时状态变化由低变高
    - 功能模块：/属性功能/DIDO属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True），当前DI1、DI2为低电平
    - 步骤描述：
    1.给DI1、DI2口接入高电平
    2.检查DI１、DI2状态
    - 预期结果：
    1.DI1、DI2状态为true
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_148():
    """
    - 用例标题：DI1.DI2电平同时状态变化由高变低
    - 功能模块：/属性功能/DIDO属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，I/O及动环上报使能为启用（True），当前DI1、DI2为高电平
    - 步骤描述：
    1.给DI1、DI2口接入低电平
    2.检查DI１、DI2状态
    - 预期结果：
    1.DI1、DI2状态为false
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
