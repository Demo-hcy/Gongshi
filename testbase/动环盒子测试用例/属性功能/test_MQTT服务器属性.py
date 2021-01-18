from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_MQTT服务器属性_{time}.log',
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
def test_动环盒子测试用例_104():
    """
    - 用例标题：成功设置智能网关MQTT主服务器地址
    - 功能模块：/属性功能/MQTT服务器属性
    - 优先级：高
    - 前置条件：
    智能网关可正常上下线
    - 步骤描述：
    1.配置正确的mqtt主服务器的地址、端口、用户名、密码
    2.查看通过MQTT工具订阅后是否能接收上报属性
    - 预期结果：
    1.设置MQTT地址后成功后，可以通MQTT工具订阅可以收到设置主服务器上报属性
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_105():
    """
    - 用例标题：成功设置智能网关MQTT备服务器地址
    - 功能模块：/属性功能/MQTT服务器属性
    - 优先级：中
    - 前置条件：
    智能网关可正常上下线
    - 步骤描述：
    1.配置正确的MQTT备服务器的地址、端口、用户名、密码
    2.查看通过MQTT工具订阅后是否能接收上报属性
    - 预期结果：
    1.设置MQTT地址后成功后，可以通MQTT工具订阅可以收到设置备服务器上报属性
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_106():
    """
    - 用例标题：根据上报属性检查配置MQTT信息
    - 功能模块：/属性功能/MQTT服务器属性
    - 优先级：中
    - 前置条件：
    智能网关可正常上下线
    - 步骤描述：
    1.通过属性上报，检查mqtt主备服务器的信息
    - 预期结果：
    1.MQTT服务器信息符合配置情况
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_107():
    """
    - 用例标题：重启智能网关不会改变MQTT主备服务器信息
    - 功能模块：/属性功能/MQTT服务器属性
    - 优先级：中
    - 前置条件：
    智能网关可正常重启，正常连接上MQTT服务器
    - 步骤描述：
    1.重启之后通过属性上报，检查MQTT主备服务器的信息
    - 预期结果：
    1.MQTT服务器的地址、端口、用户名、密码等信息符合配置情况，重启不会改变MQTT配置信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_108():
    """
    - 用例标题：智能网关上下电不会改变MQTT主备服务器信息
    - 功能模块：/属性功能/MQTT服务器属性
    - 优先级：中
    - 前置条件：
    智能网关可正常重启，正常连接上MQTT服务器
    - 步骤描述：
    1.对智能网关上下电之后通过属性上报，检查MQTT主备服务器的信息
    - 预期结果：
    1.MQTT服务器的地址、端口、用户名、密码等信息符合配置情况，上下电不会改变MQTT配置信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_109():
    """
    - 用例标题：对智能网关升级不会改变MQTT主备服务器信息
    - 功能模块：/属性功能/MQTT服务器属性
    - 优先级：中
    - 前置条件：
    智能网关可正常重启，正常连接上MQTT服务器
    - 步骤描述：
    1.对智能网关进行升级之后通过属性上报，检查MQTT主备服务器的信息
    - 预期结果：
    1.MQTT服务器的地址、端口、用户名、密码等信息符合配置情况，升级不会改变MQTT配置信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_110():
    """
    - 用例标题：使用配置读取MQTT属性信息
    - 功能模块：/属性功能/MQTT服务器属性
    - 优先级：中
    - 前置条件：
    使用配置工具
    - 步骤描述：
    1.使用配置工具读取MQTT的属性信息
    2.查看MQTT地址、端口、账号、密码的默认值
    - 预期结果：
    1.读取到MQTT属性信息中，MQTT地址、端口、账号、密码的默认值为空
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
