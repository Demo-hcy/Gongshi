from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.S1_7G_SMARTBOX_MODEL import S1_QG_SMARTBOX

mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
smartbox = S1_QG_SMARTBOX('03846600411')
platform = PlatformController(mqtt_client)


def read_list():
    print('-' * 50)
    properties = []
    properties.append(smartbox.properties.subDevList)
    r = platform.read(smartbox, properties, True)
    pprint(r.data_dict)


def add():
    print('-' * 50)
    service = smartbox.services.addSubDevs
    service.parameters.devInfos.v = [{
        'devId': '1700015',
        'devType': 'IPCOnvif',
        'productId': 'S5_DH_HFS8849ZMVSLED',
        'setting': '{"ip":"192.168.14.12", "httpPort":80,"onvifUser":"admin","onvifPassword":"admin123"}'
    }]
    r = platform.service_invoke(smartbox, service)

def delete():
    print('-' * 50)
    service = smartbox.services.delSubDevs
    service.parameters.productInfos.v=[{'productId':'S7_ZC_ZCT245RDLBQE277','devId':'1700014'}]
    r = platform.service_invoke(smartbox, service)

{"rs485Addr":"48","rs485Port":3}

# add()
# delete()
read_list()
platform.stop()