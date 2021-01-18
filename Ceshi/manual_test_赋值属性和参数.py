from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.simulator import PlatformSimulator
from library.mqtt_lib.TSL_model.DH_001_MODEL import DH_001

# 赋值属性
mqtt_client = MQTTClient(host='192.168.49.68', port=1883, timeout=60)
dh = DH_001('DH0000000002')
platform = PlatformSimulator(dh, mqtt_client)
r, m = platform.report_listen(dh.properties.holter)
r, m = platform.parse_msg(m)
if r:
    dh.properties.holter.v = m['holter']
pprint(dh.properties.holter.struct.temperature.v)