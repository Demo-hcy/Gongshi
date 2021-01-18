from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '手动控制摄像头_设置摄像头时间_{time}.log',
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
def test_testsuite1_45():
    """
    - 用例标题：正常设置
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_46():
    """
    - 用例标题：年为3位
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_47():
    """
    - 用例标题：年为5位
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_48():
    """
    - 用例标题：月为0
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_49():
    """
    - 用例标题：月为13
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_50():
    """
    - 用例标题：日期为0
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_51():
    """
    - 用例标题：非闰年，二月日期为29
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_52():
    """
    - 用例标题：闰年，二月日期为30
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_53():
    """
    - 用例标题：小月份，日期为31
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_54():
    """
    - 用例标题：大月份，日期为32
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_55():
    """
    - 用例标题：小时为-1
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_56():
    """
    - 用例标题：小时为24
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_57():
    """
    - 用例标题：分钟为-1
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_58():
    """
    - 用例标题：分钟为60
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_59():
    """
    - 用例标题：秒为-1
    - 功能模块：/手动控制摄像头/设置摄像头时间
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
def test_testsuite1_60():
    """
    - 用例标题：秒为60
    - 功能模块：/手动控制摄像头/设置摄像头时间
    - 优先级：高
    - 前置条件：
    
    - 步骤描述：
    
    - 预期结果：
    
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
