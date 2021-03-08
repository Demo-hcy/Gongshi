from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.S3_KLT_C4_MODEL import S3_KLT_C4

# 信息屏
mqtt_client = MQTTClient(host='192.168.52.21', port=1883)
inforscreen = S3_KLT_C4('1700002')
platform = PlatformController(mqtt_client, False)
platform.will_set()
platform.start()
platform.online()
platform.login_listen(inforscreen, True)
platform.stop()