from library.common import *
from library.common.g import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_485通宵配置消息_{time}.log',
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
    platform.start()


def teardown_function():
    """
    每个测试用例结束后执行一次
    """
    platform.stop()
    logs = log_path.glob('*.log')
    for log in logs:
        allure.attach.file(log, str(log).split('\\')[-1])


# 此后为测试用例脚本
@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_180():
    """
    - 用例标题：全量属性上报中包含485通讯信息
    - 功能模块：/属性功能/485通宵配置消息
    - 优先级：高
    - 前置条件：
    改变关键属性可正常上报属性消息
    - 步骤描述：
    1.改变智能网关的关键属性
    2.检查全量属性上报中是否包含485通讯信息
    - 预期结果：
    1.改变关键属性进行全量属性上报
    2.上报属性中包含波特率、数据位、停止位、校验
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    # 触发全量上报
    platform.read([dh.properties.holter])[1]
    data = platform.current_response.data['temperature']['hiThreshold']
    platform.service_invoke(dh.services.setSensor, {'tempHiThreshold': 1})
    platform.service_invoke(dh.services.setSensor, {'tempHiThreshold': data})
    # 监听全量上报
    platform.report_listen(dh.properties.rs485_1, True)[0]

    assert 'rs485-1' in platform.current_response.data.keys()
    assert 'baudRate' in platform.current_response.data['rs485-1']
    assert 'byteSize' in platform.current_response.data['rs485-1']
    assert 'stopBit' in platform.current_response.data['rs485-1']
    assert 'parities' in platform.current_response.data['rs485-1']
    assert 'parities' in platform.current_response.data['rs485-1']

    assert 'rs485-2' in platform.current_response.data.keys()
    assert 'baudRate' in platform.current_response.data['rs485-2']
    assert 'byteSize' in platform.current_response.data['rs485-2']
    assert 'stopBit' in platform.current_response.data['rs485-2']
    assert 'parities' in platform.current_response.data['rs485-2']
    assert 'parities' in platform.current_response.data['rs485-2']


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_181():
    """
    - 用例标题：普通属性上报中不包含485通讯信息
    - 功能模块：/属性功能/485通宵配置消息
    - 优先级：中
    - 前置条件：
    正常上报属性消息
    - 步骤描述：
    1.检查属性上报中是否包含485通讯信息
    - 预期结果：
    1.上报属性中不包含波特率、数据位、停止位、校验
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    platform.report_listen(dh.properties.holter, True)
    assert 'rs485-1' not in platform.current_response.data.keys()
    assert 'rs485-2' not in platform.current_response.data.keys()


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_182():
    """
    - 用例标题：检查数据位数据值
    - 功能模块：/属性功能/485通宵配置消息
    - 优先级：中
    - 前置条件：
    改变关键属性可正常上报属性消息
    - 步骤描述：
    1.检查数据位在全量属性中的值
    - 预期结果：
    1.485数据位：5/6/7/8
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    # 触发全量上报
    platform.read([dh.properties.holter])[1]
    data = platform.current_response.data['temperature']['hiThreshold']
    platform.service_invoke(dh.services.setSensor, {'tempHiThreshold': 1})
    platform.service_invoke(dh.services.setSensor, {'tempHiThreshold': data})
    # 监听全量上报
    platform.report_listen(dh.properties.rs485_1, True)[0]

    assert platform.current_response.data['rs485-1']['byteSize'] in (5, 6, 7, 8)
    assert platform.current_response.data['rs485-2']['byteSize'] in (5, 6, 7, 8)


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_183():
    """
    - 用例标题：检查停止位属性值
    - 功能模块：/属性功能/485通宵配置消息
    - 优先级：中
    - 前置条件：
    改变关键属性可正常上报属性消息
    - 步骤描述：
    1.检查停止位在全量属性中的值
    - 预期结果：
    1.485停止位：1/1.5/2
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    # 触发全量上报
    platform.read([dh.properties.holter])[1]
    data = platform.current_response.data['temperature']['hiThreshold']
    platform.service_invoke(dh.services.setSensor, {'tempHiThreshold': 1})
    platform.service_invoke(dh.services.setSensor, {'tempHiThreshold': data})
    # 监听全量上报
    platform.report_listen(dh.properties.rs485_1, True)[0]

    assert platform.current_response.data['rs485-1']['stopBit'] in ('1', '1.5', '2')
    assert platform.current_response.data['rs485-2']['stopBit'] in ('1', '1.5', '2')


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_184():
    """
    - 用例标题：检查校验属性值
    - 功能模块：/属性功能/485通宵配置消息
    - 优先级：中
    - 前置条件：
    改变关键属性可正常上报属性消息
    - 步骤描述：
    1.检查校验在全量属性中的值
    - 预期结果：
    1.485校验位，分为：N/E/O/M/S（无/偶/奇/高/低）
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    # 触发全量上报
    platform.read([dh.properties.holter])[1]
    data = platform.current_response.data['temperature']['hiThreshold']
    platform.service_invoke(dh.services.setSensor, {'tempHiThreshold': 1})
    platform.service_invoke(dh.services.setSensor, {'tempHiThreshold': data})
    # 监听全量上报
    platform.report_listen(dh.properties.rs485_1, True)[0]

    assert platform.current_response.data['rs485-1']['parities'] in ('N', 'E', 'O', 'M', 'S')
    assert platform.current_response.data['rs485-2']['parities'] in ('N', 'E', 'O', 'M', 'S')
