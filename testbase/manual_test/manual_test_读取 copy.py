from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.simulator import PlatformSimulator
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.SPEAKER_MODEL import Speaker

mqtt_client = MQTTClient(host='192.168.52.21', port=1883)

inforscreen = Colorlight('1700002')
platform = PlatformSimulator(inforscreen, mqtt_client)
print('-' * 50)
param = inforscreen.properties.onOff
result, msg = platform.read([param])
print('*' * 25, '解析数据如下', '*' * 25)
pprint(platform.current_response.data)

print('-' * 50)
param = inforscreen.properties.brightness
result, msg = platform.read([param])
print('*' * 25, '解析数据如下', '*' * 25)
pprint(platform.current_response.data)

print('-' * 50)
speaker = Speaker('1700004')
param = speaker.properties.volume
result, msg = platform.read([param])
print('*' * 25, '解析数据如下', '*' * 25)
pprint(platform.current_response.data)
platform.stop()