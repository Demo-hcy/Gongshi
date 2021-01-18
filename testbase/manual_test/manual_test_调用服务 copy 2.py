from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.simulator import PlatformSimulator
from library.mqtt_lib.TSL_model.SPEAKER_MODEL import Speaker

mqtt_client = MQTTClient(host='192.168.52.21', port=1883)

speaker = Speaker('1700004')
platform = PlatformSimulator(speaker, mqtt_client)

# print('-' * 50)
# service = speaker.services.switchMode
# result, msg = platform.service_invoke(service, {'mode': 1})
print('-' * 50)
service = speaker.services.setVolume
result, msg = platform.service_invoke(service, {'volume': 35})
print('*' * 25, '解析数据如下', '*' * 25)
pprint(platform.current_response.data)
platform.stop()