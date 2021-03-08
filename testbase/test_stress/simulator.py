from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import DeviceController
from library.mqtt_lib.TSL_model.S1_7G_SMARTBOX_MODEL import S1_QG_SMARTBOX
import csv
import time


def report(id_str):
    mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
    device = DeviceController(mqtt_client)
    SmartBox = S1_QG_SMARTBOX(id_str)
    SmartBox.properties.online.v = True
    SmartBox.properties.mode.v = 'auto'
    SmartBox.properties.configureMode.v = 'active'
    properties = [
        SmartBox.properties.sn, SmartBox.properties.model, SmartBox.properties.online, SmartBox.properties.mode,
        SmartBox.properties.ntpInfo, SmartBox.properties.upTime, SmartBox.properties.time, SmartBox.properties.hwInfo,
        SmartBox.properties.logHost, SmartBox.properties.configureMode, SmartBox.properties.version,
        SmartBox.properties.mqttInfo
    ]
    device.report(SmartBox, properties)


def main_func():
    csv_file = Path(__file__).parent.joinpath('sn.csv')

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        id_list = list(reader)

    for id_str in id_list:
        thread = ThreadWithReturnValue(target=report, args=(id_str))
        thread.start()


main_func()