from .base_model import *


class S5_DH_CP902SU2DQB(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S5_DH_CP902SU2DQB'
        self.productName = '行人闯红灯抓拍单元摄像头'
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
        self.pedestrianJunction = PedestrianJunctionAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.pedestrainRunRedLight = PedestrainRunRedLightAlarmSetDHSDKAlarmServiceParameterSpecsOptional()


class PedestrainRunRedLightAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'pedestrainRunRedLight'
        self.desc = '行人闯红灯事件'


class PedestrianJunctionAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'pedestrianJunction'
        self.desc = '行人卡口事件'


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
        self.pedestrianJunction = PedestrianJunctionEvent()
        self.pedestrainRunRedLight = PedestrainRunRedLightEvent()


class PedestrainRunRedLightEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'pedestrainRunRedLight'
        self.name = '行人闯红灯事件'
        self.parameters = PedestrainRunRedLightEventParameters()


class PedestrainRunRedLightEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypePedestrainRunRedLightEventParameter()
        self.process = ProcessPedestrainRunRedLightEventParameter()
        self.lane = LanePedestrainRunRedLightEventParameter()
        self.imagePath = ImagePathPedestrainRunRedLightEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathPedestrainRunRedLightEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class LanePedestrainRunRedLightEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LanePedestrainRunRedLightEventParameterSpecs()
        self.v: int = 0


class LanePedestrainRunRedLightEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessPedestrainRunRedLightEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessPedestrainRunRedLightEventParameterSpecs()
        self.v: int = 0


class ProcessPedestrainRunRedLightEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessPedestrainRunRedLightEventParameterSpecsOptional()


class ProcessPedestrainRunRedLightEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessPedestrainRunRedLightEventParameterSpecsOptional()


class Value1ProcessPedestrainRunRedLightEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypePedestrainRunRedLightEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypePedestrainRunRedLightEventParameterSpecs()
        self.v: str = ''


class EventTypePedestrainRunRedLightEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypePedestrainRunRedLightEventParameterSpecsOptional()


class EventTypePedestrainRunRedLightEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.pedestrainRunRedLight = PedestrainRunRedLightEventTypePedestrainRunRedLightEventParameterSpecsOptional()


class PedestrainRunRedLightEventTypePedestrainRunRedLightEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'pedestrainRunRedLight'
        self.desc = '行人闯红灯事件'


class PedestrianJunctionEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'pedestrianJunction'
        self.name = '行人卡口事件'
        self.parameters = PedestrianJunctionEventParameters()


class PedestrianJunctionEventParameters:
    def __init__(self) -> None:
        self.eventType = EventTypePedestrianJunctionEventParameter()
        self.process = ProcessPedestrianJunctionEventParameter()
        self.lane = LanePedestrianJunctionEventParameter()
        self.imagePath = ImagePathPedestrianJunctionEventParameter()

    @property
    def v(self):
        return {'eventType': self.eventType.v, 'process': self.process.v, 'lane': self.lane.v, 'imagePath': self.imagePath.v}

    @v.setter
    def v(self, value):
        if value.get('eventType') is not None: self.eventType.v = value['eventType']
        if value.get('process') is not None: self.process.v = value['process']
        if value.get('lane') is not None: self.lane.v = value['lane']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']


class ImagePathPedestrianJunctionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '文件服务器返回的图片信息'
        self.type = 'string'
        self.v: str = ''


class LanePedestrianJunctionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'lane'
        self.name = '车道号'
        self.type = 'integer'
        self.specs = LanePedestrianJunctionEventParameterSpecs()
        self.v: int = 0


class LanePedestrianJunctionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 10
        self.step = 1


class ProcessPedestrianJunctionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'process'
        self.name = '告警开始/结束'
        self.type = 'integer'
        self.specs = ProcessPedestrianJunctionEventParameterSpecs()
        self.v: int = 0


class ProcessPedestrianJunctionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ProcessPedestrianJunctionEventParameterSpecsOptional()


class ProcessPedestrianJunctionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1ProcessPedestrianJunctionEventParameterSpecsOptional()


class Value1ProcessPedestrianJunctionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '告警开始'


class EventTypePedestrianJunctionEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'eventType'
        self.name = '大华摄像机告警类型'
        self.type = 'string'
        self.specs = EventTypePedestrianJunctionEventParameterSpecs()
        self.v: str = ''


class EventTypePedestrianJunctionEventParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = EventTypePedestrianJunctionEventParameterSpecsOptional()


class EventTypePedestrianJunctionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.pedestrianJunction = PedestrianJunctionEventTypePedestrianJunctionEventParameterSpecsOptional()


class PedestrianJunctionEventTypePedestrianJunctionEventParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'pedestrianJunction'
        self.desc = '行人卡口事件'


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
        self.pedestrianJunction = PedestrianJunctionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.pedestrainRunRedLight = PedestrainRunRedLightTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class PedestrainRunRedLightTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'pedestrainRunRedLight'
        self.desc = '行人闯红灯事件'


class PedestrianJunctionTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'pedestrianJunction'
        self.desc = '行人卡口事件'


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
