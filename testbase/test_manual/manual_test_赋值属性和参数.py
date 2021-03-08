from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.D1_7G_DHWG_MODEL import D1_QG_DHWG

# 赋值属性
mqtt_client = MQTTClient(host='192.168.49.96', port=1883, timeout=60)
platform = PlatformController(mqtt_client)
dh = D1_QG_DHWG('E46854B287555333')
r = platform.report_listen(dh, [dh.properties.holter], is_parsed=True)
if r.result:
    dh.properties.holter.v = r.data_dict['holter']
pprint(dh.properties.holter.struct.temperature.v)