from .base_model import *


class S5_DH_CP902QJAU3F(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S5_DH_CP902QJAU3F'
        self.productName = '大华交通事件摄像头'
        self.properties = Properties()
        self.events = Events()
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.switchMode = SwitchModeService()
        self.reboot = RebootService()
        self.setTime = SetTimeService()
        self.refreshVideoResolution = RefreshVideoResolutionService()
        self.setAlarmPicUploadServer = SetAlarmPicUploadServerService()
        self.snapshot = SnapshotService()
        self.getVideoStream = GetVideoStreamService()
        self.setDHSDKAlarm = SetDHSDKAlarmService()


class SetDHSDKAlarmService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setDHSDKAlarm'
        self.name = '设置告警开关'
        self.type = 'management'
        self.parameters = SetDHSDKAlarmServiceParameters()
        self.output = None


class SetDHSDKAlarmServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelSetDHSDKAlarmServiceParameter()
        self.alarm = AlarmSetDHSDKAlarmServiceParameter()
        self.enable = EnableSetDHSDKAlarmServiceParameter()
        self.hasPic = HasPicSetDHSDKAlarmServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v, 'alarm': self.alarm.v, 'enable': self.enable.v, 'hasPic': self.hasPic.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('alarm') is not None: self.alarm.v = value['alarm']
        if value.get('enable') is not None: self.enable.v = value['enable']
        if value.get('hasPic') is not None: self.hasPic.v = value['hasPic']


class HasPicSetDHSDKAlarmServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'hasPic'
        self.name = '是否上传图片'
        self.type = 'integer'
        self.required = True
        self.specs = HasPicSetDHSDKAlarmServiceParameterSpecs()
        self.v: int = 0


class HasPicSetDHSDKAlarmServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = HasPicSetDHSDKAlarmServiceParameterSpecsOptional()


class HasPicSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1HasPicSetDHSDKAlarmServiceParameterSpecsOptional()
        self.value0 = Value0HasPicSetDHSDKAlarmServiceParameterSpecsOptional()


class Value0HasPicSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '不上传图片'


class Value1HasPicSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '上传图片'


class EnableSetDHSDKAlarmServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'enable'
        self.name = '订阅/取消订阅'
        self.type = 'integer'
        self.required = True
        self.specs = EnableSetDHSDKAlarmServiceParameterSpecs()
        self.v: int = 0


class EnableSetDHSDKAlarmServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EnableSetDHSDKAlarmServiceParameterSpecsOptional()


class EnableSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1EnableSetDHSDKAlarmServiceParameterSpecsOptional()
        self.value0 = Value0EnableSetDHSDKAlarmServiceParameterSpecsOptional()


class Value0EnableSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '取消订阅告警'


class Value1EnableSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '订阅告警'


class AlarmSetDHSDKAlarmServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'alarm'
        self.name = '告警类型'
        self.type = 'string'
        self.required = True
        self.specs = AlarmSetDHSDKAlarmServiceParameterSpecs()
        self.v: str = ''


class AlarmSetDHSDKAlarmServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = AlarmSetDHSDKAlarmServiceParameterSpecsOptional()


class AlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.trafficJam = TrafficJamAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.vehicleInBusRoute = VehicleInBusRouteAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.nonMotorInMotorRoute = NonMotorInMotorRouteAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.trafficAccident = TrafficAccidentAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.trafficJunctionMotor = TrafficJunctionMotorAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.trafficJunctionTruck = TrafficJunctionTruckAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.trafficPedestrain = TrafficPedestrainAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.nonMotorWithoutSafeHat = NonMotorWithoutSafeHatAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.trafficParking = TrafficParkingAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.trafficFlowState = TrafficFlowStateAlarmSetDHSDKAlarmServiceParameterSpecsOptional()


class TrafficFlowStateAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficFlowState'
        self.desc = '交通流量事件'


class TrafficParkingAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficParking'
        self.desc = '违章停车'


class NonMotorWithoutSafeHatAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'nonMotorWithoutSafeHat'
        self.desc = '非机动车未戴安全帽事件'


class TrafficPedestrainAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficPedestrain'
        self.desc = '交通行人事件'


class TrafficJunctionTruckAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJunctionTruck'
        self.desc = '交通路口事件----大卡车告警'


class TrafficJunctionMotorAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJunctionMotor'
        self.desc = '交通路口事件----机动车拌线入侵'


class TrafficAccidentAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficAccident'
        self.desc = '交通事故事件'


class NonMotorInMotorRouteAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'nonMotorInMotorRoute'
        self.desc = '非机动车占用机动车道'


class VehicleInBusRouteAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'vehicleInBusRoute'
        self.desc = '占用公交车道事件'


class TrafficJamAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJam'
        self.desc = '交通拥堵事件'


class ChannelSetDHSDKAlarmServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelSetDHSDKAlarmServiceParameterSpecs()
        self.v: int = 0


class ChannelSetDHSDKAlarmServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 1
        self.step = 1


class GetVideoStreamService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'getVideoStream'
        self.name = '获取视频流列表'
        self.type = 'management'
        self.parameters = GetVideoStreamServiceParameters()
        self.output = [GetVideoStreamServiceOutput()]


class GetVideoStreamServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.streamURL = StreamURLGetVideoStreamServiceOutput()

    @property
    def v(self):
        return {'streamURL': self.streamURL.v}

    @v.setter
    def v(self, value):
        if value.get('streamURL') is not None: self.streamURL.v = value['streamURL']


class StreamURLGetVideoStreamServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'streamURL'
        self.name = '视频流URL'
        self.type = 'string'
        self.v: str = ''


class GetVideoStreamServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelGetVideoStreamServiceParameter()
        self.stream = StreamGetVideoStreamServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v, 'stream': self.stream.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('stream') is not None: self.stream.v = value['stream']


class StreamGetVideoStreamServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'stream'
        self.name = '视频流ID'
        self.type = 'integer'
        self.required = True
        self.specs = StreamGetVideoStreamServiceParameterSpecs()
        self.v: int = 0


class StreamGetVideoStreamServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StreamGetVideoStreamServiceParameterSpecsOptional()


class StreamGetVideoStreamServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1StreamGetVideoStreamServiceParameterSpecsOptional()
        self.value2 = Value2StreamGetVideoStreamServiceParameterSpecsOptional()


class Value2StreamGetVideoStreamServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '子码流'


class Value1StreamGetVideoStreamServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '主码流'


class ChannelGetVideoStreamServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelGetVideoStreamServiceParameterSpecs()
        self.v: int = 0


class ChannelGetVideoStreamServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 1
        self.step = 1


class SnapshotService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'snapshot'
        self.name = '视频抓拍'
        self.type = 'business'
        self.parameters = SnapshotServiceParameters()
        self.output = [SnapshotServiceOutput()]


class SnapshotServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.imagePath = ImagePathSnapshotServiceOutput()

    @property
    def v(self):
        return {'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathSnapshotServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class SnapshotServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelSnapshotServiceParameter()
        self.url = UrlSnapshotServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v, 'url': self.url.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('url') is not None: self.url.v = value['url']


class UrlSnapshotServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'url'
        self.name = '图片上传地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ChannelSnapshotServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelSnapshotServiceParameterSpecs()
        self.v: int = 0


class ChannelSnapshotServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 1
        self.step = 1


class SetAlarmPicUploadServerService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setAlarmPicUploadServer'
        self.name = '设置图片上传地址'
        self.type = 'management'
        self.parameters = SetAlarmPicUploadServerServiceParameters()
        self.output = None


class SetAlarmPicUploadServerServiceParameters:
    def __init__(self) -> None:
        self.server = ServerSetAlarmPicUploadServerServiceParameter()

    @property
    def v(self):
        return {'server': self.server.v}

    @v.setter
    def v(self, value):
        if value.get('server') is not None: self.server.v = value['server']


class ServerSetAlarmPicUploadServerServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'server'
        self.name = '文件服务器地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class RefreshVideoResolutionService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'refreshVideoResolution'
        self.name = '刷新视频流分辨率'
        self.type = 'business'
        self.parameters = None
        self.output = [RefreshVideoResolutionServiceOutput()]


class RefreshVideoResolutionServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.resolutions = ResolutionsRefreshVideoResolutionServiceOutput()

    @property
    def v(self):
        return {'resolutions': self.resolutions.v}

    @v.setter
    def v(self, value):
        if value.get('resolutions') is not None: self.resolutions.v = value['resolutions']


class ResolutionsRefreshVideoResolutionServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'resolutions'
        self.name = '视频流分辨率'
        self.type = 'array'
        self.columnComplex = [ResolutionsRefreshVideoResolutionServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ResolutionsRefreshVideoResolutionServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ResolutionsRefreshVideoResolutionServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.channel = ChannelResolutionsRefreshVideoResolutionServiceOutputColumnComplexStruct()
        self.channelResolution = ChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'channel': self.channel.v, 'channelResolution': self.channelResolution.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('channelResolution') is not None: self.channelResolution.v = value['channelResolution']


class ChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelResolution'
        self.name = '通道分辨率'
        self.type = 'array'
        self.columnComplex = [ChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.name = NameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStruct()
        self.id = IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStruct()
        self.resolution = ResolutionChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'name': self.name.v, 'id': self.id.v, 'resolution': self.resolution.v}

    @v.setter
    def v(self, value):
        if value.get('name') is not None: self.name.v = value['name']
        if value.get('id') is not None: self.id.v = value['id']
        if value.get('resolution') is not None: self.resolution.v = value['resolution']


class ResolutionChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'resolution'
        self.name = '分辨率'
        self.type = 'struct'
        self.struct = ResolutionChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ResolutionChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.width = WidthResolutionChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.height = HeightResolutionChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'width': self.width.v, 'height': self.height.v}

    @v.setter
    def v(self, value):
        if value.get('width') is not None: self.width.v = value['width']
        if value.get('height') is not None: self.height.v = value['height']


class HeightResolutionChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'height'
        self.name = '垂直象素'
        self.type = 'integer'
        self.v: int = 0


class WidthResolutionChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'width'
        self.name = '水平象素'
        self.type = 'integer'
        self.v: int = 0


class IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'id'
        self.name = '视频流ID'
        self.type = 'number'
        self.specs = IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: float = 0.0


class IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()
        self.value2 = Value2IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class Value2IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '子码流'


class Value1IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '主码流'


class NameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'name'
        self.name = '视频流名称'
        self.type = 'string'
        self.specs = NameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: str = ''


class NameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = NameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class NameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.mainStream = MainStreamNameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()
        self.subStream = SubStreamNameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class SubStreamNameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'subStream'
        self.desc = '子码流'


class MainStreamNameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'mainStream'
        self.desc = '主码流'


class ChannelResolutionsRefreshVideoResolutionServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.specs = ChannelResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class ChannelResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 1
        self.step = 1


class SetTimeService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setTime'
        self.name = '设置时间'
        self.type = 'management'
        self.parameters = SetTimeServiceParameters()
        self.output = None


class SetTimeServiceParameters:
    def __init__(self) -> None:
        self.year = YearSetTimeServiceParameter()
        self.month = MonthSetTimeServiceParameter()
        self.day = DaySetTimeServiceParameter()
        self.hour = HourSetTimeServiceParameter()
        self.minute = MinuteSetTimeServiceParameter()
        self.second = SecondSetTimeServiceParameter()

    @property
    def v(self):
        return {'year': self.year.v, 'month': self.month.v, 'day': self.day.v, 'hour': self.hour.v, 'minute': self.minute.v, 'second': self.second.v}

    @v.setter
    def v(self, value):
        if value.get('year') is not None: self.year.v = value['year']
        if value.get('month') is not None: self.month.v = value['month']
        if value.get('day') is not None: self.day.v = value['day']
        if value.get('hour') is not None: self.hour.v = value['hour']
        if value.get('minute') is not None: self.minute.v = value['minute']
        if value.get('second') is not None: self.second.v = value['second']


class SecondSetTimeServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'second'
        self.name = '秒'
        self.type = 'integer'
        self.required = True
        self.specs = SecondSetTimeServiceParameterSpecs()
        self.v: int = 0


class SecondSetTimeServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 59
        self.unit = '秒'
        self.unitName = '秒'
        self.step = 1


class MinuteSetTimeServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'minute'
        self.name = '分'
        self.type = 'integer'
        self.required = True
        self.specs = MinuteSetTimeServiceParameterSpecs()
        self.v: int = 0


class MinuteSetTimeServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 59
        self.unit = '分'
        self.unitName = '分'
        self.step = 1


class HourSetTimeServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'hour'
        self.name = '时'
        self.type = 'integer'
        self.required = True
        self.specs = HourSetTimeServiceParameterSpecs()
        self.v: int = 0


class HourSetTimeServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 23
        self.unit = '时'
        self.unitName = '时'
        self.step = 1


class DaySetTimeServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'day'
        self.name = '日'
        self.type = 'integer'
        self.required = True
        self.specs = DaySetTimeServiceParameterSpecs()
        self.v: int = 0


class DaySetTimeServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 31
        self.unit = '日'
        self.unitName = '日'
        self.step = 1


class MonthSetTimeServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'month'
        self.name = '月'
        self.type = 'integer'
        self.required = True
        self.specs = MonthSetTimeServiceParameterSpecs()
        self.v: int = 0


class MonthSetTimeServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 12
        self.unit = '月'
        self.unitName = '月'
        self.step = 1


class YearSetTimeServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'year'
        self.name = '年'
        self.type = 'integer'
        self.required = True
        self.specs = YearSetTimeServiceParameterSpecs()
        self.v: int = 0


class YearSetTimeServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 9999
        self.unit = '年'
        self.unitName = '年'
        self.step = 1


class RebootService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'reboot'
        self.name = '重启'
        self.type = 'business'
        self.parameters = None
        self.output = None


class SwitchModeService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'switchMode'
        self.name = '切换控制模式'
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
        self.type = 'string'
        self.required = True
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
        self.trafficJam = TrafficJamEvent()
        self.vehicleInBusRoute = VehicleInBusRouteEvent()
        self.nonMotorInMotorRoute = NonMotorInMotorRouteEvent()
        self.trafficAccident = TrafficAccidentEvent()
        self.trafficJunctionMotor = TrafficJunctionMotorEvent()
        self.trafficJunctionTruck = TrafficJunctionTruckEvent()
        self.trafficPedestrain = TrafficPedestrainEvent()
        self.nonMotorWithoutSafeHat = NonMotorWithoutSafeHatEvent()
        self.trafficParking = TrafficParkingEvent()
        self.trafficFlowState = TrafficFlowStateEvent()


class TrafficFlowStateEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'trafficFlowState'
        self.name = '交通流量事件'
        self.parameters = TrafficFlowStateEventParameters()


class TrafficFlowStateEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeTrafficFlowStateEventParameter()
        self.stateNum = StateNumTrafficFlowStateEventParameter()
        self.states = StatesTrafficFlowStateEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'stateNum': self.stateNum.v, 'states': self.states.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('stateNum') is not None: self.stateNum.v = value['stateNum']
        if value.get('states') is not None: self.states.v = value['states']


class StatesTrafficFlowStateEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'states'
        self.name = '流量状态'
        self.type = 'array'
        self.columnComplex = [StatesTrafficFlowStateEventParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = StatesTrafficFlowStateEventParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class StatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.lane = LaneStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.dwState = DwStateStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.flow = FlowStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.period = PeriodStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.trafficFlowDir_drivingDir = TrafficFlowDir_drivingDirStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.vehicles = VehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.averageSpeed = AverageSpeedStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.averageLength = AverageLengthStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.timeOccupyRatio = TimeOccupyRatioStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.spaceOccupyRatio = SpaceOccupyRatioStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.spaceHeadway = SpaceHeadwayStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.timeHeadway = TimeHeadwayStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.density = DensityStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.overSpeedVehicles = OverSpeedVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.underSpeedVehicles = UnderSpeedVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.largeVehicles = LargeVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.mediumVehicles = MediumVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.smallVehicles = SmallVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.motoVehicles = MotoVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.longVehicles = LongVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.volume = VolumeStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.flowRate = FlowRateStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.backOfQueue = BackOfQueueStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.travelTime = TravelTimeStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.delay = DelayStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.direction = DirectionStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.directionNum = DirectionNumStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.jamState = JamStateStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.passengerCarVehicles = PassengerCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.largeTruckVehicles = LargeTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.midTruckVehicles = MidTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.saloonCarVehicles = SaloonCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.microbusVehicles = MicrobusVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.microTruckVehicles = MicroTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.tricycleVehicles = TricycleVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.motorcycleVehicles = MotorcycleVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.passerbyVehicles = PasserbyVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.rank = RankStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.nState = NStateStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.statistics = StatisticsStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.leftVehicles = LeftVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.rightVehicles = RightVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.straightVehicles = StraightVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.uTurnVehicles = UTurnVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.backOfQueue = BackOfQueueStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.periodByMili = PeriodByMiliStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.busVehicles = BusVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.MPVVehicles = MPVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.midPassengerCarVehicles = MidPassengerCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.miniCarriageVehicles = MiniCarriageVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.oilTankTruckVehicles = OilTankTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.pickupVehicles = PickupVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.SUVVehicles = SUVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.SUVorMPVVehicles = SUVorMPVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.tankCarVehicles = TankCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.unknownVehicles = UnknownVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct()
        self.customFlowAttribute = CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStruct()

    @property
    def v(self):
        return {'lane': self.lane.v, 'dwState': self.dwState.v, 'flow': self.flow.v, 'period': self.period.v, 'trafficFlowDir_drivingDir': self.trafficFlowDir_drivingDir.v, 'vehicles': self.vehicles.v, 'averageSpeed': self.averageSpeed.v, 'averageLength': self.averageLength.v, 'timeOccupyRatio': self.timeOccupyRatio.v, 'spaceOccupyRatio': self.spaceOccupyRatio.v, 'spaceHeadway': self.spaceHeadway.v, 'timeHeadway': self.timeHeadway.v, 'density': self.density.v, 'overSpeedVehicles': self.overSpeedVehicles.v, 'underSpeedVehicles': self.underSpeedVehicles.v, 'largeVehicles': self.largeVehicles.v, 'mediumVehicles': self.mediumVehicles.v, 'smallVehicles': self.smallVehicles.v, 'motoVehicles': self.motoVehicles.v, 'longVehicles': self.longVehicles.v, 'volume': self.volume.v, 'flowRate': self.flowRate.v, 'backOfQueue': self.backOfQueue.v, 'travelTime': self.travelTime.v, 'delay': self.delay.v, 'direction': self.direction.v, 'directionNum': self.directionNum.v, 'jamState': self.jamState.v, 'passengerCarVehicles': self.passengerCarVehicles.v, 'largeTruckVehicles': self.largeTruckVehicles.v, 'midTruckVehicles': self.midTruckVehicles.v, 'saloonCarVehicles': self.saloonCarVehicles.v, 'microbusVehicles': self.microbusVehicles.v, 'microTruckVehicles': self.microTruckVehicles.v, 'tricycleVehicles': self.tricycleVehicles.v, 'motorcycleVehicles': self.motorcycleVehicles.v, 'passerbyVehicles': self.passerbyVehicles.v, 'rank': self.rank.v, 'nState': self.nState.v, 'statistics': self.statistics.v, 'leftVehicles': self.leftVehicles.v, 'rightVehicles': self.rightVehicles.v, 'straightVehicles': self.straightVehicles.v, 'uTurnVehicles': self.uTurnVehicles.v, 'backOfQueue': self.backOfQueue.v, 'periodByMili': self.periodByMili.v, 'busVehicles': self.busVehicles.v, 'MPVVehicles': self.MPVVehicles.v, 'midPassengerCarVehicles': self.midPassengerCarVehicles.v, 'miniCarriageVehicles': self.miniCarriageVehicles.v, 'oilTankTruckVehicles': self.oilTankTruckVehicles.v, 'pickupVehicles': self.pickupVehicles.v, 'SUVVehicles': self.SUVVehicles.v, 'SUVorMPVVehicles': self.SUVorMPVVehicles.v, 'tankCarVehicles': self.tankCarVehicles.v, 'unknownVehicles': self.unknownVehicles.v, 'customFlowAttribute': self.customFlowAttribute.v}

    @v.setter
    def v(self, value):
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('dwState') is not None: self.dwState.v = value['dwState']
        if value.get('flow') is not None: self.flow.v = value['flow']
        if value.get('period') is not None: self.period.v = value['period']
        if value.get('trafficFlowDir_drivingDir') is not None: self.trafficFlowDir_drivingDir.v = value['trafficFlowDir_drivingDir']
        if value.get('vehicles') is not None: self.vehicles.v = value['vehicles']
        if value.get('averageSpeed') is not None: self.averageSpeed.v = value['averageSpeed']
        if value.get('averageLength') is not None: self.averageLength.v = value['averageLength']
        if value.get('timeOccupyRatio') is not None: self.timeOccupyRatio.v = value['timeOccupyRatio']
        if value.get('spaceOccupyRatio') is not None: self.spaceOccupyRatio.v = value['spaceOccupyRatio']
        if value.get('spaceHeadway') is not None: self.spaceHeadway.v = value['spaceHeadway']
        if value.get('timeHeadway') is not None: self.timeHeadway.v = value['timeHeadway']
        if value.get('density') is not None: self.density.v = value['density']
        if value.get('overSpeedVehicles') is not None: self.overSpeedVehicles.v = value['overSpeedVehicles']
        if value.get('underSpeedVehicles') is not None: self.underSpeedVehicles.v = value['underSpeedVehicles']
        if value.get('largeVehicles') is not None: self.largeVehicles.v = value['largeVehicles']
        if value.get('mediumVehicles') is not None: self.mediumVehicles.v = value['mediumVehicles']
        if value.get('smallVehicles') is not None: self.smallVehicles.v = value['smallVehicles']
        if value.get('motoVehicles') is not None: self.motoVehicles.v = value['motoVehicles']
        if value.get('longVehicles') is not None: self.longVehicles.v = value['longVehicles']
        if value.get('volume') is not None: self.volume.v = value['volume']
        if value.get('flowRate') is not None: self.flowRate.v = value['flowRate']
        if value.get('backOfQueue') is not None: self.backOfQueue.v = value['backOfQueue']
        if value.get('travelTime') is not None: self.travelTime.v = value['travelTime']
        if value.get('delay') is not None: self.delay.v = value['delay']
        if value.get('direction') is not None: self.direction.v = value['direction']
        if value.get('directionNum') is not None: self.directionNum.v = value['directionNum']
        if value.get('jamState') is not None: self.jamState.v = value['jamState']
        if value.get('passengerCarVehicles') is not None: self.passengerCarVehicles.v = value['passengerCarVehicles']
        if value.get('largeTruckVehicles') is not None: self.largeTruckVehicles.v = value['largeTruckVehicles']
        if value.get('midTruckVehicles') is not None: self.midTruckVehicles.v = value['midTruckVehicles']
        if value.get('saloonCarVehicles') is not None: self.saloonCarVehicles.v = value['saloonCarVehicles']
        if value.get('microbusVehicles') is not None: self.microbusVehicles.v = value['microbusVehicles']
        if value.get('microTruckVehicles') is not None: self.microTruckVehicles.v = value['microTruckVehicles']
        if value.get('tricycleVehicles') is not None: self.tricycleVehicles.v = value['tricycleVehicles']
        if value.get('motorcycleVehicles') is not None: self.motorcycleVehicles.v = value['motorcycleVehicles']
        if value.get('passerbyVehicles') is not None: self.passerbyVehicles.v = value['passerbyVehicles']
        if value.get('rank') is not None: self.rank.v = value['rank']
        if value.get('nState') is not None: self.nState.v = value['nState']
        if value.get('statistics') is not None: self.statistics.v = value['statistics']
        if value.get('leftVehicles') is not None: self.leftVehicles.v = value['leftVehicles']
        if value.get('rightVehicles') is not None: self.rightVehicles.v = value['rightVehicles']
        if value.get('straightVehicles') is not None: self.straightVehicles.v = value['straightVehicles']
        if value.get('uTurnVehicles') is not None: self.uTurnVehicles.v = value['uTurnVehicles']
        if value.get('backOfQueue') is not None: self.backOfQueue.v = value['backOfQueue']
        if value.get('periodByMili') is not None: self.periodByMili.v = value['periodByMili']
        if value.get('busVehicles') is not None: self.busVehicles.v = value['busVehicles']
        if value.get('MPVVehicles') is not None: self.MPVVehicles.v = value['MPVVehicles']
        if value.get('midPassengerCarVehicles') is not None: self.midPassengerCarVehicles.v = value['midPassengerCarVehicles']
        if value.get('miniCarriageVehicles') is not None: self.miniCarriageVehicles.v = value['miniCarriageVehicles']
        if value.get('oilTankTruckVehicles') is not None: self.oilTankTruckVehicles.v = value['oilTankTruckVehicles']
        if value.get('pickupVehicles') is not None: self.pickupVehicles.v = value['pickupVehicles']
        if value.get('SUVVehicles') is not None: self.SUVVehicles.v = value['SUVVehicles']
        if value.get('SUVorMPVVehicles') is not None: self.SUVorMPVVehicles.v = value['SUVorMPVVehicles']
        if value.get('tankCarVehicles') is not None: self.tankCarVehicles.v = value['tankCarVehicles']
        if value.get('unknownVehicles') is not None: self.unknownVehicles.v = value['unknownVehicles']
        if value.get('customFlowAttribute') is not None: self.customFlowAttribute.v = value['customFlowAttribute']


class CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'customFlowAttribute'
        self.name = '车道流量信息属性'
        self.type = 'integer'
        self.specs = CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value1 = Value1CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value2 = Value2CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class Value2CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '排队检测'


class Value1CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '流量监测'


class Value0CustomFlowAttributeStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class UnknownVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'unknownVehicles'
        self.name = '未知车辆交通量'
        self.type = 'integer'
        self.specs = UnknownVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class UnknownVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class TankCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'tankCarVehicles'
        self.name = '槽罐车交通量'
        self.type = 'integer'
        self.specs = TankCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class TankCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class SUVorMPVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'SUVorMPVVehicles'
        self.name = 'SUV或者MPV交通量'
        self.type = 'integer'
        self.specs = SUVorMPVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class SUVorMPVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class SUVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'SUVVehicles'
        self.name = 'SUV交通量'
        self.type = 'integer'
        self.specs = SUVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class SUVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class PickupVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pickupVehicles'
        self.name = '皮卡车交通量'
        self.type = 'integer'
        self.specs = PickupVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class PickupVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class OilTankTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'oilTankTruckVehicles'
        self.name = '油罐车交通量'
        self.type = 'integer'
        self.specs = OilTankTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class OilTankTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class MiniCarriageVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'miniCarriageVehicles'
        self.name = '微型轿车交通量'
        self.type = 'integer'
        self.specs = MiniCarriageVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class MiniCarriageVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class MidPassengerCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'midPassengerCarVehicles'
        self.name = '中客车交通量'
        self.type = 'integer'
        self.specs = MidPassengerCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class MidPassengerCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class MPVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'MPVVehicles'
        self.name = 'MPV交通量'
        self.type = 'integer'
        self.specs = MPVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class MPVVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class BusVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'busVehicles'
        self.name = '公交车交通量'
        self.type = 'integer'
        self.specs = BusVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class BusVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class PeriodByMiliStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'periodByMili'
        self.name = '流量值的毫秒时间'
        self.type = 'integer'
        self.specs = PeriodByMiliStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class PeriodByMiliStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 60000
        self.unit = '毫秒'
        self.unitName = '毫秒'
        self.step = 1


class UTurnVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'uTurnVehicles'
        self.name = '掉头车辆总数'
        self.type = 'integer'
        self.specs = UTurnVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class UTurnVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆'
        self.unitName = '辆'


class StraightVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'straightVehicles'
        self.name = '直行车辆总数'
        self.type = 'integer'
        self.specs = StraightVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class StraightVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆'
        self.unitName = '辆'


class RightVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'rightVehicles'
        self.name = '右转车辆总数'
        self.type = 'integer'
        self.specs = RightVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class RightVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆'
        self.unitName = '辆'


class LeftVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'leftVehicles'
        self.name = '左转车辆总数'
        self.type = 'integer'
        self.specs = LeftVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class LeftVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆'
        self.unitName = '辆'


class StatisticsStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'statistics'
        self.name = '流量数据是否有效'
        self.type = 'integer'
        self.specs = StatisticsStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class StatisticsStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StatisticsStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class StatisticsStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0StatisticsStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value1 = Value1StatisticsStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class Value1StatisticsStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '有效'


class Value0StatisticsStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '无效'


class NStateStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'nState'
        self.name = '流量状态'
        self.type = 'integer'
        self.specs = NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value2 = Value2NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value3 = Value3NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value4 = Value4NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value5 = Value5NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class Value5NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '流量过小恢复（良好）'


class Value4NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 4
        self.desc = '流量过小（畅通）'


class Value3NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '正常'


class Value2NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '流量过大恢复（略堵）'


class Value1NStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '流量过大（拥堵）'


class RankStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'rank'
        self.name = '道路等级'
        self.type = 'integer'
        self.specs = RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value1 = Value1RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value2 = Value2RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value3 = Value3RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value3 = Value3RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class Value3RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '支路'


class Value2RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '主干路'


class Value1RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '快速路'


class Value0RankStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class PasserbyVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'passerbyVehicles'
        self.name = '行人交通量'
        self.type = 'integer'
        self.specs = PasserbyVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class PasserbyVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class MotorcycleVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'motorcycleVehicles'
        self.name = '摩托车交通量'
        self.type = 'integer'
        self.specs = MotorcycleVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class MotorcycleVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class TricycleVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'tricycleVehicles'
        self.name = '三轮车交通量'
        self.type = 'integer'
        self.specs = TricycleVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class TricycleVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class MicroTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'microTruckVehicles'
        self.name = '小货车交通量'
        self.type = 'integer'
        self.specs = MicroTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class MicroTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class MicrobusVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'microbusVehicles'
        self.name = '面包车交通量'
        self.type = 'integer'
        self.specs = MicrobusVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class MicrobusVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class SaloonCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'saloonCarVehicles'
        self.name = '轿车交通量'
        self.type = 'integer'
        self.specs = SaloonCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class SaloonCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class MidTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'midTruckVehicles'
        self.name = '中货车交通量'
        self.type = 'integer'
        self.specs = MidTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class MidTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class LargeTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'largeTruckVehicles'
        self.name = '大货车交通量'
        self.type = 'integer'
        self.specs = LargeTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class LargeTruckVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class PassengerCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'passengerCarVehicles'
        self.name = '客车交通量'
        self.type = 'integer'
        self.specs = PassengerCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class PassengerCarVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class JamStateStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'jamState'
        self.name = '道路拥挤状况'
        self.type = 'integer'
        self.specs = JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value1 = Value1JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value2 = Value2JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value3 = Value3JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class Value3JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '拥堵'


class Value2JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '拥堵'


class Value1JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '通畅'


class Value0JamStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class DirectionNumStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'directionNum'
        self.name = '车道行驶方向个数'
        self.type = 'integer'
        self.v: int = 0


class DirectionStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'direction'
        self.name = '车道方向'
        self.type = 'string'
        self.v: str = ''


class DelayStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'delay'
        self.name = '延误'
        self.type = 'integer'
        self.specs = DelayStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class DelayStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '秒'
        self.unitName = '秒'


class TravelTimeStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'travelTime'
        self.name = '旅行时间'
        self.type = 'integer'
        self.specs = TravelTimeStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class TravelTimeStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '秒'
        self.unitName = '秒'


class BackOfQueueStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'backOfQueue'
        self.name = '排队长度'
        self.type = 'number'
        self.specs = BackOfQueueStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class BackOfQueueStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '米'
        self.unitName = '米'


class FlowRateStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'flowRate'
        self.name = '流率小车当量'
        self.type = 'integer'
        self.specs = FlowRateStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class FlowRateStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/小时'
        self.unitName = '辆/小时'


class VolumeStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'volume'
        self.name = '交通量'
        self.type = 'integer'
        self.specs = VolumeStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class VolumeStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class LongVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'longVehicles'
        self.name = '超长交通量'
        self.type = 'integer'
        self.specs = LongVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class LongVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class MotoVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'motoVehicles'
        self.name = '摩托交通量'
        self.type = 'integer'
        self.specs = MotoVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class MotoVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class SmallVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'smallVehicles'
        self.name = '小车交通量'
        self.type = 'integer'
        self.specs = SmallVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class SmallVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class MediumVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'mediumVehicles'
        self.name = '中型车交通量'
        self.type = 'integer'
        self.specs = MediumVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class MediumVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class LargeVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'largeVehicles'
        self.name = '大车交通量'
        self.type = 'integer'
        self.specs = LargeVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class LargeVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/单位时间'
        self.unitName = '辆/单位时间'


class UnderSpeedVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'underSpeedVehicles'
        self.name = '低速车辆数'
        self.type = 'integer'
        self.specs = UnderSpeedVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class UnderSpeedVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆'
        self.unitName = '辆'


class OverSpeedVehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'overSpeedVehicles'
        self.name = '超速车辆数'
        self.type = 'integer'
        self.specs = OverSpeedVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class OverSpeedVehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆'
        self.unitName = '辆'


class DensityStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'density'
        self.name = '车辆密度'
        self.type = 'number'
        self.specs = DensityStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class DensityStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆/km'
        self.unitName = '辆/km'


class TimeHeadwayStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'timeHeadway'
        self.name = '车头时距'
        self.type = 'number'
        self.specs = TimeHeadwayStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class TimeHeadwayStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '秒/辆'
        self.unitName = '秒/辆'


class SpaceHeadwayStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'spaceHeadway'
        self.name = '车头间距'
        self.type = 'number'
        self.specs = SpaceHeadwayStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class SpaceHeadwayStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '米/辆'
        self.unitName = '米/辆'


class SpaceOccupyRatioStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'spaceOccupyRatio'
        self.name = '空间占有率'
        self.type = 'number'
        self.v: float = 0.0


class TimeOccupyRatioStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'timeOccupyRatio'
        self.name = '时间占有率'
        self.type = 'number'
        self.v: float = 0.0


class AverageLengthStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'averageLength'
        self.name = '平均车长'
        self.type = 'number'
        self.specs = AverageLengthStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class AverageLengthStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '米'
        self.unitName = '米'


class AverageSpeedStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'averageSpeed'
        self.name = '平均车速'
        self.type = 'number'
        self.specs = AverageSpeedStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class AverageSpeedStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = 'km/h'
        self.unitName = 'km/h'


class VehiclesStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'vehicles'
        self.name = '通过车辆总数'
        self.type = 'integer'
        self.specs = VehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class VehiclesStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆'
        self.unitName = '辆'


class TrafficFlowDir_drivingDirStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'trafficFlowDir_drivingDir'
        self.name = '车道方向信息'
        self.type = 'integer'
        self.specs = TrafficFlowDir_drivingDirStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class TrafficFlowDir_drivingDirStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TrafficFlowDir_drivingDirStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class TrafficFlowDir_drivingDirStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1TrafficFlowDir_drivingDirStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value2 = Value2TrafficFlowDir_drivingDirStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class Value2TrafficFlowDir_drivingDirStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '下行,即车辆离设备部署点越来越远'


class Value1TrafficFlowDir_drivingDirStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '上行,即车辆离设备部署点越来越近'


class PeriodStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'period'
        self.name = '流量值对应的统计时间'
        self.type = 'integer'
        self.specs = PeriodStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class PeriodStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 250
        self.unit = '分钟'
        self.unitName = '分钟'
        self.step = 1


class FlowStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'flow'
        self.name = '流量值'
        self.type = 'integer'
        self.specs = FlowStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class FlowStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '辆'
        self.unitName = '辆'


class DwStateStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'dwState'
        self.name = '状态值'
        self.type = 'integer'
        self.specs = DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value2 = Value2DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value3 = Value3DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value4 = Value4DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()
        self.value5 = Value5DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional()


class Value5DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '流量过小恢复'


class Value4DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 4
        self.desc = '流量过小'


class Value3DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '正常'


class Value2DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '流量过大恢复'


class Value1DwStateStatesTrafficFlowStateEventParameterColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '流量过大'


class LaneStatesTrafficFlowStateEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LaneStatesTrafficFlowStateEventParameterColumnComplexStructSpecs()
        self.v: int = 0


class LaneStatesTrafficFlowStateEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class StateNumTrafficFlowStateEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'stateNum'
        self.name = '流量状态数量'
        self.type = 'integer'
        self.specs = StateNumTrafficFlowStateEventParameterSpecs()
        self.v: int = 0


class StateNumTrafficFlowStateEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class EventTypeTrafficFlowStateEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeTrafficFlowStateEventParameterSpecs()
        self.v: str = ''


class EventTypeTrafficFlowStateEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeTrafficFlowStateEventParameterSpecsOptional()


class EventTypeTrafficFlowStateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.trafficFlowState = TrafficFlowStateEventTypeTrafficFlowStateEventParameterSpecsOptional()


class TrafficFlowStateEventTypeTrafficFlowStateEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficFlowState'
        self.desc = '交通流量事件'


class TrafficParkingEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'trafficParking'
        self.name = '违章停车'
        self.parameters = TrafficParkingEventParameters()


class TrafficParkingEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeTrafficParkingEventParameter()
        self.process = ProcessTrafficParkingEventParameter()
        self.lane = LaneTrafficParkingEventParameter()
        self.objectType = ObjectTypeTrafficParkingEventParameter()
        self.type = TypeTrafficParkingEventParameter()
        self.plateNumber = PlateNumberTrafficParkingEventParameter()
        self.imagePath = ImagePathTrafficParkingEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'objectType': self.objectType.v, 'type': self.type.v, 'plateNumber': self.plateNumber.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('objectType') is not None: self.objectType.v = value['objectType']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('plateNumber') is not None: self.plateNumber.v = value['plateNumber']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathTrafficParkingEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class PlateNumberTrafficParkingEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'plateNumber'
        self.name = '车牌号'
        self.type = 'string'
        self.v: str = ''


class TypeTrafficParkingEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'type'
        self.name = '车型'
        self.type = 'string'
        self.v: str = ''


class ObjectTypeTrafficParkingEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'objectType'
        self.name = '物体类型'
        self.type = 'string'
        self.v: str = ''


class LaneTrafficParkingEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LaneTrafficParkingEventParameterSpecs()
        self.v: int = 0


class LaneTrafficParkingEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessTrafficParkingEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessTrafficParkingEventParameterSpecs()
        self.v: int = 0


class ProcessTrafficParkingEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessTrafficParkingEventParameterSpecsOptional()


class ProcessTrafficParkingEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessTrafficParkingEventParameterSpecsOptional()


class Value1ProcessTrafficParkingEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeTrafficParkingEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeTrafficParkingEventParameterSpecs()
        self.v: str = ''


class EventTypeTrafficParkingEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeTrafficParkingEventParameterSpecsOptional()


class EventTypeTrafficParkingEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.trafficParking = TrafficParkingEventTypeTrafficParkingEventParameterSpecsOptional()


class TrafficParkingEventTypeTrafficParkingEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficParking'
        self.desc = '违章停车'


class NonMotorWithoutSafeHatEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'nonMotorWithoutSafeHat'
        self.name = '非机动车未戴安全帽事件'
        self.parameters = NonMotorWithoutSafeHatEventParameters()


class NonMotorWithoutSafeHatEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeNonMotorWithoutSafeHatEventParameter()
        self.process = ProcessNonMotorWithoutSafeHatEventParameter()
        self.lane = LaneNonMotorWithoutSafeHatEventParameter()
        self.imagePath = ImagePathNonMotorWithoutSafeHatEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathNonMotorWithoutSafeHatEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class LaneNonMotorWithoutSafeHatEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LaneNonMotorWithoutSafeHatEventParameterSpecs()
        self.v: int = 0


class LaneNonMotorWithoutSafeHatEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessNonMotorWithoutSafeHatEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessNonMotorWithoutSafeHatEventParameterSpecs()
        self.v: int = 0


class ProcessNonMotorWithoutSafeHatEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessNonMotorWithoutSafeHatEventParameterSpecsOptional()


class ProcessNonMotorWithoutSafeHatEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessNonMotorWithoutSafeHatEventParameterSpecsOptional()


class Value1ProcessNonMotorWithoutSafeHatEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeNonMotorWithoutSafeHatEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeNonMotorWithoutSafeHatEventParameterSpecs()
        self.v: str = ''


class EventTypeNonMotorWithoutSafeHatEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeNonMotorWithoutSafeHatEventParameterSpecsOptional()


class EventTypeNonMotorWithoutSafeHatEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.nonMotorWithoutSafeHat = NonMotorWithoutSafeHatEventTypeNonMotorWithoutSafeHatEventParameterSpecsOptional()


class NonMotorWithoutSafeHatEventTypeNonMotorWithoutSafeHatEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'nonMotorWithoutSafeHat'
        self.desc = '非机动车未戴安全帽事件'


class TrafficPedestrainEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'trafficPedestrain'
        self.name = '交通行人事件'
        self.parameters = TrafficPedestrainEventParameters()


class TrafficPedestrainEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeTrafficPedestrainEventParameter()
        self.process = ProcessTrafficPedestrainEventParameter()
        self.lane = LaneTrafficPedestrainEventParameter()
        self.imagePath = ImagePathTrafficPedestrainEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathTrafficPedestrainEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class LaneTrafficPedestrainEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LaneTrafficPedestrainEventParameterSpecs()
        self.v: int = 0


class LaneTrafficPedestrainEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessTrafficPedestrainEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessTrafficPedestrainEventParameterSpecs()
        self.v: int = 0


class ProcessTrafficPedestrainEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessTrafficPedestrainEventParameterSpecsOptional()


class ProcessTrafficPedestrainEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessTrafficPedestrainEventParameterSpecsOptional()


class Value1ProcessTrafficPedestrainEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeTrafficPedestrainEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeTrafficPedestrainEventParameterSpecs()
        self.v: str = ''


class EventTypeTrafficPedestrainEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeTrafficPedestrainEventParameterSpecsOptional()


class EventTypeTrafficPedestrainEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.trafficPedestrain = TrafficPedestrainEventTypeTrafficPedestrainEventParameterSpecsOptional()


class TrafficPedestrainEventTypeTrafficPedestrainEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficPedestrain'
        self.desc = '交通行人事件'


class TrafficJunctionTruckEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'trafficJunctionTruck'
        self.name = '交通路口事件----大卡车告警'
        self.parameters = TrafficJunctionTruckEventParameters()


class TrafficJunctionTruckEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeTrafficJunctionTruckEventParameter()
        self.process = ProcessTrafficJunctionTruckEventParameter()
        self.lane = LaneTrafficJunctionTruckEventParameter()
        self.objectType = ObjectTypeTrafficJunctionTruckEventParameter()
        self.type = TypeTrafficJunctionTruckEventParameter()
        self.plateNumber = PlateNumberTrafficJunctionTruckEventParameter()
        self.imagePath = ImagePathTrafficJunctionTruckEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'objectType': self.objectType.v, 'type': self.type.v, 'plateNumber': self.plateNumber.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('objectType') is not None: self.objectType.v = value['objectType']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('plateNumber') is not None: self.plateNumber.v = value['plateNumber']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathTrafficJunctionTruckEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class PlateNumberTrafficJunctionTruckEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'plateNumber'
        self.name = '车牌号'
        self.type = 'string'
        self.v: str = ''


class TypeTrafficJunctionTruckEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'type'
        self.name = '车型'
        self.type = 'string'
        self.v: str = ''


class ObjectTypeTrafficJunctionTruckEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'objectType'
        self.name = '物体类型'
        self.type = 'string'
        self.v: str = ''


class LaneTrafficJunctionTruckEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LaneTrafficJunctionTruckEventParameterSpecs()
        self.v: int = 0


class LaneTrafficJunctionTruckEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessTrafficJunctionTruckEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessTrafficJunctionTruckEventParameterSpecs()
        self.v: int = 0


class ProcessTrafficJunctionTruckEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessTrafficJunctionTruckEventParameterSpecsOptional()


class ProcessTrafficJunctionTruckEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessTrafficJunctionTruckEventParameterSpecsOptional()


class Value1ProcessTrafficJunctionTruckEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeTrafficJunctionTruckEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeTrafficJunctionTruckEventParameterSpecs()
        self.v: str = ''


class EventTypeTrafficJunctionTruckEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeTrafficJunctionTruckEventParameterSpecsOptional()


class EventTypeTrafficJunctionTruckEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.trafficJunctionTruck = TrafficJunctionTruckEventTypeTrafficJunctionTruckEventParameterSpecsOptional()


class TrafficJunctionTruckEventTypeTrafficJunctionTruckEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJunctionTruck'
        self.desc = '交通路口事件----大卡车告警'


class TrafficJunctionMotorEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'trafficJunctionMotor'
        self.name = '交通路口事件----机动车拌线入侵'
        self.parameters = TrafficJunctionMotorEventParameters()


class TrafficJunctionMotorEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeTrafficJunctionMotorEventParameter()
        self.process = ProcessTrafficJunctionMotorEventParameter()
        self.lane = LaneTrafficJunctionMotorEventParameter()
        self.objectType = ObjectTypeTrafficJunctionMotorEventParameter()
        self.type = TypeTrafficJunctionMotorEventParameter()
        self.plateNumber = PlateNumberTrafficJunctionMotorEventParameter()
        self.imagePath = ImagePathTrafficJunctionMotorEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'objectType': self.objectType.v, 'type': self.type.v, 'plateNumber': self.plateNumber.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('objectType') is not None: self.objectType.v = value['objectType']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('plateNumber') is not None: self.plateNumber.v = value['plateNumber']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathTrafficJunctionMotorEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class PlateNumberTrafficJunctionMotorEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'plateNumber'
        self.name = '车牌号'
        self.type = 'string'
        self.v: str = ''


class TypeTrafficJunctionMotorEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'type'
        self.name = '车型'
        self.type = 'string'
        self.v: str = ''


class ObjectTypeTrafficJunctionMotorEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'objectType'
        self.name = '物体类型'
        self.type = 'string'
        self.v: str = ''


class LaneTrafficJunctionMotorEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LaneTrafficJunctionMotorEventParameterSpecs()
        self.v: int = 0


class LaneTrafficJunctionMotorEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessTrafficJunctionMotorEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessTrafficJunctionMotorEventParameterSpecs()
        self.v: int = 0


class ProcessTrafficJunctionMotorEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessTrafficJunctionMotorEventParameterSpecsOptional()


class ProcessTrafficJunctionMotorEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessTrafficJunctionMotorEventParameterSpecsOptional()


class Value1ProcessTrafficJunctionMotorEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeTrafficJunctionMotorEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeTrafficJunctionMotorEventParameterSpecs()
        self.v: str = ''


class EventTypeTrafficJunctionMotorEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeTrafficJunctionMotorEventParameterSpecsOptional()


class EventTypeTrafficJunctionMotorEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.trafficJunctionMotor = TrafficJunctionMotorEventTypeTrafficJunctionMotorEventParameterSpecsOptional()


class TrafficJunctionMotorEventTypeTrafficJunctionMotorEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJunctionMotor'
        self.desc = '交通路口事件----机动车拌线入侵'


class TrafficAccidentEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'trafficAccident'
        self.name = '交通事故事件'
        self.parameters = TrafficAccidentEventParameters()


class TrafficAccidentEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeTrafficAccidentEventParameter()
        self.process = ProcessTrafficAccidentEventParameter()
        self.lane = LaneTrafficAccidentEventParameter()
        self.imagePath = ImagePathTrafficAccidentEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathTrafficAccidentEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class LaneTrafficAccidentEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LaneTrafficAccidentEventParameterSpecs()
        self.v: int = 0


class LaneTrafficAccidentEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessTrafficAccidentEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessTrafficAccidentEventParameterSpecs()
        self.v: int = 0


class ProcessTrafficAccidentEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessTrafficAccidentEventParameterSpecsOptional()


class ProcessTrafficAccidentEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessTrafficAccidentEventParameterSpecsOptional()


class Value1ProcessTrafficAccidentEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeTrafficAccidentEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeTrafficAccidentEventParameterSpecs()
        self.v: str = ''


class EventTypeTrafficAccidentEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeTrafficAccidentEventParameterSpecsOptional()


class EventTypeTrafficAccidentEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.trafficAccident = TrafficAccidentEventTypeTrafficAccidentEventParameterSpecsOptional()


class TrafficAccidentEventTypeTrafficAccidentEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficAccident'
        self.desc = '交通事故事件'


class NonMotorInMotorRouteEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'nonMotorInMotorRoute'
        self.name = '非机动车占用机动车道'
        self.parameters = NonMotorInMotorRouteEventParameters()


class NonMotorInMotorRouteEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeNonMotorInMotorRouteEventParameter()
        self.process = ProcessNonMotorInMotorRouteEventParameter()
        self.lane = LaneNonMotorInMotorRouteEventParameter()
        self.imagePath = ImagePathNonMotorInMotorRouteEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathNonMotorInMotorRouteEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class LaneNonMotorInMotorRouteEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LaneNonMotorInMotorRouteEventParameterSpecs()
        self.v: int = 0


class LaneNonMotorInMotorRouteEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessNonMotorInMotorRouteEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessNonMotorInMotorRouteEventParameterSpecs()
        self.v: int = 0


class ProcessNonMotorInMotorRouteEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessNonMotorInMotorRouteEventParameterSpecsOptional()


class ProcessNonMotorInMotorRouteEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessNonMotorInMotorRouteEventParameterSpecsOptional()


class Value1ProcessNonMotorInMotorRouteEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeNonMotorInMotorRouteEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeNonMotorInMotorRouteEventParameterSpecs()
        self.v: str = ''


class EventTypeNonMotorInMotorRouteEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeNonMotorInMotorRouteEventParameterSpecsOptional()


class EventTypeNonMotorInMotorRouteEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.nonMotorInMotorRoute = NonMotorInMotorRouteEventTypeNonMotorInMotorRouteEventParameterSpecsOptional()


class NonMotorInMotorRouteEventTypeNonMotorInMotorRouteEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'nonMotorInMotorRoute'
        self.desc = '非机动车占用机动车道'


class VehicleInBusRouteEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'vehicleInBusRoute'
        self.name = '占用公交车道事件'
        self.parameters = VehicleInBusRouteEventParameters()


class VehicleInBusRouteEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeVehicleInBusRouteEventParameter()
        self.process = ProcessVehicleInBusRouteEventParameter()
        self.lane = LaneVehicleInBusRouteEventParameter()
        self.objectType = ObjectTypeVehicleInBusRouteEventParameter()
        self.type = TypeVehicleInBusRouteEventParameter()
        self.imagePath = ImagePathVehicleInBusRouteEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'objectType': self.objectType.v, 'type': self.type.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('objectType') is not None: self.objectType.v = value['objectType']
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathVehicleInBusRouteEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class TypeVehicleInBusRouteEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'type'
        self.name = '物体子类型'
        self.type = 'string'
        self.v: str = ''


class ObjectTypeVehicleInBusRouteEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'objectType'
        self.name = '物体类型'
        self.type = 'string'
        self.v: str = ''


class LaneVehicleInBusRouteEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LaneVehicleInBusRouteEventParameterSpecs()
        self.v: int = 0


class LaneVehicleInBusRouteEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessVehicleInBusRouteEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessVehicleInBusRouteEventParameterSpecs()
        self.v: int = 0


class ProcessVehicleInBusRouteEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessVehicleInBusRouteEventParameterSpecsOptional()


class ProcessVehicleInBusRouteEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessVehicleInBusRouteEventParameterSpecsOptional()


class Value1ProcessVehicleInBusRouteEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeVehicleInBusRouteEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeVehicleInBusRouteEventParameterSpecs()
        self.v: str = ''


class EventTypeVehicleInBusRouteEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeVehicleInBusRouteEventParameterSpecsOptional()


class EventTypeVehicleInBusRouteEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.vehicleInBusRoute = VehicleInBusRouteEventTypeVehicleInBusRouteEventParameterSpecsOptional()


class VehicleInBusRouteEventTypeVehicleInBusRouteEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'vehicleInBusRoute'
        self.desc = '占用公交车道事件'


class TrafficJamEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'trafficJam'
        self.name = '交通拥堵事件'
        self.parameters = TrafficJamEventParameters()


class TrafficJamEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeTrafficJamEventParameter()
        self.process = ProcessTrafficJamEventParameter()
        self.lane = LaneTrafficJamEventParameter()
        self.trafficJamLength = TrafficJamLengthTrafficJamEventParameter()
        self.imagePath = ImagePathTrafficJamEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'trafficJamLength': self.trafficJamLength.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('trafficJamLength') is not None: self.trafficJamLength.v = value['trafficJamLength']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathTrafficJamEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class TrafficJamLengthTrafficJamEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'trafficJamLength'
        self.name = '拥堵长度'
        self.type = 'integer'
        self.specs = TrafficJamLengthTrafficJamEventParameterSpecs()
        self.v: int = 0


class TrafficJamLengthTrafficJamEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.unit = '米'
        self.unitName = '米'


class LaneTrafficJamEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LaneTrafficJamEventParameterSpecs()
        self.v: int = 0


class LaneTrafficJamEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessTrafficJamEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessTrafficJamEventParameterSpecs()
        self.v: int = 0


class ProcessTrafficJamEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessTrafficJamEventParameterSpecsOptional()


class ProcessTrafficJamEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessTrafficJamEventParameterSpecsOptional()


class Value1ProcessTrafficJamEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeTrafficJamEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeTrafficJamEventParameterSpecs()
        self.v: str = ''


class EventTypeTrafficJamEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeTrafficJamEventParameterSpecsOptional()


class EventTypeTrafficJamEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.trafficJam = TrafficJamEventTypeTrafficJamEventParameterSpecsOptional()


class TrafficJamEventTypeTrafficJamEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJam'
        self.desc = '交通拥堵事件'


class Properties:
    def __init__(self) -> None:
        self.sn = SnProperty()
        self.ip = IpProperty()
        self.httpPort = HttpPortProperty()
        self.onvifUser = OnvifUserProperty()
        self.onvifPassword = OnvifPasswordProperty()
        self.online = OnlineProperty()
        self.mode = ModeProperty()
        self.manufacturer = ManufacturerProperty()
        self.model = ModelProperty()
        self.channelCnt = ChannelCntProperty()
        self.channels = ChannelsProperty()

    @property
    def v(self):
        return {'sn': self.sn.v, 'ip': self.ip.v, 'httpPort': self.httpPort.v, 'onvifUser': self.onvifUser.v, 'onvifPassword': self.onvifPassword.v, 'online': self.online.v, 'mode': self.mode.v, 'manufacturer': self.manufacturer.v, 'model': self.model.v, 'channelCnt': self.channelCnt.v, 'channels': self.channels.v}

    @v.setter
    def v(self, value):
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('ip') is not None: self.ip.v = value['ip']
        if value.get('httpPort') is not None: self.httpPort.v = value['httpPort']
        if value.get('onvifUser') is not None: self.onvifUser.v = value['onvifUser']
        if value.get('onvifPassword') is not None: self.onvifPassword.v = value['onvifPassword']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('manufacturer') is not None: self.manufacturer.v = value['manufacturer']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('channelCnt') is not None: self.channelCnt.v = value['channelCnt']
        if value.get('channels') is not None: self.channels.v = value['channels']


class ChannelsProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channels'
        self.name = '通道属性'
        self.accessMode = 'ro'
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
        self.id = IdChannelsPropertyColumnComplexStruct()
        self.alarmList = AlarmListChannelsPropertyColumnComplexStruct()
        self.streamCnt = StreamCntChannelsPropertyColumnComplexStruct()
        self.resolutions = ResolutionsChannelsPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'id': self.id.v, 'alarmList': self.alarmList.v, 'streamCnt': self.streamCnt.v, 'resolutions': self.resolutions.v}

    @v.setter
    def v(self, value):
        if value.get('id') is not None: self.id.v = value['id']
        if value.get('alarmList') is not None: self.alarmList.v = value['alarmList']
        if value.get('streamCnt') is not None: self.streamCnt.v = value['streamCnt']
        if value.get('resolutions') is not None: self.resolutions.v = value['resolutions']


class ResolutionsChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'resolutions'
        self.name = '视频流分辨率'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [ResolutionsChannelsPropertyColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ResolutionsChannelsPropertyColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ResolutionsChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.name = NameResolutionsChannelsPropertyColumnComplexStructColumnComplexStruct()
        self.id = IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStruct()
        self.resolution = ResolutionResolutionsChannelsPropertyColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'name': self.name.v, 'id': self.id.v, 'resolution': self.resolution.v}

    @v.setter
    def v(self, value):
        if value.get('name') is not None: self.name.v = value['name']
        if value.get('id') is not None: self.id.v = value['id']
        if value.get('resolution') is not None: self.resolution.v = value['resolution']


class ResolutionResolutionsChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'resolution'
        self.name = '分辨率'
        self.type = 'struct'
        self.struct = ResolutionResolutionsChannelsPropertyColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ResolutionResolutionsChannelsPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.width = WidthResolutionResolutionsChannelsPropertyColumnComplexStructColumnComplexStructStruct()
        self.height = HeightResolutionResolutionsChannelsPropertyColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'width': self.width.v, 'height': self.height.v}

    @v.setter
    def v(self, value):
        if value.get('width') is not None: self.width.v = value['width']
        if value.get('height') is not None: self.height.v = value['height']


class HeightResolutionResolutionsChannelsPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'height'
        self.name = '垂直象素'
        self.type = 'integer'
        self.v: int = 0


class WidthResolutionResolutionsChannelsPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'width'
        self.name = '水平象素'
        self.type = 'integer'
        self.v: int = 0


class IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'id'
        self.name = '视频流id'
        self.type = 'integer'
        self.specs = IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.value2 = Value2IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class Value2IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '子码流'


class Value1IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '主码流'


class NameResolutionsChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'name'
        self.name = '视频流名称'
        self.type = 'string'
        self.specs = NameResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecs()
        self.v: str = ''


class NameResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = NameResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class NameResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.mainStream = MainStreamNameResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.subStream = SubStreamNameResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class SubStreamNameResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'subStream'
        self.desc = '子码流'


class MainStreamNameResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'mainStream'
        self.desc = '主码流'


class StreamCntChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'streamCnt'
        self.name = '每个通道视频流个数'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = StreamCntChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class StreamCntChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 2
        self.step = 1


class AlarmListChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'alarmList'
        self.name = '告警事件'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [AlarmListChannelsPropertyColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = AlarmListChannelsPropertyColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class AlarmListChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.type = TypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStruct()
        self.enable = EnableAlarmListChannelsPropertyColumnComplexStructColumnComplexStruct()
        self.hasPic = HasPicAlarmListChannelsPropertyColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'type': self.type.v, 'enable': self.enable.v, 'hasPic': self.hasPic.v}

    @v.setter
    def v(self, value):
        if value.get('type') is not None: self.type.v = value['type']
        if value.get('enable') is not None: self.enable.v = value['enable']
        if value.get('hasPic') is not None: self.hasPic.v = value['hasPic']


class HasPicAlarmListChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'hasPic'
        self.name = '是否上传图片'
        self.type = 'integer'
        self.specs = HasPicAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class HasPicAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = HasPicAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class HasPicAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1HasPicAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.value0 = Value0HasPicAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class Value0HasPicAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '不上传图片'


class Value1HasPicAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '上传图片'


class EnableAlarmListChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'enable'
        self.name = '是否订阅'
        self.type = 'integer'
        self.specs = EnableAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class EnableAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EnableAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class EnableAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1EnableAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.value0 = Value0EnableAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class Value0EnableAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '告警未订阅'


class Value1EnableAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警已订阅'


class TypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'type'
        self.name = '告警类型'
        self.type = 'string'
        self.specs = TypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecs()
        self.v: str = ''


class TypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class TypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.trafficJam = TrafficJamTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.vehicleInBusRoute = VehicleInBusRouteTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.nonMotorInMotorRoute = NonMotorInMotorRouteTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.trafficAccident = TrafficAccidentTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.trafficJunctionMotor = TrafficJunctionMotorTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.trafficJunctionTruck = TrafficJunctionTruckTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.trafficPedestrain = TrafficPedestrainTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.nonMotorWithoutSafeHat = NonMotorWithoutSafeHatTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.trafficParking = TrafficParkingTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.trafficFlowState = TrafficFlowStateTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class TrafficFlowStateTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficFlowState'
        self.desc = '交通流量事件'


class TrafficParkingTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficParking'
        self.desc = '违章停车'


class NonMotorWithoutSafeHatTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'nonMotorWithoutSafeHat'
        self.desc = '非机动车未戴安全帽事件'


class TrafficPedestrainTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficPedestrain'
        self.desc = '交通行人事件'


class TrafficJunctionTruckTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJunctionTruck'
        self.desc = '交通路口事件----大卡车告警'


class TrafficJunctionMotorTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJunctionMotor'
        self.desc = '交通路口事件----机动车拌线入侵'


class TrafficAccidentTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficAccident'
        self.desc = '交通事故事件'


class NonMotorInMotorRouteTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'nonMotorInMotorRoute'
        self.desc = '非机动车占用机动车道'


class VehicleInBusRouteTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'vehicleInBusRoute'
        self.desc = '占用公交车道事件'


class TrafficJamTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJam'
        self.desc = '交通拥堵事件'


class IdChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'id'
        self.name = '通道id'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = IdChannelsPropertyColumnComplexStructSpecs()
        self.v: int = 0


class IdChannelsPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 1
        self.step = 1


class ChannelCntProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'channelCnt'
        self.name = '通道个数'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = ChannelCntPropertySpecs()
        self.v: int = 0


class ChannelCntPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 1
        self.step = 1


class ModelProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'model'
        self.name = '设备型号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class ManufacturerProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'manufacturer'
        self.name = '设备厂商'
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
        self.desc = '离线'


class Value1OnlinePropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '在线'


class OnvifPasswordProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'onvifPassword'
        self.name = 'Onvif密码'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class OnvifUserProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'onvifUser'
        self.name = 'Onvif账号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class HttpPortProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'httpPort'
        self.name = 'Onvif端口'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.v: int = 0


class IpProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'ip'
        self.name = '设备IP地址'
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
