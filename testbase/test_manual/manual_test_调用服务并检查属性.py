from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.S4_7G_SPEAKER_MODEL import S4_QG_SPEAKER

mqtt_client = MQTTClient(host='192.168.52.21', port=1883)
platform = PlatformController(mqtt_client)

speaker = S4_QG_SPEAKER('1700004')

# 音柱
# 切换到手动模式
print('-' * 50)
service = speaker.services.switchMode
service.parameters.mode.v = 'manual'
platform.service_invoke(speaker, service)

# 修改音量
print('-' * 50)
service = speaker.services.setVolume
service.parameters.volume.v = 30
r = platform.service_invoke(speaker, service, check_property=speaker.properties.volume, is_parsed=True)

print('*' * 25, '解析数据如下', '*' * 25)
print('服务调用响应数据')
pprint(r.data_dict)
print('检查的属性上报数据')
pprint(platform.check_property_data)
# 将上报数据中解析到的volume值赋值给属性speaker.properties.volume
speaker.properties.volume.v = platform.check_property_data['volume']
if speaker.properties.volume.v == 30:
    print('OK')

# 切换到自动模式
print('-' * 50)
service = speaker.services.switchMode
service.parameters.mode.v = 'auto'
platform.service_invoke(speaker, service)

platform.stop()
