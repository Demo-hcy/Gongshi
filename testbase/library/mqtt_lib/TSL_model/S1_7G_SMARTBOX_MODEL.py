from .base_model import *


class S1_QG_SMARTBOX(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S1_7G_SMARTBOX'
        self.productName = '智慧盒'
        self.properties = Properties()
        self.events = Events()
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.reboot = RebootService()
        self.switchMode = SwitchModeService()
        self.updateFirmware = UpdateFirmwareService()
        self.updateApp = UpdateAppService()
        self.startReport = StartReportService()
        self.stopReport = StopReportService()
        self.addRule = AddRuleService()
        self.updateRule = UpdateRuleService()
        self.deleteRuleByUuid = DeleteRuleByUuidService()
        self.clearAllRule = ClearAllRuleService()
        self.getAllRules = GetAllRulesService()
        self.getRulesByUuids = GetRulesByUuidsService()
        self.enableRule = EnableRuleService()
        self.disableRule = DisableRuleService()
        self.stopLinkageRuleRunning = StopLinkageRuleRunningService()
        self.outsideLinkage = OutsideLinkageService()
        self.manualControl = ManualControlService()
        self.stopManualControl = StopManualControlService()
        self.setNtpHostList = SetNtpHostListService()
        self.setMqttBroker = SetMqttBrokerService()
        self.setMqttBrokerBackup = SetMqttBrokerBackupService()
        self.editSmartBox = EditSmartBoxService()
        self.editSubDev = EditSubDevService()
        self.addSubDevs = AddSubDevsService()
        self.delSubDevs = DelSubDevsService()
        self.getAllSubDevs = GetAllSubDevsService()
        self.getSubDevs = GetSubDevsService()


class GetSubDevsService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'getSubDevs'
        self.name = '批量获取子设备'
        self.parameters = GetSubDevsServiceParameters()
        self.output = [GetSubDevsServiceOutput()]


class GetSubDevsServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.subDevs = SubDevsGetSubDevsServiceOutput()

    @property
    def v(self):
        return {'subDevs': self.subDevs.v}

    @v.setter
    def v(self, value):
        if value.get('subDevs') is not None: self.subDevs.v = value['subDevs']


class SubDevsGetSubDevsServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'subDevs'
        self.name = '设备信息列表'
        self.type = 'array'
        self.columnComplex = [SubDevsGetSubDevsServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = SubDevsGetSubDevsServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class SubDevsGetSubDevsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.productId = ProductIdSubDevsGetSubDevsServiceOutputColumnComplexStruct()
        self.devId = DevIdSubDevsGetSubDevsServiceOutputColumnComplexStruct()
        self.devType = DevTypeSubDevsGetSubDevsServiceOutputColumnComplexStruct()
        self.setting = SettingSubDevsGetSubDevsServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'productId': self.productId.v, 'devId': self.devId.v, 'devType': self.devType.v, 'setting': self.setting.v}

    @v.setter
    def v(self, value):
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('devType') is not None: self.devType.v = value['devType']
        if value.get('setting') is not None: self.setting.v = value['setting']


class SettingSubDevsGetSubDevsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'setting'
        self.name = '设备配置'
        self.type = 'string'
        self.v: str = ''


class DevTypeSubDevsGetSubDevsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devType'
        self.name = '设备类型'
        self.type = 'string'
        self.specs = DevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecs()
        self.v: str = ''


class DevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = DevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()


class DevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.GW = GWDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.IPCOnvif = IPCOnvifDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.SOSOnvif = SOSOnvifDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Trafficscreen = TrafficscreenDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Projector = ProjectorDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Power = PowerDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Rfid = RfidDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Lamp = LampDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Sensor = SensorDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Locker = LockerDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Breaker = BreakerDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Inforscreen = InforscreenDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.AI = AIDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Brocast = BrocastDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional()


class BrocastDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Brocast'
        self.desc = '广播'


class AIDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'AI'
        self.desc = 'AI'


class InforscreenDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Inforscreen'
        self.desc = '信息屏'


class BreakerDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Breaker'
        self.desc = '断路器'


class LockerDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Locker'
        self.desc = '锁'


class SensorDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Sensor'
        self.desc = '传感器'


class LampDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Lamp'
        self.desc = '灯控设备'


class RfidDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Rfid'
        self.desc = '读卡器'


class PowerDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Power'
        self.desc = '智能电源'


class ProjectorDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Projector'
        self.desc = '投影仪'


class TrafficscreenDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Trafficscreen'
        self.desc = '交通屏'


class SOSOnvifDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'SOSOnvif'
        self.desc = '一键报警'


class IPCOnvifDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'IPCOnvif'
        self.desc = 'Onvif摄像头'


class GWDevTypeSubDevsGetSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'GW'
        self.desc = '网关设备'


class DevIdSubDevsGetSubDevsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devId'
        self.name = '设备实例ID'
        self.type = 'string'
        self.v: str = ''


class ProductIdSubDevsGetSubDevsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'productId'
        self.name = '产品ID'
        self.type = 'string'
        self.v: str = ''


class GetSubDevsServiceParameters:
    def __init__(self) -> None:
        self.productInfos = ProductInfosGetSubDevsServiceParameter()

    @property
    def v(self):
        return {'productInfos': self.productInfos.v}

    @v.setter
    def v(self, value):
        if value.get('productInfos') is not None: self.productInfos.v = value['productInfos']


class ProductInfosGetSubDevsServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'productInfos'
        self.name = '设备信息列表'
        self.type = 'array'
        self.columnComplex = [ProductInfosGetSubDevsServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ProductInfosGetSubDevsServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ProductInfosGetSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.productId = ProductIdProductInfosGetSubDevsServiceParameterColumnComplexStruct()
        self.devId = DevIdProductInfosGetSubDevsServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'productId': self.productId.v, 'devId': self.devId.v}

    @v.setter
    def v(self, value):
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('devId') is not None: self.devId.v = value['devId']


class DevIdProductInfosGetSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devId'
        self.name = '设备实例ID'
        self.type = 'string'
        self.v: str = ''


class ProductIdProductInfosGetSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'productId'
        self.name = '产品ID'
        self.type = 'string'
        self.v: str = ''


class GetAllSubDevsService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'getAllSubDevs'
        self.name = '获取所有子设备'
        self.parameters = None
        self.output = [GetAllSubDevsServiceOutput()]


class GetAllSubDevsServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.subDevs = SubDevsGetAllSubDevsServiceOutput()

    @property
    def v(self):
        return {'subDevs': self.subDevs.v}

    @v.setter
    def v(self, value):
        if value.get('subDevs') is not None: self.subDevs.v = value['subDevs']


class SubDevsGetAllSubDevsServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'subDevs'
        self.name = '设备信息列表'
        self.type = 'array'
        self.columnComplex = [SubDevsGetAllSubDevsServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = SubDevsGetAllSubDevsServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class SubDevsGetAllSubDevsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.productId = ProductIdSubDevsGetAllSubDevsServiceOutputColumnComplexStruct()
        self.devId = DevIdSubDevsGetAllSubDevsServiceOutputColumnComplexStruct()
        self.devType = DevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStruct()
        self.setting = SettingSubDevsGetAllSubDevsServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'productId': self.productId.v, 'devId': self.devId.v, 'devType': self.devType.v, 'setting': self.setting.v}

    @v.setter
    def v(self, value):
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('devType') is not None: self.devType.v = value['devType']
        if value.get('setting') is not None: self.setting.v = value['setting']


class SettingSubDevsGetAllSubDevsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'setting'
        self.name = '设备配置'
        self.type = 'string'
        self.v: str = ''


class DevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devType'
        self.name = '设备类型'
        self.type = 'string'
        self.specs = DevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecs()
        self.v: str = ''


class DevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = DevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()


class DevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.GW = GWDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.IPCOnvif = IPCOnvifDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.SOSOnvif = SOSOnvifDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Trafficscreen = TrafficscreenDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Projector = ProjectorDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Power = PowerDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Rfid = RfidDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Lamp = LampDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Sensor = SensorDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Locker = LockerDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Breaker = BreakerDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Inforscreen = InforscreenDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.AI = AIDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()
        self.Brocast = BrocastDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional()


class BrocastDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Brocast'
        self.desc = '广播'


class AIDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'AI'
        self.desc = 'AI'


class InforscreenDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Inforscreen'
        self.desc = '信息屏'


class BreakerDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Breaker'
        self.desc = '断路器'


class LockerDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Locker'
        self.desc = '锁'


class SensorDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Sensor'
        self.desc = '传感器'


class LampDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Lamp'
        self.desc = '灯控设备'


class RfidDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Rfid'
        self.desc = '读卡器'


class PowerDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Power'
        self.desc = '智能电源'


class ProjectorDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Projector'
        self.desc = '投影仪'


class TrafficscreenDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Trafficscreen'
        self.desc = '交通屏'


class SOSOnvifDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'SOSOnvif'
        self.desc = '一键报警'


class IPCOnvifDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'IPCOnvif'
        self.desc = 'Onvif摄像头'


class GWDevTypeSubDevsGetAllSubDevsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'GW'
        self.desc = '网关设备'


class DevIdSubDevsGetAllSubDevsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devId'
        self.name = '设备实例ID'
        self.type = 'string'
        self.v: str = ''


class ProductIdSubDevsGetAllSubDevsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'productId'
        self.name = '产品ID'
        self.type = 'string'
        self.v: str = ''


class DelSubDevsService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'delSubDevs'
        self.name = '批量删除子设备'
        self.parameters = DelSubDevsServiceParameters()


class DelSubDevsServiceParameters:
    def __init__(self) -> None:
        self.productInfos = ProductInfosDelSubDevsServiceParameter()

    @property
    def v(self):
        return {'productInfos': self.productInfos.v}

    @v.setter
    def v(self, value):
        if value.get('productInfos') is not None: self.productInfos.v = value['productInfos']


class ProductInfosDelSubDevsServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'productInfos'
        self.name = '设备信息列表'
        self.type = 'array'
        self.columnComplex = [ProductInfosDelSubDevsServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ProductInfosDelSubDevsServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ProductInfosDelSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.productId = ProductIdProductInfosDelSubDevsServiceParameterColumnComplexStruct()
        self.devId = DevIdProductInfosDelSubDevsServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'productId': self.productId.v, 'devId': self.devId.v}

    @v.setter
    def v(self, value):
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('devId') is not None: self.devId.v = value['devId']


class DevIdProductInfosDelSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devId'
        self.name = '设备实例ID'
        self.type = 'string'
        self.v: str = ''


class ProductIdProductInfosDelSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'productId'
        self.name = '产品ID'
        self.type = 'string'
        self.v: str = ''


class AddSubDevsService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'addSubDevs'
        self.name = '批量添加子设备'
        self.parameters = AddSubDevsServiceParameters()


class AddSubDevsServiceParameters:
    def __init__(self) -> None:
        self.devInfos = DevInfosAddSubDevsServiceParameter()

    @property
    def v(self):
        return {'devInfos': self.devInfos.v}

    @v.setter
    def v(self, value):
        if value.get('devInfos') is not None: self.devInfos.v = value['devInfos']


class DevInfosAddSubDevsServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'devInfos'
        self.name = '设备信息列表'
        self.type = 'array'
        self.columnComplex = [DevInfosAddSubDevsServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DevInfosAddSubDevsServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DevInfosAddSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.productId = ProductIdDevInfosAddSubDevsServiceParameterColumnComplexStruct()
        self.devId = DevIdDevInfosAddSubDevsServiceParameterColumnComplexStruct()
        self.devType = DevTypeDevInfosAddSubDevsServiceParameterColumnComplexStruct()
        self.setting = SettingDevInfosAddSubDevsServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'productId': self.productId.v, 'devId': self.devId.v, 'devType': self.devType.v, 'setting': self.setting.v}

    @v.setter
    def v(self, value):
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('devType') is not None: self.devType.v = value['devType']
        if value.get('setting') is not None: self.setting.v = value['setting']


class SettingDevInfosAddSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'setting'
        self.name = '设备配置'
        self.type = 'string'
        self.v: str = ''


class DevTypeDevInfosAddSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devType'
        self.name = '设备类型'
        self.type = 'string'
        self.specs = DevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecs()
        self.v: str = ''


class DevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = DevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()


class DevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.GW = GWDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.IPCOnvif = IPCOnvifDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.SOSOnvif = SOSOnvifDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.Trafficscreen = TrafficscreenDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.Projector = ProjectorDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.Power = PowerDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.Rfid = RfidDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.Lamp = LampDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.Sensor = SensorDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.Locker = LockerDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.Breaker = BreakerDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.Inforscreen = InforscreenDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.AI = AIDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()
        self.Brocast = BrocastDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional()


class BrocastDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Brocast'
        self.desc = '广播'


class AIDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'AI'
        self.desc = 'AI'


class InforscreenDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Inforscreen'
        self.desc = '信息屏'


class BreakerDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Breaker'
        self.desc = '断路器'


class LockerDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Locker'
        self.desc = '锁'


class SensorDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Sensor'
        self.desc = '传感器'


class LampDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Lamp'
        self.desc = '灯控设备'


class RfidDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Rfid'
        self.desc = '读卡器'


class PowerDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Power'
        self.desc = '智能电源'


class ProjectorDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Projector'
        self.desc = '投影仪'


class TrafficscreenDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Trafficscreen'
        self.desc = '交通屏'


class SOSOnvifDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'SOSOnvif'
        self.desc = '一键报警'


class IPCOnvifDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'IPCOnvif'
        self.desc = 'Onvif摄像头'


class GWDevTypeDevInfosAddSubDevsServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'GW'
        self.desc = '网关设备'


class DevIdDevInfosAddSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devId'
        self.name = '设备实例ID'
        self.type = 'string'
        self.v: str = ''


class ProductIdDevInfosAddSubDevsServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'productId'
        self.name = '产品ID'
        self.type = 'string'
        self.v: str = ''


class EditSubDevService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'editSubDev'
        self.name = '更新子设备'
        self.parameters = EditSubDevServiceParameters()


class EditSubDevServiceParameters:
    def __init__(self) -> None:
        self.devInfos = DevInfosEditSubDevServiceParameter()

    @property
    def v(self):
        return {'devInfos': self.devInfos.v}

    @v.setter
    def v(self, value):
        if value.get('devInfos') is not None: self.devInfos.v = value['devInfos']


class DevInfosEditSubDevServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'devInfos'
        self.name = '设备信息'
        self.type = 'array'
        self.columnComplex = [DevInfosEditSubDevServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DevInfosEditSubDevServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DevInfosEditSubDevServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.productId = ProductIdDevInfosEditSubDevServiceParameterColumnComplexStruct()
        self.devId = DevIdDevInfosEditSubDevServiceParameterColumnComplexStruct()
        self.devType = DevTypeDevInfosEditSubDevServiceParameterColumnComplexStruct()
        self.setting = SettingDevInfosEditSubDevServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'productId': self.productId.v, 'devId': self.devId.v, 'devType': self.devType.v, 'setting': self.setting.v}

    @v.setter
    def v(self, value):
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('devType') is not None: self.devType.v = value['devType']
        if value.get('setting') is not None: self.setting.v = value['setting']


class SettingDevInfosEditSubDevServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'setting'
        self.name = '设备配置'
        self.type = 'string'
        self.v: str = ''


class DevTypeDevInfosEditSubDevServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devType'
        self.name = '设备类型'
        self.type = 'string'
        self.specs = DevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecs()
        self.v: str = ''


class DevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = DevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()


class DevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.GW = GWDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.IPCOnvif = IPCOnvifDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.SOSOnvif = SOSOnvifDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.Trafficscreen = TrafficscreenDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.Projector = ProjectorDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.Power = PowerDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.Rfid = RfidDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.Lamp = LampDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.Sensor = SensorDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.Locker = LockerDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.Breaker = BreakerDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.Inforscreen = InforscreenDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.AI = AIDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()
        self.Brocast = BrocastDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional()


class BrocastDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Brocast'
        self.desc = '广播'


class AIDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'AI'
        self.desc = 'AI'


class InforscreenDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Inforscreen'
        self.desc = '信息屏'


class BreakerDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Breaker'
        self.desc = '断路器'


class LockerDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Locker'
        self.desc = '锁'


class SensorDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Sensor'
        self.desc = '传感器'


class LampDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Lamp'
        self.desc = '灯控设备'


class RfidDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Rfid'
        self.desc = '读卡器'


class PowerDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Power'
        self.desc = '智能电源'


class ProjectorDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Projector'
        self.desc = '投影仪'


class TrafficscreenDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Trafficscreen'
        self.desc = '交通屏'


class SOSOnvifDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'SOSOnvif'
        self.desc = '一键报警'


class IPCOnvifDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'IPCOnvif'
        self.desc = 'Onvif摄像头'


class GWDevTypeDevInfosEditSubDevServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'GW'
        self.desc = '网关设备'


class DevIdDevInfosEditSubDevServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devId'
        self.name = '设备实例ID'
        self.type = 'string'
        self.v: str = ''


class ProductIdDevInfosEditSubDevServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'productId'
        self.name = '产品ID'
        self.type = 'string'
        self.v: str = ''


class EditSmartBoxService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'editSmartBox'
        self.name = '修改智慧盒配置'
        self.parameters = EditSmartBoxServiceParameters()


class EditSmartBoxServiceParameters:
    def __init__(self) -> None:
        self.devInfos = DevInfosEditSmartBoxServiceParameter()

    @property
    def v(self):
        return {'devInfos': self.devInfos.v}

    @v.setter
    def v(self, value):
        if value.get('devInfos') is not None: self.devInfos.v = value['devInfos']


class DevInfosEditSmartBoxServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'devInfos'
        self.name = '设备信息'
        self.type = 'array'
        self.columnComplex = [DevInfosEditSmartBoxServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DevInfosEditSmartBoxServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DevInfosEditSmartBoxServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.productId = ProductIdDevInfosEditSmartBoxServiceParameterColumnComplexStruct()
        self.devId = DevIdDevInfosEditSmartBoxServiceParameterColumnComplexStruct()
        self.devType = DevTypeDevInfosEditSmartBoxServiceParameterColumnComplexStruct()
        self.setting = SettingDevInfosEditSmartBoxServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'productId': self.productId.v, 'devId': self.devId.v, 'devType': self.devType.v, 'setting': self.setting.v}

    @v.setter
    def v(self, value):
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('devType') is not None: self.devType.v = value['devType']
        if value.get('setting') is not None: self.setting.v = value['setting']


class SettingDevInfosEditSmartBoxServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'setting'
        self.name = '设备配置'
        self.type = 'string'
        self.v: str = ''


class DevTypeDevInfosEditSmartBoxServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devType'
        self.name = '设备类型'
        self.type = 'string'
        self.specs = DevTypeDevInfosEditSmartBoxServiceParameterColumnComplexStructSpecs()
        self.v: str = ''


class DevTypeDevInfosEditSmartBoxServiceParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = DevTypeDevInfosEditSmartBoxServiceParameterColumnComplexStructSpecsOptional()


class DevTypeDevInfosEditSmartBoxServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.GW = GWDevTypeDevInfosEditSmartBoxServiceParameterColumnComplexStructSpecsOptional()


class GWDevTypeDevInfosEditSmartBoxServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'GW'
        self.desc = '网关设备'


class DevIdDevInfosEditSmartBoxServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devId'
        self.name = '设备实例ID'
        self.type = 'string'
        self.v: str = ''


class ProductIdDevInfosEditSmartBoxServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'productId'
        self.name = '产品ID'
        self.type = 'string'
        self.v: str = ''


class SetMqttBrokerBackupService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setMqttBrokerBackup'
        self.name = '设置无线mqtt服务器信息'
        self.parameters = SetMqttBrokerBackupServiceParameters()


class SetMqttBrokerBackupServiceParameters:
    def __init__(self) -> None:
        self.mqttInfo = MqttInfoSetMqttBrokerBackupServiceParameter()

    @property
    def v(self):
        return {'mqttInfo': self.mqttInfo.v}

    @v.setter
    def v(self, value):
        if value.get('mqttInfo') is not None: self.mqttInfo.v = value['mqttInfo']


class MqttInfoSetMqttBrokerBackupServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'mqttInfo'
        self.name = 'mqtt服务器信息'
        self.type = 'struct'
        self.struct = MqttInfoSetMqttBrokerBackupServiceParameterStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class MqttInfoSetMqttBrokerBackupServiceParameterStruct:
    def __init__(self) -> None:
        self.host = HostMqttInfoSetMqttBrokerBackupServiceParameterStruct()
        self.port = PortMqttInfoSetMqttBrokerBackupServiceParameterStruct()
        self.userName = UserNameMqttInfoSetMqttBrokerBackupServiceParameterStruct()
        self.passwd = PasswdMqttInfoSetMqttBrokerBackupServiceParameterStruct()

    @property
    def v(self):
        return {'host': self.host.v, 'port': self.port.v, 'userName': self.userName.v, 'passwd': self.passwd.v}

    @v.setter
    def v(self, value):
        if value.get('host') is not None: self.host.v = value['host']
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('userName') is not None: self.userName.v = value['userName']
        if value.get('passwd') is not None: self.passwd.v = value['passwd']


class PasswdMqttInfoSetMqttBrokerBackupServiceParameterStruct:
    def __init__(self) -> None:
        self.id = 'passwd'
        self.name = '密码'
        self.type = 'string'
        self.v: str = ''


class UserNameMqttInfoSetMqttBrokerBackupServiceParameterStruct:
    def __init__(self) -> None:
        self.id = 'userName'
        self.name = '用户名'
        self.type = 'string'
        self.v: str = ''


class PortMqttInfoSetMqttBrokerBackupServiceParameterStruct:
    def __init__(self) -> None:
        self.id = 'port'
        self.name = '端口'
        self.type = 'integer'
        self.specs = PortMqttInfoSetMqttBrokerBackupServiceParameterStructSpecs()
        self.v: int = 0


class PortMqttInfoSetMqttBrokerBackupServiceParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 65535


class HostMqttInfoSetMqttBrokerBackupServiceParameterStruct:
    def __init__(self) -> None:
        self.id = 'host'
        self.name = 'mqtt服务器地址'
        self.type = 'string'
        self.v: str = ''


class SetMqttBrokerService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setMqttBroker'
        self.name = '设置有线mqtt服务器信息'
        self.parameters = SetMqttBrokerServiceParameters()


class SetMqttBrokerServiceParameters:
    def __init__(self) -> None:
        self.mqttInfo = MqttInfoSetMqttBrokerServiceParameter()

    @property
    def v(self):
        return {'mqttInfo': self.mqttInfo.v}

    @v.setter
    def v(self, value):
        if value.get('mqttInfo') is not None: self.mqttInfo.v = value['mqttInfo']


class MqttInfoSetMqttBrokerServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'mqttInfo'
        self.name = 'mqtt服务器信息'
        self.type = 'struct'
        self.struct = MqttInfoSetMqttBrokerServiceParameterStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class MqttInfoSetMqttBrokerServiceParameterStruct:
    def __init__(self) -> None:
        self.host = HostMqttInfoSetMqttBrokerServiceParameterStruct()
        self.port = PortMqttInfoSetMqttBrokerServiceParameterStruct()
        self.userName = UserNameMqttInfoSetMqttBrokerServiceParameterStruct()
        self.passwd = PasswdMqttInfoSetMqttBrokerServiceParameterStruct()

    @property
    def v(self):
        return {'host': self.host.v, 'port': self.port.v, 'userName': self.userName.v, 'passwd': self.passwd.v}

    @v.setter
    def v(self, value):
        if value.get('host') is not None: self.host.v = value['host']
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('userName') is not None: self.userName.v = value['userName']
        if value.get('passwd') is not None: self.passwd.v = value['passwd']


class PasswdMqttInfoSetMqttBrokerServiceParameterStruct:
    def __init__(self) -> None:
        self.id = 'passwd'
        self.name = '密码'
        self.type = 'string'
        self.v: str = ''


class UserNameMqttInfoSetMqttBrokerServiceParameterStruct:
    def __init__(self) -> None:
        self.id = 'userName'
        self.name = '用户名'
        self.type = 'string'
        self.v: str = ''


class PortMqttInfoSetMqttBrokerServiceParameterStruct:
    def __init__(self) -> None:
        self.id = 'port'
        self.name = '端口'
        self.type = 'integer'
        self.specs = PortMqttInfoSetMqttBrokerServiceParameterStructSpecs()
        self.v: int = 0


class PortMqttInfoSetMqttBrokerServiceParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 65535


class HostMqttInfoSetMqttBrokerServiceParameterStruct:
    def __init__(self) -> None:
        self.id = 'host'
        self.name = 'mqtt服务器地址'
        self.type = 'string'
        self.v: str = ''


class SetNtpHostListService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setNtpHostList'
        self.name = '设置ntp校时服务器地址'
        self.parameters = SetNtpHostListServiceParameters()


class SetNtpHostListServiceParameters:
    def __init__(self) -> None:
        self.ntpHostList = NtpHostListSetNtpHostListServiceParameter()

    @property
    def v(self):
        return {'ntpHostList': self.ntpHostList.v}

    @v.setter
    def v(self, value):
        if value.get('ntpHostList') is not None: self.ntpHostList.v = value['ntpHostList']


class NtpHostListSetNtpHostListServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'ntpHostList'
        self.name = 'ntp校时服务器地址列表'
        self.type = 'array'
        self.columnSimple = [NtpHostListSetNtpHostListServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = NtpHostListSetNtpHostListServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class NtpHostListSetNtpHostListServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class StopManualControlService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'stopManualControl'
        self.name = '取消手动控制'
        self.parameters = StopManualControlServiceParameters()


class StopManualControlServiceParameters:
    def __init__(self) -> None:
        self.services = ServicesStopManualControlServiceParameter()

    @property
    def v(self):
        return {'services': self.services.v}

    @v.setter
    def v(self, value):
        if value.get('services') is not None: self.services.v = value['services']


class ServicesStopManualControlServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'services'
        self.name = '服务列表'
        self.type = 'array'
        self.columnComplex = [ServicesStopManualControlServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ServicesStopManualControlServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ServicesStopManualControlServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.productId = ProductIdServicesStopManualControlServiceParameterColumnComplexStruct()
        self.devId = DevIdServicesStopManualControlServiceParameterColumnComplexStruct()
        self.service = ServiceServicesStopManualControlServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'productId': self.productId.v, 'devId': self.devId.v, 'service': self.service.v}

    @v.setter
    def v(self, value):
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('service') is not None: self.service.v = value['service']


class ServiceServicesStopManualControlServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'service'
        self.name = '服务名称'
        self.type = 'string'
        self.v: str = ''


class DevIdServicesStopManualControlServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devId'
        self.name = '设备ID'
        self.type = 'string'
        self.v: str = ''


class ProductIdServicesStopManualControlServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'productId'
        self.name = '产品ID'
        self.type = 'string'
        self.v: str = ''


class ManualControlService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'manualControl'
        self.name = '临时手动干预'
        self.parameters = ManualControlServiceParameters()


class ManualControlServiceParameters:
    def __init__(self) -> None:
        self.services = ServicesManualControlServiceParameter()

    @property
    def v(self):
        return {'services': self.services.v}

    @v.setter
    def v(self, value):
        if value.get('services') is not None: self.services.v = value['services']


class ServicesManualControlServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'services'
        self.name = '服务列表'
        self.type = 'array'
        self.columnComplex = [ServicesManualControlServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ServicesManualControlServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ServicesManualControlServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.priority = PriorityServicesManualControlServiceParameterColumnComplexStruct()
        self.script = ScriptServicesManualControlServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'priority': self.priority.v, 'script': self.script.v}

    @v.setter
    def v(self, value):
        if value.get('priority') is not None: self.priority.v = value['priority']
        if value.get('script') is not None: self.script.v = value['script']


class ScriptServicesManualControlServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'script'
        self.name = '执行脚本'
        self.type = 'string'
        self.v: str = ''


class PriorityServicesManualControlServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'priority'
        self.name = '优先级'
        self.type = 'integer'
        self.specs = PriorityServicesManualControlServiceParameterColumnComplexStructSpecs()
        self.v: int = 0


class PriorityServicesManualControlServiceParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99


class OutsideLinkageService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'outsideLinkage'
        self.name = '外部联动策略'
        self.parameters = OutsideLinkageServiceParameters()


class OutsideLinkageServiceParameters:
    def __init__(self) -> None:
        self.services = ServicesOutsideLinkageServiceParameter()

    @property
    def v(self):
        return {'services': self.services.v}

    @v.setter
    def v(self, value):
        if value.get('services') is not None: self.services.v = value['services']


class ServicesOutsideLinkageServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'services'
        self.name = '服务列表'
        self.type = 'array'
        self.columnComplex = [ServicesOutsideLinkageServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ServicesOutsideLinkageServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ServicesOutsideLinkageServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.uuid = UuidServicesOutsideLinkageServiceParameterColumnComplexStruct()
        self.priority = PriorityServicesOutsideLinkageServiceParameterColumnComplexStruct()
        self.script = ScriptServicesOutsideLinkageServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'uuid': self.uuid.v, 'priority': self.priority.v, 'script': self.script.v}

    @v.setter
    def v(self, value):
        if value.get('uuid') is not None: self.uuid.v = value['uuid']
        if value.get('priority') is not None: self.priority.v = value['priority']
        if value.get('script') is not None: self.script.v = value['script']


class ScriptServicesOutsideLinkageServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'script'
        self.name = '执行脚本'
        self.type = 'string'
        self.v: str = ''


class PriorityServicesOutsideLinkageServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'priority'
        self.name = '优先级'
        self.type = 'integer'
        self.specs = PriorityServicesOutsideLinkageServiceParameterColumnComplexStructSpecs()
        self.v: int = 0


class PriorityServicesOutsideLinkageServiceParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99


class UuidServicesOutsideLinkageServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'uuid'
        self.name = '规则ID'
        self.type = 'string'
        self.v: str = ''


class StopLinkageRuleRunningService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'stopLinkageRuleRunning'
        self.name = '停止联动策略'
        self.parameters = StopLinkageRuleRunningServiceParameters()


class StopLinkageRuleRunningServiceParameters:
    def __init__(self) -> None:
        self.uuids = UuidsStopLinkageRuleRunningServiceParameter()

    @property
    def v(self):
        return {'uuids': self.uuids.v}

    @v.setter
    def v(self, value):
        if value.get('uuids') is not None: self.uuids.v = value['uuids']


class UuidsStopLinkageRuleRunningServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'uuids'
        self.name = '规则ID列表'
        self.type = 'array'
        self.columnSimple = [UuidsStopLinkageRuleRunningServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = UuidsStopLinkageRuleRunningServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class UuidsStopLinkageRuleRunningServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class DisableRuleService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'disableRule'
        self.name = '停用策略'
        self.parameters = DisableRuleServiceParameters()


class DisableRuleServiceParameters:
    def __init__(self) -> None:
        self.uuids = UuidsDisableRuleServiceParameter()

    @property
    def v(self):
        return {'uuids': self.uuids.v}

    @v.setter
    def v(self, value):
        if value.get('uuids') is not None: self.uuids.v = value['uuids']


class UuidsDisableRuleServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'uuids'
        self.name = '规则ID列表'
        self.type = 'array'
        self.columnSimple = [UuidsDisableRuleServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = UuidsDisableRuleServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class UuidsDisableRuleServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class EnableRuleService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'enableRule'
        self.name = '启用策略'
        self.parameters = EnableRuleServiceParameters()


class EnableRuleServiceParameters:
    def __init__(self) -> None:
        self.uuids = UuidsEnableRuleServiceParameter()

    @property
    def v(self):
        return {'uuids': self.uuids.v}

    @v.setter
    def v(self, value):
        if value.get('uuids') is not None: self.uuids.v = value['uuids']


class UuidsEnableRuleServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'uuids'
        self.name = '规则ID列表'
        self.type = 'array'
        self.columnSimple = [UuidsEnableRuleServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = UuidsEnableRuleServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class UuidsEnableRuleServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class GetRulesByUuidsService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'getRulesByUuids'
        self.name = '获取多个策略'
        self.parameters = GetRulesByUuidsServiceParameters()
        self.output = [GetRulesByUuidsServiceOutput()]


class GetRulesByUuidsServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.rules = RulesGetRulesByUuidsServiceOutput()

    @property
    def v(self):
        return {'rules': self.rules.v}

    @v.setter
    def v(self, value):
        if value.get('rules') is not None: self.rules.v = value['rules']


class RulesGetRulesByUuidsServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'rules'
        self.name = '规则列表'
        self.type = 'array'
        self.columnComplex = [RulesGetRulesByUuidsServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = RulesGetRulesByUuidsServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class RulesGetRulesByUuidsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.uuid = UuidRulesGetRulesByUuidsServiceOutputColumnComplexStruct()
        self.enable = EnableRulesGetRulesByUuidsServiceOutputColumnComplexStruct()
        self.type = TypeRulesGetRulesByUuidsServiceOutputColumnComplexStruct()
        self.priority = PriorityRulesGetRulesByUuidsServiceOutputColumnComplexStruct()
        self.date = DateRulesGetRulesByUuidsServiceOutputColumnComplexStruct()
        self.time = TimeRulesGetRulesByUuidsServiceOutputColumnComplexStruct()
        self.srcDevice = SrcDeviceRulesGetRulesByUuidsServiceOutputColumnComplexStruct()
        self.dstDevice = DstDeviceRulesGetRulesByUuidsServiceOutputColumnComplexStruct()
        self.script = ScriptRulesGetRulesByUuidsServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'uuid': self.uuid.v, 'enable': self.enable.v, 'type': self.type.v, 'priority': self.priority.v, 'date': self.date.v, 'time': self.time.v, 'srcDevice': self.srcDevice.v, 'dstDevice': self.dstDevice.v, 'script': self.script.v}

    @v.setter
    def v(self, value):
        if value.get('uuid') is not None: self.uuid.v = value['uuid']
        if value.get('enable') is not None: self.enable.v = value['enable']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('priority') is not None: self.priority.v = value['priority']
        if value.get('date') is not None: self.date.v = value['date']
        if value.get('time') is not None: self.time.v = value['time']
        if value.get('srcDevice') is not None: self.srcDevice.v = value['srcDevice']
        if value.get('dstDevice') is not None: self.dstDevice.v = value['dstDevice']
        if value.get('script') is not None: self.script.v = value['script']


class ScriptRulesGetRulesByUuidsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'script'
        self.name = '脚本'
        self.type = 'string'
        self.v: str = ''


class DstDeviceRulesGetRulesByUuidsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'dstDevice'
        self.name = '联动设备'
        self.type = 'array'
        self.columnSimple = [DstDeviceRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = DstDeviceRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class DstDeviceRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class SrcDeviceRulesGetRulesByUuidsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'srcDevice'
        self.name = '触发源设备'
        self.type = 'array'
        self.columnSimple = [SrcDeviceRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = SrcDeviceRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class SrcDeviceRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class TimeRulesGetRulesByUuidsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'time'
        self.name = '执行时间'
        self.type = 'array'
        self.columnComplex = [TimeRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = TimeRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class TimeRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.startTime = StartTimeTimeRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct()
        self.endTime = EndTimeTimeRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'startTime': self.startTime.v, 'endTime': self.endTime.v}

    @v.setter
    def v(self, value):
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']


class EndTimeTimeRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '结束时间'
        self.type = 'string'
        self.format = 'time'
        self.v: str = ''


class StartTimeTimeRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '开始时间'
        self.type = 'string'
        self.format = 'time'
        self.v: str = ''


class DateRulesGetRulesByUuidsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'date'
        self.name = '执行日期'
        self.type = 'array'
        self.columnComplex = [DateRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DateRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DateRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.startDate = StartDateDateRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct()
        self.endDate = EndDateDateRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'startDate': self.startDate.v, 'endDate': self.endDate.v}

    @v.setter
    def v(self, value):
        if value.get('startDate') is not None: self.startDate.v = value['startDate']
        if value.get('endDate') is not None: self.endDate.v = value['endDate']


class EndDateDateRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endDate'
        self.name = '结束日期'
        self.type = 'string'
        self.format = 'date'
        self.v: str = ''


class StartDateDateRulesGetRulesByUuidsServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startDate'
        self.name = '开始日期'
        self.type = 'string'
        self.format = 'date'
        self.v: str = ''


class PriorityRulesGetRulesByUuidsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'priority'
        self.name = '优先级'
        self.type = 'integer'
        self.specs = PriorityRulesGetRulesByUuidsServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class PriorityRulesGetRulesByUuidsServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99


class TypeRulesGetRulesByUuidsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'type'
        self.name = '规则类型'
        self.type = 'string'
        self.specs = TypeRulesGetRulesByUuidsServiceOutputColumnComplexStructSpecs()
        self.v: str = ''


class TypeRulesGetRulesByUuidsServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TypeRulesGetRulesByUuidsServiceOutputColumnComplexStructSpecsOptional()


class TypeRulesGetRulesByUuidsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.timer = TimerTypeRulesGetRulesByUuidsServiceOutputColumnComplexStructSpecsOptional()
        self.linkage = LinkageTypeRulesGetRulesByUuidsServiceOutputColumnComplexStructSpecsOptional()


class LinkageTypeRulesGetRulesByUuidsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'linkage'
        self.desc = '联动规则'


class TimerTypeRulesGetRulesByUuidsServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'timer'
        self.desc = '定时规则'


class EnableRulesGetRulesByUuidsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'enable'
        self.name = '规则使能'
        self.type = 'boolean'
        self.v: bool = True


class UuidRulesGetRulesByUuidsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'uuid'
        self.name = '规则ID'
        self.type = 'string'
        self.v: str = ''


class GetRulesByUuidsServiceParameters:
    def __init__(self) -> None:
        self.uuids = UuidsGetRulesByUuidsServiceParameter()

    @property
    def v(self):
        return {'uuids': self.uuids.v}

    @v.setter
    def v(self, value):
        if value.get('uuids') is not None: self.uuids.v = value['uuids']


class UuidsGetRulesByUuidsServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'uuids'
        self.name = '规则ID列表'
        self.type = 'array'
        self.columnSimple = [UuidsGetRulesByUuidsServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = UuidsGetRulesByUuidsServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class UuidsGetRulesByUuidsServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class GetAllRulesService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'getAllRules'
        self.name = '获取所有策略'
        self.parameters = None
        self.output = [GetAllRulesServiceOutput()]


class GetAllRulesServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.rules = RulesGetAllRulesServiceOutput()

    @property
    def v(self):
        return {'rules': self.rules.v}

    @v.setter
    def v(self, value):
        if value.get('rules') is not None: self.rules.v = value['rules']


class RulesGetAllRulesServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'rules'
        self.name = '规则列表'
        self.type = 'array'
        self.columnComplex = [RulesGetAllRulesServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = RulesGetAllRulesServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class RulesGetAllRulesServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.uuid = UuidRulesGetAllRulesServiceOutputColumnComplexStruct()
        self.enable = EnableRulesGetAllRulesServiceOutputColumnComplexStruct()
        self.type = TypeRulesGetAllRulesServiceOutputColumnComplexStruct()
        self.priority = PriorityRulesGetAllRulesServiceOutputColumnComplexStruct()
        self.date = DateRulesGetAllRulesServiceOutputColumnComplexStruct()
        self.time = TimeRulesGetAllRulesServiceOutputColumnComplexStruct()
        self.srcDevice = SrcDeviceRulesGetAllRulesServiceOutputColumnComplexStruct()
        self.dstDevice = DstDeviceRulesGetAllRulesServiceOutputColumnComplexStruct()
        self.script = ScriptRulesGetAllRulesServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'uuid': self.uuid.v, 'enable': self.enable.v, 'type': self.type.v, 'priority': self.priority.v, 'date': self.date.v, 'time': self.time.v, 'srcDevice': self.srcDevice.v, 'dstDevice': self.dstDevice.v, 'script': self.script.v}

    @v.setter
    def v(self, value):
        if value.get('uuid') is not None: self.uuid.v = value['uuid']
        if value.get('enable') is not None: self.enable.v = value['enable']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('priority') is not None: self.priority.v = value['priority']
        if value.get('date') is not None: self.date.v = value['date']
        if value.get('time') is not None: self.time.v = value['time']
        if value.get('srcDevice') is not None: self.srcDevice.v = value['srcDevice']
        if value.get('dstDevice') is not None: self.dstDevice.v = value['dstDevice']
        if value.get('script') is not None: self.script.v = value['script']


class ScriptRulesGetAllRulesServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'script'
        self.name = '脚本'
        self.type = 'string'
        self.v: str = ''


class DstDeviceRulesGetAllRulesServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'dstDevice'
        self.name = '联动设备'
        self.type = 'array'
        self.columnSimple = [DstDeviceRulesGetAllRulesServiceOutputColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = DstDeviceRulesGetAllRulesServiceOutputColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class DstDeviceRulesGetAllRulesServiceOutputColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class SrcDeviceRulesGetAllRulesServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'srcDevice'
        self.name = '触发源设备'
        self.type = 'array'
        self.columnSimple = [SrcDeviceRulesGetAllRulesServiceOutputColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = SrcDeviceRulesGetAllRulesServiceOutputColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class SrcDeviceRulesGetAllRulesServiceOutputColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class TimeRulesGetAllRulesServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'time'
        self.name = '执行时间'
        self.type = 'array'
        self.columnComplex = [TimeRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = TimeRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class TimeRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.startTime = StartTimeTimeRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct()
        self.endTime = EndTimeTimeRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'startTime': self.startTime.v, 'endTime': self.endTime.v}

    @v.setter
    def v(self, value):
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']


class EndTimeTimeRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '结束时间'
        self.type = 'string'
        self.format = 'time'
        self.v: str = ''


class StartTimeTimeRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '开始时间'
        self.type = 'string'
        self.format = 'time'
        self.v: str = ''


class DateRulesGetAllRulesServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'date'
        self.name = '执行日期'
        self.type = 'array'
        self.columnComplex = [DateRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DateRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DateRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.startDate = StartDateDateRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct()
        self.endDate = EndDateDateRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'startDate': self.startDate.v, 'endDate': self.endDate.v}

    @v.setter
    def v(self, value):
        if value.get('startDate') is not None: self.startDate.v = value['startDate']
        if value.get('endDate') is not None: self.endDate.v = value['endDate']


class EndDateDateRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endDate'
        self.name = '结束日期'
        self.type = 'string'
        self.format = 'date'
        self.v: str = ''


class StartDateDateRulesGetAllRulesServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startDate'
        self.name = '开始日期'
        self.type = 'string'
        self.format = 'date'
        self.v: str = ''


class PriorityRulesGetAllRulesServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'priority'
        self.name = '优先级'
        self.type = 'integer'
        self.specs = PriorityRulesGetAllRulesServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class PriorityRulesGetAllRulesServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99


class TypeRulesGetAllRulesServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'type'
        self.name = '规则类型'
        self.type = 'string'
        self.specs = TypeRulesGetAllRulesServiceOutputColumnComplexStructSpecs()
        self.v: str = ''


class TypeRulesGetAllRulesServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TypeRulesGetAllRulesServiceOutputColumnComplexStructSpecsOptional()


class TypeRulesGetAllRulesServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.timer = TimerTypeRulesGetAllRulesServiceOutputColumnComplexStructSpecsOptional()
        self.linkage = LinkageTypeRulesGetAllRulesServiceOutputColumnComplexStructSpecsOptional()


class LinkageTypeRulesGetAllRulesServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'linkage'
        self.desc = '联动规则'


class TimerTypeRulesGetAllRulesServiceOutputColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'timer'
        self.desc = '定时规则'


class EnableRulesGetAllRulesServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'enable'
        self.name = '规则使能'
        self.type = 'boolean'
        self.v: bool = True


class UuidRulesGetAllRulesServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'uuid'
        self.name = '规则ID'
        self.type = 'string'
        self.v: str = ''


class ClearAllRuleService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'clearAllRule'
        self.name = '清空智盒策略'
        self.parameters = None


class DeleteRuleByUuidService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'deleteRuleByUuid'
        self.name = '删除策略'
        self.parameters = DeleteRuleByUuidServiceParameters()


class DeleteRuleByUuidServiceParameters:
    def __init__(self) -> None:
        self.uuids = UuidsDeleteRuleByUuidServiceParameter()

    @property
    def v(self):
        return {'uuids': self.uuids.v}

    @v.setter
    def v(self, value):
        if value.get('uuids') is not None: self.uuids.v = value['uuids']


class UuidsDeleteRuleByUuidServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'uuids'
        self.name = '规则ID列表'
        self.type = 'array'
        self.columnSimple = [UuidsDeleteRuleByUuidServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = UuidsDeleteRuleByUuidServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class UuidsDeleteRuleByUuidServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class UpdateRuleService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'updateRule'
        self.name = '更新策略'
        self.parameters = UpdateRuleServiceParameters()


class UpdateRuleServiceParameters:
    def __init__(self) -> None:
        self.rules = RulesUpdateRuleServiceParameter()

    @property
    def v(self):
        return {'rules': self.rules.v}

    @v.setter
    def v(self, value):
        if value.get('rules') is not None: self.rules.v = value['rules']


class RulesUpdateRuleServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'rules'
        self.name = '规则列表'
        self.type = 'array'
        self.columnComplex = [RulesUpdateRuleServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = RulesUpdateRuleServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class RulesUpdateRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.uuid = UuidRulesUpdateRuleServiceParameterColumnComplexStruct()
        self.enable = EnableRulesUpdateRuleServiceParameterColumnComplexStruct()
        self.type = TypeRulesUpdateRuleServiceParameterColumnComplexStruct()
        self.priority = PriorityRulesUpdateRuleServiceParameterColumnComplexStruct()
        self.date = DateRulesUpdateRuleServiceParameterColumnComplexStruct()
        self.time = TimeRulesUpdateRuleServiceParameterColumnComplexStruct()
        self.srcDevice = SrcDeviceRulesUpdateRuleServiceParameterColumnComplexStruct()
        self.dstDevice = DstDeviceRulesUpdateRuleServiceParameterColumnComplexStruct()
        self.script = ScriptRulesUpdateRuleServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'uuid': self.uuid.v, 'enable': self.enable.v, 'type': self.type.v, 'priority': self.priority.v, 'date': self.date.v, 'time': self.time.v, 'srcDevice': self.srcDevice.v, 'dstDevice': self.dstDevice.v, 'script': self.script.v}

    @v.setter
    def v(self, value):
        if value.get('uuid') is not None: self.uuid.v = value['uuid']
        if value.get('enable') is not None: self.enable.v = value['enable']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('priority') is not None: self.priority.v = value['priority']
        if value.get('date') is not None: self.date.v = value['date']
        if value.get('time') is not None: self.time.v = value['time']
        if value.get('srcDevice') is not None: self.srcDevice.v = value['srcDevice']
        if value.get('dstDevice') is not None: self.dstDevice.v = value['dstDevice']
        if value.get('script') is not None: self.script.v = value['script']


class ScriptRulesUpdateRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'script'
        self.name = '脚本'
        self.type = 'string'
        self.v: str = ''


class DstDeviceRulesUpdateRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'dstDevice'
        self.name = '联动设备'
        self.type = 'array'
        self.columnSimple = [DstDeviceRulesUpdateRuleServiceParameterColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = DstDeviceRulesUpdateRuleServiceParameterColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class DstDeviceRulesUpdateRuleServiceParameterColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class SrcDeviceRulesUpdateRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'srcDevice'
        self.name = '触发源设备'
        self.type = 'array'
        self.columnSimple = [SrcDeviceRulesUpdateRuleServiceParameterColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = SrcDeviceRulesUpdateRuleServiceParameterColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class SrcDeviceRulesUpdateRuleServiceParameterColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class TimeRulesUpdateRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'time'
        self.name = '执行时间'
        self.type = 'array'
        self.columnComplex = [TimeRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = TimeRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class TimeRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.startTime = StartTimeTimeRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct()
        self.endTime = EndTimeTimeRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'startTime': self.startTime.v, 'endTime': self.endTime.v}

    @v.setter
    def v(self, value):
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']


class EndTimeTimeRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '结束时间'
        self.type = 'string'
        self.format = 'time'
        self.v: str = ''


class StartTimeTimeRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '开始时间'
        self.type = 'string'
        self.format = 'time'
        self.v: str = ''


class DateRulesUpdateRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'date'
        self.name = '执行日期'
        self.type = 'array'
        self.columnComplex = [DateRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DateRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DateRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.startDate = StartDateDateRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct()
        self.endDate = EndDateDateRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'startDate': self.startDate.v, 'endDate': self.endDate.v}

    @v.setter
    def v(self, value):
        if value.get('startDate') is not None: self.startDate.v = value['startDate']
        if value.get('endDate') is not None: self.endDate.v = value['endDate']


class EndDateDateRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endDate'
        self.name = '结束日期'
        self.type = 'string'
        self.format = 'date'
        self.v: str = ''


class StartDateDateRulesUpdateRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startDate'
        self.name = '开始日期'
        self.type = 'string'
        self.format = 'date'
        self.v: str = ''


class PriorityRulesUpdateRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'priority'
        self.name = '优先级'
        self.type = 'integer'
        self.specs = PriorityRulesUpdateRuleServiceParameterColumnComplexStructSpecs()
        self.v: int = 0


class PriorityRulesUpdateRuleServiceParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99


class TypeRulesUpdateRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'type'
        self.name = '规则类型'
        self.type = 'string'
        self.specs = TypeRulesUpdateRuleServiceParameterColumnComplexStructSpecs()
        self.v: str = ''


class TypeRulesUpdateRuleServiceParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TypeRulesUpdateRuleServiceParameterColumnComplexStructSpecsOptional()


class TypeRulesUpdateRuleServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.timer = TimerTypeRulesUpdateRuleServiceParameterColumnComplexStructSpecsOptional()
        self.linkage = LinkageTypeRulesUpdateRuleServiceParameterColumnComplexStructSpecsOptional()


class LinkageTypeRulesUpdateRuleServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'linkage'
        self.desc = '联动规则'


class TimerTypeRulesUpdateRuleServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'timer'
        self.desc = '定时规则'


class EnableRulesUpdateRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'enable'
        self.name = '规则使能'
        self.type = 'boolean'
        self.v: bool = True


class UuidRulesUpdateRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'uuid'
        self.name = '规则ID'
        self.type = 'string'
        self.v: str = ''


class AddRuleService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'addRule'
        self.name = '添加策略'
        self.parameters = AddRuleServiceParameters()


class AddRuleServiceParameters:
    def __init__(self) -> None:
        self.rules = RulesAddRuleServiceParameter()

    @property
    def v(self):
        return {'rules': self.rules.v}

    @v.setter
    def v(self, value):
        if value.get('rules') is not None: self.rules.v = value['rules']


class RulesAddRuleServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'rules'
        self.name = '规则列表'
        self.type = 'array'
        self.columnComplex = [RulesAddRuleServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = RulesAddRuleServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class RulesAddRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.uuid = UuidRulesAddRuleServiceParameterColumnComplexStruct()
        self.enable = EnableRulesAddRuleServiceParameterColumnComplexStruct()
        self.type = TypeRulesAddRuleServiceParameterColumnComplexStruct()
        self.priority = PriorityRulesAddRuleServiceParameterColumnComplexStruct()
        self.date = DateRulesAddRuleServiceParameterColumnComplexStruct()
        self.time = TimeRulesAddRuleServiceParameterColumnComplexStruct()
        self.srcDevice = SrcDeviceRulesAddRuleServiceParameterColumnComplexStruct()
        self.dstDevice = DstDeviceRulesAddRuleServiceParameterColumnComplexStruct()
        self.script = ScriptRulesAddRuleServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'uuid': self.uuid.v, 'enable': self.enable.v, 'type': self.type.v, 'priority': self.priority.v, 'date': self.date.v, 'time': self.time.v, 'srcDevice': self.srcDevice.v, 'dstDevice': self.dstDevice.v, 'script': self.script.v}

    @v.setter
    def v(self, value):
        if value.get('uuid') is not None: self.uuid.v = value['uuid']
        if value.get('enable') is not None: self.enable.v = value['enable']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('priority') is not None: self.priority.v = value['priority']
        if value.get('date') is not None: self.date.v = value['date']
        if value.get('time') is not None: self.time.v = value['time']
        if value.get('srcDevice') is not None: self.srcDevice.v = value['srcDevice']
        if value.get('dstDevice') is not None: self.dstDevice.v = value['dstDevice']
        if value.get('script') is not None: self.script.v = value['script']


class ScriptRulesAddRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'script'
        self.name = '脚本'
        self.type = 'string'
        self.v: str = ''


class DstDeviceRulesAddRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'dstDevice'
        self.name = '联动设备'
        self.type = 'array'
        self.columnSimple = [DstDeviceRulesAddRuleServiceParameterColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = DstDeviceRulesAddRuleServiceParameterColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class DstDeviceRulesAddRuleServiceParameterColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class SrcDeviceRulesAddRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'srcDevice'
        self.name = '触发源设备'
        self.type = 'array'
        self.columnSimple = [SrcDeviceRulesAddRuleServiceParameterColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = SrcDeviceRulesAddRuleServiceParameterColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class SrcDeviceRulesAddRuleServiceParameterColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class TimeRulesAddRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'time'
        self.name = '执行时间'
        self.type = 'array'
        self.columnComplex = [TimeRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = TimeRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class TimeRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.startTime = StartTimeTimeRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct()
        self.endTime = EndTimeTimeRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'startTime': self.startTime.v, 'endTime': self.endTime.v}

    @v.setter
    def v(self, value):
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']


class EndTimeTimeRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '结束时间'
        self.type = 'string'
        self.format = 'time'
        self.v: str = ''


class StartTimeTimeRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '开始时间'
        self.type = 'string'
        self.format = 'time'
        self.v: str = ''


class DateRulesAddRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'date'
        self.name = '执行日期'
        self.type = 'array'
        self.columnComplex = [DateRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DateRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DateRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.startDate = StartDateDateRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct()
        self.endDate = EndDateDateRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'startDate': self.startDate.v, 'endDate': self.endDate.v}

    @v.setter
    def v(self, value):
        if value.get('startDate') is not None: self.startDate.v = value['startDate']
        if value.get('endDate') is not None: self.endDate.v = value['endDate']


class EndDateDateRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endDate'
        self.name = '结束日期'
        self.type = 'string'
        self.format = 'date'
        self.v: str = ''


class StartDateDateRulesAddRuleServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startDate'
        self.name = '开始日期'
        self.type = 'string'
        self.format = 'date'
        self.v: str = ''


class PriorityRulesAddRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'priority'
        self.name = '优先级'
        self.type = 'integer'
        self.specs = PriorityRulesAddRuleServiceParameterColumnComplexStructSpecs()
        self.v: int = 0


class PriorityRulesAddRuleServiceParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99


class TypeRulesAddRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'type'
        self.name = '规则类型'
        self.type = 'string'
        self.specs = TypeRulesAddRuleServiceParameterColumnComplexStructSpecs()
        self.v: str = ''


class TypeRulesAddRuleServiceParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TypeRulesAddRuleServiceParameterColumnComplexStructSpecsOptional()


class TypeRulesAddRuleServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.timer = TimerTypeRulesAddRuleServiceParameterColumnComplexStructSpecsOptional()
        self.linkage = LinkageTypeRulesAddRuleServiceParameterColumnComplexStructSpecsOptional()


class LinkageTypeRulesAddRuleServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'linkage'
        self.desc = '联动规则'


class TimerTypeRulesAddRuleServiceParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'timer'
        self.desc = '定时规则'


class EnableRulesAddRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'enable'
        self.name = '规则使能'
        self.type = 'boolean'
        self.v: bool = True


class UuidRulesAddRuleServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'uuid'
        self.name = '规则ID'
        self.type = 'string'
        self.v: str = ''


class StopReportService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'stopReport'
        self.name = '停止监控智慧盒实时数据'
        self.parameters = None


class StartReportService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'startReport'
        self.name = '监控智慧盒实时数据'
        self.parameters = None


class UpdateAppService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'updateApp'
        self.name = '应用程序升级'
        self.parameters = UpdateAppServiceParameters()


class UpdateAppServiceParameters:
    def __init__(self) -> None:
        self.url = UrlUpdateAppServiceParameter()
        self.md5Sum = Md5SumUpdateAppServiceParameter()

    @property
    def v(self):
        return {'url': self.url.v, 'md5Sum': self.md5Sum.v}

    @v.setter
    def v(self, value):
        if value.get('url') is not None: self.url.v = value['url']
        if value.get('md5Sum') is not None: self.md5Sum.v = value['md5Sum']


class Md5SumUpdateAppServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'md5Sum'
        self.name = '应用程序文件MD5'
        self.type = 'string'
        self.v: str = ''


class UrlUpdateAppServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'url'
        self.name = '应用程序下载地址'
        self.type = 'string'
        self.v: str = ''


class UpdateFirmwareService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'updateFirmware'
        self.name = '固件升级'
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
        self.type = 'string'
        self.v: str = ''


class UrlUpdateFirmwareServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'url'
        self.name = '固件下载地址'
        self.type = 'string'
        self.v: str = ''


class SwitchModeService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'switchMode'
        self.name = '切换模式'
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
        self.auto = AutoModeSwitchModeServiceParameterSpecsOptional()
        self.manual = ManualModeSwitchModeServiceParameterSpecsOptional()


class ManualModeSwitchModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'manual'
        self.desc = '手动模式'


class AutoModeSwitchModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'auto'
        self.desc = '自动模式'


class RebootService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'reboot'
        self.name = '重启'
        self.parameters = None
        self.output = [RebootServiceOutput()]


class RebootServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.sn = SnRebootServiceOutput()
        self.time = TimeRebootServiceOutput()

    @property
    def v(self):
        return {'sn': self.sn.v, 'time': self.time.v}

    @v.setter
    def v(self, value):
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('time') is not None: self.time.v = value['time']


class TimeRebootServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'time'
        self.name = '重启时间'
        self.type = 'string'
        self.format = 'date-time'
        self.v: str = ''


class SnRebootServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'sn'
        self.name = '设备SN'
        self.type = 'string'
        self.v: str = ''


class Events:
    def __init__(self) -> None:
        self.reboot = RebootEvent()
        self.ntpSyncSuccess = NtpSyncSuccessEvent()
        self.ntpSyncFailure = NtpSyncFailureEvent()
        self.wiredConnect = WiredConnectEvent()
        self.wiredDisconnect = WiredDisconnectEvent()
        self.id4GConnect = Id4GConnectEvent()
        self.id4GDisconnect = Id4GDisconnectEvent()
        self.id5GConnect = Id5GConnectEvent()
        self.id5GDisconnect = Id5GDisconnectEvent()
        self.firmwareUpdateStart = FirmwareUpdateStartEvent()
        self.firmwareUpdateSuccess = FirmwareUpdateSuccessEvent()
        self.firmwareUpdateFailed = FirmwareUpdateFailedEvent()
        self.appUpdateStart = AppUpdateStartEvent()
        self.appUpdateSuccess = AppUpdateSuccessEvent()
        self.appUpdateFail = AppUpdateFailEvent()
        self.ruleStart = RuleStartEvent()
        self.ruleEnd = RuleEndEvent()
        self.ruleCommandStatus = RuleCommandStatusEvent()
        self.ruleDefaultCommandStatus = RuleDefaultCommandStatusEvent()
        self.ruleCommandCover = RuleCommandCoverEvent()
        self.ruleCommandIgnore = RuleCommandIgnoreEvent()
        self.customEvent = CustomEventEvent()


class CustomEventEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'customEvent'
        self.name = '用户自定义事件'
        self.parameters = CustomEventEventParameters()


class CustomEventEventParameters:
    def __init__(self) -> None:
        self.eventId = EventIdCustomEventEventParameter()
        self.srcList = SrcListCustomEventEventParameter()

    @property
    def v(self):
        return {'eventId': self.eventId.v, 'srcList': self.srcList.v}

    @v.setter
    def v(self, value):
        if value.get('eventId') is not None: self.eventId.v = value['eventId']
        if value.get('srcList') is not None: self.srcList.v = value['srcList']


class SrcListCustomEventEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'srcList'
        self.name = '触发源设备列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [SrcListCustomEventEventParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = SrcListCustomEventEventParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class SrcListCustomEventEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.productId = ProductIdSrcListCustomEventEventParameterColumnComplexStruct()
        self.deviceId = DeviceIdSrcListCustomEventEventParameterColumnComplexStruct()

    @property
    def v(self):
        return {'productId': self.productId.v, 'deviceId': self.deviceId.v}

    @v.setter
    def v(self, value):
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('deviceId') is not None: self.deviceId.v = value['deviceId']


class DeviceIdSrcListCustomEventEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'deviceId'
        self.name = '设备ID'
        self.type = 'string'
        self.v: str = ''


class ProductIdSrcListCustomEventEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'productId'
        self.name = '产品ID'
        self.type = 'string'
        self.v: str = ''


class EventIdCustomEventEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventId'
        self.name = '事件ID'
        self.type = 'string'
        self.v: str = ''


class RuleCommandIgnoreEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'ruleCommandIgnore'
        self.name = '忽略执行规则'
        self.parameters = RuleCommandIgnoreEventParameters()


class RuleCommandIgnoreEventParameters:
    def __init__(self) -> None:
        self.devId = DevIdRuleCommandIgnoreEventParameter()
        self.command = CommandRuleCommandIgnoreEventParameter()
        self.uuid = UuidRuleCommandIgnoreEventParameter()
        self.higherPriorityUuid = HigherPriorityUuidRuleCommandIgnoreEventParameter()

    @property
    def v(self):
        return {'devId': self.devId.v, 'command': self.command.v, 'uuid': self.uuid.v, 'higherPriorityUuid': self.higherPriorityUuid.v}

    @v.setter
    def v(self, value):
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('command') is not None: self.command.v = value['command']
        if value.get('uuid') is not None: self.uuid.v = value['uuid']
        if value.get('higherPriorityUuid') is not None: self.higherPriorityUuid.v = value['higherPriorityUuid']


class HigherPriorityUuidRuleCommandIgnoreEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'higherPriorityUuid'
        self.name = '正在执行的更高优先级的规则uuid'
        self.type = 'string'
        self.v: str = ''


class UuidRuleCommandIgnoreEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'uuid'
        self.name = '规则uuid'
        self.type = 'string'
        self.v: str = ''


class CommandRuleCommandIgnoreEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'command'
        self.name = '指令名称'
        self.type = 'string'
        self.v: str = ''


class DevIdRuleCommandIgnoreEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'devId'
        self.name = '设备ID'
        self.type = 'string'
        self.v: str = ''


class RuleCommandCoverEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'ruleCommandCover'
        self.name = '被高优先级规则抢占'
        self.parameters = RuleCommandCoverEventParameters()


class RuleCommandCoverEventParameters:
    def __init__(self) -> None:
        self.devId = DevIdRuleCommandCoverEventParameter()
        self.command = CommandRuleCommandCoverEventParameter()
        self.beCoverRuleUuid = BeCoverRuleUuidRuleCommandCoverEventParameter()
        self.coverRuleUuid = CoverRuleUuidRuleCommandCoverEventParameter()

    @property
    def v(self):
        return {'devId': self.devId.v, 'command': self.command.v, 'beCoverRuleUuid': self.beCoverRuleUuid.v, 'coverRuleUuid': self.coverRuleUuid.v}

    @v.setter
    def v(self, value):
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('command') is not None: self.command.v = value['command']
        if value.get('beCoverRuleUuid') is not None: self.beCoverRuleUuid.v = value['beCoverRuleUuid']
        if value.get('coverRuleUuid') is not None: self.coverRuleUuid.v = value['coverRuleUuid']


class CoverRuleUuidRuleCommandCoverEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'coverRuleUuid'
        self.name = '抢占规则uuid'
        self.type = 'string'
        self.v: str = ''


class BeCoverRuleUuidRuleCommandCoverEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'beCoverRuleUuid'
        self.name = '被抢占规则uuid'
        self.type = 'string'
        self.v: str = ''


class CommandRuleCommandCoverEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'command'
        self.name = '指令名称'
        self.type = 'string'
        self.v: str = ''


class DevIdRuleCommandCoverEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'devId'
        self.name = '设备ID'
        self.type = 'string'
        self.v: str = ''


class RuleDefaultCommandStatusEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'ruleDefaultCommandStatus'
        self.name = '规则指令执行默认参数结果'
        self.parameters = RuleDefaultCommandStatusEventParameters()


class RuleDefaultCommandStatusEventParameters:
    def __init__(self) -> None:
        self.devId = DevIdRuleDefaultCommandStatusEventParameter()
        self.command = CommandRuleDefaultCommandStatusEventParameter()
        self.resultCode = ResultCodeRuleDefaultCommandStatusEventParameter()

    @property
    def v(self):
        return {'devId': self.devId.v, 'command': self.command.v, 'resultCode': self.resultCode.v}

    @v.setter
    def v(self, value):
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('command') is not None: self.command.v = value['command']
        if value.get('resultCode') is not None: self.resultCode.v = value['resultCode']


class ResultCodeRuleDefaultCommandStatusEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'resultCode'
        self.name = '执行结果码'
        self.type = 'integer'
        self.v: int = 0


class CommandRuleDefaultCommandStatusEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'command'
        self.name = '指令名称'
        self.type = 'string'
        self.v: str = ''


class DevIdRuleDefaultCommandStatusEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'devId'
        self.name = '设备ID'
        self.type = 'string'
        self.v: str = ''


class RuleCommandStatusEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'ruleCommandStatus'
        self.name = '规则指令执行结果'
        self.parameters = RuleCommandStatusEventParameters()


class RuleCommandStatusEventParameters:
    def __init__(self) -> None:
        self.uuid = UuidRuleCommandStatusEventParameter()
        self.devId = DevIdRuleCommandStatusEventParameter()
        self.command = CommandRuleCommandStatusEventParameter()
        self.resultCode = ResultCodeRuleCommandStatusEventParameter()

    @property
    def v(self):
        return {'uuid': self.uuid.v, 'devId': self.devId.v, 'command': self.command.v, 'resultCode': self.resultCode.v}

    @v.setter
    def v(self, value):
        if value.get('uuid') is not None: self.uuid.v = value['uuid']
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('command') is not None: self.command.v = value['command']
        if value.get('resultCode') is not None: self.resultCode.v = value['resultCode']


class ResultCodeRuleCommandStatusEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'resultCode'
        self.name = '执行结果码'
        self.type = 'integer'
        self.v: int = 0


class CommandRuleCommandStatusEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'command'
        self.name = '指令名称'
        self.type = 'string'
        self.v: str = ''


class DevIdRuleCommandStatusEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'devId'
        self.name = '设备ID'
        self.type = 'string'
        self.v: str = ''


class UuidRuleCommandStatusEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'uuid'
        self.name = '规则ID'
        self.type = 'string'
        self.v: str = ''


class RuleEndEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'ruleEnd'
        self.name = '规则结束执行'
        self.parameters = RuleEndEventParameters()


class RuleEndEventParameters:
    def __init__(self) -> None:
        self.uuid = UuidRuleEndEventParameter()

    @property
    def v(self):
        return {'uuid': self.uuid.v}

    @v.setter
    def v(self, value):
        if value.get('uuid') is not None: self.uuid.v = value['uuid']


class UuidRuleEndEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'uuid'
        self.name = '规则ID'
        self.type = 'string'
        self.v: str = ''


class RuleStartEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'ruleStart'
        self.name = '规则开始执行'
        self.parameters = RuleStartEventParameters()


class RuleStartEventParameters:
    def __init__(self) -> None:
        self.uuid = UuidRuleStartEventParameter()

    @property
    def v(self):
        return {'uuid': self.uuid.v}

    @v.setter
    def v(self, value):
        if value.get('uuid') is not None: self.uuid.v = value['uuid']


class UuidRuleStartEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'uuid'
        self.name = '规则ID'
        self.type = 'string'
        self.v: str = ''


class AppUpdateFailEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'appUpdateFail'
        self.name = '应用软件升级失败'
        self.parameters = AppUpdateFailEventParameters()


class AppUpdateFailEventParameters:
    def __init__(self) -> None:
        self.resultCode = ResultCodeAppUpdateFailEventParameter()

    @property
    def v(self):
        return {'resultCode': self.resultCode.v}

    @v.setter
    def v(self, value):
        if value.get('resultCode') is not None: self.resultCode.v = value['resultCode']


class ResultCodeAppUpdateFailEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'resultCode'
        self.name = '错误码'
        self.type = 'integer'
        self.v: int = 0


class AppUpdateSuccessEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'appUpdateSuccess'
        self.name = '应用软件升级成功'
        self.parameters = AppUpdateSuccessEventParameters()


class AppUpdateSuccessEventParameters:
    def __init__(self) -> None:
        self.currentVersion = CurrentVersionAppUpdateSuccessEventParameter()

    @property
    def v(self):
        return {'currentVersion': self.currentVersion.v}

    @v.setter
    def v(self, value):
        if value.get('currentVersion') is not None: self.currentVersion.v = value['currentVersion']


class CurrentVersionAppUpdateSuccessEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'currentVersion'
        self.name = '当前应用版本号'
        self.type = 'string'
        self.v: str = ''


class AppUpdateStartEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'appUpdateStart'
        self.name = '应用软件开始升级'
        self.parameters = None


class FirmwareUpdateFailedEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'firmwareUpdateFailed'
        self.name = '固件升级失败'
        self.parameters = FirmwareUpdateFailedEventParameters()


class FirmwareUpdateFailedEventParameters:
    def __init__(self) -> None:
        self.resultCode = ResultCodeFirmwareUpdateFailedEventParameter()

    @property
    def v(self):
        return {'resultCode': self.resultCode.v}

    @v.setter
    def v(self, value):
        if value.get('resultCode') is not None: self.resultCode.v = value['resultCode']


class ResultCodeFirmwareUpdateFailedEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'resultCode'
        self.name = '执行结果码'
        self.type = 'integer'
        self.v: int = 0


class FirmwareUpdateSuccessEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'firmwareUpdateSuccess'
        self.name = '固件升级成功'
        self.parameters = FirmwareUpdateSuccessEventParameters()


class FirmwareUpdateSuccessEventParameters:
    def __init__(self) -> None:
        self.currentVersion = CurrentVersionFirmwareUpdateSuccessEventParameter()

    @property
    def v(self):
        return {'currentVersion': self.currentVersion.v}

    @v.setter
    def v(self, value):
        if value.get('currentVersion') is not None: self.currentVersion.v = value['currentVersion']


class CurrentVersionFirmwareUpdateSuccessEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'currentVersion'
        self.name = '当前版本'
        self.type = 'string'
        self.v: str = ''


class FirmwareUpdateStartEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'firmwareUpdateStart'
        self.name = '固件开始升级'
        self.parameters = None


class Id5GDisconnectEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = '5GDisconnect'
        self.name = '5G网络断开'
        self.parameters = None


class Id5GConnectEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = '5GConnect'
        self.name = '5G网络连接'
        self.parameters = None


class Id4GDisconnectEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = '4GDisconnect'
        self.name = '4G网络断开'
        self.parameters = None


class Id4GConnectEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = '4GConnect'
        self.name = '4G网络连接'
        self.parameters = None


class WiredDisconnectEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'wiredDisconnect'
        self.name = '有线网络断开'
        self.parameters = None


class WiredConnectEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'wiredConnect'
        self.name = '有线网络连接'
        self.parameters = None


class NtpSyncFailureEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'ntpSyncFailure'
        self.name = 'NTP校时失败'
        self.parameters = NtpSyncFailureEventParameters()


class NtpSyncFailureEventParameters:
    def __init__(self) -> None:
        self.ntpHost = NtpHostNtpSyncFailureEventParameter()

    @property
    def v(self):
        return {'ntpHost': self.ntpHost.v}

    @v.setter
    def v(self, value):
        if value.get('ntpHost') is not None: self.ntpHost.v = value['ntpHost']


class NtpHostNtpSyncFailureEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'ntpHost'
        self.name = '校时失败的NTP服务器'
        self.type = 'string'
        self.v: str = ''


class NtpSyncSuccessEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'ntpSyncSuccess'
        self.name = 'NTP校时成功'
        self.parameters = NtpSyncSuccessEventParameters()


class NtpSyncSuccessEventParameters:
    def __init__(self) -> None:
        self.ntpHost = NtpHostNtpSyncSuccessEventParameter()

    @property
    def v(self):
        return {'ntpHost': self.ntpHost.v}

    @v.setter
    def v(self, value):
        if value.get('ntpHost') is not None: self.ntpHost.v = value['ntpHost']


class NtpHostNtpSyncSuccessEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'ntpHost'
        self.name = '校时成功的NTP服务器'
        self.type = 'string'
        self.v: str = ''


class RebootEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'reboot'
        self.name = '智慧盒主动重启'
        self.parameters = RebootEventParameters()


class RebootEventParameters:
    def __init__(self) -> None:
        self.sn = SnRebootEventParameter()
        self.reason = ReasonRebootEventParameter()

    @property
    def v(self):
        return {'sn': self.sn.v, 'reason': self.reason.v}

    @v.setter
    def v(self, value):
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('reason') is not None: self.reason.v = value['reason']


class ReasonRebootEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'reason'
        self.name = '重启原因'
        self.type = 'string'
        self.specs = ReasonRebootEventParameterSpecs()
        self.v: str = ''


class ReasonRebootEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ReasonRebootEventParameterSpecsOptional()


class ReasonRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.firmwareUpadte = FirmwareUpadteReasonRebootEventParameterSpecsOptional()
        self.softwareUpdate = SoftwareUpdateReasonRebootEventParameterSpecsOptional()
        self.other = OtherReasonRebootEventParameterSpecsOptional()


class OtherReasonRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'other'
        self.desc = '其他'


class SoftwareUpdateReasonRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'softwareUpdate'
        self.desc = '软件升级'


class FirmwareUpadteReasonRebootEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'firmwareUpadte'
        self.desc = '固件升级'


class SnRebootEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'sn'
        self.name = '设备序列号'
        self.type = 'string'
        self.v: str = ''


class Properties:
    def __init__(self) -> None:
        self.sn = SnProperty()
        self.model = ModelProperty()
        self.productId = ProductIdProperty()
        self.online = OnlineProperty()
        self.mode = ModeProperty()
        self.networkInfo = NetworkInfoProperty()
        self.ntpInfo = NtpInfoProperty()
        self.upTime = UpTimeProperty()
        self.time = TimeProperty()
        self.hwInfo = HwInfoProperty()
        self.logHost = LogHostProperty()
        self.configureMode = ConfigureModeProperty()
        self.version = VersionProperty()
        self.mqttInfo = MqttInfoProperty()
        self.mqttInfoBackup = MqttInfoBackupProperty()
        self.ruleList = RuleListProperty()
        self.subDevList = SubDevListProperty()

    @property
    def v(self):
        return {'sn': self.sn.v, 'model': self.model.v, 'productId': self.productId.v, 'online': self.online.v, 'mode': self.mode.v, 'networkInfo': self.networkInfo.v, 'ntpInfo': self.ntpInfo.v, 'upTime': self.upTime.v, 'time': self.time.v, 'hwInfo': self.hwInfo.v, 'logHost': self.logHost.v, 'configureMode': self.configureMode.v, 'version': self.version.v, 'mqttInfo': self.mqttInfo.v, 'mqttInfoBackup': self.mqttInfoBackup.v, 'ruleList': self.ruleList.v, 'subDevList': self.subDevList.v}

    @v.setter
    def v(self, value):
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('networkInfo') is not None: self.networkInfo.v = value['networkInfo']
        if value.get('ntpInfo') is not None: self.ntpInfo.v = value['ntpInfo']
        if value.get('upTime') is not None: self.upTime.v = value['upTime']
        if value.get('time') is not None: self.time.v = value['time']
        if value.get('hwInfo') is not None: self.hwInfo.v = value['hwInfo']
        if value.get('logHost') is not None: self.logHost.v = value['logHost']
        if value.get('configureMode') is not None: self.configureMode.v = value['configureMode']
        if value.get('version') is not None: self.version.v = value['version']
        if value.get('mqttInfo') is not None: self.mqttInfo.v = value['mqttInfo']
        if value.get('mqttInfoBackup') is not None: self.mqttInfoBackup.v = value['mqttInfoBackup']
        if value.get('ruleList') is not None: self.ruleList.v = value['ruleList']
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
        self.productId = ProductIdSubDevListPropertyColumnComplexStruct()
        self.devId = DevIdSubDevListPropertyColumnComplexStruct()
        self.devType = DevTypeSubDevListPropertyColumnComplexStruct()
        self.setting = SettingSubDevListPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'productId': self.productId.v, 'devId': self.devId.v, 'devType': self.devType.v, 'setting': self.setting.v}

    @v.setter
    def v(self, value):
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('devType') is not None: self.devType.v = value['devType']
        if value.get('setting') is not None: self.setting.v = value['setting']


class SettingSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'setting'
        self.name = '设备配置'
        self.type = 'string'
        self.v: str = ''


class DevTypeSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devType'
        self.name = '设备类型'
        self.type = 'string'
        self.specs = DevTypeSubDevListPropertyColumnComplexStructSpecs()
        self.v: str = ''


class DevTypeSubDevListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = DevTypeSubDevListPropertyColumnComplexStructSpecsOptional()


class DevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.GW = GWDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.IPCOnvif = IPCOnvifDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.Lamp = LampDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.Sensor = SensorDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.Locker = LockerDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.Breaker = BreakerDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.Trafficscreen = TrafficscreenDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.Projector = ProjectorDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.Rfid = RfidDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.Power = PowerDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.SOSOnvif = SOSOnvifDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.Inforscreen = InforscreenDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.AI = AIDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()
        self.Brocast = BrocastDevTypeSubDevListPropertyColumnComplexStructSpecsOptional()


class BrocastDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Brocast'
        self.desc = '广播'


class AIDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'AI'
        self.desc = 'AI'


class InforscreenDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Inforscreen'
        self.desc = '信息屏'


class SOSOnvifDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'SOSOnvif'
        self.desc = '一键报警'


class PowerDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Power'
        self.desc = '智能电源'


class RfidDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Rfid'
        self.desc = 'rfid读写器'


class ProjectorDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Projector'
        self.desc = '投影灯'


class TrafficscreenDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Trafficscreen'
        self.desc = '横臂交通屏'


class BreakerDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Breaker'
        self.desc = '断路器'


class LockerDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Locker'
        self.desc = '智能锁'


class SensorDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Sensor'
        self.desc = '传感器'


class LampDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Lamp'
        self.desc = '灯'


class IPCOnvifDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'IPCOnvif'
        self.desc = '摄像头'


class GWDevTypeSubDevListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'GW'
        self.desc = '网关设备'


class DevIdSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'devId'
        self.name = '设备实例ID'
        self.type = 'string'
        self.v: str = ''


class ProductIdSubDevListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'productId'
        self.name = '设备产品ID'
        self.type = 'string'
        self.v: str = ''


class RuleListProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'ruleList'
        self.name = '规则列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [RuleListPropertyColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = RuleListPropertyColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class RuleListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.uuid = UuidRuleListPropertyColumnComplexStruct()
        self.enable = EnableRuleListPropertyColumnComplexStruct()
        self.type = TypeRuleListPropertyColumnComplexStruct()
        self.priority = PriorityRuleListPropertyColumnComplexStruct()
        self.date = DateRuleListPropertyColumnComplexStruct()
        self.time = TimeRuleListPropertyColumnComplexStruct()
        self.srcDevice = SrcDeviceRuleListPropertyColumnComplexStruct()
        self.dstDevice = DstDeviceRuleListPropertyColumnComplexStruct()
        self.script = ScriptRuleListPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'uuid': self.uuid.v, 'enable': self.enable.v, 'type': self.type.v, 'priority': self.priority.v, 'date': self.date.v, 'time': self.time.v, 'srcDevice': self.srcDevice.v, 'dstDevice': self.dstDevice.v, 'script': self.script.v}

    @v.setter
    def v(self, value):
        if value.get('uuid') is not None: self.uuid.v = value['uuid']
        if value.get('enable') is not None: self.enable.v = value['enable']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('priority') is not None: self.priority.v = value['priority']
        if value.get('date') is not None: self.date.v = value['date']
        if value.get('time') is not None: self.time.v = value['time']
        if value.get('srcDevice') is not None: self.srcDevice.v = value['srcDevice']
        if value.get('dstDevice') is not None: self.dstDevice.v = value['dstDevice']
        if value.get('script') is not None: self.script.v = value['script']


class ScriptRuleListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'script'
        self.name = '脚本'
        self.type = 'string'
        self.v: str = ''


class DstDeviceRuleListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'dstDevice'
        self.name = '联动设备列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnSimple = [DstDeviceRuleListPropertyColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = DstDeviceRuleListPropertyColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class DstDeviceRuleListPropertyColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class SrcDeviceRuleListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'srcDevice'
        self.name = '触发源设备列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnSimple = [SrcDeviceRuleListPropertyColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = SrcDeviceRuleListPropertyColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class SrcDeviceRuleListPropertyColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class TimeRuleListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'time'
        self.name = '执行时间'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [TimeRuleListPropertyColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = TimeRuleListPropertyColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class TimeRuleListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.startTime = StartTimeTimeRuleListPropertyColumnComplexStructColumnComplexStruct()
        self.endTime = EndTimeTimeRuleListPropertyColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'startTime': self.startTime.v, 'endTime': self.endTime.v}

    @v.setter
    def v(self, value):
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']


class EndTimeTimeRuleListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '结束时间'
        self.type = 'string'
        self.format = 'time'
        self.v: str = ''


class StartTimeTimeRuleListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '开始时间'
        self.type = 'string'
        self.format = 'time'
        self.v: str = ''


class DateRuleListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'date'
        self.name = '执行日期'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [DateRuleListPropertyColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DateRuleListPropertyColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DateRuleListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.startDate = StartDateDateRuleListPropertyColumnComplexStructColumnComplexStruct()
        self.endDate = EndDateDateRuleListPropertyColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'startDate': self.startDate.v, 'endDate': self.endDate.v}

    @v.setter
    def v(self, value):
        if value.get('startDate') is not None: self.startDate.v = value['startDate']
        if value.get('endDate') is not None: self.endDate.v = value['endDate']


class EndDateDateRuleListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endDate'
        self.name = '结束日期'
        self.type = 'string'
        self.format = 'date'
        self.v: str = ''


class StartDateDateRuleListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startDate'
        self.name = '开始日期'
        self.type = 'string'
        self.format = 'date'
        self.v: str = ''


class PriorityRuleListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'priority'
        self.name = '优先级'
        self.type = 'integer'
        self.specs = PriorityRuleListPropertyColumnComplexStructSpecs()
        self.v: int = 0


class PriorityRuleListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 99


class TypeRuleListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'type'
        self.name = '规则类型'
        self.type = 'string'
        self.specs = TypeRuleListPropertyColumnComplexStructSpecs()
        self.v: str = ''


class TypeRuleListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TypeRuleListPropertyColumnComplexStructSpecsOptional()


class TypeRuleListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.timer = TimerTypeRuleListPropertyColumnComplexStructSpecsOptional()
        self.linkage = LinkageTypeRuleListPropertyColumnComplexStructSpecsOptional()


class LinkageTypeRuleListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'linkage'
        self.desc = '联动规则'


class TimerTypeRuleListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'timer'
        self.desc = '定时规则'


class EnableRuleListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'enable'
        self.name = '是否启用'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'boolean'
        self.v: bool = True


class UuidRuleListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'uuid'
        self.name = '规则uuid'
        self.type = 'string'
        self.v: str = ''


class MqttInfoBackupProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'mqttInfoBackup'
        self.name = '无线mqtt服务器信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = MqttInfoBackupPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class MqttInfoBackupPropertyStruct:
    def __init__(self) -> None:
        self.host = HostMqttInfoBackupPropertyStruct()
        self.port = PortMqttInfoBackupPropertyStruct()
        self.userName = UserNameMqttInfoBackupPropertyStruct()
        self.passwd = PasswdMqttInfoBackupPropertyStruct()

    @property
    def v(self):
        return {'host': self.host.v, 'port': self.port.v, 'userName': self.userName.v, 'passwd': self.passwd.v}

    @v.setter
    def v(self, value):
        if value.get('host') is not None: self.host.v = value['host']
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('userName') is not None: self.userName.v = value['userName']
        if value.get('passwd') is not None: self.passwd.v = value['passwd']


class PasswdMqttInfoBackupPropertyStruct:
    def __init__(self) -> None:
        self.id = 'passwd'
        self.name = '密码'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class UserNameMqttInfoBackupPropertyStruct:
    def __init__(self) -> None:
        self.id = 'userName'
        self.name = '用户名'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class PortMqttInfoBackupPropertyStruct:
    def __init__(self) -> None:
        self.id = 'port'
        self.name = '端口'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = PortMqttInfoBackupPropertyStructSpecs()
        self.v: int = 0


class PortMqttInfoBackupPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 65535


class HostMqttInfoBackupPropertyStruct:
    def __init__(self) -> None:
        self.id = 'host'
        self.name = '地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class MqttInfoProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'mqttInfo'
        self.name = '有线mqtt服务器信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = MqttInfoPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class MqttInfoPropertyStruct:
    def __init__(self) -> None:
        self.host = HostMqttInfoPropertyStruct()
        self.port = PortMqttInfoPropertyStruct()
        self.userName = UserNameMqttInfoPropertyStruct()
        self.passwd = PasswdMqttInfoPropertyStruct()

    @property
    def v(self):
        return {'host': self.host.v, 'port': self.port.v, 'userName': self.userName.v, 'passwd': self.passwd.v}

    @v.setter
    def v(self, value):
        if value.get('host') is not None: self.host.v = value['host']
        if value.get('port') is not None: self.port.v = value['port']
        if value.get('userName') is not None: self.userName.v = value['userName']
        if value.get('passwd') is not None: self.passwd.v = value['passwd']


class PasswdMqttInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'passwd'
        self.name = '密码'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class UserNameMqttInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'userName'
        self.name = '用户名'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class PortMqttInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'port'
        self.name = '端口'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = PortMqttInfoPropertyStructSpecs()
        self.v: int = 0


class PortMqttInfoPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 65535


class HostMqttInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'host'
        self.name = '地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class VersionProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'version'
        self.name = '版本信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = VersionPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class VersionPropertyStruct:
    def __init__(self) -> None:
        self.firmwareVersion = FirmwareVersionVersionPropertyStruct()
        self.appVersion = AppVersionVersionPropertyStruct()

    @property
    def v(self):
        return {'firmwareVersion': self.firmwareVersion.v, 'appVersion': self.appVersion.v}

    @v.setter
    def v(self, value):
        if value.get('firmwareVersion') is not None: self.firmwareVersion.v = value['firmwareVersion']
        if value.get('appVersion') is not None: self.appVersion.v = value['appVersion']


class AppVersionVersionPropertyStruct:
    def __init__(self) -> None:
        self.id = 'appVersion'
        self.name = '应用版本号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class FirmwareVersionVersionPropertyStruct:
    def __init__(self) -> None:
        self.id = 'firmwareVersion'
        self.name = '固件版本号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class ConfigureModeProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'configureMode'
        self.name = '运行模式'
        self.accessMode = 'rw'
        self.required = True
        self.type = 'string'
        self.specs = ConfigureModePropertySpecs()
        self.v: str = ''


class ConfigureModePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ConfigureModePropertySpecsOptional()


class ConfigureModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.factory = FactoryConfigureModePropertySpecsOptional()
        self.configure = ConfigureConfigureModePropertySpecsOptional()
        self.networking = NetworkingConfigureModePropertySpecsOptional()
        self.active = ActiveConfigureModePropertySpecsOptional()


class ActiveConfigureModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'active'
        self.desc = '激活模式'


class NetworkingConfigureModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'networking'
        self.desc = '入网模式'


class ConfigureConfigureModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'configure'
        self.desc = '配置模式'


class FactoryConfigureModePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'factory'
        self.desc = '出厂模式'


class LogHostProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'logHost'
        self.name = '日志服务器地址'
        self.accessMode = 'rw'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class HwInfoProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'hwInfo'
        self.name = '硬件信息'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'struct'
        self.struct = HwInfoPropertyStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class HwInfoPropertyStruct:
    def __init__(self) -> None:
        self.cpuUsed = CpuUsedHwInfoPropertyStruct()
        self.memUsed = MemUsedHwInfoPropertyStruct()
        self.hdUsed = HdUsedHwInfoPropertyStruct()
        self.temperature = TemperatureHwInfoPropertyStruct()

    @property
    def v(self):
        return {'cpuUsed': self.cpuUsed.v, 'memUsed': self.memUsed.v, 'hdUsed': self.hdUsed.v, 'temperature': self.temperature.v}

    @v.setter
    def v(self, value):
        if value.get('cpuUsed') is not None: self.cpuUsed.v = value['cpuUsed']
        if value.get('memUsed') is not None: self.memUsed.v = value['memUsed']
        if value.get('hdUsed') is not None: self.hdUsed.v = value['hdUsed']
        if value.get('temperature') is not None: self.temperature.v = value['temperature']


class TemperatureHwInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'temperature'
        self.name = '当前工作温度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'number'
        self.specs = TemperatureHwInfoPropertyStructSpecs()
        self.v: float = 0.0


class TemperatureHwInfoPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -40
        self.max = 100
        self.unit = '℃'
        self.unitName = '摄氏度'


class HdUsedHwInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'hdUsed'
        self.name = '硬盘使用率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = HdUsedHwInfoPropertyStructSpecs()
        self.v: int = 0


class HdUsedHwInfoPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = '%'
        self.unitName = '%'


class MemUsedHwInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'memUsed'
        self.name = '内存使用率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = MemUsedHwInfoPropertyStructSpecs()
        self.v: int = 0


class MemUsedHwInfoPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = '%'
        self.unitName = '%'


class CpuUsedHwInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'cpuUsed'
        self.name = 'CPU使用率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = CpuUsedHwInfoPropertyStructSpecs()
        self.v: int = 0


class CpuUsedHwInfoPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.unit = '%'
        self.unitName = '%'


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
        self.name = '系统启动时间'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = UpTimePropertySpecs()
        self.v: int = 0


class UpTimePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 2147483647
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
        self.ntpHostList = NtpHostListNtpInfoPropertyStruct()
        self.ntpStatus = NtpStatusNtpInfoPropertyStruct()

    @property
    def v(self):
        return {'ntpHostList': self.ntpHostList.v, 'ntpStatus': self.ntpStatus.v}

    @v.setter
    def v(self, value):
        if value.get('ntpHostList') is not None: self.ntpHostList.v = value['ntpHostList']
        if value.get('ntpStatus') is not None: self.ntpStatus.v = value['ntpStatus']


class NtpStatusNtpInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'ntpStatus'
        self.name = 'NTP校时状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = NtpStatusNtpInfoPropertyStructSpecs()
        self.v: int = 0


class NtpStatusNtpInfoPropertyStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = NtpStatusNtpInfoPropertyStructSpecsOptional()


class NtpStatusNtpInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1NtpStatusNtpInfoPropertyStructSpecsOptional()
        self.value0 = Value0NtpStatusNtpInfoPropertyStructSpecsOptional()


class Value0NtpStatusNtpInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未连通'


class Value1NtpStatusNtpInfoPropertyStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '已联通'


class NtpHostListNtpInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'ntpHostList'
        self.name = 'NTP校时服务器地址列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnSimple = [NtpHostListNtpInfoPropertyStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = NtpHostListNtpInfoPropertyStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class NtpHostListNtpInfoPropertyStructColumnSimpleStruct:
    def __init__(self) -> None:
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
        self.mac = MacNetworkInfoPropertyStruct()
        self.ip = IpNetworkInfoPropertyStruct()
        self.gateway = GatewayNetworkInfoPropertyStruct()
        self.mask = MaskNetworkInfoPropertyStruct()

    @property
    def v(self):
        return {'networkType': self.networkType.v, 'wirelessSupport': self.wirelessSupport.v, 'mac': self.mac.v, 'ip': self.ip.v, 'gateway': self.gateway.v, 'mask': self.mask.v}

    @v.setter
    def v(self, value):
        if value.get('networkType') is not None: self.networkType.v = value['networkType']
        if value.get('wirelessSupport') is not None: self.wirelessSupport.v = value['wirelessSupport']
        if value.get('mac') is not None: self.mac.v = value['mac']
        if value.get('ip') is not None: self.ip.v = value['ip']
        if value.get('gateway') is not None: self.gateway.v = value['gateway']
        if value.get('mask') is not None: self.mask.v = value['mask']


class MaskNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'mask'
        self.name = '有线子网掩码'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class GatewayNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'gateway'
        self.name = '有线默认网关'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class IpNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'ip'
        self.name = '有线IP地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.format = 'ipv4'
        self.v: str = ''


class MacNetworkInfoPropertyStruct:
    def __init__(self) -> None:
        self.id = 'mac'
        self.name = '有线MAC地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


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
        self.name = '当前网络类型'
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


class ModeProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'mode'
        self.name = '控制模式'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.description = '当前控制模式，自动(auto)/手动(manual)'
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


class OnlineProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'online'
        self.name = '在线状态'
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
        self.value1 = Value1OnlinePropertySpecsOptional()
        self.value0 = Value0OnlinePropertySpecsOptional()


class Value0OnlinePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '设备离线'


class Value1OnlinePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '设备在线'


class ProductIdProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'productId'
        self.name = '产品标识符'
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


class SnProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'sn'
        self.name = '设备序列号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''
