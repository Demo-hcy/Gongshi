from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
import time

mqtt_client = MQTTClient(host='192.168.52.21', port=1883)
platform = PlatformController(mqtt_client)

inforscreen = Colorlight('1700002')
# 信息屏 切换手动模式
print('-' * 50)
service = inforscreen.services.switchMode
service.parameters.mode.v = 'manual'
r = platform.service_invoke(inforscreen, service)

# 信息屏 添加节目
print('-' * 50)
service = inforscreen.services.addProgram
service.parameters.url.v = 'http://192.168.49.96/iot-api/programFile/5bb41908c1b8494ea2ba70ccf68a4a5e.tar'
service.parameters.fileName.v = '12345'
service.parameters.md5Sum.v = 'ee02115131f6ff6c2414fdfd3f99232c'
r = platform.service_invoke(inforscreen, service)

# 信息屏 播放节目
print('-' * 50)
service = inforscreen.services.playProgram
service.parameters.fileName.v = '12345'
r = platform.service_invoke(inforscreen, service)

time.sleep(2)

# 信息屏 停止节目
print('-' * 50)
service = inforscreen.services.stopProgram
r = platform.service_invoke(inforscreen, service)

# 信息屏 切换自动模式
print('-' * 50)
service = inforscreen.services.switchMode
service.parameters.mode.v = 'auto'
r = platform.service_invoke(inforscreen, service)

platform.stop()