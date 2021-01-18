from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.SMARTBOX_MODEL import SmartBox
from library.mqtt_lib.TSL_model.D1_7G_DHWG_MODEL import D1_QG_DHWG
import time

mqtt_client = MQTTClient(host='192.168.49.68', port = 1883,user= "mosquitto",password="tN9NQe#fPh")

# Attributes = ['sn','model', 'networkInfo', 'mqttPrefix','serverA','serverB', 'ntpInfo',
#               'upTime','time','rs485_1','rs485_2' ,'hwVersion','fwVersion', 'holter']
# dh = DH_001('D26670974B34332A')
# Alldate: List[Tuple[bool,str]] = []
# platform = PlatformSimulator(dh, mqtt_client) # 定义一个平台
# for Read_Model in Attributes:
#     print('-' * 50)
#     param = getattr(dh.properties, Read_Model)
#     result, msg = platform.read([param])
#     print("读取的属性为：",Read_Model)
#     print('*' * 25, '解析数据如下', '*' * 25)
#     pprint(platform.parse_msg(msg))
#     Alldate.append(platform.read([param]))
# # Alldate = ''.join(date)
# # json.dumps(Alldate)
# print(msg["timestamp"])
# if 'timestamp' in msg.keys():
#     t = time.localtime(msg['timestamp'] / 1000)
#     t = time.strftime('%Y-%m-%d %H:%M:%S', t)
# #     print(t)
# pprint(Alldate)
# platform.stop()

mqtt_client = MQTTClient(host='192.168.49.68', port=1883)
dh = D1_QG_DHWG('D26670974B34332A')
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

