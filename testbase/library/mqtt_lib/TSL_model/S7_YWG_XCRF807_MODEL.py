from .base_model import *


class S7_YWG_XCRF807(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S7_YWG_XCRF807'
        self.productName = '远望谷RFID读卡器'
        self.properties = Properties()
        self.events = Events()
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


class Events:
    def __init__(self) -> None:
        self.userData = UserDataEvent()


class UserDataEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'userData'
        self.name = 'rfid读取告警'
        self.parameters = UserDataEventParameters()


class UserDataEventParameters:
    def __init__(self) -> None:
        self.data = DataUserDataEventParameter()
        self.labelTimes = LabelTimesUserDataEventParameter()

    @property
    def v(self):
        return {'data': self.data.v, 'labelTimes': self.labelTimes.v}

    @v.setter
    def v(self, value):
        if value.get('data') is not None: self.data.v = value['data']
        if value.get('labelTimes') is not None: self.labelTimes.v = value['labelTimes']


class LabelTimesUserDataEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'labelTimes'
        self.name = '时间戳'
        self.type = 'integer'
        self.specs = LabelTimesUserDataEventParameterSpecs()
        self.v: int = 0


class LabelTimesUserDataEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class DataUserDataEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'data'
        self.name = '读取类型'
        self.type = 'string'
        self.specs = DataUserDataEventParameterSpecs()
        self.v: str = ''


class DataUserDataEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class Properties:
    def __init__(self) -> None:
        self.online = OnlineProperty()
        self.mode = ModeProperty()
        self.sn = SnProperty()
        self.model = ModelProperty()
        self.antennaPort = AntennaPortProperty()
        self.mac = MacProperty()
        self.labelFiltrationTime = LabelFiltrationTimeProperty()
        self.netInfo = NetInfoProperty()
        self.port = PortProperty()
        self.antennaPortPower = AntennaPortPowerProperty()

    @property
    def v(self):
        return {'online': self.online.v, 'mode': self.mode.v, 'sn': self.sn.v, 'model': self.model.v, 'antennaPort': self.antennaPort.v, 'mac': self.mac.v, 'labelFiltrationTime': self.labelFiltrationTime.v, 'netInfo': self.netInfo.v, 'port': self.port.v, 'antennaPortPower': self.antennaPortPower.v}

    @v.setter
    def v(self, value):
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('antennaPort') is not None: self.antennaPort.v = value['antennaPort']
        if value.get('mac') is not None: self.mac.v = value['mac']
        if value.get('labelFiltrationTime') is not None: self.labelFiltrationTime.v = value['labelFiltrationTime']
        if value.get('netInfo') is not None: self.netInfo.v = value['netInfo']
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('antennaPortPower') is not None: self.antennaPortPower.v = value['antennaPortPower']


class AntennaPortPowerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'antennaPortPower'
        self.name = '端口功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = AntennaPortPowerPropertySpecs()
        self.v: str = ''


class AntennaPortPowerPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class PortProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'port'
        self.name = '端口号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class NetInfoProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'netInfo'
        self.name = '以太网信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [NetInfoPropertyColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = NetInfoPropertyColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class NetInfoPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.ip = IpNetInfoPropertyColumnComplexStruct()
        self.mask = MaskNetInfoPropertyColumnComplexStruct()
        self.gateway = GatewayNetInfoPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'ip': self.ip.v, 'mask': self.mask.v, 'gateway': self.gateway.v}

    @v.setter
    def v(self, value):
        if value.get('ip') is not None: self.ip.v = value['ip']
        if value.get('mask') is not None: self.mask.v = value['mask']
        if value.get('gateway') is not None: self.gateway.v = value['gateway']


class GatewayNetInfoPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'gateway'
        self.name = '网关'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = GatewayNetInfoPropertyColumnComplexStructSpecs()
        self.v: str = ''


class GatewayNetInfoPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class MaskNetInfoPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'mask'
        self.name = '掩码'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = MaskNetInfoPropertyColumnComplexStructSpecs()
        self.v: str = ''


class MaskNetInfoPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class IpNetInfoPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'ip'
        self.name = 'ip地址'
        self.required = True
        self.type = 'string'
        self.specs = IpNetInfoPropertyColumnComplexStructSpecs()
        self.v: str = ''


class IpNetInfoPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class LabelFiltrationTimeProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'labelFiltrationTime'
        self.name = '标签过滤时间'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class MacProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'mac'
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
        self.type = 'string'
        self.specs = AntennaPortPropertySpecs()
        self.v: str = ''


class AntennaPortPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class ModelProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'model'
        self.name = 'RFID型号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class SnProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'sn'
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
