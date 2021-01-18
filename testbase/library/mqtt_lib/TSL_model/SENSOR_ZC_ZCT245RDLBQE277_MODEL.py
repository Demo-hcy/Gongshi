from .base_model import *


class S7_ZC_ZCT245RDLBQE277(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S7_ZC_ZCT245RDLBQE277'
        self.productName = '直川倾斜传感器'
        self.properties = Properties()
        self.events = Events()
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.setCurrentAsZero = SetCurrentAsZeroService()
        self.setXAlarmAngleThreshold = SetXAlarmAngleThresholdService()
        self.setYAlarmAngleThreshold = SetYAlarmAngleThresholdService()
        self.setAlarmInterval = SetAlarmIntervalService()
        self.switchMode = SwitchModeService()


class SwitchModeService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'switchMode'
        self.name = '切换模式'
        self.type = 'management'
        self.parameters = SwitchModeServiceParameters()
        self.output = None


class SwitchModeServiceParameters:
    def __init__(self) -> None:
        self.mode = ModeSwitchModeServiceParameter()

    @property
    def v(self):
        return {'mode': self.mode.v}

    @v.setter
    def v(self, value):
        if value.get('mode') is not None: self.mode.v = value['mode']


class ModeSwitchModeServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'mode'
        self.name = '模式'
        self.required = True
        self.type = 'string'
        self.specs = ModeSwitchModeServiceParameterSpecs()
        self.v: str = ''


class ModeSwitchModeServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ModeSwitchModeServiceParameterSpecsOptional()


class ModeSwitchModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.manual = ManualModeSwitchModeServiceParameterSpecsOptional()
        self.auto = AutoModeSwitchModeServiceParameterSpecsOptional()


class AutoModeSwitchModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'auto'
        self.desc = '自动'


class ManualModeSwitchModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'manual'
        self.desc = '手动'


class SetAlarmIntervalService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setAlarmInterval'
        self.name = '设置告警间隔'
        self.parameters = SetAlarmIntervalServiceParameters()
        self.output = None


class SetAlarmIntervalServiceParameters:
    def __init__(self) -> None:
        self.interval = IntervalSetAlarmIntervalServiceParameter()

    @property
    def v(self):
        return {'interval': self.interval.v}

    @v.setter
    def v(self, value):
        if value.get('interval') is not None: self.interval.v = value['interval']


class IntervalSetAlarmIntervalServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'interval'
        self.name = '告警间隔'
        self.required = True
        self.type = 'integer'
        self.specs = IntervalSetAlarmIntervalServiceParameterSpecs()
        self.v: int = 0


class IntervalSetAlarmIntervalServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 86400
        self.unit = 'S'
        self.unitName = '秒'
        self.step = 1


class SetYAlarmAngleThresholdService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setYAlarmAngleThreshold'
        self.name = '设置Y轴倾斜阈值'
        self.parameters = SetYAlarmAngleThresholdServiceParameters()
        self.output = None


class SetYAlarmAngleThresholdServiceParameters:
    def __init__(self) -> None:
        self.Threshold = ThresholdSetYAlarmAngleThresholdServiceParameter()

    @property
    def v(self):
        return {'Threshold': self.Threshold.v}

    @v.setter
    def v(self, value):
        if value.get('Threshold') is not None: self.Threshold.v = value['Threshold']


class ThresholdSetYAlarmAngleThresholdServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'Threshold'
        self.name = 'Y轴倾斜阈值'
        self.required = True
        self.type = 'integer'
        self.specs = ThresholdSetYAlarmAngleThresholdServiceParameterSpecs()
        self.v: int = 0


class ThresholdSetYAlarmAngleThresholdServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 45
        self.unit = '°'
        self.unitName = '度'
        self.step = 1


class SetXAlarmAngleThresholdService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setXAlarmAngleThreshold'
        self.name = '设置X轴倾斜阈值'
        self.parameters = SetXAlarmAngleThresholdServiceParameters()
        self.output = None


class SetXAlarmAngleThresholdServiceParameters:
    def __init__(self) -> None:
        self.Threshold = ThresholdSetXAlarmAngleThresholdServiceParameter()

    @property
    def v(self):
        return {'Threshold': self.Threshold.v}

    @v.setter
    def v(self, value):
        if value.get('Threshold') is not None: self.Threshold.v = value['Threshold']


class ThresholdSetXAlarmAngleThresholdServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'Threshold'
        self.name = 'X轴倾斜阈值'
        self.required = True
        self.type = 'integer'
        self.specs = ThresholdSetXAlarmAngleThresholdServiceParameterSpecs()
        self.v: int = 0


class ThresholdSetXAlarmAngleThresholdServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 45
        self.unit = '°'
        self.unitName = '度'
        self.step = 1


class SetCurrentAsZeroService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setCurrentAsZero'
        self.name = '设置零点模式'
        self.parameters = None
        self.output = None


class Events:
    def __init__(self) -> None:
        self.xTiltAlarm = XTiltAlarmEvent()
        self.yTiltAlarm = YTiltAlarmEvent()


class YTiltAlarmEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'yTiltAlarm'
        self.name = 'Y轴倾斜告警'
        self.parameters = None


class XTiltAlarmEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'xTiltAlarm'
        self.name = 'X轴倾斜告警'
        self.parameters = None


class Properties:
    def __init__(self) -> None:
        self.xAngle = XAngleProperty()
        self.yAngle = YAngleProperty()
        self.xAngleThreshold = XAngleThresholdProperty()
        self.yAngleThreshold = YAngleThresholdProperty()
        self.rs485Port = Rs485PortProperty()
        self.rs485Addr = Rs485AddrProperty()
        self.rs485Baund = Rs485BaundProperty()
        self.rs485DataBit = Rs485DataBitProperty()
        self.rs485Parity = Rs485ParityProperty()
        self.rs485StopBit = Rs485StopBitProperty()
        self.online = OnlineProperty()
        self.mode = ModeProperty()
        self.sn = SnProperty()
        self.alarmInterval = AlarmIntervalProperty()

    @property
    def v(self):
        return {'xAngle': self.xAngle.v, 'yAngle': self.yAngle.v, 'xAngleThreshold': self.xAngleThreshold.v, 'yAngleThreshold': self.yAngleThreshold.v, 'rs485Port': self.rs485Port.v, 'rs485Addr': self.rs485Addr.v, 'rs485Baund': self.rs485Baund.v, 'rs485DataBit': self.rs485DataBit.v, 'rs485Parity': self.rs485Parity.v, 'rs485StopBit': self.rs485StopBit.v, 'online': self.online.v, 'mode': self.mode.v, 'sn': self.sn.v, 'alarmInterval': self.alarmInterval.v}

    @v.setter
    def v(self, value):
        if value.get('xAngle') is not None: self.xAngle.v = value['xAngle']
        if value.get('yAngle') is not None: self.yAngle.v = value['yAngle']
        if value.get('xAngleThreshold') is not None: self.xAngleThreshold.v = value['xAngleThreshold']
        if value.get('yAngleThreshold') is not None: self.yAngleThreshold.v = value['yAngleThreshold']
        if value.get('rs485Port') is not None: self.rs485Port.v = value['rs485Port']
        if value.get('rs485Addr') is not None: self.rs485Addr.v = value['rs485Addr']
        if value.get('rs485Baund') is not None: self.rs485Baund.v = value['rs485Baund']
        if value.get('rs485DataBit') is not None: self.rs485DataBit.v = value['rs485DataBit']
        if value.get('rs485Parity') is not None: self.rs485Parity.v = value['rs485Parity']
        if value.get('rs485StopBit') is not None: self.rs485StopBit.v = value['rs485StopBit']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('alarmInterval') is not None: self.alarmInterval.v = value['alarmInterval']


class AlarmIntervalProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'alarmInterval'
        self.name = '告警间隔'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = AlarmIntervalPropertySpecs()
        self.v: int = 0


class AlarmIntervalPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 86400
        self.step = 1
        self.unit = 'S'
        self.unitName = '秒'


class SnProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'sn'
        self.name = '设备sn'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = SnPropertySpecs()
        self.v: str = ''


class SnPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class ModeProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'mode'
        self.name = '控制模式'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = ModePropertySpecs()
        self.v: str = ''


class ModePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ModePropertySpecsOptional()


class ModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.manual = ManualModePropertySpecsOptional()
        self.auto = AutoModePropertySpecsOptional()


class AutoModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'auto'
        self.desc = '自动'


class ManualModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'manual'
        self.desc = '手动'


class OnlineProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'online'
        self.name = '在线状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = OnlinePropertySpecs()
        self.v: int = 0


class OnlinePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OnlinePropertySpecsOptional()


class OnlinePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0OnlinePropertySpecsOptional()
        self.value1 = Value1OnlinePropertySpecsOptional()


class Value1OnlinePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '在线'


class Value0OnlinePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '离线'


class Rs485StopBitProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485StopBit'
        self.name = 'rs485停止位'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = Rs485StopBitPropertySpecs()
        self.v: int = 0


class Rs485StopBitPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = Rs485StopBitPropertySpecsOptional()


class Rs485StopBitPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1Rs485StopBitPropertySpecsOptional()
        self.value2 = Value2Rs485StopBitPropertySpecsOptional()


class Value2Rs485StopBitPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '2停止位'


class Value1Rs485StopBitPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '1停止位'


class Rs485ParityProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485Parity'
        self.name = 'rs485校验位'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = Rs485ParityPropertySpecs()
        self.v: str = ''


class Rs485ParityPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = Rs485ParityPropertySpecsOptional()


class Rs485ParityPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.N = NRs485ParityPropertySpecsOptional()
        self.E = ERs485ParityPropertySpecsOptional()
        self.O = ORs485ParityPropertySpecsOptional()


class ORs485ParityPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'O'
        self.desc = '奇校验'


class ERs485ParityPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'E'
        self.desc = '偶校验'


class NRs485ParityPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'N'
        self.desc = '无校验'


class Rs485DataBitProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485DataBit'
        self.name = 'rs485数据位'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = Rs485DataBitPropertySpecs()
        self.v: int = 0


class Rs485DataBitPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 5
        self.max = 8
        self.step = 1


class Rs485BaundProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485Baund'
        self.name = 'rs485波特率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = Rs485BaundPropertySpecs()
        self.v: int = 0


class Rs485BaundPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1200
        self.max = 19200


class Rs485AddrProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485Addr'
        self.name = 'rs485设备地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class Rs485PortProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485Port'
        self.name = 'rs485端口'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = Rs485PortPropertySpecs()
        self.v: int = 0


class Rs485PortPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 4
        self.step = 1


class YAngleThresholdProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'yAngleThreshold'
        self.name = 'Y轴倾斜阈值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = YAngleThresholdPropertySpecs()
        self.v: float = 0.0


class YAngleThresholdPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -45
        self.max = 45
        self.unit = '°'
        self.unitName = '度'
        self.step = 1


class XAngleThresholdProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'xAngleThreshold'
        self.name = 'X轴倾斜阈值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = XAngleThresholdPropertySpecs()
        self.v: float = 0.0


class XAngleThresholdPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -45
        self.max = 45
        self.unit = '°'
        self.unitName = '度'
        self.step = 1


class YAngleProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'yAngle'
        self.name = 'Y轴倾斜角度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = YAnglePropertySpecs()
        self.v: float = 0.0


class YAnglePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -45
        self.max = 45
        self.unit = '°'
        self.unitName = '度'
        self.step = 1


class XAngleProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'xAngle'
        self.name = 'X轴倾斜角度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = XAnglePropertySpecs()
        self.v: float = 0.0


class XAnglePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -45
        self.max = 45
        self.unit = '°'
        self.unitName = '度'
        self.step = 1
