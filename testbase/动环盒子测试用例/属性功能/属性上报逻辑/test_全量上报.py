from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_属性上报逻辑_全量上报_{time}.log',
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
def test_动环盒子测试用例_32():
    """
    - 用例标题：重启智能网关后需上报全量属性
    - 功能模块：/属性功能/属性上报逻辑/全量上报
    - 优先级：高
    - 前置条件：
    智能网关可正常重启，上下线
    - 步骤描述：
    1.重启智能网关，等待智能网关重启后进行消息上报
    - 预期结果：
    1.重启智能网关后上报全量属性
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_33():
    """
    - 用例标题：智能网关上电后需上报全量属性
    - 功能模块：/属性功能/属性上报逻辑/全量上报
    - 优先级：中
    - 前置条件：
    智能网关可正常重启，上下线
    - 步骤描述：
    1.智能网关上电后，等待消息上报
    - 预期结果：
    1.智能网关上电后上报全量属性
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_34():
    """
    - 用例标题：智能网关进行重连后需上报全量属性
    - 功能模块：/属性功能/属性上报逻辑/全量上报
    - 优先级：中
    - 前置条件：
    智能网关可正常重启，上下线
    - 步骤描述：
    1.智能网关的网络或者MQTT进行重连后，等待消息上报
    - 预期结果：
    1.智能网关重连后上报全量属性
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_35():
    """
    - 用例标题：手动服务查询需上报全量属性
    - 功能模块：/属性功能/属性上报逻辑/全量上报
    - 优先级：中
    - 前置条件：
    智能网关可正常调用服务
    - 步骤描述：
    1.调用智能网关的服务查询，查看属性信息
    - 预期结果：
    1.智能网关收到服务调用后，上报全量属性
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_36():
    """
    - 用例标题：改变关键属性需上报全量属性
    - 功能模块：/属性功能/属性上报逻辑/全量上报
    - 优先级：中
    - 前置条件：
    智能网关可以改变关键属性状态
    - 步骤描述：
    1.改变智能网关的关键属性，查看属性信息
    - 预期结果：
    1.改变智能网关关键属性后需上报全量属性
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
