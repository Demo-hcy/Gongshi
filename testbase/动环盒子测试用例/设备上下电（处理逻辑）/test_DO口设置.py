from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '设备上下电（处理逻辑）_DO口设置_{time}.log',
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
def test_动环盒子测试用例_5():
    """
    - 用例标题：重启智能网关DO口为默认状态
    - 功能模块：/设备上下电（处理逻辑）/DO口设置
    - 优先级：高
    - 前置条件：
    设备可正常使用
    - 步骤描述：
    1. 设备重启
    2. 重启之后读取信息查看Do口默认状态
    - 预期结果：
    1. Do默认状态为False
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_6():
    """
    - 用例标题：智能网关上电DO口为默认状态
    - 功能模块：/设备上下电（处理逻辑）/DO口设置
    - 优先级：高
    - 前置条件：
    设备可正常使用
    - 步骤描述：
    1. 设备上电
    2. 重启之后读取信息查看Do口默认状态
    - 预期结果：
    1. Do默认状态为False
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_7():
    """
    - 用例标题：未设置默认Do口
    - 功能模块：/设备上下电（处理逻辑）/DO口设置
    - 优先级：中
    - 前置条件：
    设备可正常使用
    - 步骤描述：
    1. 设备Do口保持默认
    2. 没有通过配置工具去设置默认Do口
    - 预期结果：
    1. Do口不执行任何动作
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
