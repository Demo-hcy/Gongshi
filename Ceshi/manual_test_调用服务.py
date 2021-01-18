from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
# from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.D1_7G_DHWG_MODEL import D1_QG_DHWG

mqtt_client = MQTTClient(host='192.168.49.68', port=1883)
platform = PlatformController(mqtt_client)

# DongHuan = D1_QG_DHWG('E46854B287555333')
DongHuan = D1_QG_DHWG('D26670974B34332A')

print('-' * 50)

# 基本设置
# I/O及动环上报使能	enabled
# 定时上报间隔	interval
# 告警间隔	alarmInterval
# DO1默认状态	do1
# DO2默认状态	do2

# service=DongHuan.services.setBasic
# service.parameters.alarmInterval.v=600
# service.parameters.enabled.v=True
# service.parameters.interval.v=600
# service.parameters.do1.v=True
# service.parameters.do2.v=True
# r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.holter.struct.alarmInterval,
#                             is_parsed=True)


# # 设置DO状态
# 端口号	port
# 状态	status
# 点动时间	shootTime

# service=DongHuan.services.setDO
# service.parameters.port.v=1
# service.parameters.status.v=False
# service.parameters.shootTime.v=0
# r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.holter.struct.do2,is_parsed=True)


# 重启
# service=DongHuan.services.reboot
# r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.sn,
#                             is_parsed=True)


# 更新固件
# 固件下载地址	url
# 固件文件MD5	md5Sum
#
# service=DongHuan.services.updateFirmware
# service.parameters.url.v = "http://192.168.52.21:5002/download?fileId=uImage"
# # service.parameters.md5Sum.v ="2c3f4a00fb60684113fa2ea369ce2004"
# service.parameters.md5Sum.v ="f435ea19a2c8f1f71b6a979efa9eea51"
# r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.fwVersion,
#                             is_parsed=True)


# 设置ntp服务器地址
# ntp校时服务器A	hostA
# ntp校时服务器B	hostB

# service = DongHuan.services.setNtpHost
# service.parameters.hostA.v = "47.116.64.22"  # 47.116.64.22
# service.parameters.hostB.v = ""
# r = platform.service_invoke(DongHuan, service, check_property=DongHuan.properties.ntpInfo.struct.ntpStatus,
#                             is_parsed=True)

# 485串口设置
# 端口号	port
# 波特率	baudRate
# 数据位	byteSize
# 停止位	stopBit
# 校验	parities

# service =DongHuan.services.setRs485
# service.parameters.port.v = 1
# service.parameters.baudRate.v = 250000
# service.parameters.byteSize.v = 5
# service.parameters.stopBit.v = "1"
# service.parameters.parities.v = "N"
# r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.rs485_1.struct.baudRate,
#                             is_parsed=True)


# 485发送
# 端口号	port
# 数据	data
# 清空缓冲区	flush

# service =DongHuan.services.writeRs485
# service.parameters.port.v = 1
# service.parameters.data.v = "2300"
# service.parameters.flush.v = True
# r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.sn,
#                             is_parsed=True)


# 485接收
# 端口号	port
# 数据长度	len
# 超时时间	wait
# 清空缓冲区	flush

# service = DongHuan.services.readRs485
# service.parameters.port.v = 1
# service.parameters.len.v = 1000
# service.parameters.wait.v = 10000
# service.parameters.flush.v = False
# r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.sn,
#                             is_parsed=True)


# 传感器
# 设置倾斜相对零点	tiltCalibrate
# 倾斜告警阈值	tiltThreshold
# 高温告警阈值	tempHiThreshold
# 低温告警阈值	tempLowThreshold
# 高湿告警阈值	humiHiThreshold
# 低湿告警阈值	humiLowThreshold

service= DongHuan.services.setSensor
service.parameters.tiltCalibrate.v = True
service.parameters.tiltThreshold.v = 29
service.parameters.tempHiThreshold.v = 70
service.parameters.tempLowThreshold.v = 10
service.parameters.humiHiThreshold.v = 40
service.parameters.humiLowThreshold.v = 10
r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.holter.struct.tilt,
                            is_parsed=True)

# 设置音量
# 音量	volume

# service = DongHuan.services.setVolume
# service.parameters.volume.v =80
# r = platform.service_invoke(DongHuan,service,check_property=DongHuan.properties.holter.struct.voip,
#                             is_parsed=True)

print('*' * 25, '解析数据如下', '*' * 25)
print('服务调用响应数据')
pprint(r.data_dict)
pprint(platform.check_property_data)
