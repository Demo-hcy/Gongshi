from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_属性上报逻辑_全量上报失败_{time}.log',
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
def test_动环盒子测试用例_37():
    """
    - 用例标题：全量属性上报失败每10s进行重试，直到成功
    - 功能模块：/属性功能/属性上报逻辑/全量上报失败
    - 优先级：高
    - 前置条件：
    智能网关在线
    - 步骤描述：
    1.监测MQTT工具
    2.触发全量属性上报失败，查看重试上报间隔
    - 预期结果：
    1.全量属性上报失败，则每10S进行重试上报，直到上报成功
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_38():
    """
    - 用例标题：新的全量属性上报会顶替上报失败的全量属性
    - 功能模块：/属性功能/属性上报逻辑/全量上报失败
    - 优先级：中
    - 前置条件：
    智能网关在线
    - 步骤描述：
    1.改变关键参数查看新的全量属性是否会将全量属性上报失败的替换掉
    - 预期结果：
    1.新的全量属性数据会顶替全量属性上报失败的数据
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_39():
    """
    - 用例标题：传感器类型告警会通过告警间隔实时展示告警状态
    - 功能模块：/属性功能/属性上报逻辑/全量上报失败
    - 优先级：中
    - 前置条件：
    智能网关在线
    - 步骤描述：
    1.触发传感器告警
    2.等待告警间隔上报
    - 预期结果：
    1.每次告警间隔都会上报传感器最新状态
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
