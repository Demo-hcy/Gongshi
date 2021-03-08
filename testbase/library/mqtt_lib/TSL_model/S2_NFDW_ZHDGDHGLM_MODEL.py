from .base_model import *


class S2_NFDW_ZHDGDHGLM(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S2_NFDW_ZHDGDHGLM'
        self.productName = '南网智能电源'
        self.properties = Properties()
        self.events = None
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.setOnOff = SetOnOffService()
        self.switchMode = SwitchModeService()
        self.setHolding = SetHoldingService()


class SetHoldingService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setHolding'
        self.name = '设置通道是否保持'
        self.parameters = SetHoldingServiceParameters()
        self.output = None


class SetHoldingServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelSetHoldingServiceParameter()
        self.status = StatusSetHoldingServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v, 'status': self.status.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('status') is not None: self.status.v = value['status']


class StatusSetHoldingServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'status'
        self.name = '是否保持'
        self.required = True
        self.type = 'integer'
        self.specs = StatusSetHoldingServiceParameterSpecs()
        self.v: int = 0


class StatusSetHoldingServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StatusSetHoldingServiceParameterSpecsOptional()


class StatusSetHoldingServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0StatusSetHoldingServiceParameterSpecsOptional()
        self.value1 = Value1StatusSetHoldingServiceParameterSpecsOptional()


class Value1StatusSetHoldingServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '是'


class Value0StatusSetHoldingServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '否'


class ChannelSetHoldingServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelSetHoldingServiceParameterSpecs()
        self.v: int = 0


class ChannelSetHoldingServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ChannelSetHoldingServiceParameterSpecsOptional()


class ChannelSetHoldingServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ChannelSetHoldingServiceParameterSpecsOptional()
        self.value2 = Value2ChannelSetHoldingServiceParameterSpecsOptional()
        self.value3 = Value3ChannelSetHoldingServiceParameterSpecsOptional()
        self.value5 = Value5ChannelSetHoldingServiceParameterSpecsOptional()
        self.value6 = Value6ChannelSetHoldingServiceParameterSpecsOptional()
        self.value0 = Value0ChannelSetHoldingServiceParameterSpecsOptional()


class Value0ChannelSetHoldingServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '通道0'


class Value6ChannelSetHoldingServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '通道6'


class Value5ChannelSetHoldingServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '通道5'


class Value3ChannelSetHoldingServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '通道3'


class Value2ChannelSetHoldingServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '通道2'


class Value1ChannelSetHoldingServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '通道1'


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
        self.channel = ChannelSetOnOffServiceParameter()

    @property
    def v(self):
        return {'onOff': self.onOff.v, 'channel': self.channel.v}

    @v.setter
    def v(self, value):
        if value.get('onOff') is not None: self.onOff.v = value['onOff']
        if value.get('channel') is not None: self.channel.v = value['channel']


class ChannelSetOnOffServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelSetOnOffServiceParameterSpecs()
        self.v: int = 0


class ChannelSetOnOffServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ChannelSetOnOffServiceParameterSpecsOptional()


class ChannelSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ChannelSetOnOffServiceParameterSpecsOptional()
        self.value2 = Value2ChannelSetOnOffServiceParameterSpecsOptional()
        self.value3 = Value3ChannelSetOnOffServiceParameterSpecsOptional()
        self.value5 = Value5ChannelSetOnOffServiceParameterSpecsOptional()
        self.value6 = Value6ChannelSetOnOffServiceParameterSpecsOptional()
        self.value0 = Value0ChannelSetOnOffServiceParameterSpecsOptional()


class Value0ChannelSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '通道0'


class Value6ChannelSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '通道6'


class Value5ChannelSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '通道5'


class Value3ChannelSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '通道3'


class Value2ChannelSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '通道2'


class Value1ChannelSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '通道1'


class OnOffSetOnOffServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'onOff'
        self.name = '开关'
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
        self.sn = SnProperty()
        self.rs485Addr = Rs485AddrProperty()
        self.rs485Port = Rs485PortProperty()
        self.rs485Baund = Rs485BaundProperty()
        self.rs485DataBit = Rs485DataBitProperty()
        self.rs485Parity = Rs485ParityProperty()
        self.rs485StopBit = Rs485StopBitProperty()
        self.online = OnlineProperty()
        self.mode = ModeProperty()
        self.model = ModelProperty()
        self.systemError = SystemErrorProperty()
        self.hardwareVersion = HardwareVersionProperty()
        self.softwareVersion = SoftwareVersionProperty()
        self.voltage = VoltageProperty()
        self.leakageCurrent = LeakageCurrentProperty()
        self.frequency = FrequencyProperty()
        self.apparentPower = ApparentPowerProperty()
        self.activePower = ActivePowerProperty()
        self.reactivePower = ReactivePowerProperty()
        self.powerFactor = PowerFactorProperty()
        self.activeTotalEnergy = ActiveTotalEnergyProperty()
        self.reactiveTotalEnergy = ReactiveTotalEnergyProperty()
        self.channels = ChannelsProperty()

    @property
    def v(self):
        return {'sn': self.sn.v, 'rs485Addr': self.rs485Addr.v, 'rs485Port': self.rs485Port.v, 'rs485Baund': self.rs485Baund.v, 'rs485DataBit': self.rs485DataBit.v, 'rs485Parity': self.rs485Parity.v, 'rs485StopBit': self.rs485StopBit.v, 'online': self.online.v, 'mode': self.mode.v, 'model': self.model.v, 'systemError': self.systemError.v, 'hardwareVersion': self.hardwareVersion.v, 'softwareVersion': self.softwareVersion.v, 'voltage': self.voltage.v, 'leakageCurrent': self.leakageCurrent.v, 'frequency': self.frequency.v, 'apparentPower': self.apparentPower.v, 'activePower': self.activePower.v, 'reactivePower': self.reactivePower.v, 'powerFactor': self.powerFactor.v, 'activeTotalEnergy': self.activeTotalEnergy.v, 'reactiveTotalEnergy': self.reactiveTotalEnergy.v, 'channels': self.channels.v}

    @v.setter
    def v(self, value):
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('rs485Addr') is not None: self.rs485Addr.v = value['rs485Addr']
        if value.get('rs485Port') is not None: self.rs485Port.v = value['rs485Port']
        if value.get('rs485Baund') is not None: self.rs485Baund.v = value['rs485Baund']
        if value.get('rs485DataBit') is not None: self.rs485DataBit.v = value['rs485DataBit']
        if value.get('rs485Parity') is not None: self.rs485Parity.v = value['rs485Parity']
        if value.get('rs485StopBit') is not None: self.rs485StopBit.v = value['rs485StopBit']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('systemError') is not None: self.systemError.v = value['systemError']
        if value.get('hardwareVersion') is not None: self.hardwareVersion.v = value['hardwareVersion']
        if value.get('softwareVersion') is not None: self.softwareVersion.v = value['softwareVersion']
        if value.get('voltage') is not None: self.voltage.v = value['voltage']
        if value.get('leakageCurrent') is not None: self.leakageCurrent.v = value['leakageCurrent']
        if value.get('frequency') is not None: self.frequency.v = value['frequency']
        if value.get('apparentPower') is not None: self.apparentPower.v = value['apparentPower']
        if value.get('activePower') is not None: self.activePower.v = value['activePower']
        if value.get('reactivePower') is not None: self.reactivePower.v = value['reactivePower']
        if value.get('powerFactor') is not None: self.powerFactor.v = value['powerFactor']
        if value.get('activeTotalEnergy') is not None: self.activeTotalEnergy.v = value['activeTotalEnergy']
        if value.get('reactiveTotalEnergy') is not None: self.reactiveTotalEnergy.v = value['reactiveTotalEnergy']
        if value.get('channels') is not None: self.channels.v = value['channels']


class ChannelsProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channels'
        self.name = '通道属性'
        self.required = True
        self.type = 'array'
        self.columnComplex = [ChannelsPropertyColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ChannelsPropertyColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.channel = ChannelChannelsPropertyColumnComplexStruct()
        self.onOff = OnOffChannelsPropertyColumnComplexStruct()
        self.current = CurrentChannelsPropertyColumnComplexStruct()
        self.voltage = VoltageChannelsPropertyColumnComplexStruct()
        self.leakageCurrent = LeakageCurrentChannelsPropertyColumnComplexStruct()
        self.frequency = FrequencyChannelsPropertyColumnComplexStruct()
        self.apparentPower = ApparentPowerChannelsPropertyColumnComplexStruct()
        self.powerFactor = PowerFactorChannelsPropertyColumnComplexStruct()
        self.activePower = ActivePowerChannelsPropertyColumnComplexStruct()
        self.reactivePower = ReactivePowerChannelsPropertyColumnComplexStruct()
        self.activeTotalEnergy = ActiveTotalEnergyChannelsPropertyColumnComplexStruct()
        self.holding = HoldingChannelsPropertyColumnComplexStruct()
        self.channelError = ChannelErrorChannelsPropertyColumnComplexStruct()
        self.arcError = ArcErrorChannelsPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'channel': self.channel.v, 'onOff': self.onOff.v, 'current': self.current.v, 'voltage': self.voltage.v, 'leakageCurrent': self.leakageCurrent.v, 'frequency': self.frequency.v, 'apparentPower': self.apparentPower.v, 'powerFactor': self.powerFactor.v, 'activePower': self.activePower.v, 'reactivePower': self.reactivePower.v, 'activeTotalEnergy': self.activeTotalEnergy.v, 'holding': self.holding.v, 'channelError': self.channelError.v, 'arcError': self.arcError.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('onOff') is not None: self.onOff.v = value['onOff']
        if value.get('current') is not None: self.current.v = value['current']
        if value.get('voltage') is not None: self.voltage.v = value['voltage']
        if value.get('leakageCurrent') is not None: self.leakageCurrent.v = value['leakageCurrent']
        if value.get('frequency') is not None: self.frequency.v = value['frequency']
        if value.get('apparentPower') is not None: self.apparentPower.v = value['apparentPower']
        if value.get('powerFactor') is not None: self.powerFactor.v = value['powerFactor']
        if value.get('activePower') is not None: self.activePower.v = value['activePower']
        if value.get('reactivePower') is not None: self.reactivePower.v = value['reactivePower']
        if value.get('activeTotalEnergy') is not None: self.activeTotalEnergy.v = value['activeTotalEnergy']
        if value.get('holding') is not None: self.holding.v = value['holding']
        if value.get('channelError') is not None: self.channelError.v = value['channelError']
        if value.get('arcError') is not None: self.arcError.v = value['arcError']


class ArcErrorChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'arcError'
        self.name = '线路电弧故障状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.specs = ArcErrorChannelsPropertyColumnComplexStructSpecs()
        self.v: bool = True


class ArcErrorChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class ChannelErrorChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelError'
        self.name = '通道异常'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnSimple = [ChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.specs = ChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecs()
        self.v: str = ''


class ChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()


class ChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.lostVoltage = LostVoltageChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.underVoltage = UnderVoltageChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.overVoltage = OverVoltageChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.lostCurrent = LostCurrentChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.overCurrent = OverCurrentChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.overLoad = OverLoadChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.reverse = ReverseChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.lostPhase = LostPhaseChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.activeExcess = ActiveExcessChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.reactiveExcess = ReactiveExcessChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.powerExceed = PowerExceedChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.cutCurrent = CutCurrentChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.shortCircuit = ShortCircuitChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.inShortCircuit = InShortCircuitChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()
        self.leakage = LeakageChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional()


class LeakageChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'leakage'
        self.desc = '零序超限'


class InShortCircuitChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'inShortCircuit'
        self.desc = '瞬时短路'


class ShortCircuitChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'shortCircuit'
        self.desc = '短路'


class CutCurrentChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'cutCurrent'
        self.desc = '断流'


class PowerExceedChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'powerExceed'
        self.desc = '功率因数超下限'


class ReactiveExcessChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'reactiveExcess'
        self.desc = '无功超需量'


class ActiveExcessChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'activeExcess'
        self.desc = '有功超需量'


class LostPhaseChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'lostPhase'
        self.desc = '断相'


class ReverseChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'reverse'
        self.desc = '潮流反向'


class OverLoadChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'overLoad'
        self.desc = '过载'


class OverCurrentChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'overCurrent'
        self.desc = '过流'


class LostCurrentChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'lostCurrent'
        self.desc = '失流'


class OverVoltageChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'overVoltage'
        self.desc = '过压'


class UnderVoltageChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'underVoltage'
        self.desc = '欠压'


class LostVoltageChannelErrorChannelsPropertyColumnComplexStructColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'lostVoltage'
        self.desc = '失压'


class HoldingChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'holding'
        self.name = '通道保持'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.specs = HoldingChannelsPropertyColumnComplexStructSpecs()
        self.v: bool = True


class HoldingChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class ActiveTotalEnergyChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'activeTotalEnergy'
        self.name = '有功总电能'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ActiveTotalEnergyChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class ActiveTotalEnergyChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'Wh'
        self.unitName = '瓦时'


class ReactivePowerChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'reactivePower'
        self.name = '无功功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ReactivePowerChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class ReactivePowerChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'var'
        self.unitName = '无功功率单位'


class ActivePowerChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'activePower'
        self.name = '有功功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ActivePowerChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class ActivePowerChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'W'
        self.unitName = '瓦特'


class PowerFactorChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'powerFactor'
        self.name = '功率因素'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = PowerFactorChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class PowerFactorChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'permill'
        self.unitName = '通道功率因数单位'


class ApparentPowerChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'apparentPower'
        self.name = '视在功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ApparentPowerChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class ApparentPowerChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'W'
        self.unitName = '瓦'


class FrequencyChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'frequency'
        self.name = '频率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = FrequencyChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class FrequencyChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'Hz'
        self.unitName = '赫兹'


class LeakageCurrentChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'leakageCurrent'
        self.name = '漏电电流值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = LeakageCurrentChannelsPropertyColumnComplexStructSpecs()
        self.v: float = 0.0


class LeakageCurrentChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'mA'
        self.unitName = '毫安'


class VoltageChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'voltage'
        self.name = '电压'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = VoltageChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class VoltageChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'mV'
        self.unitName = '毫伏'


class CurrentChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'current'
        self.name = '电流'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = CurrentChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class CurrentChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unitName = '安培'


class OnOffChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'onOff'
        self.name = '开关状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = OnOffChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class OnOffChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OnOffChannelsPropertyColumnComplexStructSpecsOptional()


class OnOffChannelsPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1OnOffChannelsPropertyColumnComplexStructSpecsOptional()
        self.value0 = Value0OnOffChannelsPropertyColumnComplexStructSpecsOptional()


class Value0OnOffChannelsPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '关'


class Value1OnOffChannelsPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开'


class ChannelChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channel'
        self.name = '通道号'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class ChannelChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ChannelChannelsPropertyColumnComplexStructSpecsOptional()


class ChannelChannelsPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0ChannelChannelsPropertyColumnComplexStructSpecsOptional()
        self.value1 = Value1ChannelChannelsPropertyColumnComplexStructSpecsOptional()
        self.value2 = Value2ChannelChannelsPropertyColumnComplexStructSpecsOptional()
        self.value3 = Value3ChannelChannelsPropertyColumnComplexStructSpecsOptional()
        self.value5 = Value5ChannelChannelsPropertyColumnComplexStructSpecsOptional()
        self.value6 = Value6ChannelChannelsPropertyColumnComplexStructSpecsOptional()


class Value6ChannelChannelsPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '通道6'


class Value5ChannelChannelsPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '通道5'


class Value3ChannelChannelsPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '通道3'


class Value2ChannelChannelsPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '通道2'


class Value1ChannelChannelsPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '通道1'


class Value0ChannelChannelsPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '通道0'


class ReactiveTotalEnergyProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'reactiveTotalEnergy'
        self.name = '无功总电能'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ReactiveTotalEnergyPropertySpecs()
        self.v: int = 0


class ReactiveTotalEnergyPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'Wh'
        self.unitName = '瓦时'


class ActiveTotalEnergyProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'activeTotalEnergy'
        self.name = '有功总电能'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ActiveTotalEnergyPropertySpecs()
        self.v: int = 0


class ActiveTotalEnergyPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'Wh'
        self.unitName = '瓦时'


class PowerFactorProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'powerFactor'
        self.name = '功率因数'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = PowerFactorPropertySpecs()
        self.v: int = 0


class PowerFactorPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'permill'
        self.unitName = '通道功率因数单位'


class ReactivePowerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'reactivePower'
        self.name = '无功功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ReactivePowerPropertySpecs()
        self.v: int = 0


class ReactivePowerPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'Var'
        self.unitName = '无功功率单位'


class ActivePowerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'activePower'
        self.name = '有功功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ActivePowerPropertySpecs()
        self.v: int = 0


class ActivePowerPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'W'
        self.unitName = '瓦'


class ApparentPowerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'apparentPower'
        self.name = '视在功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ApparentPowerPropertySpecs()
        self.v: int = 0


class ApparentPowerPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'W'
        self.unitName = '瓦'


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
        self.unit = 'Hz'
        self.unitName = '赫兹'


class LeakageCurrentProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'leakageCurrent'
        self.name = '漏电电流值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = LeakageCurrentPropertySpecs()
        self.v: int = 0


class LeakageCurrentPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'mA'
        self.unitName = '毫安'


class VoltageProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'voltage'
        self.name = '电压值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = VoltagePropertySpecs()
        self.v: int = 0


class VoltagePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'mV'
        self.unitName = '毫伏'


class SoftwareVersionProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'softwareVersion'
        self.name = '设备软件版本'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = SoftwareVersionPropertySpecs()
        self.v: str = ''


class SoftwareVersionPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class HardwareVersionProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'hardwareVersion'
        self.name = '设备硬件版本'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = HardwareVersionPropertySpecs()
        self.v: str = ''


class HardwareVersionPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class SystemErrorProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'systemError'
        self.name = '系统异常'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnSimple = [SystemErrorPropertyColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = SystemErrorPropertyColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class SystemErrorPropertyColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.specs = SystemErrorPropertyColumnSimpleStructSpecs()
        self.v: str = ''


class SystemErrorPropertyColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = SystemErrorPropertyColumnSimpleStructSpecsOptional()


class SystemErrorPropertyColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.DS18B20_2_ERROR = DS18B20_2_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional()
        self.DS18B20_1_ERROR = DS18B20_1_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional()
        self.FLASH_ERROR = FLASH_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional()
        self.RAM_ERROR = RAM_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional()
        self.CLOCK_ERROR = CLOCK_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional()
        self.EEPROM_ERROR = EEPROM_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional()


class EEPROM_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'EEPROM_ERROR'
        self.desc = 'EEPROM错误'


class CLOCK_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'CLOCK_ERROR'
        self.desc = '硬时钟芯片故障'


class RAM_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'RAM_ERROR'
        self.desc = '内部RAM错误'


class FLASH_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'FLASH_ERROR'
        self.desc = '外部FLASH错误'


class DS18B20_1_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'DS18B20_1_ERROR'
        self.desc = 'DS18B20_1故障'


class DS18B20_2_ERRORSystemErrorPropertyColumnSimpleStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'DS18B20_2_ERROR'
        self.desc = 'DS18B20_2故障'


class ModelProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'model'
        self.name = '设备型号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = ModelPropertySpecs()
        self.v: str = ''


class ModelPropertySpecs(BaseSpecs):
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
        self.specs = Rs485AddrPropertySpecs()
        self.v: str = ''


class Rs485AddrPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class SnProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'sn'
        self.name = '设备sn号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = SnPropertySpecs()
        self.v: str = ''


class SnPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass