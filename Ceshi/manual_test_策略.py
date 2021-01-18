from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.simulator import PlatformSimulator
from library.mqtt_lib import rule
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.SPEAKER_MODEL import Speaker
from library.mqtt_lib.TSL_model.SMARTBOX_MODEL import SmartBox

mqtt_client = MQTTClient(host='192.168.52.21', port=1883)
inforscreen = Colorlight('1700002')
sperker = Speaker('1700004')

property = get_var_name(sperker.properties.volume)
rp = rule.RefProperty(sperker, property)
condition1 = rule.Condition(rp, '>', 30)
conditions = [condition1]

service = get_var_name(inforscreen.services.setOnOff)
cs = rule.CallService(inforscreen, service, 0,
                      {inforscreen.services.setOnOff.parameters.onOff.id: 0})

e = ''

st = rule.Strategy(conditions, [cs], [e])

smartbox = SmartBox('03846600411')
platform = PlatformSimulator(smartbox, mqtt_client)
rule1 = rule.Rule('7777', True, rule.RuleType.linkage, 1,
                  [rule.RuleDate('2020-12-7', '2020-12-8')],
                  [rule.RuleTime('11:00:00', '21:00:00')], [inforscreen],
                  [inforscreen], st)
data = {'ruls': [rule1]}
platform.service_invoke(smartbox.services.addRule, data)
print('*' * 25, '解析数据如下', '*' * 25)
pprint(platform.current_response.data)
platform.stop()