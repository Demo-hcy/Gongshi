from .base_model import *


class ZCT245RD_LBQ_E2_77(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'ZCT245RD-LBQ-E2-77'
        self.productName = '直川倾斜传感器'
        self.properties = Properties()
        self.events = Events()
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.setZeroMode = SetZeroModeService()
        self.setXAlarmAngle = SetXAlarmAngleService()
        self.setYAlarmAngle = SetYAlarmAngleService()
        self.setXAlarmFrequency = SetXAlarmFrequencyService()
        self.setYAlarmFrequency = SetYAlarmFrequencyService()
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
        self.accessMode = 'ro'
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


class SetYAlarmFrequencyService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setYAlarmFrequency'
        self.name = '设置y轴告警重复上报频率'
        self.type = 'business'
        self.parameters = SetYAlarmFrequencyServiceParameters()
        self.output = None


class SetYAlarmFrequencyServiceParameters:
    def __init__(self) -> None:
        self.frequency = FrequencySetYAlarmFrequencyServiceParameter()

    @property
    def v(self):
        return {'frequency': self.frequency.v}

    @v.setter
    def v(self, value):
        if value.get('frequency') is not None: self.frequency.v = value['frequency']


class FrequencySetYAlarmFrequencyServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'frequency'
        self.name = 'Y轴告警频率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = FrequencySetYAlarmFrequencyServiceParameterSpecs()
        self.v: int = 0


class FrequencySetYAlarmFrequencyServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 86400
        self.unit = 's'
        self.unitName = '秒'
        self.step = 1


class SetXAlarmFrequencyService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setXAlarmFrequency'
        self.name = '设置X轴告警重复上报频率'
        self.type = 'business'
        self.parameters = SetXAlarmFrequencyServiceParameters()
        self.output = None


class SetXAlarmFrequencyServiceParameters:
    def __init__(self) -> None:
        self.frequency = FrequencySetXAlarmFrequencyServiceParameter()

    @property
    def v(self):
        return {'frequency': self.frequency.v}

    @v.setter
    def v(self, value):
        if value.get('frequency') is not None: self.frequency.v = value['frequency']


class FrequencySetXAlarmFrequencyServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'frequency'
        self.name = 'X轴告警频率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = FrequencySetXAlarmFrequencyServiceParameterSpecs()
        self.v: int = 0


class FrequencySetXAlarmFrequencyServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 86400
        self.unit = 's'
        self.unitName = '秒'
        self.step = 1


class SetYAlarmAngleService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setYAlarmAngle'
        self.name = '设置y轴倾斜阈值'
        self.type = 'business'
        self.parameters = SetYAlarmAngleServiceParameters()
        self.output = None


class SetYAlarmAngleServiceParameters:
    def __init__(self) -> None:
        self.yAlarmAngle = YAlarmAngleSetYAlarmAngleServiceParameter()

    @property
    def v(self):
        return {'yAlarmAngle': self.yAlarmAngle.v}

    @v.setter
    def v(self, value):
        if value.get('yAlarmAngle') is not None: self.yAlarmAngle.v = value['yAlarmAngle']


class YAlarmAngleSetYAlarmAngleServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'yAlarmAngle'
        self.name = 'y轴倾斜阈值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = YAlarmAngleSetYAlarmAngleServiceParameterSpecs()
        self.v: float = 0.0


class YAlarmAngleSetYAlarmAngleServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -45
        self.max = 45
        self.unit = '°'
        self.unitName = '度'
        self.step = 1


class SetXAlarmAngleService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setXAlarmAngle'
        self.name = '设置x轴倾斜阈值'
        self.type = 'business'
        self.parameters = SetXAlarmAngleServiceParameters()
        self.output = None


class SetXAlarmAngleServiceParameters:
    def __init__(self) -> None:
        self.xAlarmAngle = XAlarmAngleSetXAlarmAngleServiceParameter()

    @property
    def v(self):
        return {'xAlarmAngle': self.xAlarmAngle.v}

    @v.setter
    def v(self, value):
        if value.get('xAlarmAngle') is not None: self.xAlarmAngle.v = value['xAlarmAngle']


class XAlarmAngleSetXAlarmAngleServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'xAlarmAngle'
        self.name = 'x轴倾斜阈值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = XAlarmAngleSetXAlarmAngleServiceParameterSpecs()
        self.v: float = 0.0


class XAlarmAngleSetXAlarmAngleServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -45
        self.max = 45
        self.unit = '°'
        self.unitName = '度'
        self.step = 1


class SetZeroModeService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setZeroMode'
        self.name = '设置零点模式'
        self.type = 'business'
        self.parameters = SetZeroModeServiceParameters()
        self.output = None


class SetZeroModeServiceParameters:
    def __init__(self) -> None:
        self.zeroMode = ZeroModeSetZeroModeServiceParameter()

    @property
    def v(self):
        return {'zeroMode': self.zeroMode.v}

    @v.setter
    def v(self, value):
        if value.get('zeroMode') is not None: self.zeroMode.v = value['zeroMode']


class ZeroModeSetZeroModeServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'zeroMode'
        self.name = '零点模式'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ZeroModeSetZeroModeServiceParameterSpecs()
        self.v: int = 0


class ZeroModeSetZeroModeServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ZeroModeSetZeroModeServiceParameterSpecsOptional()


class ZeroModeSetZeroModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0ZeroModeSetZeroModeServiceParameterSpecsOptional()
        self.value1 = Value1ZeroModeSetZeroModeServiceParameterSpecsOptional()


class Value1ZeroModeSetZeroModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '零点模式'


class Value0ZeroModeSetZeroModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '绝对模式'


class Events:
    def __init__(self) -> None:
        self.xAlarmStart = XAlarmStartEvent()
        self.xAlarmStop = XAlarmStopEvent()
        self.yAlarmStart = YAlarmStartEvent()
        self.yAlarmStop = YAlarmStopEvent()


class YAlarmStopEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'yAlarmStop'
        self.name = 'y轴倾斜告警结束'
        self.parameters = None


class YAlarmStartEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'yAlarmStart'
        self.name = 'y轴倾斜告警开始'
        self.parameters = None


class XAlarmStopEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'xAlarmStop'
        self.name = 'x轴倾斜告警结束'
        self.parameters = None


class XAlarmStartEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'xAlarmStart'
        self.name = 'x轴倾斜告警开始'
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
        self.sn = SnProperty()

    @property
    def v(self):
        return {'xAngle': self.xAngle.v, 'yAngle': self.yAngle.v, 'xAngleThreshold': self.xAngleThreshold.v, 'yAngleThreshold': self.yAngleThreshold.v, 'rs485Port': self.rs485Port.v, 'rs485Addr': self.rs485Addr.v, 'rs485Baund': self.rs485Baund.v, 'rs485DataBit': self.rs485DataBit.v, 'rs485Parity': self.rs485Parity.v, 'rs485StopBit': self.rs485StopBit.v, 'online': self.online.v, 'sn': self.sn.v}

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
        if value.get('sn') is not None: self.sn.v = value['sn']


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

class OnlineProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'online'
        self.name = '在线状态'
        self.accessMode = 'rw'
        self.required = False
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
        self.name = '停止位'
        self.accessMode = 'rw'
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
        self.name = '校验位'
        self.accessMode = 'rw'
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
        self.name = '数据位'
        self.accessMode = 'rw'
        self.required = True
        self.type = 'integer'
        self.specs = Rs485DataBitPropertySpecs()
        self.v: int = 0


class Rs485DataBitPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = Rs485DataBitPropertySpecsOptional()


class Rs485DataBitPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value6 = Value6Rs485DataBitPropertySpecsOptional()
        self.value7 = Value7Rs485DataBitPropertySpecsOptional()
        self.value8 = Value8Rs485DataBitPropertySpecsOptional()


class Value8Rs485DataBitPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 8
        self.desc = '8数据位'


class Value7Rs485DataBitPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 7
        self.desc = '7数据位'


class Value6Rs485DataBitPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '6数据位'


class Rs485BaundProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485Baund'
        self.name = '波特率'
        self.accessMode = 'rw'
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
        self.name = '设备地址'
        self.accessMode = 'rw'
        self.required = True
        self.type = 'integer'
        self.specs = Rs485AddrPropertySpecs()
        self.v: int = 0


class Rs485AddrPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 255


class Rs485PortProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485Port'
        self.name = '485端口'
        self.accessMode = 'rw'
        self.required = True
        self.type = 'integer'
        self.specs = Rs485PortPropertySpecs()
        self.v: int = 0


class Rs485PortPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 8


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
