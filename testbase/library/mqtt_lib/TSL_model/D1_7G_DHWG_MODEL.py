from .base_model import *


class D1_QG_DHWG(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'D1_7G_DHWG'
        self.productName = '7G智能网关'
        self.properties = Properties()
        self.events = Events()
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.reboot = RebootService()
        self.setBasic = SetBasicService()
        self.setDO = SetDOService()
        self.updateFirmware = UpdateFirmwareService()
        self.setNtpHost = SetNtpHostService()
        self.setSensor = SetSensorService()
        self.setRs485 = SetRs485Service()
        self.writeRs485 = WriteRs485Service()
        self.readRs485 = ReadRs485Service()
        self.setVolume = SetVolumeService()


class SetVolumeService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setVolume'
        self.name = '设置音量'
        self.parameters = SetVolumeServiceParameters()


class SetVolumeServiceParameters:
    def __init__(self) -> None:
        self.volume = VolumeSetVolumeServiceParameter()

    @property
    def v(self):
        return {'volume': self.volume.v}

    @v.setter
    def v(self, value):
        if value.get('volume') is not None: self.volume.v = value['volume']


class VolumeSetVolumeServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'volume'
        self.name = '音量'
        self.required = True
        self.type = 'integer'
        self.specs = VolumeSetVolumeServiceParameterSpecs()
        self.v: int = 0


class VolumeSetVolumeServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = '%'


class ReadRs485Service(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'readRs485'
        self.name = 'RS485读取数据'
        self.parameters = ReadRs485ServiceParameters()


class ReadRs485ServiceParameters:
    def __init__(self) -> None:
        self.port = PortReadRs485ServiceParameter()
        self.len = LenReadRs485ServiceParameter()
        self.wait = WaitReadRs485ServiceParameter()
        self.flush = FlushReadRs485ServiceParameter()

    @property
    def v(self):
        return {'port': self.port.v, 'len': self.len.v, 'wait': self.wait.v, 'flush': self.flush.v}

    @v.setter
    def v(self, value):
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('len') is not None: self.len.v = value['len']
        if value.get('wait') is not None: self.wait.v = value['wait']
        if value.get('flush') is not None: self.flush.v = value['flush']


class FlushReadRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'flush'
        self.name = '清空接收缓冲区'
        self.required = False
        self.type = 'boolean'
        self.specs = FlushReadRs485ServiceParameterSpecs()
        self.v: bool = True


class FlushReadRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = FlushReadRs485ServiceParameterSpecsOptional()


class FlushReadRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.valueTrue = ValueTrueFlushReadRs485ServiceParameterSpecsOptional()
        self.valueFalse = ValueFalseFlushReadRs485ServiceParameterSpecsOptional()


class ValueFalseFlushReadRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = False
        self.desc = '读取前不清空接收缓冲区'


class ValueTrueFlushReadRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = True
        self.desc = '读取前清空接收缓冲区'


class WaitReadRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'wait'
        self.name = '读取等待时长'
        self.required = True
        self.type = 'integer'
        self.specs = WaitReadRs485ServiceParameterSpecs()
        self.v: int = 0


class WaitReadRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10000


class LenReadRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'len'
        self.name = '要读取的数据长度'
        self.required = False
        self.type = 'integer'
        self.specs = LenReadRs485ServiceParameterSpecs()
        self.v: int = 0


class LenReadRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 4096


class PortReadRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'port'
        self.name = '端口号'
        self.required = True
        self.type = 'integer'
        self.specs = PortReadRs485ServiceParameterSpecs()
        self.v: int = 0


class PortReadRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = PortReadRs485ServiceParameterSpecsOptional()


class PortReadRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1PortReadRs485ServiceParameterSpecsOptional()
        self.value2 = Value2PortReadRs485ServiceParameterSpecsOptional()


class Value2PortReadRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '2号RS485口'


class Value1PortReadRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '1号RS485口'


class WriteRs485Service(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'writeRs485'
        self.name = 'RS485发送数据'
        self.parameters = WriteRs485ServiceParameters()


class WriteRs485ServiceParameters:
    def __init__(self) -> None:
        self.port = PortWriteRs485ServiceParameter()
        self.data = DataWriteRs485ServiceParameter()
        self.flush = FlushWriteRs485ServiceParameter()

    @property
    def v(self):
        return {'port': self.port.v, 'data': self.data.v, 'flush': self.flush.v}

    @v.setter
    def v(self, value):
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('data') is not None: self.data.v = value['data']
        if value.get('flush') is not None: self.flush.v = value['flush']


class FlushWriteRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'flush'
        self.name = '清空接收缓冲区'
        self.required = False
        self.type = 'boolean'
        self.specs = FlushWriteRs485ServiceParameterSpecs()
        self.v: bool = True


class FlushWriteRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = FlushWriteRs485ServiceParameterSpecsOptional()


class FlushWriteRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.valueTrue = ValueTrueFlushWriteRs485ServiceParameterSpecsOptional()
        self.valueFalse = ValueFalseFlushWriteRs485ServiceParameterSpecsOptional()


class ValueFalseFlushWriteRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = False
        self.desc = '发送前不清空接收缓冲区'


class ValueTrueFlushWriteRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = True
        self.desc = '发送前清空接收缓冲区'


class DataWriteRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'data'
        self.name = '要发送的数据'
        self.required = True
        self.type = 'string'
        self.specs = DataWriteRs485ServiceParameterSpecs()
        self.v: str = ''


class DataWriteRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.max = 4096


class PortWriteRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'port'
        self.name = '端口号'
        self.required = True
        self.type = 'integer'
        self.specs = PortWriteRs485ServiceParameterSpecs()
        self.v: int = 0


class PortWriteRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = PortWriteRs485ServiceParameterSpecsOptional()


class PortWriteRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1PortWriteRs485ServiceParameterSpecsOptional()
        self.value2 = Value2PortWriteRs485ServiceParameterSpecsOptional()


class Value2PortWriteRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '2号RS485口'


class Value1PortWriteRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '1号RS485口'


class SetRs485Service(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setRs485'
        self.name = '设置RS485'
        self.parameters = SetRs485ServiceParameters()


class SetRs485ServiceParameters:
    def __init__(self) -> None:
        self.port = PortSetRs485ServiceParameter()
        self.baudRate = BaudRateSetRs485ServiceParameter()
        self.byteSize = ByteSizeSetRs485ServiceParameter()
        self.stopBit = StopBitSetRs485ServiceParameter()
        self.parities = ParitiesSetRs485ServiceParameter()

    @property
    def v(self):
        return {'port': self.port.v, 'baudRate': self.baudRate.v, 'byteSize': self.byteSize.v, 'stopBit': self.stopBit.v, 'parities': self.parities.v}

    @v.setter
    def v(self, value):
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('baudRate') is not None: self.baudRate.v = value['baudRate']
        if value.get('byteSize') is not None: self.byteSize.v = value['byteSize']
        if value.get('stopBit') is not None: self.stopBit.v = value['stopBit']
        if value.get('parities') is not None: self.parities.v = value['parities']


class ParitiesSetRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'parities'
        self.name = '校验'
        self.required = True
        self.type = 'string'
        self.specs = ParitiesSetRs485ServiceParameterSpecs()
        self.v: str = ''


class ParitiesSetRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ParitiesSetRs485ServiceParameterSpecsOptional()


class ParitiesSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.N = NParitiesSetRs485ServiceParameterSpecsOptional()
        self.E = EParitiesSetRs485ServiceParameterSpecsOptional()
        self.O = OParitiesSetRs485ServiceParameterSpecsOptional()
        self.M = MParitiesSetRs485ServiceParameterSpecsOptional()
        self.S = SParitiesSetRs485ServiceParameterSpecsOptional()


class SParitiesSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'S'
        self.desc = '低'


class MParitiesSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'M'
        self.desc = '高'


class OParitiesSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'O'
        self.desc = '奇'


class EParitiesSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'E'
        self.desc = '偶'


class NParitiesSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'N'
        self.desc = '无'


class StopBitSetRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'stopBit'
        self.name = '停止位'
        self.required = True
        self.type = 'string'
        self.specs = StopBitSetRs485ServiceParameterSpecs()
        self.v: str = ''


class StopBitSetRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StopBitSetRs485ServiceParameterSpecsOptional()


class StopBitSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1StopBitSetRs485ServiceParameterSpecsOptional()
        self.value1_5 = Value1_5StopBitSetRs485ServiceParameterSpecsOptional()
        self.value2 = Value2StopBitSetRs485ServiceParameterSpecsOptional()


class Value2StopBitSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '2'
        self.desc = '2位'


class Value1_5StopBitSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '1.5'
        self.desc = '1.5位'


class Value1StopBitSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '1'
        self.desc = '1位'


class ByteSizeSetRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'byteSize'
        self.name = '数据位'
        self.required = True
        self.type = 'integer'
        self.specs = ByteSizeSetRs485ServiceParameterSpecs()
        self.v: int = 0


class ByteSizeSetRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 5
        self.max = 8


class BaudRateSetRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'baudRate'
        self.name = '波特率'
        self.required = True
        self.type = 'integer'
        self.specs = BaudRateSetRs485ServiceParameterSpecs()
        self.v: int = 0


class BaudRateSetRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2400
        self.max = 250000


class PortSetRs485ServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'port'
        self.name = '端口号'
        self.required = True
        self.type = 'integer'
        self.specs = PortSetRs485ServiceParameterSpecs()
        self.v: int = 0


class PortSetRs485ServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = PortSetRs485ServiceParameterSpecsOptional()


class PortSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1PortSetRs485ServiceParameterSpecsOptional()
        self.value2 = Value2PortSetRs485ServiceParameterSpecsOptional()


class Value2PortSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '2号RS485口'


class Value1PortSetRs485ServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '1号RS485口'


class SetSensorService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setSensor'
        self.name = '设置传感器信息'
        self.parameters = SetSensorServiceParameters()


class SetSensorServiceParameters:
    def __init__(self) -> None:
        self.tiltCalibrate = TiltCalibrateSetSensorServiceParameter()
        self.tiltThreshold = TiltThresholdSetSensorServiceParameter()
        self.tempHiThreshold = TempHiThresholdSetSensorServiceParameter()
        self.tempLowThreshold = TempLowThresholdSetSensorServiceParameter()
        self.humiHiThreshold = HumiHiThresholdSetSensorServiceParameter()
        self.humiLowThreshold = HumiLowThresholdSetSensorServiceParameter()

    @property
    def v(self):
        return {'tiltCalibrate': self.tiltCalibrate.v, 'tiltThreshold': self.tiltThreshold.v, 'tempHiThreshold': self.tempHiThreshold.v, 'tempLowThreshold': self.tempLowThreshold.v, 'humiHiThreshold': self.humiHiThreshold.v, 'humiLowThreshold': self.humiLowThreshold.v}

    @v.setter
    def v(self, value):
        if value.get('tiltCalibrate') is not None: self.tiltCalibrate.v = value['tiltCalibrate']
        if value.get('tiltThreshold') is not None: self.tiltThreshold.v = value['tiltThreshold']
        if value.get('tempHiThreshold') is not None: self.tempHiThreshold.v = value['tempHiThreshold']
        if value.get('tempLowThreshold') is not None: self.tempLowThreshold.v = value['tempLowThreshold']
        if value.get('humiHiThreshold') is not None: self.humiHiThreshold.v = value['humiHiThreshold']
        if value.get('humiLowThreshold') is not None: self.humiLowThreshold.v = value['humiLowThreshold']


class HumiLowThresholdSetSensorServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'humiLowThreshold'
        self.name = '低湿告警值'
        self.required = False
        self.type = 'integer'
        self.specs = HumiLowThresholdSetSensorServiceParameterSpecs()
        self.v: int = 0


class HumiLowThresholdSetSensorServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class HumiHiThresholdSetSensorServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'humiHiThreshold'
        self.name = '高湿告警值'
        self.required = False
        self.type = 'integer'
        self.specs = HumiHiThresholdSetSensorServiceParameterSpecs()
        self.v: int = 0


class HumiHiThresholdSetSensorServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class TempLowThresholdSetSensorServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'tempLowThreshold'
        self.name = '低温告警值'
        self.required = False
        self.type = 'integer'
        self.specs = TempLowThresholdSetSensorServiceParameterSpecs()
        self.v: int = 0


class TempLowThresholdSetSensorServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -50
        self.max = 100


class TempHiThresholdSetSensorServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'tempHiThreshold'
        self.name = '高温告警值'
        self.required = False
        self.type = 'integer'
        self.specs = TempHiThresholdSetSensorServiceParameterSpecs()
        self.v: int = 0


class TempHiThresholdSetSensorServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -50
        self.max = 100


class TiltThresholdSetSensorServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'tiltThreshold'
        self.name = '倾斜告警值'
        self.required = False
        self.type = 'integer'
        self.specs = TiltThresholdSetSensorServiceParameterSpecs()
        self.v: int = 0


class TiltThresholdSetSensorServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 5
        self.max = 30


class TiltCalibrateSetSensorServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'tiltCalibrate'
        self.name = '倾斜校准'
        self.required = False
        self.type = 'boolean'
        self.specs = TiltCalibrateSetSensorServiceParameterSpecs()
        self.v: bool = True


class TiltCalibrateSetSensorServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TiltCalibrateSetSensorServiceParameterSpecsOptional()


class TiltCalibrateSetSensorServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.valueTrue = ValueTrueTiltCalibrateSetSensorServiceParameterSpecsOptional()
        self.valueFalse = ValueFalseTiltCalibrateSetSensorServiceParameterSpecsOptional()


class ValueFalseTiltCalibrateSetSensorServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = False
        self.desc = '无操作'


class ValueTrueTiltCalibrateSetSensorServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = True
        self.desc = '校准'


class SetNtpHostService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setNtpHost'
        self.name = '设置ntp校时服务器地址'
        self.parameters = SetNtpHostServiceParameters()


class SetNtpHostServiceParameters:
    def __init__(self) -> None:
        self.hostA = HostASetNtpHostServiceParameter()
        self.hostB = HostBSetNtpHostServiceParameter()

    @property
    def v(self):
        return {'hostA': self.hostA.v, 'hostB': self.hostB.v}

    @v.setter
    def v(self, value):
        if value.get('hostA') is not None: self.hostA.v = value['hostA']
        if value.get('hostB') is not None: self.hostB.v = value['hostB']


class HostBSetNtpHostServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'hostB'
        self.name = '备ntp校时服务器'
        self.required = False
        self.type = 'string'
        self.format = 'ipv4'
        self.v: str = ''


class HostASetNtpHostServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'hostA'
        self.name = '主ntp校时服务器'
        self.required = False
        self.type = 'string'
        self.format = 'ipv4'
        self.v: str = ''


class UpdateFirmwareService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'updateFirmware'
        self.name = '更新固件'
        self.parameters = UpdateFirmwareServiceParameters()


class UpdateFirmwareServiceParameters:
    def __init__(self) -> None:
        self.url = UrlUpdateFirmwareServiceParameter()
        self.md5Sum = Md5SumUpdateFirmwareServiceParameter()

    @property
    def v(self):
        return {'url': self.url.v, 'md5Sum': self.md5Sum.v}

    @v.setter
    def v(self, value):
        if value.get('url') is not None: self.url.v = value['url']
        if value.get('md5Sum') is not None: self.md5Sum.v = value['md5Sum']


class Md5SumUpdateFirmwareServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'md5Sum'
        self.name = '固件文件MD5'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class UrlUpdateFirmwareServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'url'
        self.name = '固件下载地址'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class SetDOService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setDO'
        self.name = '设置DO输出'
        self.parameters = SetDOServiceParameters()


class SetDOServiceParameters:
    def __init__(self) -> None:
        self.port = PortSetDOServiceParameter()
        self.status = StatusSetDOServiceParameter()
        self.shootTime = ShootTimeSetDOServiceParameter()

    @property
    def v(self):
        return {'port': self.port.v, 'status': self.status.v, 'shootTime': self.shootTime.v}

    @v.setter
    def v(self, value):
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('status') is not None: self.status.v = value['status']
        if value.get('shootTime') is not None: self.shootTime.v = value['shootTime']


class ShootTimeSetDOServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'shootTime'
        self.name = '持续时间'
        self.required = True
        self.type = 'integer'
        self.specs = ShootTimeSetDOServiceParameterSpecs()
        self.v: int = 0


class ShootTimeSetDOServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10000
        self.optional = ShootTimeSetDOServiceParameterSpecsOptional()


class ShootTimeSetDOServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0ShootTimeSetDOServiceParameterSpecsOptional()


class Value0ShootTimeSetDOServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '保持'


class StatusSetDOServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'status'
        self.name = '状态'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class PortSetDOServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'port'
        self.name = '端口号'
        self.required = True
        self.type = 'integer'
        self.specs = PortSetDOServiceParameterSpecs()
        self.v: int = 0


class PortSetDOServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = PortSetDOServiceParameterSpecsOptional()


class PortSetDOServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1PortSetDOServiceParameterSpecsOptional()
        self.value2 = Value2PortSetDOServiceParameterSpecsOptional()


class Value2PortSetDOServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = 'DO2'


class Value1PortSetDOServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = 'DO1'


class SetBasicService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setBasic'
        self.name = '动环设置'
        self.parameters = SetBasicServiceParameters()


class SetBasicServiceParameters:
    def __init__(self) -> None:
        self.enabled = EnabledSetBasicServiceParameter()
        self.interval = IntervalSetBasicServiceParameter()
        self.alarmInterval = AlarmIntervalSetBasicServiceParameter()
        self.do1 = Do1SetBasicServiceParameter()
        self.do2 = Do2SetBasicServiceParameter()

    @property
    def v(self):
        return {'enabled': self.enabled.v, 'interval': self.interval.v, 'alarmInterval': self.alarmInterval.v, 'do1': self.do1.v, 'do2': self.do2.v}

    @v.setter
    def v(self, value):
        if value.get('enabled') is not None: self.enabled.v = value['enabled']
        if value.get('interval') is not None: self.interval.v = value['interval']
        if value.get('alarmInterval') is not None: self.alarmInterval.v = value['alarmInterval']
        if value.get('do1') is not None: self.do1.v = value['do1']
        if value.get('do2') is not None: self.do2.v = value['do2']


class Do2SetBasicServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'do2'
        self.name = 'DO2默认状态'
        self.required = False
        self.type = 'boolean'
        self.v: bool = True


class Do1SetBasicServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'do1'
        self.name = 'DO1默认状态'
        self.required = False
        self.type = 'boolean'
        self.v: bool = True


class AlarmIntervalSetBasicServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'alarmInterval'
        self.name = '告警上报间隔'
        self.required = False
        self.type = 'integer'
        self.specs = AlarmIntervalSetBasicServiceParameterSpecs()
        self.v: int = 0


class AlarmIntervalSetBasicServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 10
        self.max = 65535
        self.unit = 's'
        self.unitName = '秒'


class IntervalSetBasicServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'interval'
        self.name = '定时上报间隔'
        self.required = False
        self.type = 'integer'
        self.specs = IntervalSetBasicServiceParameterSpecs()
        self.v: int = 0


class IntervalSetBasicServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 10
        self.max = 65535
        self.unit = 's'
        self.unitName = '秒'


class EnabledSetBasicServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'enabled'
        self.name = '定时上报开关'
        self.required = False
        self.type = 'boolean'
        self.v: bool = True


class RebootService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'reboot'
        self.name = '重启'
        self.parameters = None


class Events:
    def __init__(self) -> None:
        self.firmwareUpdate = FirmwareUpdateEvent()
        self.reboot = RebootEvent()
        self.calibrate = CalibrateEvent()


class CalibrateEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'calibrate'
        self.name = '倾斜校准'
        self.parameters = CalibrateEventParameters()


class CalibrateEventParameters:
    def __init__(self) -> None:
        self.status = StatusCalibrateEventParameter()
        self.resultCode = ResultCodeCalibrateEventParameter()

    @property
    def v(self):
        return {'status': self.status.v, 'resultCode': self.resultCode.v}

    @v.setter
    def v(self, value):
        if value.get('status') is not None: self.status.v = value['status']
        if value.get('resultCode') is not None: self.resultCode.v = value['resultCode']


class ResultCodeCalibrateEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'resultCode'
        self.name = '结果码'
        self.type = 'integer'
        self.specs = ResultCodeCalibrateEventParameterSpecs()
        self.v: int = 0


class ResultCodeCalibrateEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ResultCodeCalibrateEventParameterSpecsOptional()


class ResultCodeCalibrateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0ResultCodeCalibrateEventParameterSpecsOptional()
        self.value1 = Value1ResultCodeCalibrateEventParameterSpecsOptional()


class Value1ResultCodeCalibrateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '失败'


class Value0ResultCodeCalibrateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '成功'


class StatusCalibrateEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'status'
        self.name = '操作状态'
        self.type = 'string'
        self.specs = StatusCalibrateEventParameterSpecs()
        self.v: str = ''


class StatusCalibrateEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StatusCalibrateEventParameterSpecsOptional()


class StatusCalibrateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.success = SuccessStatusCalibrateEventParameterSpecsOptional()
        self.failed = FailedStatusCalibrateEventParameterSpecsOptional()


class FailedStatusCalibrateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'failed'
        self.desc = '失败'


class SuccessStatusCalibrateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'success'
        self.desc = '成功'


class RebootEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'reboot'
        self.name = '重启'
        self.parameters = RebootEventParameters()


class RebootEventParameters:
    def __init__(self) -> None:
        self.status = StatusRebootEventParameter()
        self.resultCode = ResultCodeRebootEventParameter()

    @property
    def v(self):
        return {'status': self.status.v, 'resultCode': self.resultCode.v}

    @v.setter
    def v(self, value):
        if value.get('status') is not None: self.status.v = value['status']
        if value.get('resultCode') is not None: self.resultCode.v = value['resultCode']


class ResultCodeRebootEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'resultCode'
        self.name = '结果码'
        self.type = 'integer'
        self.specs = ResultCodeRebootEventParameterSpecs()
        self.v: int = 0


class ResultCodeRebootEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ResultCodeRebootEventParameterSpecsOptional()


class ResultCodeRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0ResultCodeRebootEventParameterSpecsOptional()
        self.value1 = Value1ResultCodeRebootEventParameterSpecsOptional()
        self.value2 = Value2ResultCodeRebootEventParameterSpecsOptional()


class Value2ResultCodeRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '其他'


class Value1ResultCodeRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '配置参数更改'


class Value0ResultCodeRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '系统升级'


class StatusRebootEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'status'
        self.name = '重启原因'
        self.type = 'string'
        self.specs = StatusRebootEventParameterSpecs()
        self.v: str = ''


class StatusRebootEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StatusRebootEventParameterSpecsOptional()


class StatusRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.update = UpdateStatusRebootEventParameterSpecsOptional()
        self.configchanged = ConfigchangedStatusRebootEventParameterSpecsOptional()
        self.other = OtherStatusRebootEventParameterSpecsOptional()


class OtherStatusRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'other'
        self.desc = '其他'


class ConfigchangedStatusRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'config changed'
        self.desc = '配置参数更改'


class UpdateStatusRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'update'
        self.desc = '系统升级'


class FirmwareUpdateEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'firmwareUpdate'
        self.name = '固件升级'
        self.parameters = FirmwareUpdateEventParameters()


class FirmwareUpdateEventParameters:
    def __init__(self) -> None:
        self.status = StatusFirmwareUpdateEventParameter()
        self.resultCode = ResultCodeFirmwareUpdateEventParameter()

    @property
    def v(self):
        return {'status': self.status.v, 'resultCode': self.resultCode.v}

    @v.setter
    def v(self, value):
        if value.get('status') is not None: self.status.v = value['status']
        if value.get('resultCode') is not None: self.resultCode.v = value['resultCode']


class ResultCodeFirmwareUpdateEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'resultCode'
        self.name = '结果码'
        self.type = 'integer'
        self.specs = ResultCodeFirmwareUpdateEventParameterSpecs()
        self.v: int = 0


class ResultCodeFirmwareUpdateEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ResultCodeFirmwareUpdateEventParameterSpecsOptional()


class ResultCodeFirmwareUpdateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0ResultCodeFirmwareUpdateEventParameterSpecsOptional()
        self.value1 = Value1ResultCodeFirmwareUpdateEventParameterSpecsOptional()
        self.value2 = Value2ResultCodeFirmwareUpdateEventParameterSpecsOptional()
        self.value3 = Value3ResultCodeFirmwareUpdateEventParameterSpecsOptional()
        self.value4 = Value4ResultCodeFirmwareUpdateEventParameterSpecsOptional()


class Value4ResultCodeFirmwareUpdateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 4
        self.desc = '文件无法识别'


class Value3ResultCodeFirmwareUpdateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = 'MD5错误'


class Value2ResultCodeFirmwareUpdateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '下载失败'


class Value1ResultCodeFirmwareUpdateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '升级失败'


class Value0ResultCodeFirmwareUpdateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '成功'


class StatusFirmwareUpdateEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'status'
        self.name = '操作状态'
        self.type = 'string'
        self.specs = StatusFirmwareUpdateEventParameterSpecs()
        self.v: str = ''


class StatusFirmwareUpdateEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StatusFirmwareUpdateEventParameterSpecsOptional()


class StatusFirmwareUpdateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.start = StartStatusFirmwareUpdateEventParameterSpecsOptional()
        self.success = SuccessStatusFirmwareUpdateEventParameterSpecsOptional()
        self.failed = FailedStatusFirmwareUpdateEventParameterSpecsOptional()


class FailedStatusFirmwareUpdateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'failed'
        self.desc = '失败'


class SuccessStatusFirmwareUpdateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'success'
        self.desc = '成功'


class StartStatusFirmwareUpdateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'start'
        self.desc = '开始'


class Properties:
    def __init__(self) -> None:
        self.sn = SnProperty()
        self.model = ModelProperty()
        self.networkInfo = NetworkInfoProperty()
        self.mqttPrefix = MqttPrefixProperty()
        self.ntpInfo = NtpInfoProperty()
        self.upTime = UpTimeProperty()
        self.time = TimeProperty()
        self.fwVersion = FwVersionProperty()
        self.hwVersion = HwVersionProperty()
        self.voipServer = VoipServerProperty()
        self.holter = HolterProperty()
        self.serverA = ServerAProperty()
        self.serverB = ServerBProperty()
        self.rs485_1 = Rs485_1Property()
        self.rs485_2 = Rs485_2Property()

    @property
    def v(self):
        return {'sn': self.sn.v, 'model': self.model.v, 'networkInfo': self.networkInfo.v, 'mqttPrefix': self.mqttPrefix.v, 'ntpInfo': self.ntpInfo.v, 'upTime': self.upTime.v, 'time': self.time.v, 'fwVersion': self.fwVersion.v, 'hwVersion': self.hwVersion.v, 'voipServer': self.voipServer.v, 'holter': self.holter.v, 'serverA': self.serverA.v, 'serverB': self.serverB.v, 'rs485_1': self.rs485_1.v, 'rs485_2': self.rs485_2.v}

    @v.setter
    def v(self, value):
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('networkInfo') is not None: self.networkInfo.v = value['networkInfo']
        if value.get('mqttPrefix') is not None: self.mqttPrefix.v = value['mqttPrefix']
        if value.get('ntpInfo') is not None: self.ntpInfo.v = value['ntpInfo']
        if value.get('upTime') is not None: self.upTime.v = value['upTime']
        if value.get('time') is not None: self.time.v = value['time']
        if value.get('fwVersion') is not None: self.fwVersion.v = value['fwVersion']
        if value.get('hwVersion') is not None: self.hwVersion.v = value['hwVersion']
        if value.get('voipServer') is not None: self.voipServer.v = value['voipServer']
        if value.get('holter') is not None: self.holter.v = value['holter']
        if value.get('serverA') is not None: self.serverA.v = value['serverA']
        if value.get('serverB') is not None: self.serverB.v = value['serverB']
        if value.get('rs485_1') is not None: self.rs485_1.v = value['rs485_1']
        if value.get('rs485_2') is not None: self.rs485_2.v = value['rs485_2']


class Rs485_2Property(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485_2'
        self.name = '2号RS485口配置信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = Rs485_2PropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class Rs485_2PropertyStruct:
    def __init__(self) -> None:
        self.baudRate = BaudRateRs485_2PropertyStruct()
        self.byteSize = ByteSizeRs485_2PropertyStruct()
        self.stopBit = StopBitRs485_2PropertyStruct()
        self.parities = ParitiesRs485_2PropertyStruct()

    @property
    def v(self):
        return {'baudRate': self.baudRate.v, 'byteSize': self.byteSize.v, 'stopBit': self.stopBit.v, 'parities': self.parities.v}

    @v.setter
    def v(self, value):
        if value.get('baudRate') is not None: self.baudRate.v = value['baudRate']
        if value.get('byteSize') is not None: self.byteSize.v = value['byteSize']
        if value.get('stopBit') is not None: self.stopBit.v = value['stopBit']
        if value.get('parities') is not None: self.parities.v = value['parities']


class ParitiesRs485_2PropertyStruct:
    def __init__(self) -> None:
        self.id = 'parities'
        self.name = '校验'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = ParitiesRs485_2PropertyStructSpecs()
        self.v: str = ''


class ParitiesRs485_2PropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ParitiesRs485_2PropertyStructSpecsOptional()


class ParitiesRs485_2PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.N = NParitiesRs485_2PropertyStructSpecsOptional()
        self.E = EParitiesRs485_2PropertyStructSpecsOptional()
        self.O = OParitiesRs485_2PropertyStructSpecsOptional()
        self.M = MParitiesRs485_2PropertyStructSpecsOptional()
        self.S = SParitiesRs485_2PropertyStructSpecsOptional()


class SParitiesRs485_2PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'S'
        self.desc = '低'


class MParitiesRs485_2PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'M'
        self.desc = '高'


class OParitiesRs485_2PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'O'
        self.desc = '奇'


class EParitiesRs485_2PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'E'
        self.desc = '偶'


class NParitiesRs485_2PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'N'
        self.desc = '无'


class StopBitRs485_2PropertyStruct:
    def __init__(self) -> None:
        self.id = 'stopBit'
        self.name = '停止位'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = StopBitRs485_2PropertyStructSpecs()
        self.v: str = ''


class StopBitRs485_2PropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StopBitRs485_2PropertyStructSpecsOptional()


class StopBitRs485_2PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1StopBitRs485_2PropertyStructSpecsOptional()
        self.value1_5 = Value1_5StopBitRs485_2PropertyStructSpecsOptional()
        self.value2 = Value2StopBitRs485_2PropertyStructSpecsOptional()


class Value2StopBitRs485_2PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '2'
        self.desc = '2位'


class Value1_5StopBitRs485_2PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '1.5'
        self.desc = '1.5位'


class Value1StopBitRs485_2PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '1'
        self.desc = '1位'


class ByteSizeRs485_2PropertyStruct:
    def __init__(self) -> None:
        self.id = 'byteSize'
        self.name = '数据位'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ByteSizeRs485_2PropertyStructSpecs()
        self.v: int = 0


class ByteSizeRs485_2PropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 5
        self.max = 8


class BaudRateRs485_2PropertyStruct:
    def __init__(self) -> None:
        self.id = 'baudRate'
        self.name = '波特率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = BaudRateRs485_2PropertyStructSpecs()
        self.v: int = 0


class BaudRateRs485_2PropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2400
        self.max = 250000


class Rs485_1Property(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'rs485_1'
        self.name = '1号RS485口配置信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = Rs485_1PropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class Rs485_1PropertyStruct:
    def __init__(self) -> None:
        self.baudRate = BaudRateRs485_1PropertyStruct()
        self.byteSize = ByteSizeRs485_1PropertyStruct()
        self.stopBit = StopBitRs485_1PropertyStruct()
        self.parities = ParitiesRs485_1PropertyStruct()

    @property
    def v(self):
        return {'baudRate': self.baudRate.v, 'byteSize': self.byteSize.v, 'stopBit': self.stopBit.v, 'parities': self.parities.v}

    @v.setter
    def v(self, value):
        if value.get('baudRate') is not None: self.baudRate.v = value['baudRate']
        if value.get('byteSize') is not None: self.byteSize.v = value['byteSize']
        if value.get('stopBit') is not None: self.stopBit.v = value['stopBit']
        if value.get('parities') is not None: self.parities.v = value['parities']


class ParitiesRs485_1PropertyStruct:
    def __init__(self) -> None:
        self.id = 'parities'
        self.name = '校验'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = ParitiesRs485_1PropertyStructSpecs()
        self.v: str = ''


class ParitiesRs485_1PropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ParitiesRs485_1PropertyStructSpecsOptional()


class ParitiesRs485_1PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.N = NParitiesRs485_1PropertyStructSpecsOptional()
        self.E = EParitiesRs485_1PropertyStructSpecsOptional()
        self.O = OParitiesRs485_1PropertyStructSpecsOptional()
        self.M = MParitiesRs485_1PropertyStructSpecsOptional()
        self.S = SParitiesRs485_1PropertyStructSpecsOptional()


class SParitiesRs485_1PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'S'
        self.desc = '低'


class MParitiesRs485_1PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'M'
        self.desc = '高'


class OParitiesRs485_1PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'O'
        self.desc = '奇'


class EParitiesRs485_1PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'E'
        self.desc = '偶'


class NParitiesRs485_1PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'N'
        self.desc = '无'


class StopBitRs485_1PropertyStruct:
    def __init__(self) -> None:
        self.id = 'stopBit'
        self.name = '停止位'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = StopBitRs485_1PropertyStructSpecs()
        self.v: str = ''


class StopBitRs485_1PropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StopBitRs485_1PropertyStructSpecsOptional()


class StopBitRs485_1PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1StopBitRs485_1PropertyStructSpecsOptional()
        self.value1_5 = Value1_5StopBitRs485_1PropertyStructSpecsOptional()
        self.value2 = Value2StopBitRs485_1PropertyStructSpecsOptional()


class Value2StopBitRs485_1PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '2'
        self.desc = '2位'


class Value1_5StopBitRs485_1PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '1.5'
        self.desc = '1.5位'


class Value1StopBitRs485_1PropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '1'
        self.desc = '1位'


class ByteSizeRs485_1PropertyStruct:
    def __init__(self) -> None:
        self.id = 'byteSize'
        self.name = '数据位'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ByteSizeRs485_1PropertyStructSpecs()
        self.v: int = 0


class ByteSizeRs485_1PropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 5
        self.max = 8


class BaudRateRs485_1PropertyStruct:
    def __init__(self) -> None:
        self.id = 'baudRate'
        self.name = '波特率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = BaudRateRs485_1PropertyStructSpecs()
        self.v: int = 0


class BaudRateRs485_1PropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2400
        self.max = 250000


class ServerBProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'serverB'
        self.name = '无线MQTT服务器信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = ServerBPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ServerBPropertyStruct:
    def __init__(self) -> None:
        self.host = HostServerBPropertyStruct()
        self.port = PortServerBPropertyStruct()
        self.user = UserServerBPropertyStruct()
        self.password = PasswordServerBPropertyStruct()

    @property
    def v(self):
        return {'host': self.host.v, 'port': self.port.v, 'user': self.user.v, 'password': self.password.v}

    @v.setter
    def v(self, value):
        if value.get('host') is not None: self.host.v = value['host']
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('user') is not None: self.user.v = value['user']
        if value.get('password') is not None: self.password.v = value['password']


class PasswordServerBPropertyStruct:
    def __init__(self) -> None:
        self.id = 'password'
        self.name = '密码'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class UserServerBPropertyStruct:
    def __init__(self) -> None:
        self.id = 'user'
        self.name = '用户名'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class PortServerBPropertyStruct:
    def __init__(self) -> None:
        self.id = 'port'
        self.name = '端口'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.v: int = 0


class HostServerBPropertyStruct:
    def __init__(self) -> None:
        self.id = 'host'
        self.name = 'IP地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class ServerAProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'serverA'
        self.name = '有线MQTT服务器信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = ServerAPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ServerAPropertyStruct:
    def __init__(self) -> None:
        self.host = HostServerAPropertyStruct()
        self.port = PortServerAPropertyStruct()
        self.user = UserServerAPropertyStruct()
        self.password = PasswordServerAPropertyStruct()

    @property
    def v(self):
        return {'host': self.host.v, 'port': self.port.v, 'user': self.user.v, 'password': self.password.v}

    @v.setter
    def v(self, value):
        if value.get('host') is not None: self.host.v = value['host']
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('user') is not None: self.user.v = value['user']
        if value.get('password') is not None: self.password.v = value['password']


class PasswordServerAPropertyStruct:
    def __init__(self) -> None:
        self.id = 'password'
        self.name = '密码'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class UserServerAPropertyStruct:
    def __init__(self) -> None:
        self.id = 'user'
        self.name = '用户名'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class PortServerAPropertyStruct:
    def __init__(self) -> None:
        self.id = 'port'
        self.name = '端口'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.v: int = 0


class HostServerAPropertyStruct:
    def __init__(self) -> None:
        self.id = 'host'
        self.name = 'IP地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class HolterProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'holter'
        self.name = '动环信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = HolterPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class HolterPropertyStruct:
    def __init__(self) -> None:
        self.enabled = EnabledHolterPropertyStruct()
        self.interval = IntervalHolterPropertyStruct()
        self.alarmInterval = AlarmIntervalHolterPropertyStruct()
        self.do1Default = Do1DefaultHolterPropertyStruct()
        self.do2Default = Do2DefaultHolterPropertyStruct()
        self.di1 = Di1HolterPropertyStruct()
        self.di2 = Di2HolterPropertyStruct()
        self.do1 = Do1HolterPropertyStruct()
        self.do2 = Do2HolterPropertyStruct()
        self.eth = EthHolterPropertyStruct()
        self.tilt = TiltHolterPropertyStruct()
        self.temperature = TemperatureHolterPropertyStruct()
        self.humidity = HumidityHolterPropertyStruct()
        self.water = WaterHolterPropertyStruct()
        self.voip = VoipHolterPropertyStruct()

    @property
    def v(self):
        return {'enabled': self.enabled.v, 'interval': self.interval.v, 'alarmInterval': self.alarmInterval.v, 'do1Default': self.do1Default.v, 'do2Default': self.do2Default.v, 'di1': self.di1.v, 'di2': self.di2.v, 'do1': self.do1.v, 'do2': self.do2.v, 'eth': self.eth.v, 'tilt': self.tilt.v, 'temperature': self.temperature.v, 'humidity': self.humidity.v, 'water': self.water.v, 'voip': self.voip.v}

    @v.setter
    def v(self, value):
        if value.get('enabled') is not None: self.enabled.v = value['enabled']
        if value.get('interval') is not None: self.interval.v = value['interval']
        if value.get('alarmInterval') is not None: self.alarmInterval.v = value['alarmInterval']
        if value.get('do1Default') is not None: self.do1Default.v = value['do1Default']
        if value.get('do2Default') is not None: self.do2Default.v = value['do2Default']
        if value.get('di1') is not None: self.di1.v = value['di1']
        if value.get('di2') is not None: self.di2.v = value['di2']
        if value.get('do1') is not None: self.do1.v = value['do1']
        if value.get('do2') is not None: self.do2.v = value['do2']
        if value.get('eth') is not None: self.eth.v = value['eth']
        if value.get('tilt') is not None: self.tilt.v = value['tilt']
        if value.get('temperature') is not None: self.temperature.v = value['temperature']
        if value.get('humidity') is not None: self.humidity.v = value['humidity']
        if value.get('water') is not None: self.water.v = value['water']
        if value.get('voip') is not None: self.voip.v = value['voip']


class VoipHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'voip'
        self.name = '广播信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = VoipHolterPropertyStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class VoipHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.online = OnlineVoipHolterPropertyStructStruct()
        self.volume = VolumeVoipHolterPropertyStructStruct()
        self.busy = BusyVoipHolterPropertyStructStruct()

    @property
    def v(self):
        return {'online': self.online.v, 'volume': self.volume.v, 'busy': self.busy.v}

    @v.setter
    def v(self, value):
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('volume') is not None: self.volume.v = value['volume']
        if value.get('busy') is not None: self.busy.v = value['busy']


class BusyVoipHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'busy'
        self.name = '通话状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class VolumeVoipHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'volume'
        self.name = '音量'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = VolumeVoipHolterPropertyStructStructSpecs()
        self.v: int = 0


class VolumeVoipHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = '%'


class OnlineVoipHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'online'
        self.name = '在线状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class WaterHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'water'
        self.name = '水浸信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = WaterHolterPropertyStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class WaterHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.online = OnlineWaterHolterPropertyStructStruct()
        self.status = StatusWaterHolterPropertyStructStruct()

    @property
    def v(self):
        return {'online': self.online.v, 'status': self.status.v}

    @v.setter
    def v(self, value):
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('status') is not None: self.status.v = value['status']


class StatusWaterHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'status'
        self.name = '水浸状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class OnlineWaterHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'online'
        self.name = '在线状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class HumidityHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'humidity'
        self.name = '湿度信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = HumidityHolterPropertyStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class HumidityHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.online = OnlineHumidityHolterPropertyStructStruct()
        self.humidity = HumidityHumidityHolterPropertyStructStruct()
        self.hiThreshold = HiThresholdHumidityHolterPropertyStructStruct()
        self.lowThreshold = LowThresholdHumidityHolterPropertyStructStruct()
        self.type = TypeHumidityHolterPropertyStructStruct()
        self.alarming = AlarmingHumidityHolterPropertyStructStruct()

    @property
    def v(self):
        return {'online': self.online.v, 'humidity': self.humidity.v, 'hiThreshold': self.hiThreshold.v, 'lowThreshold': self.lowThreshold.v, 'type': self.type.v, 'alarming': self.alarming.v}

    @v.setter
    def v(self, value):
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('humidity') is not None: self.humidity.v = value['humidity']
        if value.get('hiThreshold') is not None: self.hiThreshold.v = value['hiThreshold']
        if value.get('lowThreshold') is not None: self.lowThreshold.v = value['lowThreshold']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('alarming') is not None: self.alarming.v = value['alarming']


class AlarmingHumidityHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'alarming'
        self.name = '告警状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class TypeHumidityHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'type'
        self.name = '告警类型'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = TypeHumidityHolterPropertyStructStructSpecs()
        self.v: str = ''


class TypeHumidityHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TypeHumidityHolterPropertyStructStructSpecsOptional()


class TypeHumidityHolterPropertyStructStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.hi = HiTypeHumidityHolterPropertyStructStructSpecsOptional()
        self.low = LowTypeHumidityHolterPropertyStructStructSpecsOptional()


class LowTypeHumidityHolterPropertyStructStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'low'
        self.desc = '低湿'


class HiTypeHumidityHolterPropertyStructStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'hi'
        self.desc = '高湿'


class LowThresholdHumidityHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'lowThreshold'
        self.name = '低湿告警值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = LowThresholdHumidityHolterPropertyStructStructSpecs()
        self.v: int = 0


class LowThresholdHumidityHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = '%'
        self.unitName = '相对湿度'


class HiThresholdHumidityHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'hiThreshold'
        self.name = '高湿告警值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = HiThresholdHumidityHolterPropertyStructStructSpecs()
        self.v: int = 0


class HiThresholdHumidityHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = '%'
        self.unitName = '相对湿度'


class HumidityHumidityHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'humidity'
        self.name = '湿度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = HumidityHumidityHolterPropertyStructStructSpecs()
        self.v: int = 0


class HumidityHumidityHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '%'
        self.unitName = '相对湿度'


class OnlineHumidityHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'online'
        self.name = '在线状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class TemperatureHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'temperature'
        self.name = '温度信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = TemperatureHolterPropertyStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class TemperatureHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.online = OnlineTemperatureHolterPropertyStructStruct()
        self.temperature = TemperatureTemperatureHolterPropertyStructStruct()
        self.hiThreshold = HiThresholdTemperatureHolterPropertyStructStruct()
        self.lowThreshold = LowThresholdTemperatureHolterPropertyStructStruct()
        self.type = TypeTemperatureHolterPropertyStructStruct()
        self.alarming = AlarmingTemperatureHolterPropertyStructStruct()

    @property
    def v(self):
        return {'online': self.online.v, 'temperature': self.temperature.v, 'hiThreshold': self.hiThreshold.v, 'lowThreshold': self.lowThreshold.v, 'type': self.type.v, 'alarming': self.alarming.v}

    @v.setter
    def v(self, value):
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('temperature') is not None: self.temperature.v = value['temperature']
        if value.get('hiThreshold') is not None: self.hiThreshold.v = value['hiThreshold']
        if value.get('lowThreshold') is not None: self.lowThreshold.v = value['lowThreshold']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('alarming') is not None: self.alarming.v = value['alarming']


class AlarmingTemperatureHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'alarming'
        self.name = '告警状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class TypeTemperatureHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'type'
        self.name = '告警类型'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = TypeTemperatureHolterPropertyStructStructSpecs()
        self.v: str = ''


class TypeTemperatureHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TypeTemperatureHolterPropertyStructStructSpecsOptional()


class TypeTemperatureHolterPropertyStructStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.hi = HiTypeTemperatureHolterPropertyStructStructSpecsOptional()
        self.low = LowTypeTemperatureHolterPropertyStructStructSpecsOptional()


class LowTypeTemperatureHolterPropertyStructStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'low'
        self.desc = '低温'


class HiTypeTemperatureHolterPropertyStructStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'hi'
        self.desc = '高温'


class LowThresholdTemperatureHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'lowThreshold'
        self.name = '低温告警值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = LowThresholdTemperatureHolterPropertyStructStructSpecs()
        self.v: int = 0


class LowThresholdTemperatureHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -50
        self.max = 100
        self.unit = '°C'
        self.unitName = '摄氏度'


class HiThresholdTemperatureHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'hiThreshold'
        self.name = '高温告警值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = HiThresholdTemperatureHolterPropertyStructStructSpecs()
        self.v: int = 0


class HiThresholdTemperatureHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -50
        self.max = 100
        self.unit = '°C'
        self.unitName = '摄氏度'


class TemperatureTemperatureHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'temperature'
        self.name = '温度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = TemperatureTemperatureHolterPropertyStructStructSpecs()
        self.v: int = 0


class TemperatureTemperatureHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '°C'
        self.unitName = '摄氏度'


class OnlineTemperatureHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'online'
        self.name = '在线状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class TiltHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'tilt'
        self.name = '倾斜信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = TiltHolterPropertyStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class TiltHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.online = OnlineTiltHolterPropertyStructStruct()
        self.angle = AngleTiltHolterPropertyStructStruct()
        self.threshold = ThresholdTiltHolterPropertyStructStruct()
        self.alarming = AlarmingTiltHolterPropertyStructStruct()

    @property
    def v(self):
        return {'online': self.online.v, 'angle': self.angle.v, 'threshold': self.threshold.v, 'alarming': self.alarming.v}

    @v.setter
    def v(self, value):
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('angle') is not None: self.angle.v = value['angle']
        if value.get('threshold') is not None: self.threshold.v = value['threshold']
        if value.get('alarming') is not None: self.alarming.v = value['alarming']


class AlarmingTiltHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'alarming'
        self.name = '告警状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class ThresholdTiltHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'threshold'
        self.name = '告警值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ThresholdTiltHolterPropertyStructStructSpecs()
        self.v: int = 0


class ThresholdTiltHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 5
        self.max = 30
        self.unit = '°'
        self.unitName = '度'


class AngleTiltHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'angle'
        self.name = '倾斜角度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = AngleTiltHolterPropertyStructStructSpecs()
        self.v: int = 0


class AngleTiltHolterPropertyStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -1
        self.max = 30
        self.unit = '°'
        self.unitName = '度'


class OnlineTiltHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'online'
        self.name = '在线状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class EthHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'eth'
        self.name = '网口连接状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = EthHolterPropertyStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class EthHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.port1 = Port1EthHolterPropertyStructStruct()
        self.port2 = Port2EthHolterPropertyStructStruct()
        self.port3 = Port3EthHolterPropertyStructStruct()
        self.port4 = Port4EthHolterPropertyStructStruct()

    @property
    def v(self):
        return {'port1': self.port1.v, 'port2': self.port2.v, 'port3': self.port3.v, 'port4': self.port4.v}

    @v.setter
    def v(self, value):
        if value.get('port1') is not None: self.port1.v = value['port1']
        if value.get('port2') is not None: self.port2.v = value['port2']
        if value.get('port3') is not None: self.port3.v = value['port3']
        if value.get('port4') is not None: self.port4.v = value['port4']


class Port4EthHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'port4'
        self.name = '网口4状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class Port3EthHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'port3'
        self.name = '网口3状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class Port2EthHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'port2'
        self.name = '网口2状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class Port1EthHolterPropertyStructStruct:
    def __init__(self) -> None:
        self.id = 'port1'
        self.name = '网口1状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class Do2HolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'do2'
        self.name = 'DO2状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class Do1HolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'do1'
        self.name = 'DO1状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class Di2HolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'di2'
        self.name = 'DI2状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class Di1HolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'di1'
        self.name = 'DI1状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class Do2DefaultHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'do2Default'
        self.name = 'DO2默认状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class Do1DefaultHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'do1Default'
        self.name = 'DO1默认状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class AlarmIntervalHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'alarmInterval'
        self.name = '告警上报间隔'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = AlarmIntervalHolterPropertyStructSpecs()
        self.v: int = 0


class AlarmIntervalHolterPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 10
        self.max = 65535
        self.unit = 's'
        self.unitName = '秒'


class IntervalHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'interval'
        self.name = '定时上报间隔'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = IntervalHolterPropertyStructSpecs()
        self.v: int = 0


class IntervalHolterPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 10
        self.max = 65535
        self.unit = 's'
        self.unitName = '秒'


class EnabledHolterPropertyStruct:
    def __init__(self) -> None:
        self.id = 'enabled'
        self.name = '定时上报开关'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class VoipServerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'voipServer'
        self.name = '广播服务器信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = VoipServerPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class VoipServerPropertyStruct:
    def __init__(self) -> None:
        self.host = HostVoipServerPropertyStruct()
        self.port = PortVoipServerPropertyStruct()

    @property
    def v(self):
        return {'host': self.host.v, 'port': self.port.v}

    @v.setter
    def v(self, value):
        if value.get('host') is not None: self.host.v = value['host']
        if value.get('port') is not None: self.port.v = value['port']


class PortVoipServerPropertyStruct:
    def __init__(self) -> None:
        self.id = 'port'
        self.name = '端口'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.v: int = 0


class HostVoipServerPropertyStruct:
    def __init__(self) -> None:
        self.id = 'host'
        self.name = '地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class HwVersionProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'hwVersion'
        self.name = '硬件版本'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class FwVersionProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'fwVersion'
        self.name = '软件版本'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class TimeProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'time'
        self.name = '系统时间'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.format = 'date-time'
        self.v: str = ''


class UpTimeProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'upTime'
        self.name = '系统启动时长'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = UpTimePropertySpecs()
        self.v: str = ''


class UpTimePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'S'
        self.unitName = '秒'


class NtpInfoProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'ntpInfo'
        self.name = 'NTP信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = NtpInfoPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class NtpInfoPropertyStruct:
    def __init__(self) -> None:
        self.ntpStatus = NtpStatusNtpInfoPropertyStruct()
        self.hostA = HostANtpInfoPropertyStruct()
        self.hostB = HostBNtpInfoPropertyStruct()

    @property
    def v(self):
        return {'ntpStatus': self.ntpStatus.v, 'hostA': self.hostA.v, 'hostB': self.hostB.v}

    @v.setter
    def v(self, value):
        if value.get('ntpStatus') is not None: self.ntpStatus.v = value['ntpStatus']
        if value.get('hostA') is not None: self.hostA.v = value['hostA']
        if value.get('hostB') is not None: self.hostB.v = value['hostB']


class HostBNtpInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'hostB'
        self.name = '备NTP校时服务器'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class HostANtpInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'hostA'
        self.name = '主NTP校时服务器'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class NtpStatusNtpInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'ntpStatus'
        self.name = 'NTP校时状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class MqttPrefixProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'mqttPrefix'
        self.name = 'MQTT Topic 前缀'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class NetworkInfoProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'networkInfo'
        self.name = '网络信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = NetworkInfoPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class NetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.networkType = NetworkTypeNetworkInfoPropertyStruct()
        self.wirelessSupport = WirelessSupportNetworkInfoPropertyStruct()
        self.networkAvailable = NetworkAvailableNetworkInfoPropertyStruct()
        self.mac = MacNetworkInfoPropertyStruct()
        self.dhcp = DhcpNetworkInfoPropertyStruct()
        self.ip = IpNetworkInfoPropertyStruct()
        self.gateway = GatewayNetworkInfoPropertyStruct()
        self.mask = MaskNetworkInfoPropertyStruct()

    @property
    def v(self):
        return {'networkType': self.networkType.v, 'wirelessSupport': self.wirelessSupport.v, 'networkAvailable': self.networkAvailable.v, 'mac': self.mac.v, 'dhcp': self.dhcp.v, 'ip': self.ip.v, 'gateway': self.gateway.v, 'mask': self.mask.v}

    @v.setter
    def v(self, value):
        if value.get('networkType') is not None: self.networkType.v = value['networkType']
        if value.get('wirelessSupport') is not None: self.wirelessSupport.v = value['wirelessSupport']
        if value.get('networkAvailable') is not None: self.networkAvailable.v = value['networkAvailable']
        if value.get('mac') is not None: self.mac.v = value['mac']
        if value.get('dhcp') is not None: self.dhcp.v = value['dhcp']
        if value.get('ip') is not None: self.ip.v = value['ip']
        if value.get('gateway') is not None: self.gateway.v = value['gateway']
        if value.get('mask') is not None: self.mask.v = value['mask']


class MaskNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'mask'
        self.name = '子网掩码'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class GatewayNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'gateway'
        self.name = '网关'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class IpNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'ip'
        self.name = 'IP地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.format = 'ipv4'
        self.v: str = ''


class DhcpNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'dhcp'
        self.name = '是否启用DHCP'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class MacNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'mac'
        self.name = 'MAC地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class NetworkAvailableNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'networkAvailable'
        self.name = '是否支持有线网络'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class WirelessSupportNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'wirelessSupport'
        self.name = '支持的无线网络'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = WirelessSupportNetworkInfoPropertyStructSpecs()
        self.v: str = ''


class WirelessSupportNetworkInfoPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = WirelessSupportNetworkInfoPropertyStructSpecsOptional()


class WirelessSupportNetworkInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.none = NoneWirelessSupportNetworkInfoPropertyStructSpecsOptional()
        self.value4G = Value4GWirelessSupportNetworkInfoPropertyStructSpecsOptional()
        self.value5G = Value5GWirelessSupportNetworkInfoPropertyStructSpecsOptional()


class Value5GWirelessSupportNetworkInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '5G'
        self.desc = '支持5G无线网络'


class Value4GWirelessSupportNetworkInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '4G'
        self.desc = '支持4G无线网络'


class NoneWirelessSupportNetworkInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'none'
        self.desc = '不支持无线网络'


class NetworkTypeNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'networkType'
        self.name = '网络类型'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = NetworkTypeNetworkInfoPropertyStructSpecs()
        self.v: str = ''


class NetworkTypeNetworkInfoPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = NetworkTypeNetworkInfoPropertyStructSpecsOptional()


class NetworkTypeNetworkInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.wired = WiredNetworkTypeNetworkInfoPropertyStructSpecsOptional()
        self.value4G = Value4GNetworkTypeNetworkInfoPropertyStructSpecsOptional()
        self.value5G = Value5GNetworkTypeNetworkInfoPropertyStructSpecsOptional()


class Value5GNetworkTypeNetworkInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '5G'
        self.desc = '5G'


class Value4GNetworkTypeNetworkInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = '4G'
        self.desc = '4G'


class WiredNetworkTypeNetworkInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'wired'
        self.desc = '有线'


class ModelProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'model'
        self.name = '设备型号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class SnProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'sn'
        self.name = '设备序列号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''
