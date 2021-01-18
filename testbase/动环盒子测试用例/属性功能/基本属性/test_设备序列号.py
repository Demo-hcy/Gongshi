from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_基本属性_设备序列号_{time}.log',
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
def test_动环盒子测试用例_42():
    """
    - 用例标题：读取属性中包含设备序列号字段及属性
    - 功能模块：/属性功能/基本属性/设备序列号
    - 优先级：高
    - 前置条件：
    智能网关可以正常上报属性
    - 步骤描述：
    1.等待MQTT进行属性上报
    2.根据上报的属性查看属性中包含的设备序列号是否和出厂设置的序列号一致
    - 预期结果：
    1.上报属性中包含序列号属性，并且一致
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_43():
    """
    - 用例标题：重启智能网关设备序列号SN不会发生改变
    - 功能模块：/属性功能/基本属性/设备序列号
    - 优先级：中
    - 前置条件：
    智能网关可以正常重启
    - 步骤描述：
    1.重启智慧盒查看上报的全量属性中设备序列号是否和重启前的序列号一致
    - 预期结果：
    1.重启后和重启前的序列号保持一致
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_44():
    """
    - 用例标题：上下电不会影响设备序列号SN发生改变
    - 功能模块：/属性功能/基本属性/设备序列号
    - 优先级：中
    - 前置条件：
    智能网关可以正常上下电
    - 步骤描述：
    1.查看智慧盒重新上下电是否会改变上报属性的中设备序列号
    - 预期结果：
    1.上下电不会影响设备序列号
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_45():
    """
    - 用例标题：设备升级不会对设备序列号发生改变
    - 功能模块：/属性功能/基本属性/设备序列号
    - 优先级：中
    - 前置条件：
    智能网关可以升级
    - 步骤描述：
    1.升级智能网关并读取属性上报的设备序列号，查看是否改变
    - 预期结果：
    1.升级不会改变设备序列号
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_46():
    """
    - 用例标题：设备序列号唯一不可重复
    - 功能模块：/属性功能/基本属性/设备序列号
    - 优先级：中
    - 前置条件：
    智能网关可以正常上报属性
    - 步骤描述：
    1.对比不同的智能网关，检查设备序列号
    - 预期结果：
    1.设备序列号每个都不一样
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_47():
    """
    - 用例标题：无法修改设备序列号
    - 功能模块：/属性功能/基本属性/设备序列号
    - 优先级：中
    - 前置条件：
    智能网关可以正常上报属性
    - 步骤描述：
    1.修改设备序列号，等待信息上报
    2.检查设备序列号是否修改成功
    - 预期结果：
    1.修改失败，无法修改设备序列号
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
