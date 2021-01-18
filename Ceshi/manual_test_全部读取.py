from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.simulator import PlatformSimulator
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.DH_001_MODEL import DH_001

mqtt_client = MQTTClient(host='192.168.49.68', port=1883)

dh = DH_001('DH0000000002')
platform = PlatformSimulator(dh, mqtt_client, False)

platform.start()

l = {}
for i in range(1):
    l1 = {}
    for k, v in dh.properties.__dict__.items():
        print('-' * 50)
        param = v
        result, msg = platform.read([param])
        l1[k] = platform.current_response.data
    l[i] = l1

result, msg = platform.read(dh.properties.__dict__.values())
l[3] = platform.current_response.data

platform.stop()
print('*' * 25, '解析数据如下', '*' * 25)
pprint(l)
