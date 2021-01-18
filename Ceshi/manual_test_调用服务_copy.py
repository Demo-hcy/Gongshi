from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
# from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.D1_7G_DHWG_MODEL import D1_QG_DHWG

mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
platform = PlatformController(mqtt_client)

DongHuan = D1_QG_DHWG('E46854B287555333')

print('-' * 50)

# 基本设置
service=DongHuan.services.setBasic
service.parameters.alarmInterval.v=30
service.parameters.enabled.v=True
service.parameters.interval.v=240
service.parameters.do1.v=False
service.parameters.do2.v=True
r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.holter.struct.alarmInterval,
                            is_parsed=True)

# {
#
#         # I/O及动环上报使能
#         # "enabled": True,
#
#         # 定时上报间隔
#         # "interval": 240,
#
#         # 告警间隔
#         "alarmInterval": 30,
#
#         # DO1默认状态
#         # "do1": False,
#
#         # DO2默认状态
#         # "do2": True
#     }


# # 设置DO状态
service=DongHuan.services.setDO
service.parameters.port.v=1
service.parameters.status.v=True
service.parameters.shootTime.v=0

r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.holter.struct.do1,
                            is_parsed=True)

# service= DongHuan.services.setDO
# result, msg = platform.service_invoke(
#     service, {
#
#         #  端口号
#         # "port":1,
#         "port": 2,
#
#         #  状态
#         #  "status": True,
#          "status": True,
#
#         #  点动时间
#         #  "shootTime": 0
#         "shootTime": 300
#
#     })



# 重启
# service= DongHuan.services.reboot
# result, msg = platform.service_invoke(
#     service, {
#
#     })



# 更新固件
# service= DongHuan.services.updateFirmware
# result, msg = platform.service_invoke(
#     service, {
#
#         #  固件下载地址
#          "url":"http://192.168.52.21:5002/download?fileId=uImage",
#
#         #  固件文件MD5
#         #  "md5Sum": "3b82ea75c937557005bdb33c3e015f60"
#
#
#         #  "url": True,
#         #  "md5Sum":"af3112a91ee3af396eb2cbf367643321"
#
#         # "url":"http://192.168.52.21:5002/download?fileId=XingRenYueJieJinRuJiDongCheDao.mp3",
#         "md5Sum": "13fba4d076ce745bd7db9d9feb21cc9d"
#     })



# 设置ntp服务器地址
# service= DongHuan.services.setNtpHost
# result, msg = platform.service_invoke(
#     service, {
#
#         #  ntp校时服务器A
#          "hostA":"47.116.64.22",
#         #  "hostA": "",
#         #  ntp校时服务器B
#         #  "hostB":"174.42.54.5",
#          "hostB":""
#
#     })



#  设置mqtt服务器
# service= DongHuan.services.setMqttBroker
# result, msg = platform.service_invoke(
#     service, {
#
#          # 主备服务器
#          "master": True,
#
#          # mqtt服务器地址
#          "host":"192.168.52.21",
#
#          # 端口
#          "port":1883,
#
#          # 用户名
#          "userName":"tN9NQe#fPh",
#
#          # 密码
#          "passwd":"mosquitto"
#     })



# 485串口设置
# service= DongHuan.services.setRs485
# result, msg = platform.service_invoke(
#     service, {
#
#         #  端口号
#         "port":1,
#         # "port": 2,
#
#         #  波特率
#         "baudRate": 2300,
#
#         #  数据位
#         "byteSize": 8,
#
#         # 停止位
#         "stopBit": "1",
#
#         # 校验
# 	    "parities":"N"
#
#     })



# 485发送
# service= DongHuan.services.writeRs485
# result, msg = platform.service_invoke(
#     service, {
#
#         #  端口号
#         "port":1,
#         # "port": 2,
#
#         # 数据
#         "data": "8755",
#
#         # 清空缓冲区
#         "flush":True
#
#     })


# 485接收
# service = DongHuan.services.readRs485
# result, msg = platform.service_invoke(
#     service, {
#
#         #  端口号
#         "port":1,
#         # "port": 2,
#
#         # 数据长度
#         "len": 1000,
#
#         # 超时时间
#         "wait":10000,
#
#         # 清空缓冲区
#         "flush": False
#
#     })



# 传感器
# service= DongHuan.services.setSensor
# result, msg = platform.service_invoke(
#     service, {
#
#         #  倾斜校准
#         #  "tiltCalibrate":True,
#
#         #  倾斜告警阈值
#         #  "tiltThreshold": 30,
#
#         #  高温告警阈值
#         #  "tempHiThreshold": 50,
#
#         #  低温告警阈值
#         #  "tempLowThreshold": 10,
#
#         #  高湿告警阈值
#         #  "humiHiThreshold":50,
#
#         #  低湿告警阈值
#          "humiLowThreshold": 10,
#     })

print('*' * 25, '解析数据如下', '*' * 25)
print('服务调用响应数据')
pprint(r.data_dict)
pprint(platform.check_property_data)
