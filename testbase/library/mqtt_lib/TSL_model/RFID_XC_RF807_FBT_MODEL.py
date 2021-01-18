from .base_model import *


class XC_RF807_FBT(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'XC-RF807-FBT'
        self.productName = '远望谷RFID读卡器'
        self.properties = Properties()
        self.events = None
        self.services = Services()


class Services:
    def __init__(self) -> None:
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


class Properties:
    def __init__(self) -> None:
        self.onOff = OnOffProperty()
        self.online = OnlineProperty()
        self.mode = ModeProperty()
        self.SN = SNProperty()
        self.model = ModelProperty()
        self.antennaPort = AntennaPortProperty()
        self.macAddress = MacAddressProperty()
        self.netInfo = NetInfoProperty()
        self.antennaPortPower = AntennaPortPowerProperty()

    @property
    def v(self):
        return {'onOff': self.onOff.v, 'online': self.online.v, 'mode': self.mode.v, 'SN': self.SN.v, 'model': self.model.v, 'antennaPort': self.antennaPort.v, 'macAddress': self.macAddress.v, 'netInfo': self.netInfo.v, 'antennaPortPower': self.antennaPortPower.v}

    @v.setter
    def v(self, value):
        if value.get('onOff') is not None: self.onOff.v = value['onOff']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('SN') is not None: self.SN.v = value['SN']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('antennaPort') is not None: self.antennaPort.v = value['antennaPort']
        if value.get('macAddress') is not None: self.macAddress.v = value['macAddress']
        if value.get('netInfo') is not None: self.netInfo.v = value['netInfo']
        if value.get('antennaPortPower') is not None: self.antennaPortPower.v = value['antennaPortPower']


class AntennaPortPowerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'antennaPortPower'
        self.name = '端口功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = AntennaPortPowerPropertySpecs()
        self.v: int = 0


class AntennaPortPowerPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
        self.unit = 'dbm'
        self.unitName = '分贝毫瓦'
        self.step = 1


class NetInfoProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'netInfo'
        self.name = '以太网信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class MacAddressProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'macAddress'
        self.name = 'MAC地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class AntennaPortProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'antennaPort'
        self.name = '天线端口号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = AntennaPortPropertySpecs()
        self.v: int = 0


class AntennaPortPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 4
        self.step = 1


class ModelProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'model'
        self.name = 'RFID型号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class SNProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'SN'
        self.name = '设备sn'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class ModeProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'mode'
        self.name = '控制模式'
        self.accessMode = 'rw'
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
        self.name = '离线在线'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = OnlinePropertySpecs()
        self.v: str = ''


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


class OnOffProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'onOff'
        self.name = 'RFID状态'
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
        self.desc = '关'


class Value1OnOffPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开'
