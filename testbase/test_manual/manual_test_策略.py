from library import common
from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib import rule
from library.mqtt_lib.TSL_model.S3_KLT_C4_MODEL import S3_KLT_C4
from library.mqtt_lib.TSL_model.S4_7G_SPEAKER_MODEL import S4_QG_SPEAKER
from library.mqtt_lib.TSL_model.S1_7G_SMARTBOX_MODEL import S1_QG_SMARTBOX
from library.mqtt_lib.TSL_model.S6_YM_1031LRKCT_MODEL import S6_YM_1031LRKCT
from library.mqtt_lib.TSL_model.S5_DH_SD6A9233XAHNT_MODEL import S5_DH_SD6A9233XAHNT
from library.mqtt_lib.TSL_model.S2_NFDW_ZHDGDHGLM_MODEL import S2_NFDW_ZHDGDHGLM

mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
platform = PlatformController(mqtt_client)

inforscreen = S3_KLT_C4('1700002')
sperker = S4_QG_SPEAKER('1700004')
lamp = S6_YM_1031LRKCT('1700001')
smartbox = S1_QG_SMARTBOX('03846600411')
camera = S5_DH_SD6A9233XAHNT('dddd')
nfdw=S2_NFDW_ZHDGDHGLM('cccc')

# # 联动
# property = get_var_name(sperker.properties.volume)
# rp = rule.RefProperty(sperker, property)
# condition1 = rule.Condition(rp, '>', 30)

# service = get_var_name(inforscreen.services.setOnOff)
# param1 = inforscreen.services.setOnOff.parameters.onOff
# if_block1 = rule.CallService(inforscreen, service, 0, {param1: 0})

# script = rule.Script([condition1], [if_block1])

# rule1 = rule.LinkageRule('7777', True, 1, [rule.RuleDate('2020-12-7', '2020-12-8')],
#                          [rule.RuleTime('11:00:00', '21:00:00')], [sperker], [inforscreen], script)
# data = rule.Rules([rule1])
# smartbox.services.addRule.parameters.rules.v = data

# r = platform.service_invoke(smartbox, smartbox.services.addRule, is_parsed=True)
# print('*' * 25, '解析数据如下', '*' * 25)
# pprint(r.data_dict)

# # 定时
# # 信息屏
# service = get_var_name(inforscreen.services.setBrightness)
# param1 = inforscreen.services.setBrightness.parameters.brightness
# if_block1 = rule.CallService(inforscreen, service, 0, {param1: 1})

# script = rule.Script(if_block=[if_block1])

# rule1 = rule.TimerRule('123', True, 1, [rule.RuleDate('2020-12-10', '2020-12-10')],
#                        [rule.RuleTime('16:17:00', '16:17:30')], [inforscreen], [inforscreen], script)
# data = rule.Rules([rule1])
# smartbox.services.addRule.parameters.v = data

# r = platform.service_invoke(smartbox, smartbox.services.addRule, is_parsed=True)
# print('*' * 25, '解析数据如下', '*' * 25)
# pprint(r.data_dict)

# # 灯控
# service = get_var_name(lamp.services.setOnOff)
# param1 = lamp.services.setOnOff.parameters.onOff
# if_block1 = rule.CallService(lamp, service, 0, {param1: '1'})

# script = rule.Script(if_block=[if_block1])

# rule1 = rule.TimerRule('33333', True, 1, [rule.RuleDate('2020-12-10', '2020-12-10')],
#                        [rule.RuleTime('15:36:00', '15:37:00')], [lamp], [lamp], script)
# data = rule.Rules([rule1])
# smartbox.services.addRule.parameters.rules.v = data

# r = platform.service_invoke(smartbox, smartbox.services.addRule, is_parsed=True)
# print('*' * 25, '解析数据如下', '*' * 25)
# pprint(r.data_dict)

# 事件驱动
event = get_var_name(camera.events.trafficParking)
duration = rule.Duration(camera, event)
condition1 = rule.Condition(duration, '>', 10)

ep = get_var_name(camera.events.trafficParking.parameters.plateNumber)
re = rule.RefEvent(camera, ep,'aaa')

service = get_var_name(inforscreen.services.playCustomizeProgram)
param1 = inforscreen.services.playCustomizeProgram.parameters.textList
if_block1 = rule.CallService(inforscreen, service, 0, {param1: re})

centerX = inforscreen.services.playCustomizeProgram.parameters.centerX
centerY = inforscreen.services.playCustomizeProgram.parameters.centerY
imageMd5Sum = inforscreen.services.playCustomizeProgram.parameters.imageMd5Sum
maxHeight = inforscreen.services.playCustomizeProgram.parameters.maxHeight
imageUrl = inforscreen.services.playCustomizeProgram.parameters.imageUrl
maxWidth = inforscreen.services.playCustomizeProgram.parameters.maxWidth
moduleMd5Sum = inforscreen.services.playCustomizeProgram.parameters.moduleMd5Sum
textList = inforscreen.services.playCustomizeProgram.parameters.textList
play_custom_blo = rule.CallService(
    inforscreen, service, 60, {
        centerX:
        64,
        centerY:
        144,
        imageMd5Sum:
        "823c7d34e1a26ffb01499a5072512eb8",
        imageUrl:
        "http://192.168.52.21:5002/download?fileId=fmodule.jpg",
        maxWidth:
        100,
        maxHeight:
        100,
        moduleMd5Sum:
        "ed7169e13405857d8a5d4301c0eb60b3",
        textList: [{
            "rectX": 10,
            "rectY": 50,
            "rectWidth": 100,
            "rectHeight": 48,
            "rectA": 50,
            "rectR": 0,
            "rectG": 255,
            "rectB": 0,
            "textA": 255,
            "textR": 255,
            "textG": 0,
            "textB": 0,
            "isScroll": 1,
            "fontSize": 48,
            "text": re
        }]
    })

script = rule.Script([condition1], [play_custom_blo])
print(script)

rule1 = rule.LinkageRule('8888', True, 1, [rule.RuleDate('2020-12-10', '2020-12-10')],
                         [rule.RuleTime('15:36:00', '15:37:00')], [camera], [inforscreen], [script])
data = rule.Rules([rule1])
print(data)

# smartbox.services.addRule.parameters.rules.v = data

# r = platform.service_invoke(smartbox, smartbox.services.addRule, is_parsed=True)
# print('*' * 25, '解析数据如下', '*' * 25)
# pprint(r.data_dict)

property = get_var_name(nfdw.properties.channels.columnComplex[0].channel)
rp = rule.RefProperty(nfdw, property)
print(rp)

platform.stop()