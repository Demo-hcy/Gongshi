from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_基本属性_固件版本号_{time}.log',
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
def test_动环盒子测试用例_53():
    """
    - 用例标题：读取属性中包含设备固件版本号字段及属性
    - 功能模块：/属性功能/基本属性/固件版本号
    - 优先级：高
    - 前置条件：
    智能网关可以正常上报属性
    - 步骤描述：
    1.等待MQTT进行属性上报
    2.根据上报的属性查看属性中是否包含设备固件版本号
    - 预期结果：
    1.上报属性中包含固件版本号属性，由嵌入式软件读取自身软件版本号
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_54():
    """
    - 用例标题：重启智能网关设备固件版本号不会发生改变
    - 功能模块：/属性功能/基本属性/固件版本号
    - 优先级：中
    - 前置条件：
    智能网关可以正常重启
    - 步骤描述：
    1.重启智慧盒查看上报的全量属性中设备固件版本号是否和重启前的固件版本号一致
    - 预期结果：
    1.重启后和重启前的固件版本号保持一致
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_55():
    """
    - 用例标题：上下电不会影响设备固件版本号发生改变
    - 功能模块：/属性功能/基本属性/固件版本号
    - 优先级：中
    - 前置条件：
    智能网关可以正常上下电
    - 步骤描述：
    1.查看智慧盒重新上下电是否会改变上报属性的中设备固件版本号
    - 预期结果：
    1.上下电不会影响设备固件版本号
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_56():
    """
    - 用例标题：设备升级成功会对设备固件版本号发生改变
    - 功能模块：/属性功能/基本属性/固件版本号
    - 优先级：中
    - 前置条件：
    智能网关可以升级
    - 步骤描述：
    1.升级智能网关成功后读取属性上报的设备固件版本号，查看是否改变
    - 预期结果：
    1.升级成功会改变设备固件版本号
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_57():
    """
    - 用例标题：设备升级失败不会对设备固件版本号发生改变
    - 功能模块：/属性功能/基本属性/固件版本号
    - 优先级：中
    - 前置条件：
    智能网关可以升级
    - 步骤描述：
    1.升级智能网关失败后读取属性上报的设备固件版本号，查看是否改变
    - 预期结果：
    1.升级失败不会改变设备固件版本号
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
