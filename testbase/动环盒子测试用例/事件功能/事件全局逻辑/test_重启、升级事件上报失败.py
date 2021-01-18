from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '事件功能_事件全局逻辑_重启、升级事件上报失败_{time}.log',
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
def test_动环盒子测试用例_185():
    """
    - 用例标题：上报失败每10s进行一次重试上报
    - 功能模块：/事件功能/事件全局逻辑/重启、升级事件上报失败
    - 优先级：高
    - 前置条件：
    智能网关在线，可正常上报事件
    - 步骤描述：
    1.对事件进行监听
    2.检查升级或重启上报失败是否每10s进行一次重试上报
    - 预期结果：
    1.重启或升级事件上报失败后，每10s重试进行上报
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_186():
    """
    - 用例标题：重试不过直接升级
    - 功能模块：/事件功能/事件全局逻辑/重启、升级事件上报失败
    - 优先级：中
    - 前置条件：
    智能网关在线，可正常上报事件
    - 步骤描述：
    1.对事件进行监听
    2.记录重试上报次数
    3.当达到6次后检查是否进行升级
    - 预期结果：
    1.重试6次失败后直接返回失败；然后直接进行重启
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_187():
    """
    - 用例标题：重试不过直接升级
    - 功能模块：/事件功能/事件全局逻辑/重启、升级事件上报失败
    - 优先级：中
    - 前置条件：
    智能网关在线，可正常上报事件
    - 步骤描述：
    1.对事件进行监听
    2.记录重试上报次数
    3.当达到6次后检查是否进行升级
    - 预期结果：
    1.重试6次失败后直接返回失败；然后直接进行升级
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
