from .base_model import *


class QG_ZNDY_001(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = '7G-ZNDY-001'
        self.productName = '智慧灯杆电源'
        self.properties = Properties()
        self.events = None
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.setOnOff = SetOnOffService()
        self.setChannelOnOff = SetChannelOnOffService()
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
        self.status = StatusSetHoldingServiceParameter()

    @property
    def v(self):
        return {'status': self.status.v}

    @v.setter
    def v(self, value):
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


class SetChannelOnOffService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setChannelOnOff'
        self.name = '开关智能电源'
        self.parameters = SetChannelOnOffServiceParameters()
        self.output = None


class SetChannelOnOffServiceParameters:
    def __init__(self) -> None:
        self.onOff = OnOffSetChannelOnOffServiceParameter()
        self.channel = ChannelSetChannelOnOffServiceParameter()

    @property
    def v(self):
        return {'onOff': self.onOff.v, 'channel': self.channel.v}

    @v.setter
    def v(self, value):
        if value.get('onOff') is not None: self.onOff.v = value['onOff']
        if value.get('channel') is not None: self.channel.v = value['channel']


class ChannelSetChannelOnOffServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelSetChannelOnOffServiceParameterSpecs()
        self.v: int = 0


class ChannelSetChannelOnOffServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ChannelSetChannelOnOffServiceParameterSpecsOptional()


class ChannelSetChannelOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0ChannelSetChannelOnOffServiceParameterSpecsOptional()
        self.value1 = Value1ChannelSetChannelOnOffServiceParameterSpecsOptional()
        self.value2 = Value2ChannelSetChannelOnOffServiceParameterSpecsOptional()
        self.value3 = Value3ChannelSetChannelOnOffServiceParameterSpecsOptional()
        self.value5 = Value5ChannelSetChannelOnOffServiceParameterSpecsOptional()
        self.value6 = Value6ChannelSetChannelOnOffServiceParameterSpecsOptional()


class Value6ChannelSetChannelOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '通道号'


class Value5ChannelSetChannelOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '通道号'


class Value3ChannelSetChannelOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '通道号'


class Value2ChannelSetChannelOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '通道号'


class Value1ChannelSetChannelOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '通道号'


class Value0ChannelSetChannelOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '通道号'


class OnOffSetChannelOnOffServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'onOff'
        self.name = '开关'
        self.required = True
        self.type = 'integer'
        self.specs = OnOffSetChannelOnOffServiceParameterSpecs()
        self.v: int = 0


class OnOffSetChannelOnOffServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OnOffSetChannelOnOffServiceParameterSpecsOptional()


class OnOffSetChannelOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0OnOffSetChannelOnOffServiceParameterSpecsOptional()
        self.value1 = Value1OnOffSetChannelOnOffServiceParameterSpecsOptional()


class Value1OnOffSetChannelOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开'


class Value0OnOffSetChannelOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '关'


class SetOnOffService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setOnOff'
        self.name = '开关智能电源'
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
        self.required = True
        self.type = 'string'
        self.specs = OnOffSetOnOffServiceParameterSpecs()
        self.v: str = ''


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
        self.desc = '开'


class Value0OnOffSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '关'


class Properties:
    def __init__(self) -> None:
        self.SN = SNProperty()
        self.rs485Addr = Rs485AddrProperty()
        self.rs485Port = Rs485PortProperty()
        self.rs485Baund = Rs485BaundProperty()
        self.rs485DataBit = Rs485DataBitProperty()
        self.rs485Parity = Rs485ParityProperty()
        self.rs485StopBit = Rs485StopBitProperty()
        self.mode = ModeProperty()
        self.channelNumber = ChannelNumberProperty()
        self.model = ModelProperty()
        self.systemError = SystemErrorProperty()
        self.channelError = ChannelErrorProperty()
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
        self.channelVoltage = ChannelVoltageProperty()
        self.channelLeakageCurrent = ChannelLeakageCurrentProperty()
        self.channelApparentPower = ChannelApparentPowerProperty()
        self.channelActivePower = ChannelActivePowerProperty()
        self.channelReactivePower = ChannelReactivePowerProperty()
        self.channelPowerFactor = ChannelPowerFactorProperty()
        self.channelActiveTotalEnergy = ChannelActiveTotalEnergyProperty()
        self.channelReactiveTotalEnergy = ChannelReactiveTotalEnergyProperty()
        self.channelCurrent = ChannelCurrentProperty()
        self.channelArcError = ChannelArcErrorProperty()
        self.channelHolding = ChannelHoldingProperty()
        self.channelOnOff = ChannelOnOffProperty()
        self.channelChannelError = ChannelChannelErrorProperty()

    @property
    def v(self):
        return {'SN': self.SN.v, 'rs485Addr': self.rs485Addr.v, 'rs485Port': self.rs485Port.v, 'rs485Baund': self.rs485Baund.v, 'rs485DataBit': self.rs485DataBit.v, 'rs485Parity': self.rs485Parity.v, 'rs485StopBit': self.rs485StopBit.v, 'mode': self.mode.v, 'channelNumber': self.channelNumber.v, 'model': self.model.v, 'systemError': self.systemError.v, 'channelError': self.channelError.v, 'hardwareVersion': self.hardwareVersion.v, 'softwareVersion': self.softwareVersion.v, 'voltage': self.voltage.v, 'leakageCurrent': self.leakageCurrent.v, 'frequency': self.frequency.v, 'apparentPower': self.apparentPower.v, 'activePower': self.activePower.v, 'reactivePower': self.reactivePower.v, 'powerFactor': self.powerFactor.v, 'activeTotalEnergy': self.activeTotalEnergy.v, 'reactiveTotalEnergy': self.reactiveTotalEnergy.v, 'channelVoltage': self.channelVoltage.v, 'channelLeakageCurrent': self.channelLeakageCurrent.v, 'channelApparentPower': self.channelApparentPower.v, 'channelActivePower': self.channelActivePower.v, 'channelReactivePower': self.channelReactivePower.v, 'channelPowerFactor': self.channelPowerFactor.v, 'channelActiveTotalEnergy': self.channelActiveTotalEnergy.v, 'channelReactiveTotalEnergy': self.channelReactiveTotalEnergy.v, 'channelCurrent': self.channelCurrent.v, 'channelArcError': self.channelArcError.v, 'channelHolding': self.channelHolding.v, 'channelOnOff': self.channelOnOff.v, 'channelChannelError': self.channelChannelError.v}

    @v.setter
    def v(self, value):
        if value.get('SN') is not None: self.SN.v = value['SN']
        if value.get('rs485Addr') is not None: self.rs485Addr.v = value['rs485Addr']
        if value.get('rs485Port') is not None: self.rs485Port.v = value['rs485Port']
        if value.get('rs485Baund') is not None: self.rs485Baund.v = value['rs485Baund']
        if value.get('rs485DataBit') is not None: self.rs485DataBit.v = value['rs485DataBit']
        if value.get('rs485Parity') is not None: self.rs485Parity.v = value['rs485Parity']
        if value.get('rs485StopBit') is not None: self.rs485StopBit.v = value['rs485StopBit']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('channelNumber') is not None: self.channelNumber.v = value['channelNumber']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('systemError') is not None: self.systemError.v = value['systemError']
        if value.get('channelError') is not None: self.channelError.v = value['channelError']
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
        if value.get('channelVoltage') is not None: self.channelVoltage.v = value['channelVoltage']
        if value.get('channelLeakageCurrent') is not None: self.channelLeakageCurrent.v = value['channelLeakageCurrent']
        if value.get('channelApparentPower') is not None: self.channelApparentPower.v = value['channelApparentPower']
        if value.get('channelActivePower') is not None: self.channelActivePower.v = value['channelActivePower']
        if value.get('channelReactivePower') is not None: self.channelReactivePower.v = value['channelReactivePower']
        if value.get('channelPowerFactor') is not None: self.channelPowerFactor.v = value['channelPowerFactor']
        if value.get('channelActiveTotalEnergy') is not None: self.channelActiveTotalEnergy.v = value['channelActiveTotalEnergy']
        if value.get('channelReactiveTotalEnergy') is not None: self.channelReactiveTotalEnergy.v = value['channelReactiveTotalEnergy']
        if value.get('channelCurrent') is not None: self.channelCurrent.v = value['channelCurrent']
        if value.get('channelArcError') is not None: self.channelArcError.v = value['channelArcError']
        if value.get('channelHolding') is not None: self.channelHolding.v = value['channelHolding']
        if value.get('channelOnOff') is not None: self.channelOnOff.v = value['channelOnOff']
        if value.get('channelChannelError') is not None: self.channelChannelError.v = value['channelChannelError']


class ChannelChannelErrorProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelChannelError'
        self.name = 'channel通道异常'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = ChannelChannelErrorPropertySpecs()
        self.v: str = ''


class ChannelChannelErrorPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ChannelChannelErrorPropertySpecsOptional()


class ChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.lostVoltage = LostVoltageChannelChannelErrorPropertySpecsOptional()
        self.underVoltage = UnderVoltageChannelChannelErrorPropertySpecsOptional()
        self.overVoltage = OverVoltageChannelChannelErrorPropertySpecsOptional()
        self.lostCurrent = LostCurrentChannelChannelErrorPropertySpecsOptional()
        self.overCurrent = OverCurrentChannelChannelErrorPropertySpecsOptional()
        self.overLoad = OverLoadChannelChannelErrorPropertySpecsOptional()
        self.reverse = ReverseChannelChannelErrorPropertySpecsOptional()
        self.lostPhase = LostPhaseChannelChannelErrorPropertySpecsOptional()
        self.cutCurrent = CutCurrentChannelChannelErrorPropertySpecsOptional()
        self.activeExcess = ActiveExcessChannelChannelErrorPropertySpecsOptional()
        self.reactiveExcess = ReactiveExcessChannelChannelErrorPropertySpecsOptional()
        self.powerExceed = PowerExceedChannelChannelErrorPropertySpecsOptional()
        self.cutCurrent = CutCurrentChannelChannelErrorPropertySpecsOptional()
        self.shortCircuit = ShortCircuitChannelChannelErrorPropertySpecsOptional()
        self.inShortCircuit = InShortCircuitChannelChannelErrorPropertySpecsOptional()
        self.leakage = LeakageChannelChannelErrorPropertySpecsOptional()


class LeakageChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'leakage'
        self.desc = 'leakage'


class InShortCircuitChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'inShortCircuit'
        self.desc = 'inShortCircuit'


class ShortCircuitChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'shortCircuit'
        self.desc = 'shortCircuit'


class PowerExceedChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'powerExceed'
        self.desc = 'powerExceed'


class ReactiveExcessChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'reactiveExcess'
        self.desc = 'reactiveExcess'


class ActiveExcessChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'activeExcess'
        self.desc = 'activeExcess'


class CutCurrentChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'cutCurrent'
        self.desc = 'cutCurrent'


class LostPhaseChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'lostPhase'
        self.desc = 'lostPhase'


class ReverseChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'reverse'
        self.desc = 'reverse'


class OverLoadChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'overLoad'
        self.desc = 'overLoad'


class OverCurrentChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'overCurrent'
        self.desc = 'overCurrent'


class LostCurrentChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'lostCurrent'
        self.desc = 'lostCurrent'


class OverVoltageChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'overVoltage'
        self.desc = 'overVoltage'


class UnderVoltageChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'underVoltage'
        self.desc = 'underVoltage'


class LostVoltageChannelChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'lostVoltage'
        self.desc = 'lostVoltage'


class ChannelOnOffProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelOnOff'
        self.name = '开关状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.specs = ChannelOnOffPropertySpecs()
        self.v: bool = True


class ChannelOnOffPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class ChannelHoldingProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelHolding'
        self.name = '通道保持'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.specs = ChannelHoldingPropertySpecs()
        self.v: bool = True


class ChannelHoldingPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class ChannelArcErrorProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelArcError'
        self.name = '通道线路电弧故障状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.specs = ChannelArcErrorPropertySpecs()
        self.v: bool = True


class ChannelArcErrorPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class ChannelCurrentProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelCurrent'
        self.name = '通道电流值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelCurrentPropertySpecs()
        self.v: int = 0


class ChannelCurrentPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
        self.unit = 'mA'
        self.unitName = '毫安'
        self.step = 1


class ChannelReactiveTotalEnergyProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelReactiveTotalEnergy'
        self.name = '通道无功总电能'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelReactiveTotalEnergyPropertySpecs()
        self.v: int = 0


class ChannelReactiveTotalEnergyPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10000
        self.unit = 'Wh'
        self.unitName = '瓦时'
        self.step = 1


class ChannelActiveTotalEnergyProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelActiveTotalEnergy'
        self.name = '通道有功总电能'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelActiveTotalEnergyPropertySpecs()
        self.v: int = 0


class ChannelActiveTotalEnergyPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
        self.unit = 'Wh'
        self.unitName = '瓦时'
        self.step = 1


class ChannelPowerFactorProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelPowerFactor'
        self.name = '通道功率因数'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelPowerFactorPropertySpecs()
        self.v: int = 0


class ChannelPowerFactorPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 500
        self.max = 900
        self.unit = 'permill'
        self.step = 1


class ChannelReactivePowerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelReactivePower'
        self.name = '通道无功功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelReactivePowerPropertySpecs()
        self.v: int = 0


class ChannelReactivePowerPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
        self.unit = 'Var'
        self.unitName = '无功功率单位'
        self.step = 1


class ChannelActivePowerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelActivePower'
        self.name = '通道有功功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelActivePowerPropertySpecs()
        self.v: int = 0


class ChannelActivePowerPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100000
        self.unit = 'W'
        self.unitName = '瓦特'
        self.step = 1


class ChannelApparentPowerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelApparentPower'
        self.name = '通道视在功率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelApparentPowerPropertySpecs()
        self.v: int = 0


class ChannelApparentPowerPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1000000
        self.unit = 'W'
        self.unitName = '瓦特'
        self.step = 1


class ChannelLeakageCurrentProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelLeakageCurrent'
        self.name = '通道漏电电流值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelLeakageCurrentPropertySpecs()
        self.v: int = 0


class ChannelLeakageCurrentPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 5
        self.unit = 'mA'
        self.unitName = '毫安'
        self.step = 0.1


class ChannelVoltageProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelVoltage'
        self.name = '通道电压值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelVoltagePropertySpecs()
        self.v: int = 0


class ChannelVoltagePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 180000
        self.max = 260000
        self.unit = 'mV'
        self.unitName = '伏'
        self.step = 1


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
        self.min = 0
        self.max = 1000000
        self.unit = 'Wh'
        self.unitName = '瓦时'
        self.step = 1


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
        self.min = 0
        self.max = 100000
        self.unit = 'Wh'
        self.unitName = '瓦时'
        self.step = 1


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
        self.min = 500
        self.max = 900
        self.unit = 'permill'
        self.unitName = '通道功率因数单位'
        self.step = 1


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
        self.min = 0
        self.max = 100000
        self.unit = 'Var'
        self.unitName = '无功功率单位'
        self.step = 1


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
        self.min = 0
        self.max = 1000000
        self.unit = 'W'
        self.unitName = '瓦'
        self.step = 1


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
        self.min = 0
        self.max = 10000000
        self.unit = 'W'
        self.unitName = '瓦'
        self.step = 1


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
        self.min = 25
        self.max = 100
        self.unit = 'Hz'
        self.unitName = '赫兹'
        self.step = 1


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
        self.min = 0
        self.max = 5
        self.unit = 'mA'
        self.unitName = '毫安'
        self.step = 0.1


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
        self.min = 180000
        self.max = 260000
        self.unit = 'mV'
        self.unitName = '毫伏'
        self.step = 100


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

class ChannelErrorProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelError'
        self.name = '通道异常'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = ChannelErrorPropertySpecs()
        self.v: str = ''


class ChannelErrorPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ChannelErrorPropertySpecsOptional()


class ChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.lostVoltage = LostVoltageChannelErrorPropertySpecsOptional()
        self.underVoltage = UnderVoltageChannelErrorPropertySpecsOptional()
        self.overVoltage = OverVoltageChannelErrorPropertySpecsOptional()
        self.lostCurrent = LostCurrentChannelErrorPropertySpecsOptional()
        self.overCurrent = OverCurrentChannelErrorPropertySpecsOptional()
        self.overLoad = OverLoadChannelErrorPropertySpecsOptional()
        self.reverse = ReverseChannelErrorPropertySpecsOptional()
        self.lostPhase = LostPhaseChannelErrorPropertySpecsOptional()
        self.cutCurrent = CutCurrentChannelErrorPropertySpecsOptional()
        self.activeExcess = ActiveExcessChannelErrorPropertySpecsOptional()
        self.reactiveExcess = ReactiveExcessChannelErrorPropertySpecsOptional()
        self.powerExceed = PowerExceedChannelErrorPropertySpecsOptional()
        self.cutCurrent = CutCurrentChannelErrorPropertySpecsOptional()
        self.shortCircuit = ShortCircuitChannelErrorPropertySpecsOptional()
        self.inShortCircuit = InShortCircuitChannelErrorPropertySpecsOptional()
        self.leakage = LeakageChannelErrorPropertySpecsOptional()


class LeakageChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'leakage'
        self.desc = 'leakage'


class InShortCircuitChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'inShortCircuit'
        self.desc = 'inShortCircuit'


class ShortCircuitChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'shortCircuit'
        self.desc = 'shortCircuit'


class PowerExceedChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'powerExceed'
        self.desc = 'powerExceed'


class ReactiveExcessChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'reactiveExcess'
        self.desc = 'reactiveExcess'


class ActiveExcessChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'activeExcess'
        self.desc = 'activeExcess'


class CutCurrentChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'cutCurrent'
        self.desc = 'cutCurrent'


class LostPhaseChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'lostPhase'
        self.desc = 'lostPhase'


class ReverseChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'reverse'
        self.desc = 'reverse'


class OverLoadChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'overLoad'
        self.desc = 'overLoad'


class OverCurrentChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'overCurrent'
        self.desc = 'overCurrent'


class LostCurrentChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'lostCurrent'
        self.desc = 'lostCurrent'


class OverVoltageChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'overVoltage'
        self.desc = 'overVoltage'


class UnderVoltageChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'underVoltage'
        self.desc = 'underVoltage'


class LostVoltageChannelErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'lostVoltage'
        self.desc = 'lostVoltage'


class SystemErrorProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'systemError'
        self.name = '系统异常'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = SystemErrorPropertySpecs()
        self.v: str = ''


class SystemErrorPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = SystemErrorPropertySpecsOptional()


class SystemErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.DS18B20_2_ERROR = DS18B20_2_ERRORSystemErrorPropertySpecsOptional()
        self.DS18B20_1_ERROR = DS18B20_1_ERRORSystemErrorPropertySpecsOptional()
        self.FLASH_ERROR = FLASH_ERRORSystemErrorPropertySpecsOptional()
        self.RAM_ERROR = RAM_ERRORSystemErrorPropertySpecsOptional()
        self.CLOCK_ERROR = CLOCK_ERRORSystemErrorPropertySpecsOptional()
        self.EEPROM_ERROR = EEPROM_ERRORSystemErrorPropertySpecsOptional()


class EEPROM_ERRORSystemErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'EEPROM_ERROR'
        self.desc = 'EEPROM_ERROR'


class CLOCK_ERRORSystemErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'CLOCK_ERROR'
        self.desc = 'CLOCK_ERROR'


class RAM_ERRORSystemErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'RAM_ERROR'
        self.desc = 'RAM_ERROR'


class FLASH_ERRORSystemErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'FLASH_ERROR'
        self.desc = 'FLASH_ERROR'


class DS18B20_1_ERRORSystemErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'DS18B20_1_ERROR'
        self.desc = 'DS18B20_1_ERROR'


class DS18B20_2_ERRORSystemErrorPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'DS18B20_2_ERROR'
        self.desc = 'DS18B20_2_ERROR'


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

class ChannelNumberProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelNumber'
        self.name = '通道号'
        self.accessMode = 'rw'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelNumberPropertySpecs()
        self.v: int = 0


class ChannelNumberPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ChannelNumberPropertySpecsOptional()


class ChannelNumberPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0ChannelNumberPropertySpecsOptional()
        self.value1 = Value1ChannelNumberPropertySpecsOptional()
        self.value2 = Value2ChannelNumberPropertySpecsOptional()
        self.value3 = Value3ChannelNumberPropertySpecsOptional()
        self.value5 = Value5ChannelNumberPropertySpecsOptional()
        self.value6 = Value6ChannelNumberPropertySpecsOptional()


class Value6ChannelNumberPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '通道号'


class Value5ChannelNumberPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '通道号'


class Value3ChannelNumberPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '通道号'


class Value2ChannelNumberPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '通道号'


class Value1ChannelNumberPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '通道号'


class Value0ChannelNumberPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '通道号'


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
        self.specs = Rs485AddrPropertySpecs()
        self.v: str = ''


class Rs485AddrPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class SNProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'SN'
        self.name = '设备SN号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = SNPropertySpecs()
        self.v: str = ''


class SNPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass