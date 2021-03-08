from .base_model import *


class S2_SFQ_KQI3SZK(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S2_SFQ_KQI3SZK'
        self.productName = '赛飞奇断路器'
        self.properties = Properties()
        self.events = None
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.setOnOff = SetOnOffService()
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


class SetOnOffService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setOnOff'
        self.name = '设置合分闸'
        self.type = 'business'
        self.parameters = SetOnOffServiceParameters()
        self.output = None


class SetOnOffServiceParameters:
    def __init__(self) -> None:
        self.onOff = OnOffSetOnOffServiceParameter()
        self.channelId = ChannelIdSetOnOffServiceParameter()

    @property
    def v(self):
        return {'onOff': self.onOff.v, 'channelId': self.channelId.v}

    @v.setter
    def v(self, value):
        if value.get('onOff') is not None: self.onOff.v = value['onOff']
        if value.get('channelId') is not None: self.channelId.v = value['channelId']


class ChannelIdSetOnOffServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channelId'
        self.name = '通道号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelIdSetOnOffServiceParameterSpecs()
        self.v: int = 0


class ChannelIdSetOnOffServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 8


class OnOffSetOnOffServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'onOff'
        self.name = '合分闸状态'
        self.accessMode = 'ro'
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
        self.value0 = Value0OnOffSetOnOffServiceParameterSpecsOptional()
        self.value1 = Value1OnOffSetOnOffServiceParameterSpecsOptional()


class Value1OnOffSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '合闸'


class Value0OnOffSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '分闸'


class Properties:
    def __init__(self) -> None:
        self.model = ModelProperty()
        self.sn = SnProperty()
        self.mode = ModeProperty()
        self.subDevCount = SubDevCountProperty()
        self.rs485Port = Rs485PortProperty()
        self.rs485Addr = Rs485AddrProperty()
        self.rs485Baund = Rs485BaundProperty()
        self.rs485DataBit = Rs485DataBitProperty()
        self.rs485Parity = Rs485ParityProperty()
        self.rs485StopBit = Rs485StopBitProperty()
        self.subDevList = SubDevListProperty()

    @property
    def v(self):
        return {'model': self.model.v, 'sn': self.sn.v, 'mode': self.mode.v, 'subDevCount': self.subDevCount.v, 'rs485Port': self.rs485Port.v, 'rs485Addr': self.rs485Addr.v, 'rs485Baund': self.rs485Baund.v, 'rs485DataBit': self.rs485DataBit.v, 'rs485Parity': self.rs485Parity.v, 'rs485StopBit': self.rs485StopBit.v, 'subDevList': self.subDevList.v}

    @v.setter
    def v(self, value):
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('subDevCount') is not None: self.subDevCount.v = value['subDevCount']
        if value.get('rs485Port') is not None: self.rs485Port.v = value['rs485Port']
        if value.get('rs485Addr') is not None: self.rs485Addr.v = value['rs485Addr']
        if value.get('rs485Baund') is not None: self.rs485Baund.v = value['rs485Baund']
        if value.get('rs485DataBit') is not None: self.rs485DataBit.v = value['rs485DataBit']
        if value.get('rs485Parity') is not None: self.rs485Parity.v = value['rs485Parity']
        if value.get('rs485StopBit') is not None: self.rs485StopBit.v = value['rs485StopBit']
        if value.get('subDevList') is not None: self.subDevList.v = value['subDevList']


class SubDevListProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'subDevList'
        self.name = '子设备列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [SubDevListPropertyColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = SubDevListPropertyColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class SubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.channelId = ChannelIdSubDevListPropertyColumnComplexStruct()
        self.online = OnlineSubDevListPropertyColumnComplexStruct()
        self.onOff = OnOffSubDevListPropertyColumnComplexStruct()
        self.overCurrentStatus = OverCurrentStatusSubDevListPropertyColumnComplexStruct()
        self.overVoltageStatus = OverVoltageStatusSubDevListPropertyColumnComplexStruct()
        self.underVoltageStatus = UnderVoltageStatusSubDevListPropertyColumnComplexStruct()
        self.overPowerStatus = OverPowerStatusSubDevListPropertyColumnComplexStruct()
        self.batteryExhausted = BatteryExhaustedSubDevListPropertyColumnComplexStruct()
        self.overTempretureStatus = OverTempretureStatusSubDevListPropertyColumnComplexStruct()
        self.shortCircuitStatus = ShortCircuitStatusSubDevListPropertyColumnComplexStruct()
        self.leakageStatus = LeakageStatusSubDevListPropertyColumnComplexStruct()
        self.current = CurrentSubDevListPropertyColumnComplexStruct()
        self.voltage = VoltageSubDevListPropertyColumnComplexStruct()
        self.leakage = LeakageSubDevListPropertyColumnComplexStruct()
        self.storedTotalBattery = StoredTotalBatterySubDevListPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'channelId': self.channelId.v, 'online': self.online.v, 'onOff': self.onOff.v, 'overCurrentStatus': self.overCurrentStatus.v, 'overVoltageStatus': self.overVoltageStatus.v, 'underVoltageStatus': self.underVoltageStatus.v, 'overPowerStatus': self.overPowerStatus.v, 'batteryExhausted': self.batteryExhausted.v, 'overTempretureStatus': self.overTempretureStatus.v, 'shortCircuitStatus': self.shortCircuitStatus.v, 'leakageStatus': self.leakageStatus.v, 'current': self.current.v, 'voltage': self.voltage.v, 'leakage': self.leakage.v, 'storedTotalBattery': self.storedTotalBattery.v}

    @v.setter
    def v(self, value):
        if value.get('channelId') is not None: self.channelId.v = value['channelId']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('onOff') is not None: self.onOff.v = value['onOff']
        if value.get('overCurrentStatus') is not None: self.overCurrentStatus.v = value['overCurrentStatus']
        if value.get('overVoltageStatus') is not None: self.overVoltageStatus.v = value['overVoltageStatus']
        if value.get('underVoltageStatus') is not None: self.underVoltageStatus.v = value['underVoltageStatus']
        if value.get('overPowerStatus') is not None: self.overPowerStatus.v = value['overPowerStatus']
        if value.get('batteryExhausted') is not None: self.batteryExhausted.v = value['batteryExhausted']
        if value.get('overTempretureStatus') is not None: self.overTempretureStatus.v = value['overTempretureStatus']
        if value.get('shortCircuitStatus') is not None: self.shortCircuitStatus.v = value['shortCircuitStatus']
        if value.get('leakageStatus') is not None: self.leakageStatus.v = value['leakageStatus']
        if value.get('current') is not None: self.current.v = value['current']
        if value.get('voltage') is not None: self.voltage.v = value['voltage']
        if value.get('leakage') is not None: self.leakage.v = value['leakage']
        if value.get('storedTotalBattery') is not None: self.storedTotalBattery.v = value['storedTotalBattery']


class StoredTotalBatterySubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'storedTotalBattery'
        self.name = '保存的总电量'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = StoredTotalBatterySubDevListPropertyColumnComplexStructSpecs()
        self.v: float = 0.0


class StoredTotalBatterySubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 65535
        self.unit = 'W.h'
        self.unitName = '瓦时'
        self.step = 1


class LeakageSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'leakage'
        self.name = '漏电有效值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = LeakageSubDevListPropertyColumnComplexStructSpecs()
        self.v: float = 0.0


class LeakageSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10000
        self.unit = 'mA'
        self.unitName = '毫安'
        self.step = 1


class VoltageSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'voltage'
        self.name = '电压有效值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = VoltageSubDevListPropertyColumnComplexStructSpecs()
        self.v: float = 0.0


class VoltageSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 2800
        self.unit = 'mV'
        self.unitName = '毫伏'
        self.step = 1


class CurrentSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'current'
        self.name = '电流有效值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = CurrentSubDevListPropertyColumnComplexStructSpecs()
        self.v: float = 0.0


class CurrentSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10000
        self.unit = 'mA'
        self.unitName = '毫安'
        self.step = 1


class LeakageStatusSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'leakageStatus'
        self.name = '发生漏电保护'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = LeakageStatusSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class LeakageStatusSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = LeakageStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class LeakageStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1LeakageStatusSubDevListPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0LeakageStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class Value0LeakageStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '否'


class Value1LeakageStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '是'


class ShortCircuitStatusSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'shortCircuitStatus'
        self.name = '发生短路保护'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ShortCircuitStatusSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class ShortCircuitStatusSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ShortCircuitStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class ShortCircuitStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ShortCircuitStatusSubDevListPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0ShortCircuitStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class Value0ShortCircuitStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '否'


class Value1ShortCircuitStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '是'


class OverTempretureStatusSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'overTempretureStatus'
        self.name = '发生过温保护'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = OverTempretureStatusSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class OverTempretureStatusSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OverTempretureStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class OverTempretureStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1OverTempretureStatusSubDevListPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0OverTempretureStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class Value0OverTempretureStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '否'


class Value1OverTempretureStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '是'


class BatteryExhaustedSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'batteryExhausted'
        self.name = '电量用完'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = BatteryExhaustedSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class BatteryExhaustedSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = BatteryExhaustedSubDevListPropertyColumnComplexStructSpecsOptional()


class BatteryExhaustedSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1BatteryExhaustedSubDevListPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0BatteryExhaustedSubDevListPropertyColumnComplexStructSpecsOptional()


class Value0BatteryExhaustedSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '否'


class Value1BatteryExhaustedSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '是'


class OverPowerStatusSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'overPowerStatus'
        self.name = '发生过载保护'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = OverPowerStatusSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class OverPowerStatusSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OverPowerStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class OverPowerStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1OverPowerStatusSubDevListPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0OverPowerStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class Value0OverPowerStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '否'


class Value1OverPowerStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '是'


class UnderVoltageStatusSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'underVoltageStatus'
        self.name = '发生欠压保护'
        self.accessMode = 'ro'
        self.required = False
        self.type = 'integer'
        self.specs = UnderVoltageStatusSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class UnderVoltageStatusSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = UnderVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class UnderVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1UnderVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0UnderVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class Value0UnderVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '否'


class Value1UnderVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '是'


class OverVoltageStatusSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'overVoltageStatus'
        self.name = '发生过压保护'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = OverVoltageStatusSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class OverVoltageStatusSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OverVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class OverVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1OverVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0OverVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class Value0OverVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '否'


class Value1OverVoltageStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '是'


class OverCurrentStatusSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'overCurrentStatus'
        self.name = '发生过流保护'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = OverCurrentStatusSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class OverCurrentStatusSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OverCurrentStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class OverCurrentStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1OverCurrentStatusSubDevListPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0OverCurrentStatusSubDevListPropertyColumnComplexStructSpecsOptional()


class Value0OverCurrentStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '否'


class Value1OverCurrentStatusSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '是'


class OnOffSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'onOff'
        self.name = '开关状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = OnOffSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class OnOffSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OnOffSubDevListPropertyColumnComplexStructSpecsOptional()


class OnOffSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1OnOffSubDevListPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0OnOffSubDevListPropertyColumnComplexStructSpecsOptional()


class Value0OnOffSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '分闸'


class Value1OnOffSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '合闸'


class OnlineSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'online'
        self.name = '通信状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = OnlineSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class OnlineSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OnlineSubDevListPropertyColumnComplexStructSpecsOptional()


class OnlineSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1OnlineSubDevListPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0OnlineSubDevListPropertyColumnComplexStructSpecsOptional()


class Value0OnlineSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '设备离线'


class Value1OnlineSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '设备在线'


class ChannelIdSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelId'
        self.name = '通道号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelIdSubDevListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class ChannelIdSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


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


class Rs485AddrProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485Addr'
        self.name = '设备地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class Rs485PortProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485Port'
        self.name = '485端口'
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


class SubDevCountProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'subDevCount'
        self.name = '连接子设备数量'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = SubDevCountPropertySpecs()
        self.v: int = 0


class SubDevCountPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 8


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
        self.desc = '手动模式'


class AutoModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'auto'
        self.desc = '自动模式'


class SnProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'sn'
        self.name = '设备标识符'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class ModelProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'model'
        self.name = '设备型号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''
