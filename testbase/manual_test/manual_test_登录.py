from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight

# 信息屏
mqtt_client = MQTTClient(host='192.168.52.21', port=1883)
inforscreen = Colorlight('1700002')
platform = PlatformController(mqtt_client, False)
platform.will_set()
platform.start()
platform.online()
platform.login_listen(inforscreen, True)
platform.stop()