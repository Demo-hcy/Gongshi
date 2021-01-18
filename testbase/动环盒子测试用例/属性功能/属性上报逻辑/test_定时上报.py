from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_属性上报逻辑_定时上报_{time}.log',
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
@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_40():
    """
    - 用例标题：根据设置的时间上报属性
    - 功能模块：/属性功能/属性上报逻辑/定时上报
    - 优先级：中
    - 前置条件：
    智能网关可以正常上报属性
    - 步骤描述：
    1.根据默认的定时上报，查看间隔180s是否收到属性上报
    - 预期结果：
    1.每间隔180s收到属性上报
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
