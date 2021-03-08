from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.S3_KLT_C4_MODEL import S3_KLT_C4
from library.mqtt_lib.TSL_model.S1_7G_SMARTBOX_MODEL import S1_QG_SMARTBOX
import time

mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
platform = PlatformController(mqtt_client)

inforscreen = S3_KLT_C4('1700002')
smartbox = S1_QG_SMARTBOX('03846600411')
# smartbox = S1_QG_SMARTBOX('04132500855')
# # 信息屏 切换手动模式
# print('-' * 50)
# service = inforscreen.services.switchMode
# service.parameters.mode.v = 'manual'
# r = platform.service_invoke(inforscreen, service)

# # 信息屏 添加节目
# print('-' * 50)
# service = inforscreen.services.addProgram
# service.parameters.url.v = 'http://192.168.49.96/iot-api/programFile/5bb41908c1b8494ea2ba70ccf68a4a5e.tar'
# service.parameters.fileName.v = '12345'
# service.parameters.md5Sum.v = 'ee02115131f6ff6c2414fdfd3f99232c'
# r = platform.service_invoke(inforscreen, service)

# # 信息屏 播放节目
# print('-' * 50)
# service = inforscreen.services.playProgram
# service.parameters.fileName.v = '12345'
# r = platform.service_invoke(inforscreen, service)

# time.sleep(2)

# # 信息屏 停止节目
# print('-' * 50)
# service = inforscreen.services.stopProgram
# r = platform.service_invoke(inforscreen, service)

# # 信息屏 切换自动模式
# print('-' * 50)
# service = inforscreen.services.switchMode
# service.parameters.mode.v = 'auto'
# r = platform.service_invoke(inforscreen, service)



print('-' * 50)
service = smartbox.services.getAllRules
# service.parameters.uuids.v=['SCREEN,S3_KLT_C4,11,11,03846600411']
r = platform.service_invoke(smartbox, service)

platform.stop()