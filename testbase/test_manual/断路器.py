from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.S2_SFQ_KQI3SZK_MODEL import S2_SFQ_KQI3SZK
import time

mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
platform = PlatformController(mqtt_client)
device = S2_SFQ_KQI3SZK('1700014')
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
    service = device.services.setOnOff
    service.parameters.onOff.v = 1
    service.parameters.channelId.v = 1
    r = platform.service_invoke(device, service)
    time.sleep(5)
    r = platform.read(device, [device.properties.subDevList])
    platform.stop()


def write():
    device.properties.subDevCount.v = 1
    device.properties.rs485Port.v = 3
    device.properties.rs485Addr.v = '1'
    device.properties.rs485Baund.v = 9600
    device.properties.rs485DataBit.v = 8
    device.properties.rs485Parity.v = 'N'
    device.properties.rs485StopBit.v = 1
    device.properties.subDevList.columnComplex[0].underVoltageStatus.v = 0

    for k, v in vars(device.properties).items():
        print('-' * 50)
        # if v.accessMode == 'rw':
        if v.id == 'subDevList':
            params = [v]
            r = platform.set(device, params, is_parsed=True)
    # 单条发布读取全部属性
    # r = platform.set(device, vars(device.properties).values(), is_parsed=True)


service()
# read()
# write()