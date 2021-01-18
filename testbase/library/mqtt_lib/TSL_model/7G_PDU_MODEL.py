from .base_model import *


class QG_PDU(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = '7G_PDU'
        self.productName = '7G光电盒'
        self.properties = Properties()
        self.events = None
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.setOnOff = SetOnOffService()
        self.switchMode = SwitchModeService()
        self.reboot = RebootService()
        self.electricEnergyClear = ElectricEnergyClearService()
        self.channelEnergyClear = ChannelEnergyClearService()


class ChannelEnergyClearService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'channelEnergyClear'
        self.name = '通道电能清零'
        self.accessMode = 'rw'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelEnergyClearServiceSpecs()
        self.v: int = 0


class ChannelEnergyClearServiceSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ChannelEnergyClearServiceSpecsOptional()


class ChannelEnergyClearServiceSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ChannelEnergyClearServiceSpecsOptional()
        self.value2 = Value2ChannelEnergyClearServiceSpecsOptional()
        self.value3 = Value3ChannelEnergyClearServiceSpecsOptional()
        self.value4 = Value4ChannelEnergyClearServiceSpecsOptional()


class Value4ChannelEnergyClearServiceSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 4
        self.desc = '通道'


class Value3ChannelEnergyClearServiceSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '通道'


class Value2ChannelEnergyClearServiceSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '通道'


class Value1ChannelEnergyClearServiceSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '通道'


class ElectricEnergyClearService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'electricEnergyClear'
        self.name = '总电能清零'
        self.parameters = None
        self.output = None


class RebootService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'reboot'
        self.name = '重启'
        self.parameters = None
        self.output = None


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
        self.rs485Addr = Rs485AddrProperty()
        self.rs485Port = Rs485PortProperty()
        self.rs485Baund = Rs485BaundProperty()
        self.rs485DataBit = Rs485DataBitProperty()
        self.rs485Parity = Rs485ParityProperty()
        self.rs485StopBit = Rs485StopBitProperty()
        self.mode = ModeProperty()
        self.voltage = VoltageProperty()
        self.current = CurrentProperty()
        self.totalPower = TotalPowerProperty()
        self.deviceNumber = DeviceNumberProperty()
        self.frequency = FrequencyProperty()
        self.model = ModelProperty()
        self.sn = SnProperty()
        self.online = OnlineProperty()
        self.channelAttritbutes = ChannelAttritbutesProperty()

    @property
    def v(self):
        return {'rs485Addr': self.rs485Addr.v, 'rs485Port': self.rs485Port.v, 'rs485Baund': self.rs485Baund.v, 'rs485DataBit': self.rs485DataBit.v, 'rs485Parity': self.rs485Parity.v, 'rs485StopBit': self.rs485StopBit.v, 'mode': self.mode.v, 'voltage': self.voltage.v, 'current': self.current.v, 'totalPower': self.totalPower.v, 'deviceNumber': self.deviceNumber.v, 'frequency': self.frequency.v, 'model': self.model.v, 'sn': self.sn.v, 'online': self.online.v, 'channelAttritbutes': self.channelAttritbutes.v}

    @v.setter
    def v(self, value):
        if value.get('rs485Addr') is not None: self.rs485Addr.v = value['rs485Addr']
        if value.get('rs485Port') is not None: self.rs485Port.v = value['rs485Port']
        if value.get('rs485Baund') is not None: self.rs485Baund.v = value['rs485Baund']
        if value.get('rs485DataBit') is not None: self.rs485DataBit.v = value['rs485DataBit']
        if value.get('rs485Parity') is not None: self.rs485Parity.v = value['rs485Parity']
        if value.get('rs485StopBit') is not None: self.rs485StopBit.v = value['rs485StopBit']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('voltage') is not None: self.voltage.v = value['voltage']
        if value.get('current') is not None: self.current.v = value['current']
        if value.get('totalPower') is not None: self.totalPower.v = value['totalPower']
        if value.get('deviceNumber') is not None: self.deviceNumber.v = value['deviceNumber']
        if value.get('frequency') is not None: self.frequency.v = value['frequency']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('channelAttritbutes') is not None: self.channelAttritbutes.v = value['channelAttritbutes']


class ChannelAttritbutesProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelAttritbutes'
        self.name = '通道号'
        self.required = True
        self.type = 'struct'
        self.struct = ChannelAttritbutesPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.channel = ChannelChannelAttritbutesPropertyStruct()
        self.onOff = OnOffChannelAttritbutesPropertyStruct()
        self.current = CurrentChannelAttritbutesPropertyStruct()
        self.voltage = VoltageChannelAttritbutesPropertyStruct()
        self.powerFactor = PowerFactorChannelAttritbutesPropertyStruct()
        self.activePower = ActivePowerChannelAttritbutesPropertyStruct()
        self.reactivePower = ReactivePowerChannelAttritbutesPropertyStruct()
        self.activeTotalEnergy = ActiveTotalEnergyChannelAttritbutesPropertyStruct()
        self.activeForwardEnergy = ActiveForwardEnergyChannelAttritbutesPropertyStruct()
        self.activeBackwardEnergy = ActiveBackwardEnergyChannelAttritbutesPropertyStruct()

    @property
    def v(self):
        return {'channel': self.channel.v, 'onOff': self.onOff.v, 'current': self.current.v, 'voltage': self.voltage.v, 'powerFactor': self.powerFactor.v, 'activePower': self.activePower.v, 'reactivePower': self.reactivePower.v, 'activeTotalEnergy': self.activeTotalEnergy.v, 'activeForwardEnergy': self.activeForwardEnergy.v, 'activeBackwardEnergy': self.activeBackwardEnergy.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('onOff') is not None: self.onOff.v = value['onOff']
        if value.get('current') is not None: self.current.v = value['current']
        if value.get('voltage') is not None: self.voltage.v = value['voltage']
        if value.get('powerFactor') is not None: self.powerFactor.v = value['powerFactor']
        if value.get('activePower') is not None: self.activePower.v = value['activePower']
        if value.get('reactivePower') is not None: self.reactivePower.v = value['reactivePower']
        if value.get('activeTotalEnergy') is not None: self.activeTotalEnergy.v = value['activeTotalEnergy']
        if value.get('activeForwardEnergy') is not None: self.activeForwardEnergy.v = value['activeForwardEnergy']
        if value.get('activeBackwardEnergy') is not None: self.activeBackwardEnergy.v = value['activeBackwardEnergy']


class ActiveBackwardEnergyChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.id = 'activeBackwardEnergy'
        self.name = '有功反向电能'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ActiveBackwardEnergyChannelAttritbutesPropertyStructSpecs()
        self.v: int = 0


class ActiveBackwardEnergyChannelAttritbutesPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
        self.unit = 'Wh'
        self.unitName = '瓦时'
        self.step = 1


class ActiveForwardEnergyChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.id = 'activeForwardEnergy'
        self.name = '有功正向电能'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ActiveForwardEnergyChannelAttritbutesPropertyStructSpecs()
        self.v: int = 0


class ActiveForwardEnergyChannelAttritbutesPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
        self.unit = 'Wh'
        self.unitName = '瓦时'
        self.step = 1


class ActiveTotalEnergyChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.id = 'activeTotalEnergy'
        self.name = '有功总电能'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ActiveTotalEnergyChannelAttritbutesPropertyStructSpecs()
        self.v: int = 0


class ActiveTotalEnergyChannelAttritbutesPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
        self.unit = 'Wh'
        self.unitName = '瓦时'
        self.step = 1


class ReactivePowerChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.id = 'reactivePower'
        self.name = '无功功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ReactivePowerChannelAttritbutesPropertyStructSpecs()
        self.v: int = 0


class ReactivePowerChannelAttritbutesPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
        self.unit = 'var'
        self.unitName = '无功功率单位'
        self.step = 1


class ActivePowerChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.id = 'activePower'
        self.name = '有功功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ActivePowerChannelAttritbutesPropertyStructSpecs()
        self.v: int = 0


class ActivePowerChannelAttritbutesPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
        self.unit = 'W'
        self.unitName = '瓦特'
        self.step = 1


class PowerFactorChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.id = 'powerFactor'
        self.name = '功率因素'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = PowerFactorChannelAttritbutesPropertyStructSpecs()
        self.v: int = 0


class PowerFactorChannelAttritbutesPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1000
        self.unit = 'permill'
        self.unitName = '通道功率因数单位'
        self.step = 1


class VoltageChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.id = 'voltage'
        self.name = '电压'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = VoltageChannelAttritbutesPropertyStructSpecs()
        self.v: int = 0


class VoltageChannelAttritbutesPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 220
        self.unit = 'V'
        self.unitName = '伏'
        self.step = 1


class CurrentChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.id = 'current'
        self.name = '电流'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = CurrentChannelAttritbutesPropertyStructSpecs()
        self.v: int = 0


class CurrentChannelAttritbutesPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99
        self.unit = 'A'
        self.unitName = '安培'
        self.step = 1


class OnOffChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.id = 'onOff'
        self.name = '开关状态'
        self.accessMode = 'rw'
        self.required = True
        self.type = 'integer'
        self.specs = OnOffChannelAttritbutesPropertyStructSpecs()
        self.v: int = 0


class OnOffChannelAttritbutesPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OnOffChannelAttritbutesPropertyStructSpecsOptional()


class OnOffChannelAttritbutesPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1OnOffChannelAttritbutesPropertyStructSpecsOptional()
        self.value0 = Value0OnOffChannelAttritbutesPropertyStructSpecsOptional()


class Value0OnOffChannelAttritbutesPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '关'


class Value1OnOffChannelAttritbutesPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开'


class ChannelChannelAttritbutesPropertyStruct:
    def __init__(self) -> None:
        self.id = 'channel'
        self.name = '通道号'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelChannelAttritbutesPropertyStructSpecs()
        self.v: int = 0


class ChannelChannelAttritbutesPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ChannelChannelAttritbutesPropertyStructSpecsOptional()


class ChannelChannelAttritbutesPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0ChannelChannelAttritbutesPropertyStructSpecsOptional()
        self.value1 = Value1ChannelChannelAttritbutesPropertyStructSpecsOptional()
        self.value2 = Value2ChannelChannelAttritbutesPropertyStructSpecsOptional()
        self.value3 = Value3ChannelChannelAttritbutesPropertyStructSpecsOptional()
        self.value4 = Value4ChannelChannelAttritbutesPropertyStructSpecsOptional()


class Value4ChannelChannelAttritbutesPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 4
        self.desc = '通道号'


class Value3ChannelChannelAttritbutesPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '通道号'


class Value2ChannelChannelAttritbutesPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '通道号'


class Value1ChannelChannelAttritbutesPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '通道号'


class Value0ChannelChannelAttritbutesPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '通道号'


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


class SnProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'sn'
        self.name = 'sn序列号'
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


class FrequencyProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'frequency'
        self.name = '频率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = FrequencyPropertySpecs()
        self.v: int = 0


class FrequencyPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = 'Hz'
        self.unitName = '赫兹'
        self.step = 1


class DeviceNumberProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'deviceNumber'
        self.name = '设备编号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = DeviceNumberPropertySpecs()
        self.v: int = 0


class DeviceNumberPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1000
        self.step = 1


class TotalPowerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'totalPower'
        self.name = '总电能功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = TotalPowerPropertySpecs()
        self.v: int = 0


class TotalPowerPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
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
        self.unit = 'V'
        self.unitName = '伏'
        self.step = 1


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
        self.step = 1200


class Rs485PortProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485Port'
        self.name = 'rs485端口'
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
