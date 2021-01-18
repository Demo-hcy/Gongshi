from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.simulator import PlatformSimulator
from library.mqtt_lib.TSL_model.SPEAKER_MODEL import Speaker

mqtt_client = MQTTClient(host='192.168.52.21', port=1883)

speaker = Speaker('1700004')
platform = PlatformSimulator(speaker, mqtt_client)

# 音柱 修改音量
print('-' * 50)
service = speaker.services.setVolume
check_property = speaker.properties.volume
result, msg = platform.service_invoke(service, {'volume': 30},
                                      check_properties=[check_property])

print('*' * 25, '解析数据如下', '*' * 25)
print('服务调用响应数据')
pprint(platform.current_response.data)
print('检查的属性上报数据')
pprint(platform.check_properties_data)
platform.stop()
