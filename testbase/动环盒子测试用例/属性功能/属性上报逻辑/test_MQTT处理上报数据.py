from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_属性上报逻辑_MQTT处理上报数据_{time}.log',
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
def test_动环盒子测试用例_41():
    """
    - 用例标题：MQTT在线或离线都丢弃上报失败的数据
    - 功能模块：/属性功能/属性上报逻辑/MQTT处理上报数据
    - 优先级：中
    - 前置条件：
    智能网关MQTT可用
    - 步骤描述：
    1.查看当MQTT在线或离线时处理定时上报失败的数据
    - 预期结果：
    1.无论MQTT在线离线，定时上报失败的数据都直接丢弃掉
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
