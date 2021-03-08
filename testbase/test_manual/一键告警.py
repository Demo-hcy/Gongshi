from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.S8_HK_DSPEA22F_MODEL import S8_HK_DSPEA22F

mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
platform = PlatformController(mqtt_client)
device = S8_HK_DSPEA22F('1700013')

# # 登录
# # platform.will_set()
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
    # r = platform.read(device, [device.properties.mode], is_parsed=True)

    # service = device.services.switchMode
    # service.parameters.mode.v = 'auto'
    # r = platform.service_invoke(device, service)

    # service = device.services.switchMode
    # service.parameters.mode.v = '123'
    # r = platform.service_invoke(device, service)
    platform.stop()


def write():
    device.properties.ip.v = '192.168.52.161'
    device.properties.httpPort.v = 80
    device.properties.onvifUser.v = 'admin'
    device.properties.onvifPassword.v = 'Admin@123'
    device.properties.mode.v = 'auto'

    for k, v in vars(device.properties).items():
        print('-' * 50)
        if v.accessMode == 'rw':
            params = [v]
            r = platform.set(device, params, is_parsed=True)
    # 单条发布读取全部属性
    # r = platform.set(device, vars(device.properties).values(), is_parsed=True)


# service()
read()
# write()