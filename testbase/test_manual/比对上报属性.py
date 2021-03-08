from library.common import *
from library.mqtt_lib import TSL_model
from library.mqtt_lib.TSL_model import *


def cp(l, device):
    listA = list(vars(device.properties).keys())
    listB = list(l['params'].keys())
    x1 = set(listA).difference(set(listB))
    x2 = set(listB).difference(set(listA))
    print('物模型多的属性：')
    pprint(x1)
    print('上报多的属性：')
    pprint(x2)


l = {
    "msgId": "19961019",
    "timestamp": 1611562649872,
    "code": 0,
    "message": "qjBoxOpcodeSucess",
    "data": {
        "resolutions": [{
            "channel":
            1,
            "channelResolution": [{
                "name": "mainStream",
                "id": 1,
                "resolution": {
                    "width": 3840,
                    "height": 2160
                }
            }, {
                "name": "subStream",
                "id": 2,
                "resolution": {
                    "width": 704,
                    "height": 576
                }
            }, {
                "name": "thirdStream",
                "id": 3,
                "resolution": {
                    "width": 1920,
                    "height": 1080
                }
            }]
        }]
    }
}
device = TSL_model.S5_DH_HFS8849ZMVSLED('')
cp(l, device)
