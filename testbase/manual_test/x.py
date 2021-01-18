from os import device_encoding
from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.simulator import DeviceSimulator
from library.mqtt_lib.rule import *
from library.mqtt_lib.TSL_model.D1_7G_DHWG_MODEL import D1_QG_DHWG

# 动环盒子
mqtt_client = MQTTClient(host='192.168.49.96', port=1883, timeout=60)
dh_id = 'DH14'
dh = D1_QG_DHWG(dh_id)
dh.properties.fwVersion.v = '03.03'
dh.properties.holter.v = {
    'enabled': True,
    'interval': 60,
    'alarmInterval': 60,
    'do1Default': True,
    'do2Default': True,
    'di1': False,
    'di2': False,
    'do1': True,
    'do2': True,
    'eth': {
        'port1': False,
        'port2': False,
        'port3': False,
        'port4': False
    },
    'tilt': {
        'online': True,
        'angle': 0,
        'threshold': 30,
        'alarming': False
    },
    'temperature': {
        'online': True,
        'temperature': 30,
        'hiThreshold': 50,
        'lowThreshold': 10,
        'type': 'none',
        'alarming': False
    },
    'humidity': {
        'online': True,
        'humidity': 50,
        'hiThreshold': 90,
        'lowThreshold': 30,
        'type': 'none',
        'alarming': False
    },
    'water': {
        'online': True,
        'status': False
    }
}
dh.properties.hwVersion.v = '1.5'
dh.properties.model.v = 'D1_7G_DHWG'
dh.properties.mqttPrefix.v = '/device/D1_7G_DHWG'
dh.properties.networkInfo.v = {
    'networkType': 'wired',
    'wirelessSupport': 'none',
    'networkAvailable': True,
    'mac': '09:00:27:00:01:96',
    'dhcp': False,
    'ip': '192.168.54.5',
    'gateway': '192.168.54.1',
    'mask': '255.255.255.0'
}
dh.properties.ntpInfo.v = {'ntpStatus': True, 'hostA': '47.116.64.22', 'hostB': '47.116.64.22'}
dh.properties.rs485_1.v = {'baudRate': 9600, 'byteSize': 8, 'stopBit': '1', 'parities': 'N'}
dh.properties.rs485_2.v = {'baudRate': 9600, 'byteSize': 8, 'stopBit': '1', 'parities': 'N'}
dh.properties.serverA.v = {'host': '192.168.49.96', 'port': 1883, 'user': 'qjzh2020', 'password': 'qjzh2020'}
dh.properties.serverB.v = {'host': '192.168.49.96', 'port': 1883, 'user': 'qjzh2020', 'password': 'qjzh2020'}
dh.properties.sn.v = dh_id
device = DeviceSimulator(dh, mqtt_client)

param = {getattr(dh.properties, x): getattr(dh.properties, x).v for x in vars(dh.properties)}
device.read_listen([], True, code=0)
