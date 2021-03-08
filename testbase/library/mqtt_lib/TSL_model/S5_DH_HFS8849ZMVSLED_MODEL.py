from .base_model import *


class S5_DH_HFS8849ZMVSLED(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S5_DH_HFS8849ZMVSLED'
        self.productName = '大华交通摄像头'
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
        self.crossLineDetection = CrossLineDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.crossRegionDetection = CrossRegionDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.leftDetection = LeftDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.moveDetection = MoveDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.parkingDetection = ParkingDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.rioterDetection = RioterDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.takenawayDetection = TakenawayDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.wanderDetection = WanderDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.humanTrait = HumanTraitAlarmSetDHSDKAlarmServiceParameterSpecsOptional()


class HumanTraitAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'humanTrait'
        self.desc = '人体特征事件'


class WanderDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'wanderDetection'
        self.desc = '徘徊事件'


class TakenawayDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'takenawayDetection'
        self.desc = '物品搬移事件'


class RioterDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'rioterDetection'
        self.desc = '聚众事件'


class ParkingDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'parkingDetection'
        self.desc = '非法停车事件'


class MoveDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'moveDetection'
        self.desc = '移动事件'


class LeftDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'leftDetection'
        self.desc = '物品遗留事件'


class CrossRegionDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'crossRegionDetection'
        self.desc = '警戒区事件'


class CrossLineDetectionAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'crossLineDetection'
        self.desc = '警戒线事件'


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
        self.value3 = Value3StreamGetVideoStreamServiceParameterSpecsOptional()


class Value3StreamGetVideoStreamServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '三码流'


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
        self.value3 = Value3IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class Value3IdChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '三码流'


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
        self.thirdStream = ThirdStreamNameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class ThirdStreamNameChannelResolutionResolutionsRefreshVideoResolutionServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'thirdStream'
        self.desc = '三码流'


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
        self.crossLineDetection = CrossLineDetectionEvent()
        self.crossRegionDetection = CrossRegionDetectionEvent()
        self.leftDetection = LeftDetectionEvent()
        self.moveDetection = MoveDetectionEvent()
        self.parkingDetection = ParkingDetectionEvent()
        self.rioterDetection = RioterDetectionEvent()
        self.takenawayDetection = TakenawayDetectionEvent()
        self.wanderDetection = WanderDetectionEvent()
        self.humanTrait = HumanTraitEvent()


class HumanTraitEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'humanTrait'
        self.name = '人体特征事件'
        self.parameters = HumanTraitEventParameters()


class HumanTraitEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeHumanTraitEventParameter()
        self.process = ProcessHumanTraitEventParameter()
        self.human = HumanHumanTraitEventParameter()
        self.face = FaceHumanTraitEventParameter()
        self.imagePath = ImagePathHumanTraitEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'human': self.human.v, 'face': self.face.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('human') is not None: self.human.v = value['human']
        if value.get('face') is not None: self.face.v = value['face']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathHumanTraitEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class FaceHumanTraitEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'face'
        self.name = '人脸属性'
        self.type = 'struct'
        self.struct = FaceHumanTraitEventParameterStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class FaceHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.sex = SexFaceHumanTraitEventParameterStruct()
        self.age = AgeFaceHumanTraitEventParameterStruct()
        self.complexion = ComplexionFaceHumanTraitEventParameterStruct()
        self.eye = EyeFaceHumanTraitEventParameterStruct()
        self.mouth = MouthFaceHumanTraitEventParameterStruct()
        self.mask = MaskFaceHumanTraitEventParameterStruct()
        self.beard = BeardFaceHumanTraitEventParameterStruct()
        self.attractive = AttractiveFaceHumanTraitEventParameterStruct()

    @property
    def v(self):
        return {'sex': self.sex.v, 'age': self.age.v, 'complexion': self.complexion.v, 'eye': self.eye.v, 'mouth': self.mouth.v, 'mask': self.mask.v, 'beard': self.beard.v, 'attractive': self.attractive.v}

    @v.setter
    def v(self, value):
        if value.get('sex') is not None: self.sex.v = value['sex']
        if value.get('age') is not None: self.age.v = value['age']
        if value.get('complexion') is not None: self.complexion.v = value['complexion']
        if value.get('eye') is not None: self.eye.v = value['eye']
        if value.get('mouth') is not None: self.mouth.v = value['mouth']
        if value.get('mask') is not None: self.mask.v = value['mask']
        if value.get('beard') is not None: self.beard.v = value['beard']
        if value.get('attractive') is not None: self.attractive.v = value['attractive']


class AttractiveFaceHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'attractive'
        self.name = '魅力值'
        self.type = 'integer'
        self.specs = AttractiveFaceHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class AttractiveFaceHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
        self.step = 1


class BeardFaceHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'beard'
        self.name = '胡子状态'
        self.type = 'integer'
        self.specs = BeardFaceHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class BeardFaceHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = BeardFaceHumanTraitEventParameterStructSpecsOptional()


class BeardFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0BeardFaceHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1BeardFaceHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2BeardFaceHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3BeardFaceHumanTraitEventParameterStructSpecsOptional()


class Value3BeardFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '有胡子'


class Value2BeardFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '没胡子'


class Value1BeardFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '未识别'


class Value0BeardFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class MaskFaceHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'mask'
        self.name = '口罩状态'
        self.type = 'integer'
        self.specs = MaskFaceHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class MaskFaceHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = MaskFaceHumanTraitEventParameterStructSpecsOptional()


class MaskFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0MaskFaceHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1MaskFaceHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2MaskFaceHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3MaskFaceHumanTraitEventParameterStructSpecsOptional()


class Value3MaskFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '戴口罩'


class Value2MaskFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '没戴口罩'


class Value1MaskFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '未识别'


class Value0MaskFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class MouthFaceHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'mouth'
        self.name = '嘴巴状态'
        self.type = 'integer'
        self.specs = MouthFaceHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class MouthFaceHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = MouthFaceHumanTraitEventParameterStructSpecsOptional()


class MouthFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0MouthFaceHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1MouthFaceHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2MouthFaceHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3MouthFaceHumanTraitEventParameterStructSpecsOptional()


class Value3MouthFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '张嘴'


class Value2MouthFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '闭嘴'


class Value1MouthFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '未识别'


class Value0MouthFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class EyeFaceHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'eye'
        self.name = '眼睛状态'
        self.type = 'integer'
        self.specs = EyeFaceHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class EyeFaceHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EyeFaceHumanTraitEventParameterStructSpecsOptional()


class EyeFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0EyeFaceHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1EyeFaceHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2EyeFaceHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3EyeFaceHumanTraitEventParameterStructSpecsOptional()


class Value3EyeFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '睁眼'


class Value2EyeFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '闭眼'


class Value1EyeFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '未识别'


class Value0EyeFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class ComplexionFaceHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'complexion'
        self.name = '肤色'
        self.type = 'integer'
        self.specs = ComplexionFaceHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class ComplexionFaceHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ComplexionFaceHumanTraitEventParameterStructSpecsOptional()


class ComplexionFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0ComplexionFaceHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1ComplexionFaceHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2ComplexionFaceHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3ComplexionFaceHumanTraitEventParameterStructSpecsOptional()


class Value3ComplexionFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '白'


class Value2ComplexionFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '黑'


class Value1ComplexionFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '黄'


class Value0ComplexionFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未识别'


class AgeFaceHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'age'
        self.name = '年龄'
        self.type = 'integer'
        self.specs = AgeFaceHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class AgeFaceHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = -1
        self.max = 200
        self.step = 1


class SexFaceHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'sex'
        self.name = '性别'
        self.type = 'integer'
        self.specs = SexFaceHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class SexFaceHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = SexFaceHumanTraitEventParameterStructSpecsOptional()


class SexFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0SexFaceHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1SexFaceHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2SexFaceHumanTraitEventParameterStructSpecsOptional()


class Value2SexFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '女性'


class Value1SexFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '男性'


class Value0SexFaceHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class HumanHumanTraitEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'human'
        self.name = '人体属性'
        self.type = 'struct'
        self.struct = HumanHumanTraitEventParameterStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class HumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.coatColor = CoatColorHumanHumanTraitEventParameterStruct()
        self.coatType = CoatTypeHumanHumanTraitEventParameterStruct()
        self.trousersColor = TrousersColorHumanHumanTraitEventParameterStruct()
        self.trousersType = TrousersTypeHumanHumanTraitEventParameterStruct()
        self.hasHat = HasHatHumanHumanTraitEventParameterStruct()
        self.hasBag = HasBagHumanHumanTraitEventParameterStruct()
        self.age = AgeHumanHumanTraitEventParameterStruct()
        self.sex = SexHumanHumanTraitEventParameterStruct()
        self.hasUmbrella = HasUmbrellaHumanHumanTraitEventParameterStruct()
        self.bag = BagHumanHumanTraitEventParameterStruct()
        self.upperPattern = UpperPatternHumanHumanTraitEventParameterStruct()
        self.hairStyle = HairStyleHumanHumanTraitEventParameterStruct()
        self.cap = CapHumanHumanTraitEventParameterStruct()

    @property
    def v(self):
        return {'coatColor': self.coatColor.v, 'coatType': self.coatType.v, 'trousersColor': self.trousersColor.v, 'trousersType': self.trousersType.v, 'hasHat': self.hasHat.v, 'hasBag': self.hasBag.v, 'age': self.age.v, 'sex': self.sex.v, 'hasUmbrella': self.hasUmbrella.v, 'bag': self.bag.v, 'upperPattern': self.upperPattern.v, 'hairStyle': self.hairStyle.v, 'cap': self.cap.v}

    @v.setter
    def v(self, value):
        if value.get('coatColor') is not None: self.coatColor.v = value['coatColor']
        if value.get('coatType') is not None: self.coatType.v = value['coatType']
        if value.get('trousersColor') is not None: self.trousersColor.v = value['trousersColor']
        if value.get('trousersType') is not None: self.trousersType.v = value['trousersType']
        if value.get('hasHat') is not None: self.hasHat.v = value['hasHat']
        if value.get('hasBag') is not None: self.hasBag.v = value['hasBag']
        if value.get('age') is not None: self.age.v = value['age']
        if value.get('sex') is not None: self.sex.v = value['sex']
        if value.get('hasUmbrella') is not None: self.hasUmbrella.v = value['hasUmbrella']
        if value.get('bag') is not None: self.bag.v = value['bag']
        if value.get('upperPattern') is not None: self.upperPattern.v = value['upperPattern']
        if value.get('hairStyle') is not None: self.hairStyle.v = value['hairStyle']
        if value.get('cap') is not None: self.cap.v = value['cap']


class CapHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'cap'
        self.name = '帽类型'
        self.type = 'integer'
        self.specs = CapHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class CapHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = CapHumanHumanTraitEventParameterStructSpecsOptional()


class CapHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0CapHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1CapHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2CapHumanHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3CapHumanHumanTraitEventParameterStructSpecsOptional()


class Value3CapHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '安全帽'


class Value2CapHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '头盔'


class Value1CapHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '普通帽子'


class Value0CapHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class HairStyleHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'hairStyle'
        self.name = '头发样式'
        self.type = 'integer'
        self.specs = HairStyleHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class HairStyleHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = HairStyleHumanHumanTraitEventParameterStructSpecsOptional()


class HairStyleHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0HairStyleHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1HairStyleHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2HairStyleHumanHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3HairStyleHumanHumanTraitEventParameterStructSpecsOptional()
        self.value4 = Value4HairStyleHumanHumanTraitEventParameterStructSpecsOptional()
        self.value5 = Value5HairStyleHumanHumanTraitEventParameterStructSpecsOptional()
        self.value6 = Value6HairStyleHumanHumanTraitEventParameterStructSpecsOptional()


class Value6HairStyleHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '无头发'


class Value5HairStyleHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '头部被遮挡'


class Value4HairStyleHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 4
        self.desc = '盘发'


class Value3HairStyleHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '马尾'


class Value2HairStyleHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '短发'


class Value1HairStyleHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '长发'


class Value0HairStyleHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class UpperPatternHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'upperPattern'
        self.name = '上半身衣服图案'
        self.type = 'integer'
        self.specs = UpperPatternHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class UpperPatternHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = UpperPatternHumanHumanTraitEventParameterStructSpecsOptional()


class UpperPatternHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0UpperPatternHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1UpperPatternHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2UpperPatternHumanHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3UpperPatternHumanHumanTraitEventParameterStructSpecsOptional()
        self.value4 = Value4UpperPatternHumanHumanTraitEventParameterStructSpecsOptional()
        self.value5 = Value5UpperPatternHumanHumanTraitEventParameterStructSpecsOptional()
        self.value6 = Value6UpperPatternHumanHumanTraitEventParameterStructSpecsOptional()


class Value6UpperPatternHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '拼接'


class Value5UpperPatternHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '格子'


class Value4UpperPatternHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 4
        self.desc = '缝隙'


class Value3UpperPatternHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '图案'


class Value2UpperPatternHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '条纹'


class Value1UpperPatternHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '纯色'


class Value0UpperPatternHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class BagHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'bag'
        self.name = '包类型'
        self.type = 'integer'
        self.specs = BagHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class BagHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = BagHumanHumanTraitEventParameterStructSpecsOptional()


class BagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0BagHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1BagHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2BagHumanHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3BagHumanHumanTraitEventParameterStructSpecsOptional()
        self.value4 = Value4BagHumanHumanTraitEventParameterStructSpecsOptional()
        self.value5 = Value5BagHumanHumanTraitEventParameterStructSpecsOptional()
        self.value6 = Value6BagHumanHumanTraitEventParameterStructSpecsOptional()


class Value6BagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '无包'


class Value5BagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '腰包'


class Value4BagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 4
        self.desc = '拉杆箱'


class Value3BagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '背包'


class Value2BagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '肩包'


class Value1BagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '手提包'


class Value0BagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class HasUmbrellaHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'hasUmbrella'
        self.name = '是否打伞'
        self.type = 'integer'
        self.specs = HasUmbrellaHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class HasUmbrellaHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = HasUmbrellaHumanHumanTraitEventParameterStructSpecsOptional()


class HasUmbrellaHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0HasUmbrellaHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1HasUmbrellaHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2HasUmbrellaHumanHumanTraitEventParameterStructSpecsOptional()


class Value2HasUmbrellaHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '打伞'


class Value1HasUmbrellaHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '未打伞'


class Value0HasUmbrellaHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class SexHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'sex'
        self.name = '性别'
        self.type = 'integer'
        self.specs = SexHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class SexHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = SexHumanHumanTraitEventParameterStructSpecsOptional()


class SexHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0SexHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1SexHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2SexHumanHumanTraitEventParameterStructSpecsOptional()


class Value2SexHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '女性'


class Value1SexHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '男性'


class Value0SexHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class AgeHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'age'
        self.name = '年龄'
        self.type = 'integer'
        self.specs = AgeHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class AgeHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 200
        self.step = 1


class HasBagHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'hasBag'
        self.name = '是否带包'
        self.type = 'integer'
        self.specs = HasBagHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class HasBagHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = HasBagHumanHumanTraitEventParameterStructSpecsOptional()


class HasBagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0HasBagHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1HasBagHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2HasBagHumanHumanTraitEventParameterStructSpecsOptional()


class Value2HasBagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '带包'


class Value1HasBagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '不带包'


class Value0HasBagHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class HasHatHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'hasHat'
        self.name = '是否戴帽子'
        self.type = 'integer'
        self.specs = HasHatHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class HasHatHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = HasHatHumanHumanTraitEventParameterStructSpecsOptional()


class HasHatHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0HasHatHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1HasHatHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2HasHatHumanHumanTraitEventParameterStructSpecsOptional()


class Value2HasHatHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '戴帽子'


class Value1HasHatHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '不戴帽子'


class Value0HasHatHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class TrousersTypeHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'trousersType'
        self.name = '裤子类型'
        self.type = 'integer'
        self.specs = TrousersTypeHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class TrousersTypeHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TrousersTypeHumanHumanTraitEventParameterStructSpecsOptional()


class TrousersTypeHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0TrousersTypeHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1TrousersTypeHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2TrousersTypeHumanHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3TrousersTypeHumanHumanTraitEventParameterStructSpecsOptional()


class Value3TrousersTypeHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '裙子'


class Value2TrousersTypeHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '短裤'


class Value1TrousersTypeHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '长裤'


class Value0TrousersTypeHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class TrousersColorHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'trousersColor'
        self.name = '裤子颜色'
        self.type = 'integer'
        self.specs = TrousersColorHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class TrousersColorHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()


class TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value4 = Value4TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value5 = Value5TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value6 = Value6TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value7 = Value7TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value8 = Value8TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value9 = Value9TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value10 = Value10TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value11 = Value11TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value12 = Value12TrousersColorHumanHumanTraitEventParameterStructSpecsOptional()


class Value12TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 12
        self.desc = '其他颜色'


class Value11TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 11
        self.desc = '棕色'


class Value10TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 10
        self.desc = '紫色'


class Value9TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 9
        self.desc = '绿色'


class Value8TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 8
        self.desc = '蓝色'


class Value7TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 7
        self.desc = '灰色'


class Value6TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '黄色'


class Value5TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '红色'


class Value4TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 4
        self.desc = '黑色'


class Value3TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '粉色'


class Value2TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '橙色'


class Value1TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '白色'


class Value0TrousersColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class CoatTypeHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'coatType'
        self.name = '上衣类型'
        self.type = 'integer'
        self.specs = CoatTypeHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class CoatTypeHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = CoatTypeHumanHumanTraitEventParameterStructSpecsOptional()


class CoatTypeHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0CoatTypeHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1CoatTypeHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2CoatTypeHumanHumanTraitEventParameterStructSpecsOptional()


class Value2CoatTypeHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '短袖'


class Value1CoatTypeHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '长袖'


class Value0CoatTypeHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class CoatColorHumanHumanTraitEventParameterStruct:
    def __init__(self) -> None:
        self.id = 'coatColor'
        self.name = '上衣颜色'
        self.type = 'integer'
        self.specs = CoatColorHumanHumanTraitEventParameterStructSpecs()
        self.v: int = 0


class CoatColorHumanHumanTraitEventParameterStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = CoatColorHumanHumanTraitEventParameterStructSpecsOptional()


class CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value1 = Value1CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value2 = Value2CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value3 = Value3CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value4 = Value4CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value5 = Value5CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value6 = Value6CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value7 = Value7CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value8 = Value8CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value9 = Value9CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value10 = Value10CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value11 = Value11CoatColorHumanHumanTraitEventParameterStructSpecsOptional()
        self.value12 = Value12CoatColorHumanHumanTraitEventParameterStructSpecsOptional()


class Value12CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 12
        self.desc = '其他颜色'


class Value11CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 11
        self.desc = '棕色'


class Value10CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 10
        self.desc = '紫色'


class Value9CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 9
        self.desc = '绿色'


class Value8CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 8
        self.desc = '蓝色'


class Value7CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 7
        self.desc = '灰色'


class Value6CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 6
        self.desc = '黄色'


class Value5CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 5
        self.desc = '红色'


class Value4CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 4
        self.desc = '黑色'


class Value3CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '粉色'


class Value2CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '橙色'


class Value1CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '白色'


class Value0CoatColorHumanHumanTraitEventParameterStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未知'


class ProcessHumanTraitEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessHumanTraitEventParameterSpecs()
        self.v: int = 0


class ProcessHumanTraitEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessHumanTraitEventParameterSpecsOptional()


class ProcessHumanTraitEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessHumanTraitEventParameterSpecsOptional()


class Value1ProcessHumanTraitEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeHumanTraitEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeHumanTraitEventParameterSpecs()
        self.v: str = ''


class EventTypeHumanTraitEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeHumanTraitEventParameterSpecsOptional()


class EventTypeHumanTraitEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.humanTrait = HumanTraitEventTypeHumanTraitEventParameterSpecsOptional()


class HumanTraitEventTypeHumanTraitEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'humanTrait'
        self.desc = '人体特征事件'


class WanderDetectionEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'wanderDetection'
        self.name = '徘徊事件'
        self.parameters = WanderDetectionEventParameters()


class WanderDetectionEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeWanderDetectionEventParameter()
        self.process = ProcessWanderDetectionEventParameter()
        self.imagePath = ImagePathWanderDetectionEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathWanderDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class ProcessWanderDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessWanderDetectionEventParameterSpecs()
        self.v: int = 0


class ProcessWanderDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessWanderDetectionEventParameterSpecsOptional()


class ProcessWanderDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessWanderDetectionEventParameterSpecsOptional()


class Value1ProcessWanderDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeWanderDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeWanderDetectionEventParameterSpecs()
        self.v: str = ''


class EventTypeWanderDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeWanderDetectionEventParameterSpecsOptional()


class EventTypeWanderDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.wanderDetection = WanderDetectionEventTypeWanderDetectionEventParameterSpecsOptional()


class WanderDetectionEventTypeWanderDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'wanderDetection'
        self.desc = '徘徊事件'


class TakenawayDetectionEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'takenawayDetection'
        self.name = '物品搬移事件'
        self.parameters = TakenawayDetectionEventParameters()


class TakenawayDetectionEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeTakenawayDetectionEventParameter()
        self.process = ProcessTakenawayDetectionEventParameter()
        self.objectType = ObjectTypeTakenawayDetectionEventParameter()
        self.imagePath = ImagePathTakenawayDetectionEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'objectType': self.objectType.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('objectType') is not None: self.objectType.v = value['objectType']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathTakenawayDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class ObjectTypeTakenawayDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'objectType'
        self.name = '物体类型'
        self.type = 'string'
        self.v: str = ''


class ProcessTakenawayDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessTakenawayDetectionEventParameterSpecs()
        self.v: int = 0


class ProcessTakenawayDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessTakenawayDetectionEventParameterSpecsOptional()


class ProcessTakenawayDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessTakenawayDetectionEventParameterSpecsOptional()


class Value1ProcessTakenawayDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeTakenawayDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeTakenawayDetectionEventParameterSpecs()
        self.v: str = ''


class EventTypeTakenawayDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeTakenawayDetectionEventParameterSpecsOptional()


class EventTypeTakenawayDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.takenawayDetection = TakenawayDetectionEventTypeTakenawayDetectionEventParameterSpecsOptional()


class TakenawayDetectionEventTypeTakenawayDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'takenawayDetection'
        self.desc = '物品搬移事件'


class RioterDetectionEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'rioterDetection'
        self.name = '聚众事件'
        self.parameters = RioterDetectionEventParameters()


class RioterDetectionEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeRioterDetectionEventParameter()
        self.process = ProcessRioterDetectionEventParameter()
        self.imagePath = ImagePathRioterDetectionEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathRioterDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class ProcessRioterDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessRioterDetectionEventParameterSpecs()
        self.v: int = 0


class ProcessRioterDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessRioterDetectionEventParameterSpecsOptional()


class ProcessRioterDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessRioterDetectionEventParameterSpecsOptional()


class Value1ProcessRioterDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeRioterDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeRioterDetectionEventParameterSpecs()
        self.v: str = ''


class EventTypeRioterDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeRioterDetectionEventParameterSpecsOptional()


class EventTypeRioterDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.rioterDetection = RioterDetectionEventTypeRioterDetectionEventParameterSpecsOptional()


class RioterDetectionEventTypeRioterDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'rioterDetection'
        self.desc = '聚众事件'


class ParkingDetectionEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'parkingDetection'
        self.name = '非法停车事件'
        self.parameters = ParkingDetectionEventParameters()


class ParkingDetectionEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeParkingDetectionEventParameter()
        self.process = ProcessParkingDetectionEventParameter()
        self.objectType = ObjectTypeParkingDetectionEventParameter()
        self.imagePath = ImagePathParkingDetectionEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'objectType': self.objectType.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('objectType') is not None: self.objectType.v = value['objectType']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathParkingDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class ObjectTypeParkingDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'objectType'
        self.name = '物体类型'
        self.type = 'string'
        self.v: str = ''


class ProcessParkingDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessParkingDetectionEventParameterSpecs()
        self.v: int = 0


class ProcessParkingDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessParkingDetectionEventParameterSpecsOptional()


class ProcessParkingDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessParkingDetectionEventParameterSpecsOptional()


class Value1ProcessParkingDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeParkingDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeParkingDetectionEventParameterSpecs()
        self.v: str = ''


class EventTypeParkingDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeParkingDetectionEventParameterSpecsOptional()


class EventTypeParkingDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.parkingDetection = ParkingDetectionEventTypeParkingDetectionEventParameterSpecsOptional()


class ParkingDetectionEventTypeParkingDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'parkingDetection'
        self.desc = '非法停车事件'


class MoveDetectionEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'moveDetection'
        self.name = '移动事件'
        self.parameters = MoveDetectionEventParameters()


class MoveDetectionEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeMoveDetectionEventParameter()
        self.process = ProcessMoveDetectionEventParameter()
        self.objectType = ObjectTypeMoveDetectionEventParameter()
        self.imagePath = ImagePathMoveDetectionEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'objectType': self.objectType.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('objectType') is not None: self.objectType.v = value['objectType']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathMoveDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class ObjectTypeMoveDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'objectType'
        self.name = '物体类型'
        self.type = 'string'
        self.v: str = ''


class ProcessMoveDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessMoveDetectionEventParameterSpecs()
        self.v: int = 0


class ProcessMoveDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessMoveDetectionEventParameterSpecsOptional()


class ProcessMoveDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessMoveDetectionEventParameterSpecsOptional()


class Value1ProcessMoveDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeMoveDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeMoveDetectionEventParameterSpecs()
        self.v: str = ''


class EventTypeMoveDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeMoveDetectionEventParameterSpecsOptional()


class EventTypeMoveDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.moveDetection = MoveDetectionEventTypeMoveDetectionEventParameterSpecsOptional()


class MoveDetectionEventTypeMoveDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'moveDetection'
        self.desc = '移动事件'


class LeftDetectionEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'leftDetection'
        self.name = '物品遗留事件'
        self.parameters = LeftDetectionEventParameters()


class LeftDetectionEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeLeftDetectionEventParameter()
        self.process = ProcessLeftDetectionEventParameter()
        self.objectType = ObjectTypeLeftDetectionEventParameter()
        self.imagePath = ImagePathLeftDetectionEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'objectType': self.objectType.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('objectType') is not None: self.objectType.v = value['objectType']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathLeftDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class ObjectTypeLeftDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'objectType'
        self.name = '物体类型'
        self.type = 'string'
        self.v: str = ''


class ProcessLeftDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessLeftDetectionEventParameterSpecs()
        self.v: int = 0


class ProcessLeftDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessLeftDetectionEventParameterSpecsOptional()


class ProcessLeftDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessLeftDetectionEventParameterSpecsOptional()


class Value1ProcessLeftDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeLeftDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeLeftDetectionEventParameterSpecs()
        self.v: str = ''


class EventTypeLeftDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeLeftDetectionEventParameterSpecsOptional()


class EventTypeLeftDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.leftDetection = LeftDetectionEventTypeLeftDetectionEventParameterSpecsOptional()


class LeftDetectionEventTypeLeftDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'leftDetection'
        self.desc = '物品遗留事件'


class CrossRegionDetectionEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'crossRegionDetection'
        self.name = '警戒区事件'
        self.parameters = CrossRegionDetectionEventParameters()


class CrossRegionDetectionEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeCrossRegionDetectionEventParameter()
        self.process = ProcessCrossRegionDetectionEventParameter()
        self.direction = DirectionCrossRegionDetectionEventParameter()
        self.actionType = ActionTypeCrossRegionDetectionEventParameter()
        self.objectType = ObjectTypeCrossRegionDetectionEventParameter()
        self.imagePath = ImagePathCrossRegionDetectionEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'direction': self.direction.v, 'actionType': self.actionType.v, 'objectType': self.objectType.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('direction') is not None: self.direction.v = value['direction']
        if value.get('actionType') is not None: self.actionType.v = value['actionType']
        if value.get('objectType') is not None: self.objectType.v = value['objectType']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathCrossRegionDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class ObjectTypeCrossRegionDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'objectType'
        self.name = '物体类型'
        self.type = 'string'
        self.v: str = ''


class ActionTypeCrossRegionDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'actionType'
        self.name = '动作类型'
        self.type = 'string'
        self.specs = ActionTypeCrossRegionDetectionEventParameterSpecs()
        self.v: str = ''


class ActionTypeCrossRegionDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ActionTypeCrossRegionDetectionEventParameterSpecsOptional()


class ActionTypeCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.appear = AppearActionTypeCrossRegionDetectionEventParameterSpecsOptional()
        self.disappear = DisappearActionTypeCrossRegionDetectionEventParameterSpecsOptional()
        self.inRegion = InRegionActionTypeCrossRegionDetectionEventParameterSpecsOptional()
        self.crossRegion = CrossRegionActionTypeCrossRegionDetectionEventParameterSpecsOptional()


class CrossRegionActionTypeCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'crossRegion'
        self.desc = '穿越区域'


class InRegionActionTypeCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'inRegion'
        self.desc = '在区域内'


class DisappearActionTypeCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'disappear'
        self.desc = '消失'


class AppearActionTypeCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'appear'
        self.desc = '出现'


class DirectionCrossRegionDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'direction'
        self.name = '入侵方向'
        self.type = 'string'
        self.specs = DirectionCrossRegionDetectionEventParameterSpecs()
        self.v: str = ''


class DirectionCrossRegionDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = DirectionCrossRegionDetectionEventParameterSpecsOptional()


class DirectionCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.in_ = InDirectionCrossRegionDetectionEventParameterSpecsOptional()
        self.out = OutDirectionCrossRegionDetectionEventParameterSpecsOptional()
        self.appear = AppearDirectionCrossRegionDetectionEventParameterSpecsOptional()
        self.disappear = DisappearDirectionCrossRegionDetectionEventParameterSpecsOptional()


class DisappearDirectionCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'disappear'
        self.desc = '消失'


class AppearDirectionCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'appear'
        self.desc = '出现'


class OutDirectionCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'out'
        self.desc = '离开'


class InDirectionCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'in'
        self.desc = '进入'


class ProcessCrossRegionDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessCrossRegionDetectionEventParameterSpecs()
        self.v: int = 0


class ProcessCrossRegionDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessCrossRegionDetectionEventParameterSpecsOptional()


class ProcessCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessCrossRegionDetectionEventParameterSpecsOptional()


class Value1ProcessCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeCrossRegionDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeCrossRegionDetectionEventParameterSpecs()
        self.v: str = ''


class EventTypeCrossRegionDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeCrossRegionDetectionEventParameterSpecsOptional()


class EventTypeCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.crossRegionDetection = CrossRegionDetectionEventTypeCrossRegionDetectionEventParameterSpecsOptional()


class CrossRegionDetectionEventTypeCrossRegionDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'crossRegionDetection'
        self.desc = '警戒区事件'


class CrossLineDetectionEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'crossLineDetection'
        self.name = '警戒线事件'
        self.parameters = CrossLineDetectionEventParameters()


class CrossLineDetectionEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypeCrossLineDetectionEventParameter()
        self.process = ProcessCrossLineDetectionEventParameter()
        self.direction = DirectionCrossLineDetectionEventParameter()
        self.objectType = ObjectTypeCrossLineDetectionEventParameter()
        self.imagePath = ImagePathCrossLineDetectionEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'direction': self.direction.v, 'objectType': self.objectType.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('direction') is not None: self.direction.v = value['direction']
        if value.get('objectType') is not None: self.objectType.v = value['objectType']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathCrossLineDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class ObjectTypeCrossLineDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'objectType'
        self.name = '物体类型'
        self.type = 'string'
        self.v: str = ''


class DirectionCrossLineDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'direction'
        self.name = '越线方向'
        self.type = 'string'
        self.specs = DirectionCrossLineDetectionEventParameterSpecs()
        self.v: str = ''


class DirectionCrossLineDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = DirectionCrossLineDetectionEventParameterSpecsOptional()


class DirectionCrossLineDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.leftToRight = LeftToRightDirectionCrossLineDetectionEventParameterSpecsOptional()
        self.rightToLeft = RightToLeftDirectionCrossLineDetectionEventParameterSpecsOptional()


class RightToLeftDirectionCrossLineDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'rightToLeft'
        self.desc = '从右到左'


class LeftToRightDirectionCrossLineDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'leftToRight'
        self.desc = '从左到右'


class ProcessCrossLineDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessCrossLineDetectionEventParameterSpecs()
        self.v: int = 0


class ProcessCrossLineDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessCrossLineDetectionEventParameterSpecsOptional()


class ProcessCrossLineDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessCrossLineDetectionEventParameterSpecsOptional()


class Value1ProcessCrossLineDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypeCrossLineDetectionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypeCrossLineDetectionEventParameterSpecs()
        self.v: str = ''


class EventTypeCrossLineDetectionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypeCrossLineDetectionEventParameterSpecsOptional()


class EventTypeCrossLineDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.crossLineDetection = CrossLineDetectionEventTypeCrossLineDetectionEventParameterSpecsOptional()


class CrossLineDetectionEventTypeCrossLineDetectionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'crossLineDetection'
        self.desc = '警戒线事件'


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
        self.value3 = Value3IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class Value3IdResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 3
        self.desc = '三码流'


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
        self.thirdStream = ThirdStreamNameResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class ThirdStreamNameResolutionsChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'thirdStream'
        self.desc = '三码流'


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
        self.max = 3
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
        self.crossLineDetection = CrossLineDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.crossRegionDetection = CrossRegionDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.leftDetection = LeftDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.moveDetection = MoveDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.parkingDetection = ParkingDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.rioterDetection = RioterDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.takenawayDetection = TakenawayDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.wanderDetection = WanderDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.humanTrait = HumanTraitTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class HumanTraitTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'humanTrait'
        self.desc = '人体特征事件'


class WanderDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'wanderDetection'
        self.desc = '徘徊事件'


class TakenawayDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'takenawayDetection'
        self.desc = '物品搬移事件'


class RioterDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'rioterDetection'
        self.desc = '聚众事件'


class ParkingDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'parkingDetection'
        self.desc = '非法停车事件'


class MoveDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'moveDetection'
        self.desc = '移动事件'


class LeftDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'leftDetection'
        self.desc = '物品遗留事件'


class CrossRegionDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'crossRegionDetection'
        self.desc = '警戒区事件'


class CrossLineDetectionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'crossLineDetection'
        self.desc = '警戒线事件'


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
