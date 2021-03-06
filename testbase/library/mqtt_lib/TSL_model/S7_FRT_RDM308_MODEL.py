from .base_model import *


class S7_FRT_RDM308(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S7_FRT_RDM308'
        self.productName = '富奥通308'
        self.properties = Properties()
        self.services = Services()


class Services:
    def __init__(self) -> None:
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


class Properties:
    def __init__(self) -> None:
        self.minWindDirection = MinWindDirectionProperty()
        self.model = ModelProperty()
        self.windDirection = WindDirectionProperty()
        self.maxWindDirection = MaxWindDirectionProperty()
        self.airPressure = AirPressureProperty()
        self.temperature = TemperatureProperty()
        self.humidity = HumidityProperty()
        self.noise = NoiseProperty()
        self.precipitation = PrecipitationProperty()
        self.radiation = RadiationProperty()
        self.ultravioletIntensity = UltravioletIntensityProperty()
        self.minWindSpeed = MinWindSpeedProperty()
        self.windSpeed = WindSpeedProperty()
        self.maxWindSpeed = MaxWindSpeedProperty()
        self.PM2_5 = PM2_5Property()
        self.PM10 = PM10Property()
        self.rs485Port = Rs485PortProperty()
        self.rs485Addr = Rs485AddrProperty()
        self.rs485Baund = Rs485BaundProperty()
        self.rs485DataBit = Rs485DataBitProperty()
        self.rs485Parity = Rs485ParityProperty()
        self.rs485StopBit = Rs485StopBitProperty()
        self.online = OnlineProperty()
        self.mode = ModeProperty()
        self.sn = SnProperty()

    @property
    def v(self):
        return {'minWindDirection': self.minWindDirection.v, 'model': self.model.v, 'windDirection': self.windDirection.v, 'maxWindDirection': self.maxWindDirection.v, 'airPressure': self.airPressure.v, 'temperature': self.temperature.v, 'humidity': self.humidity.v, 'noise': self.noise.v, 'precipitation': self.precipitation.v, 'radiation': self.radiation.v, 'ultravioletIntensity': self.ultravioletIntensity.v, 'minWindSpeed': self.minWindSpeed.v, 'windSpeed': self.windSpeed.v, 'maxWindSpeed': self.maxWindSpeed.v, 'PM2_5': self.PM2_5.v, 'PM10': self.PM10.v, 'rs485Port': self.rs485Port.v, 'rs485Addr': self.rs485Addr.v, 'rs485Baund': self.rs485Baund.v, 'rs485DataBit': self.rs485DataBit.v, 'rs485Parity': self.rs485Parity.v, 'rs485StopBit': self.rs485StopBit.v, 'online': self.online.v, 'mode': self.mode.v, 'sn': self.sn.v}

    @v.setter
    def v(self, value):
        if value.get('minWindDirection') is not None: self.minWindDirection.v = value['minWindDirection']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('windDirection') is not None: self.windDirection.v = value['windDirection']
        if value.get('maxWindDirection') is not None: self.maxWindDirection.v = value['maxWindDirection']
        if value.get('airPressure') is not None: self.airPressure.v = value['airPressure']
        if value.get('temperature') is not None: self.temperature.v = value['temperature']
        if value.get('humidity') is not None: self.humidity.v = value['humidity']
        if value.get('noise') is not None: self.noise.v = value['noise']
        if value.get('precipitation') is not None: self.precipitation.v = value['precipitation']
        if value.get('radiation') is not None: self.radiation.v = value['radiation']
        if value.get('ultravioletIntensity') is not None: self.ultravioletIntensity.v = value['ultravioletIntensity']
        if value.get('minWindSpeed') is not None: self.minWindSpeed.v = value['minWindSpeed']
        if value.get('windSpeed') is not None: self.windSpeed.v = value['windSpeed']
        if value.get('maxWindSpeed') is not None: self.maxWindSpeed.v = value['maxWindSpeed']
        if value.get('PM2_5') is not None: self.PM2_5.v = value['PM2_5']
        if value.get('PM10') is not None: self.PM10.v = value['PM10']
        if value.get('rs485Port') is not None: self.rs485Port.v = value['rs485Port']
        if value.get('rs485Addr') is not None: self.rs485Addr.v = value['rs485Addr']
        if value.get('rs485Baund') is not None: self.rs485Baund.v = value['rs485Baund']
        if value.get('rs485DataBit') is not None: self.rs485DataBit.v = value['rs485DataBit']
        if value.get('rs485Parity') is not None: self.rs485Parity.v = value['rs485Parity']
        if value.get('rs485StopBit') is not None: self.rs485StopBit.v = value['rs485StopBit']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('mode') is not None: self.mode.v = value['mode']
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
        self.specs = Rs485AddrPropertySpecs()
        self.v: str = ''


class Rs485AddrPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

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


class PM10Property(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'PM10'
        self.name = '细颗粒物浓度值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = PM10PropertySpecs()
        self.v: float = 0.0


class PM10PropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1000
        self.unit = 'ug/m2'
        self.unitName = 'ug/m2'


class PM2_5Property(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'PM2_5'
        self.name = '细颗粒物浓度值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = PM2_5PropertySpecs()
        self.v: float = 0.0


class PM2_5PropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1000
        self.unit = 'ug/m2'
        self.unitName = 'ug/m2'


class MaxWindSpeedProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'maxWindSpeed'
        self.name = '最大风速'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = MaxWindSpeedPropertySpecs()
        self.v: float = 0.0


class MaxWindSpeedPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 70
        self.unit = 'm/s'
        self.unitName = '米每秒'


class WindSpeedProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'windSpeed'
        self.name = '风速'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = WindSpeedPropertySpecs()
        self.v: float = 0.0


class WindSpeedPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 70
        self.unit = 'm/s'
        self.unitName = '米每秒'


class MinWindSpeedProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'minWindSpeed'
        self.name = '最小风速'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = MinWindSpeedPropertySpecs()
        self.v: float = 0.0


class MinWindSpeedPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 70
        self.unit = 'm/s'
        self.unitName = '米每秒'


class UltravioletIntensityProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'ultravioletIntensity'
        self.name = '紫外线强度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = UltravioletIntensityPropertySpecs()
        self.v: float = 0.0


class UltravioletIntensityPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 290
        self.max = 400
        self.unit = 'nm'


class RadiationProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'radiation'
        self.name = '辐射'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = RadiationPropertySpecs()
        self.v: float = 0.0


class RadiationPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 2000
        self.unit = 'w/m2'


class PrecipitationProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'precipitation'
        self.name = '降雨量'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = PrecipitationPropertySpecs()
        self.v: float = 0.0


class PrecipitationPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1000
        self.unit = 'M'
        self.unitName = '毫米'


class NoiseProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'noise'
        self.name = '噪声'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = NoisePropertySpecs()
        self.v: float = 0.0


class NoisePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 30
        self.max = 130
        self.unit = 'dB'
        self.unitName = '分贝'


class HumidityProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'humidity'
        self.name = '湿度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = HumidityPropertySpecs()
        self.v: float = 0.0


class HumidityPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = '%'
        self.unitName = '百分比'


class TemperatureProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'temperature'
        self.name = '温度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = TemperaturePropertySpecs()
        self.v: float = 0.0


class TemperaturePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -50
        self.max = 80
        self.unit = '°'
        self.unitName = '摄氏度'


class AirPressureProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'airPressure'
        self.name = '气压'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = AirPressurePropertySpecs()
        self.v: float = 0.0


class AirPressurePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 10
        self.max = 1300
        self.unit = 'Pa'
        self.unitName = '帕'


class MaxWindDirectionProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'maxWindDirection'
        self.name = '最大风向角度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = MaxWindDirectionPropertySpecs()
        self.v: int = 0


class MaxWindDirectionPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 360
        self.unit = '°'
        self.unitName = '度'
        self.step = 1


class WindDirectionProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'windDirection'
        self.name = '平均风向角度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = WindDirectionPropertySpecs()
        self.v: int = 0


class WindDirectionPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 360
        self.unit = '°'
        self.unitName = '度'
        self.step = 1


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

class MinWindDirectionProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'minWindDirection'
        self.name = '最小风向角度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = MinWindDirectionPropertySpecs()
        self.v: int = 0


class MinWindDirectionPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 360
        self.unit = '°'
        self.unitName = '度'
        self.step = 1
