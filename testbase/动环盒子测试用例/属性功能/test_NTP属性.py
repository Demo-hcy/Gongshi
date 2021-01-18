from library.common import *

trace = 0


def setup_moudle():
    """
    本文件开始前执行一次
    """
    trace = logger.add(str(log_path) + '属性功能_NTP属性_{time}.log',
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
def test_动环盒子测试用例_111():
    """
    - 用例标题：查看属性上报中NTP属性值
    - 功能模块：/属性功能/NTP属性
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，智能网关未配置NTP校时
    - 步骤描述：
    1.改变关键属性等待全量属性上报
    2.检查NTP属性值是否包含NTP校时状态、NTP服务器A、NTP服务器B
    - 预期结果：
    1.属性中包含NTP校时状态、NTP服务器A（默认空）、NTP服务器B（默认空）
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_动环盒子测试用例_112():
    """
    - 用例标题：配置单个NTP校时服务器（A）
    - 功能模块：/属性功能/NTP属性
    - 优先级：高
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性
    - 步骤描述：
    1.配置单个NTP服务器A地址
    2. 检查NTP信息
    - 预期结果：
    1.配置成功
    2.配置的NTP校时服务器A与配置值一致，另外一个为空
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_113():
    """
    - 用例标题：配置NTP服务器A和B
    - 功能模块：/属性功能/NTP属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性
    - 步骤描述：
    1.配置NTP服务器A和B地址
    2. 检查NTP信息
    - 预期结果：
    1.配置成功
    2.配置的NTP校时服务器与配置值一致
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_114():
    """
    - 用例标题：配置正确的NTP校时服务器
    - 功能模块：/属性功能/NTP属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性
    - 步骤描述：
    1.配置NTP服务器A和B地址
    2.NTP校时服务器可用
    3. 检查NTP状态信息
    - 预期结果：
    1.配置成功
    2.NTP校时服气状态为：True
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_115():
    """
    - 用例标题：配置错误的NTP校时服务器
    - 功能模块：/属性功能/NTP属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性
    - 步骤描述：
    1.配置NTP服务器A和B地址
    2.NTP校时服务器不可用
    3. 检查NTP状态信息
    - 预期结果：
    1.配置成功
    2.NTP校时服气状态为：False
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_116():
    """
    - 用例标题：改动时间验证NTP联通是否为1分钟
    - 功能模块：/属性功能/NTP属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性，NTP校时服务器可用
    - 步骤描述：
    1.当前时间为：10:10
    2.修改当前时间为：10:12
    3.查看是否在10:11NTP进行校时
    - 预期结果：
    1.NTP每分钟尝试联通一次，更新此校时状态
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_117():
    """
    - 用例标题：重启智能网关不会改变NTP主备服务器信息
    - 功能模块：/属性功能/NTP属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性
    - 步骤描述：
    1.重启之后通过属性上报，检查NTP主备服务器的信息
    2.对比重启前的NTP配置信息
    - 预期结果：
    1.重启不会改变NTP主备服务器信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_118():
    """
    - 用例标题：智能网关上下电不会改变NTP主备服务器信息
    - 功能模块：/属性功能/NTP属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性
    - 步骤描述：
    1.智能网关上下电之后通过属性上报，检查NTP主备服务器的信息
    2.对比上下电前的NTP配置信息
    - 预期结果：
    1.上下电不会改变NTP主备服务器信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_动环盒子测试用例_119():
    """
    - 用例标题：智能网关升级不会改变NTP主备服务器信息
    - 功能模块：/属性功能/NTP属性
    - 优先级：中
    - 前置条件：
    智能网关MQTT连接成功，并可以上报属性
    - 步骤描述：
    1.对智能进行升级之后通过属性上报，检查NTP主备服务器的信息
    2.对比升级前的NTP配置信息
    - 预期结果：
    1.升级不会改变NTP主备服务器信息
    - 备注：
    
    - 标签：
    冒烟测试 | 集成测试 | 系统测试
    """
    pass
