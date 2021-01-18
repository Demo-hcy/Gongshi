from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '事件功能_事件列表_即将重启_{time}.log',
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
def test_动环盒子测试用例_188():
    """
    - 用例标题：配置参数更改进行重启需上报事件
    - 功能模块：/事件功能/事件列表/即将重启
    - 优先级：高
    - 前置条件：
    智能网关在线，可正常上报事件
    - 步骤描述：
    1.对事件进行监听
    2.监听当配置参数进行重启是否上报事件
    - 预期结果：
    1.配置参数进行重启后上报事件
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_189():
    """
    - 用例标题：升级进行重启需上报事件
    - 功能模块：/事件功能/事件列表/即将重启
    - 优先级：高
    - 前置条件：
    智能网关在线，可正常上报事件
    - 步骤描述：
    1.对事件进行监听
    2.监听当升级进行重启是否上报事件
    - 预期结果：
    1.升级进行重启后上报事件
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_190():
    """
    - 用例标题：上报事件成功进行重启
    - 功能模块：/事件功能/事件列表/即将重启
    - 优先级：中
    - 前置条件：
    智能网关在线，可正常上报事件
    - 步骤描述：
    1.当此事件（升级、更改配置参数、其他）上报成功后
    2.查看智能网关状态
    - 预期结果：
    1.智能网关进行重启并上报事件
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_191():
    """
    - 用例标题：上报事件失败进行重启
    - 功能模块：/事件功能/事件列表/即将重启
    - 优先级：中
    - 前置条件：
    智能网关在线，可正常上报事件
    - 步骤描述：
    1.当此事件（升级、更改配置参数、其他）上报失败后
    2.监听是否每3s进行重试上报，上报20次
    3.查看上报20次后的状态
    - 预期结果：
    1.上报失败后，按照事件上报逻辑，每3秒重试上报一次；20次重试后，仍然失败则直接进行重启
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
