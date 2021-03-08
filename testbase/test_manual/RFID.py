from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.S7_YWG_XCRF807_MODEL import S7_YWG_XCRF807

mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
platform = PlatformController(mqtt_client)
device = S7_YWG_XCRF807('1700012')
# # 登录
# platform.will_set()
# platform.start()
# thread = ThreadWithReturnValue(target=platform.login_listen, args=(device, True))
# thread.start()
# platform.online()  # 平台上线
# r = thread.join()

def read():
    l = {}
    num = 1

    # 读取传感器
    # 循环读取全部属性
    for i in range(num):
        l1 = {}
        for k, v in vars(device.properties).items():
            print('-' * 50)
            params = [v]
            r = platform.read(device, params, is_parsed=True)
            if r.result and r.data_dict:
                l1.update(r.data_dict)
            else:
                l1[k] = '读取错误：' + r.data_str
        l[str(i)] = l1
    # 单条发布读取全部属性
    r = platform.read(device, vars(device.properties).values(), is_parsed=True)
    l[str(num)] = r.data_dict

    print('*' * 25, '解析数据如下', '*' * 25)
    pprint(l)
    platform.stop()


def service():
    service = device.services.switchMode
    service.parameters.mode.v = 'manual'
    r = platform.service_invoke(device, service)

    service = device.services.switchMode
    service.parameters.mode.v = 'auto'
    r = platform.service_invoke(device, service)

    service = device.services.switchMode
    service.parameters.mode.v = '123'
    r = platform.service_invoke(device, service)

    r = platform.read(device, [device.properties.mode], is_parsed=True)
    platform.stop()


def write():
    device.properties.mode.v = 'auto'

    for k, v in vars(device.properties).items():
        print('-' * 50)
        # if v.accessMode == 'rw':
        if v.id == 'mac':
            params = [v]
            r = platform.set(device, params, is_parsed=True)
    # 单条发布读取全部属性
    # r = platform.set(Sensor, vars(Sensor.properties).values(), is_parsed=True)
    platform.stop()


# service()
read()
# write()