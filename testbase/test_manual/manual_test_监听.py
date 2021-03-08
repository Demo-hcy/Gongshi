from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.D1_7G_DHWG_MODEL import D1_QG_DHWG

# 动环盒子
mqtt_client = MQTTClient(host='192.168.49.96', port=1883, timeout=60)
platform = PlatformController(mqtt_client)
dh = D1_QG_DHWG('E46854B287555333')

# 监听属性
print('-' * 50)
platform.report_listen(dh, [dh.properties.rs485_1], True)
print('-' * 50)
r = platform.report_listen(dh, [dh.properties.holter], True)
print('*' * 25, '解析数据如下', '*' * 25)
pprint(r.data_dict)

# 监听事件
print('-' * 50)
r = platform.event_report_listen(dh, dh.events.calibrate, True)
print('*' * 25, '解析数据如下', '*' * 25)
pprint(r.data_dict)

platform.stop()