from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.simulator import PlatformSimulator
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.SMARTBOX_MODEL import SmartBox

mqtt_client = MQTTClient(host='192.168.52.21', port=1883)

inforscreen = Colorlight('1700002')
platform = PlatformSimulator(inforscreen, mqtt_client)

# print('-' * 50)
# service = inforscreen.services.switchMode
# result, msg = platform.service_invoke(service, {'mode': 1})
# print('*' * 25, '解析数据如下', '*' * 25)
# pprint(platform.current_response.data)

smart=SmartBox('03846600411')
service=smart.services.switchMode
result, msg = platform.service_invoke(service, {'mode': 1})
print('*' * 25, '解析数据如下', '*' * 25)
pprint(platform.current_response.data)

platform.stop()