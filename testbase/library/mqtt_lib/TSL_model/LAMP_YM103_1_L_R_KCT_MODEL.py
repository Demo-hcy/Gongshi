from .base_model import *


class YM103_1_L_R_KCT(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'YM103_1_L_R_KCT'
        self.productName = '裕明单灯控制器'
        self.properties = Properties()
        self.events = None
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.setOnOff = SetOnOffService()
        self.setBrightness = SetBrightnessService()
        self.switchMode = SwitchModeService()


class SwitchModeService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'switchMode'
        self.name = '切换控制模式'
        self.parameters = SwitchModeServiceParameters()


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
        self.name = '控制模式'
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
        self.auto = AutoModeSwitchModeServiceParameterSpecsOptional()
        self.manual = ManualModeSwitchModeServiceParameterSpecsOptional()


class ManualModeSwitchModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'manual'
        self.desc = '手动'


class AutoModeSwitchModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'auto'
        self.desc = '自动'


class SetBrightnessService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setBrightness'
        self.name = '设置亮度'
        self.parameters = SetBrightnessServiceParameters()
        self.output = None


class SetBrightnessServiceParameters:
    def __init__(self) -> None:
        self.brightness = BrightnessSetBrightnessServiceParameter()

    @property
    def v(self):
        return {'brightness': self.brightness.v}

    @v.setter
    def v(self, value):
        if value.get('brightness') is not None: self.brightness.v = value['brightness']


class BrightnessSetBrightnessServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'brightness'
        self.name = '亮度'
        self.accessMode = 'rw'
        self.required = True
        self.type = 'integer'
        self.specs = BrightnessSetBrightnessServiceParameterSpecs()
        self.v: int = 0


class BrightnessSetBrightnessServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = '%'
        self.unitName = '百分比'
        self.step = 1


class SetOnOffService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setOnOff'
        self.name = '设置开关'
        self.parameters = SetOnOffServiceParameters()
        self.output = None


class SetOnOffServiceParameters:
    def __init__(self) -> None:
        self.onOff = OnOffSetOnOffServiceParameter()

    @property
    def v(self):
        return {'onOff': self.onOff.v}

    @v.setter
    def v(self, value):
        if value.get('onOff') is not None: self.onOff.v = value['onOff']


class OnOffSetOnOffServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'onOff'
        self.name = '开关'
        self.accessMode = 'rw'
        self.required = True
        self.type = 'integer'
        self.specs = OnOffSetOnOffServiceParameterSpecs()
        self.v: int = 0


class OnOffSetOnOffServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OnOffSetOnOffServiceParameterSpecsOptional()


class OnOffSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1OnOffSetOnOffServiceParameterSpecsOptional()
        self.value0 = Value0OnOffSetOnOffServiceParameterSpecsOptional()


class Value0OnOffSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '关'


class Value1OnOffSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开'


class Properties:
    def __init__(self) -> None:
        self.onOff = OnOffProperty()
        self.rs485Addr = Rs485AddrProperty()
        self.rs485Port = Rs485PortProperty()
        self.rs485Baund = Rs485BaundProperty()
        self.rs485DataBit = Rs485DataBitProperty()
        self.rs485Parity = Rs485ParityProperty()
        self.rs485StopBit = Rs485StopBitProperty()
        self.mode = ModeProperty()
        self.sn = SnProperty()
        self.model = ModelProperty()
        self.online = OnlineProperty()
        self.brightness = BrightnessProperty()
        self.voltage = VoltageProperty()
        self.laekageCurrent = LaekageCurrentProperty()
        self.totalEnergy = TotalEnergyProperty()
        self.versionNumber = VersionNumberProperty()
        self.current = CurrentProperty()
        self.activePower = ActivePowerProperty()

    @property
    def v(self):
        return {'onOff': self.onOff.v, 'rs485Addr': self.rs485Addr.v, 'rs485Port': self.rs485Port.v, 'rs485Baund': self.rs485Baund.v, 'rs485DataBit': self.rs485DataBit.v, 'rs485Parity': self.rs485Parity.v, 'rs485StopBit': self.rs485StopBit.v, 'mode': self.mode.v, 'sn': self.sn.v, 'model': self.model.v, 'online': self.online.v, 'brightness': self.brightness.v, 'voltage': self.voltage.v, 'laekageCurrent': self.laekageCurrent.v, 'totalEnergy': self.totalEnergy.v, 'versionNumber': self.versionNumber.v, 'current': self.current.v, 'activePower': self.activePower.v}

    @v.setter
    def v(self, value):
        if value.get('onOff') is not None: self.onOff.v = value['onOff']
        if value.get('rs485Addr') is not None: self.rs485Addr.v = value['rs485Addr']
        if value.get('rs485Port') is not None: self.rs485Port.v = value['rs485Port']
        if value.get('rs485Baund') is not None: self.rs485Baund.v = value['rs485Baund']
        if value.get('rs485DataBit') is not None: self.rs485DataBit.v = value['rs485DataBit']
        if value.get('rs485Parity') is not None: self.rs485Parity.v = value['rs485Parity']
        if value.get('rs485StopBit') is not None: self.rs485StopBit.v = value['rs485StopBit']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('brightness') is not None: self.brightness.v = value['brightness']
        if value.get('voltage') is not None: self.voltage.v = value['voltage']
        if value.get('laekageCurrent') is not None: self.laekageCurrent.v = value['laekageCurrent']
        if value.get('totalEnergy') is not None: self.totalEnergy.v = value['totalEnergy']
        if value.get('versionNumber') is not None: self.versionNumber.v = value['versionNumber']
        if value.get('current') is not None: self.current.v = value['current']
        if value.get('activePower') is not None: self.activePower.v = value['activePower']


class ActivePowerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'activePower'
        self.name = '功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ActivePowerPropertySpecs()
        self.v: int = 0


class ActivePowerPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99
        self.unit = 'W'
        self.unitName = '瓦特'
        self.step = 1


class CurrentProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'current'
        self.name = '电流'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = CurrentPropertySpecs()
        self.v: int = 0


class CurrentPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99
        self.unit = 'A'
        self.unitName = '安培'
        self.step = 1


class VersionNumberProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'versionNumber'
        self.name = '灯控软件版本号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = VersionNumberPropertySpecs()
        self.v: int = 0


class VersionNumberPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99
        self.step = 1


class TotalEnergyProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'totalEnergy'
        self.name = '总电能'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = TotalEnergyPropertySpecs()
        self.v: int = 0


class TotalEnergyPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1000000
        self.unit = 'Wh'
        self.unitName = '瓦时'
        self.step = 1


class LaekageCurrentProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'laekageCurrent'
        self.name = '漏电流值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = LaekageCurrentPropertySpecs()
        self.v: int = 0


class LaekageCurrentPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99
        self.unit = 'A'
        self.unitName = '漏电安培'
        self.step = 1


class VoltageProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'voltage'
        self.name = '电压'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = VoltagePropertySpecs()
        self.v: int = 0


class VoltagePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 220
        self.unit = 'v'
        self.unitName = '伏'
        self.step = 1


class BrightnessProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'brightness'
        self.name = '灯亮度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = BrightnessPropertySpecs()
        self.v: int = 0


class BrightnessPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = '%'
        self.unitName = '百分值'
        self.step = 1


class OnlineProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'online'
        self.name = '离线在线'
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


class ModelProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'model'
        self.name = '设备model'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = ModelPropertySpecs()
        self.v: str = ''


class ModelPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

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
        self.auto = AutoModePropertySpecsOptional()
        self.manual = ManualModePropertySpecsOptional()


class ManualModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'manual'
        self.desc = '手动'


class AutoModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'auto'
        self.desc = '自动'


class Rs485StopBitProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485StopBit'
        self.name = '停止位'
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
        self.name = '校验位'
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
        self.name = '数据位'
        self.accessMode = 'ro'
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
        self.step = 1200


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
        self.max = 8
        self.step = 1


class Rs485AddrProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485Addr'
        self.name = 'rs485地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class OnOffProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'onOff'
        self.name = '灯状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = OnOffPropertySpecs()
        self.v: int = 0


class OnOffPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OnOffPropertySpecsOptional()


class OnOffPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1OnOffPropertySpecsOptional()
        self.value0 = Value0OnOffPropertySpecsOptional()


class Value0OnOffPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '离线'


class Value1OnOffPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '在线'
