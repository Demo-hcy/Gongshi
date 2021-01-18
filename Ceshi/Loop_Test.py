# from library.common import *
# from library.mqtt_lib.mqtt_client import MQTTClient
# from library.mqtt_lib.simulator import PlatformSimulator
# from library.mqtt_lib.TSL_model.DH_001_MODEL import DH_001
#
# # 动环盒子
# mqtt_client = MQTTClient(host='192.168.49.68', port=1883, timeout=600)
#
# # 循环去改变属性
# DongHuan = DH_001('DH0000000002')
# platform = PlatformSimulator(DongHuan, mqtt_client)
#
# print('-' * 50)
# for i in range(50):
#     service = DongHuan.services.setBasic
#     result, msg = platform.service_invoke(
#         service, {
#             "tempHiThreshold": 50
#         })
#     print('*' * 25, '解析数据如下', '*' * 25)
#     print('服务调用响应数据')
#     pprint(platform.parse_msg(msg)[1])
#     i++
#
import socket
IP = socket.gethostbyname(socket.gethostname())
print ("本机IP：",IP)