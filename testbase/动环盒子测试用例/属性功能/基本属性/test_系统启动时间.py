from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_基本属性_系统启动时间_{time}.log',
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
def test_动环盒子测试用例_63():
    """
    - 用例标题：读取属性中包含系统启动时间字段及属性
    - 功能模块：/属性功能/基本属性/系统启动时间
    - 优先级：高
    - 前置条件：
    智能网关可以正常上报属性
    - 步骤描述：
    1.改变关键属性，检查全量上报信息中是否包含系统启动时间
    - 预期结果：
    1.属性中包含系统启动时间，并且记录启动的秒数
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_64():
    """
    - 用例标题：重启系统后查看系统时间是否重新计时
    - 功能模块：/属性功能/基本属性/系统启动时间
    - 优先级：中
    - 前置条件：
    智能网关可以正常上报属性
    - 步骤描述：
    1.根据上报的属性查看属性的系统启动时间是否重新计时
    - 预期结果：
    1.属性中的系统启动时间会根据每次重启重新开始计时
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
