from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.SMARTBOX_MODEL import SmartBox
from library.mqtt_lib.TSL_model.D1_7G_DHWG_MODEL import D1_QG_DHWG
import time

mqtt_client = MQTTClient(host='192.168.49.96', port=1883, user="mosquitto", password="tN9NQe#fPh")

# dh = D1_QG_DHWG('D26670974B34332A')
dh = D1_QG_DHWG('E46854B287555333')
platform = PlatformController(mqtt_client)
properties = []
properties.append(dh.properties.networkInfo)
r = platform.read(dh, properties)
print('*' * 25, '解析数据如下', '*' * 25)
print("时间戳为:", r.data_dict['timestamp'])
if 'timestamp' in r.data_dict.keys():
    t = time.localtime(r.data_dict['timestamp'] / 1000)
    t = time.strftime('%Y-%m-%d %H:%M:%S', t)
    print("时间戳转换后为：", t)
pprint(platform.parse_msg(r.data_dict).data_dict)
platform.stop()
