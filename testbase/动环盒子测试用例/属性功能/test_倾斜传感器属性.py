from library.common import *
from library.common.g import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_倾斜传感器属性_{time}.log',
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
def test_动环盒子测试用例_156():
    """
    - 用例标题：配置相对零点
    - 功能模块：/属性功能/倾斜传感器属性
    - 优先级：高
    - 前置条件：
    当前网关可以正确上报属性消息，倾斜传感器在线，未配置过相对零点
    - 步骤描述：
    1.直立智能网关
    2.调用服务配置当前角度为相对零点
    3.检查倾斜角度和方位角
    - 预期结果：
    1.调用服务成功，倾斜角度为0，方位角为0
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    if logger_prompt('直立智能网关'):
        platform.service_invoke(dh.services.setSensor, {'tiltCalibrate': True})
        platform.read([dh.properties.holter])[1]
        assert platform.current_response.data['tilt']['angle'] == 0
        assert platform.current_response.data['tilt']['direction'] == 0
    else:
        pytest.skip()


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_157():
    """
    - 用例标题：设置告警阈值并成功触发
    - 功能模块：/属性功能/倾斜传感器属性
    - 优先级：高
    - 前置条件：
    当前网关可以正确上报属性消息，倾斜传感器在线，直立网关为相对零点
    - 步骤描述：
    1.设置告警阈值为30°
    2.倾斜网关50°
    3.检查是否有告警上来
    - 预期结果：
    1.当大于30°触发告警并上报全量属性数据
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    platform.service_invoke(dh.services.setSensor, {'tiltThreshold': 30})
    if logger_prompt('倾斜智能网关50°'):
        data = platform.report_listen(dh.properties.holter, True)[1]['params']
        data = data['holter']
        assert data['tilt']['alarming']
    else:
        pytest.skip()


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_158():
    """
    - 用例标题：根据定时上报间隔上报倾斜传感器属性
    - 功能模块：/属性功能/倾斜传感器属性
    - 优先级：中
    - 前置条件：
    当前网关可以正确上报属性消息，倾斜传感器在线，设置了相对零点，当前定时间隔为180s，未告警
    - 步骤描述：
    1.检查定时上报是否每180s在收到的属性中包含在线状态、倾斜角度、方位角、告警阈值、告警状态
    - 预期结果：
    1.每隔180s上报一次属性，属性中包含在线状态、倾斜角度、方位角、告警阈值、告警状态（默认状态未告警）等数据信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_159():
    """
    - 用例标题：当倾斜传感器上线时上报倾斜传感器属性
    - 功能模块：/属性功能/倾斜传感器属性
    - 优先级：中
    - 前置条件：
    当前网关可以正确上报属性消息，倾斜传感器离线，设置了相对零点，当前定时间隔为180s，未告警
    - 步骤描述：
    1.检查当传感器上线时是否会上报属性信息
    - 预期结果：
    1.当倾斜传感器上线时会上报一次属性，属性中包含在线状态、倾斜角度、方位角、告警阈值、告警状态（默认状态未告警）等数据信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_160():
    """
    - 用例标题：进行校准并检查倾斜角度和方位角
    - 功能模块：/属性功能/倾斜传感器属性
    - 优先级：中
    - 前置条件：
    当前网关可以正确上报属性消息，倾斜传感器在线，未设置相对零点
    - 步骤描述：
    1.将盒子向前倾斜30°
    2.调用服务配置当前角度为相对零点
    3.检查倾斜角度和方位角
    - 预期结果：
    1.调用服务成功，倾斜角度为0，方位角为0
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_161():
    """
    - 用例标题：设置正常范围5倾斜角度和方位角
    - 功能模块：/属性功能/倾斜传感器属性
    - 优先级：中
    - 前置条件：
    当前网关可以正确上报属性消息，倾斜传感器在线，未设置相对零点
    - 步骤描述：
    1.设置倾斜角0、10、20、29、30，方位角0、50、100、150、200、250、300、350、358、359
    - 预期结果：
    1.调用服务成功，可以正常设置倾斜角、方位角
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_162():
    """
    - 用例标题：设置正常范围告警阈值
    - 功能模块：/属性功能/倾斜传感器属性
    - 优先级：中
    - 前置条件：
    当前网关可以正确上报属性消息，倾斜传感器在线，未设置相对零点
    - 步骤描述：
    1.设置告警阈值5、6、10、20、29、30
    2.分别倾斜超过对应阈值角度，检查是否是否会上报告警
    - 预期结果：
    1.当超过告警阈值就会上报告警，告警状态为告警
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
