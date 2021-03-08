from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.S2_SFQ_KQI3SZK_MODEL import S2_SFQ_KQI3SZK

mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
platform = PlatformController(mqtt_client)
device = S2_SFQ_KQI3SZK('1700014')


def read():
    msg = ''
    l = ['mode', 'model', 'sn', 'productId', 'online']
    for x in l:
        r = platform.read(device, [getattr(device.properties, x)], True)
        if r.result:
            msg += f'包含：{x}\n'
        else:
            msg += f'不包含：{x}\n'
    return msg


def service():
    msg = ''
    service = device.services.switchMode
    service.parameters.mode.v = 'manual'
    r = platform.service_invoke(device, service)
    r1 = platform.read(device, [device.properties.mode])
    if r.result:
        msg += f'包含：switchMode\n'
    else:
        msg += f'不包含：switchMode\n'
    return msg


m1 = service()
m2 = read()
print(m1)
print(m2)
platform.stop()