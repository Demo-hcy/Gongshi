from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.S1_7G_SMARTBOX_MODEL import S1_QG_SMARTBOX

mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
smartbox = S1_QG_SMARTBOX('03846600411')
platform = PlatformController(mqtt_client)

# 切换到手动模式
service = smartbox.services.switchMode
service.parameters.mode.v = 'manual'
r = platform.service_invoke(smartbox, service)

# 智盒重启
service = smartbox.services.reboot
r = platform.service_invoke(smartbox, service)

platform.stop()