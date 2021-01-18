from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.SMARTBOX_MODEL import SmartBox
from library.mqtt_lib.TSL_model.D1_7G_DHWG_MODEL import D1_QG_DHWG
import time

# 信息屏 读取开关
# mqtt_client = MQTTClient(host='192.168.52.21', port=1883)
# inforscreen = Colorlight('1700002')
# platform = PlatformController(mqtt_client)
# print('-' * 50)
# properties = []
# properties.append(inforscreen.properties.onOff)
# r = platform.read(inforscreen, properties)
# print('*' * 25, '解析数据如下', '*' * 25)
# pprint(r.data_dict)
# platform.stop()

# 智盒 读取模式
# mqtt_client = MQTTClient(host='192.168.52.21', port=1883)
# smartbox = SmartBox('03846600411')
# platform = PlatformController(mqtt_client)
# print('-' * 50)
# properties = []
# properties.append(smartbox.properties.mode)
# r = platform.read(smartbox, properties)
# print('*' * 25, '解析数据如下', '*' * 25)
# pprint(r.data_dict)
# platform.stop()

# 获取时间戳转换为时间格式
mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
dh = D1_QG_DHWG('E46854B287555333')
platform = PlatformController(mqtt_client)
properties = []
properties.append(dh.properties.networkInfo)
r = platform.read(dh, properties)
print('*' * 25, '解析数据如下', '*' * 25)
print(r.data_dict['timestamp'])
if 'timestamp' in r.data_dict.keys():
    t = time.localtime(r.data_dict['timestamp'] / 1000)
    t = time.strftime('%Y-%m-%d %H:%M:%S', t)
    print(t)
pprint(platform.parse_msg(r.data_dict).data_dict)
platform.stop()