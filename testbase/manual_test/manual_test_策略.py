from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib import rule
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.SPEAKER_MODEL import Speaker
from library.mqtt_lib.TSL_model.SMARTBOX_MODEL import SmartBox
from library.mqtt_lib.TSL_model.LAMP_YM103_1_L_R_KCT_MODEL import YM103_1_L_R_KCT

mqtt_client = MQTTClient(host='192.168.52.21', port=1883)
platform = PlatformController(mqtt_client)

inforscreen = Colorlight('1700002')
sperker = Speaker('1700004')
lamp = YM103_1_L_R_KCT('1700001')
smartbox = SmartBox('03846600411')

# 联动
property = get_var_name(sperker.properties.volume)
rp = rule.RefProperty(sperker, property)
condition1 = rule.Condition(rp, '>', 30)

service = get_var_name(inforscreen.services.setOnOff)
param1 = inforscreen.services.setOnOff.parameters.onOff
if_block1 = rule.CallService(inforscreen, service, 0, {param1: 0})

script = rule.Script([condition1], [if_block1])

rule1 = rule.LinkageRule('7777', True, 1, [rule.RuleDate('2020-12-7', '2020-12-8')],
                         [rule.RuleTime('11:00:00', '21:00:00')], [sperker], [inforscreen], script)
data = rule.Rules([rule1])
smartbox.services.addRule.parameters.rules.v = data

r = platform.service_invoke(smartbox, smartbox.services.addRule, is_parsed=True)
print('*' * 25, '解析数据如下', '*' * 25)
pprint(r.data_dict)

# 定时
# 信息屏
service = get_var_name(inforscreen.services.setBrightness)
param1 = inforscreen.services.setBrightness.parameters.brightness
if_block1 = rule.CallService(inforscreen, service, 0, {param1: 1})

script = rule.Script(if_block=[if_block1])

rule1 = rule.TimerRule('123', True, 1, [rule.RuleDate('2020-12-10', '2020-12-10')],
                       [rule.RuleTime('16:17:00', '16:17:30')], [inforscreen], [inforscreen], script)
data = rule.Rules([rule1])
smartbox.services.addRule.parameters.rules.v = data

r = platform.service_invoke(smartbox, smartbox.services.addRule, is_parsed=True)
print('*' * 25, '解析数据如下', '*' * 25)
pprint(r.data_dict)

# 灯控
service = get_var_name(lamp.services.setOnOff)
param1 = lamp.services.setOnOff.parameters.onOff
if_block1 = rule.CallService(lamp, service, 0, {param1: '1'})

script = rule.Script(if_block=[if_block1])

rule1 = rule.TimerRule('33333', True, 1, [rule.RuleDate('2020-12-10', '2020-12-10')],
                       [rule.RuleTime('15:36:00', '15:37:00')], [lamp], [lamp], script)
data = rule.Rules([rule1])
smartbox.services.addRule.parameters.rules.v = data

r = platform.service_invoke(smartbox, smartbox.services.addRule, is_parsed=True)
print('*' * 25, '解析数据如下', '*' * 25)
pprint(r.data_dict)

platform.stop()