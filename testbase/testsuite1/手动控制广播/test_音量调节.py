from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '手动控制广播_音量调节_{time}.log',
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
def test_testsuite1_125():
    """
    - 用例标题：音量为0
    - 功能模块：/手动控制广播/音量调节
    - 优先级：高
    - 前置条件：
    
    - 步骤描述：
    
    - 预期结果：
    
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_testsuite1_126():
    """
    - 用例标题：音量为100
    - 功能模块：/手动控制广播/音量调节
    - 优先级：高
    - 前置条件：
    
    - 步骤描述：
    
    - 预期结果：
    
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_testsuite1_127():
    """
    - 用例标题：音量为-1
    - 功能模块：/手动控制广播/音量调节
    - 优先级：高
    - 前置条件：
    
    - 步骤描述：
    
    - 预期结果：
    
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_testsuite1_128():
    """
    - 用例标题：音量为101
    - 功能模块：/手动控制广播/音量调节
    - 优先级：高
    - 前置条件：
    
    - 步骤描述：
    
    - 预期结果：
    
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
