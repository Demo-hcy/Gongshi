from .base_model import *


class S5_DH_8A1840WAT8Z4(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S5_DH_8A1840WAT8Z4'
        self.productName = '大华枪球联动摄像头'
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
        self.movePtz = MovePtzService()
        self.setPreset = SetPresetService()
        self.removePreset = RemovePresetService()
        self.clearAllPreset = ClearAllPresetService()
        self.getPresets = GetPresetsService()
        self.gotoPreset = GotoPresetService()
        self.stopPtz = StopPtzService()
        self.setZoom = SetZoomService()
        self.setFocus = SetFocusService()
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
        self.trafficJunctionMotor = TrafficJunctionMotorAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.trafficPedestrain = TrafficPedestrainAlarmSetDHSDKAlarmServiceParameterSpecsOptional()
        self.trafficParking = TrafficParkingAlarmSetDHSDKAlarmServiceParameterSpecsOptional()


class TrafficParkingAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficParking'
        self.desc = '违章停车'


class TrafficPedestrainAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficPedestrain'
        self.desc = '交通行人事件'


class TrafficJunctionMotorAlarmSetDHSDKAlarmServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJunctionMotor'
        self.desc = '交通路口事件----机动车拌线入侵'


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
        self.min = 2
        self.max = 2
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
        self.max = 2
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
        self.max = 2
        self.step = 1


class SetFocusService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setFocus'
        self.name = '设置摄像头焦点'
        self.type = 'business'
        self.parameters = SetFocusServiceParameters()
        self.output = None


class SetFocusServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelSetFocusServiceParameter()
        self.focus = FocusSetFocusServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v, 'focus': self.focus.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('focus') is not None: self.focus.v = value['focus']


class FocusSetFocusServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'focus'
        self.name = '聚焦'
        self.type = 'integer'
        self.required = True
        self.specs = FocusSetFocusServiceParameterSpecs()
        self.v: int = 0


class FocusSetFocusServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = FocusSetFocusServiceParameterSpecsOptional()


class FocusSetFocusServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value1 = Value1FocusSetFocusServiceParameterSpecsOptional()
        self.value0 = Value0FocusSetFocusServiceParameterSpecsOptional()


class Value0FocusSetFocusServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '聚焦-'


class Value1FocusSetFocusServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '聚焦+'


class ChannelSetFocusServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelSetFocusServiceParameterSpecs()
        self.v: int = 0


class ChannelSetFocusServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2
        self.max = 2
        self.step = 1


class SetZoomService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setZoom'
        self.name = '设置焦距'
        self.type = 'business'
        self.parameters = SetZoomServiceParameters()
        self.output = None


class SetZoomServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelSetZoomServiceParameter()
        self.zoomOut = ZoomOutSetZoomServiceParameter()
        self.zoomIn = ZoomInSetZoomServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v, 'zoomOut': self.zoomOut.v, 'zoomIn': self.zoomIn.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('zoomOut') is not None: self.zoomOut.v = value['zoomOut']
        if value.get('zoomIn') is not None: self.zoomIn.v = value['zoomIn']


class ZoomInSetZoomServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'zoomIn'
        self.name = '放大，拉近'
        self.type = 'integer'
        self.required = False
        self.specs = ZoomInSetZoomServiceParameterSpecs()
        self.v: int = 0


class ZoomInSetZoomServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10
        self.step = 1


class ZoomOutSetZoomServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'zoomOut'
        self.name = '缩小，拉远'
        self.type = 'integer'
        self.required = False
        self.specs = ZoomOutSetZoomServiceParameterSpecs()
        self.v: int = 0


class ZoomOutSetZoomServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10
        self.step = 1


class ChannelSetZoomServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelSetZoomServiceParameterSpecs()
        self.v: int = 0


class ChannelSetZoomServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2
        self.max = 2
        self.step = 1


class StopPtzService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'stopPtz'
        self.name = '停止摄像头移动'
        self.type = 'business'
        self.parameters = StopPtzServiceParameters()
        self.output = None


class StopPtzServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelStopPtzServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']


class ChannelStopPtzServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelStopPtzServiceParameterSpecs()
        self.v: int = 0


class ChannelStopPtzServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2
        self.max = 2
        self.step = 1


class GotoPresetService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'gotoPreset'
        self.name = '移动至某个预置位'
        self.type = 'business'
        self.parameters = GotoPresetServiceParameters()
        self.output = None


class GotoPresetServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelGotoPresetServiceParameter()
        self.token = TokenGotoPresetServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v, 'token': self.token.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('token') is not None: self.token.v = value['token']


class TokenGotoPresetServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'token'
        self.name = '预置位token'
        self.type = 'integer'
        self.required = True
        self.specs = TokenGotoPresetServiceParameterSpecs()
        self.v: int = 0


class TokenGotoPresetServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 999
        self.step = 1


class ChannelGotoPresetServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelGotoPresetServiceParameterSpecs()
        self.v: int = 0


class ChannelGotoPresetServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2
        self.max = 2
        self.step = 1


class GetPresetsService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'getPresets'
        self.name = '获取预置位列表'
        self.type = 'management'
        self.parameters = GetPresetsServiceParameters()
        self.output = [GetPresetsServiceOutput()]


class GetPresetsServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.presets = PresetsGetPresetsServiceOutput()

    @property
    def v(self):
        return {'presets': self.presets.v}

    @v.setter
    def v(self, value):
        if value.get('presets') is not None: self.presets.v = value['presets']


class PresetsGetPresetsServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'presets'
        self.name = '预置位列表'
        self.type = 'array'
        self.columnComplex = [PresetsGetPresetsServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = PresetsGetPresetsServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class PresetsGetPresetsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.token = TokenPresetsGetPresetsServiceOutputColumnComplexStruct()
        self.name = NamePresetsGetPresetsServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'token': self.token.v, 'name': self.name.v}

    @v.setter
    def v(self, value):
        if value.get('token') is not None: self.token.v = value['token']
        if value.get('name') is not None: self.name.v = value['name']


class NamePresetsGetPresetsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'name'
        self.name = '预置位名称'
        self.type = 'string'
        self.v: str = ''


class TokenPresetsGetPresetsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'token'
        self.name = '预置位token'
        self.type = 'integer'
        self.specs = TokenPresetsGetPresetsServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class TokenPresetsGetPresetsServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 999
        self.step = 1


class GetPresetsServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelGetPresetsServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']


class ChannelGetPresetsServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelGetPresetsServiceParameterSpecs()
        self.v: int = 0


class ChannelGetPresetsServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2
        self.max = 2
        self.step = 1


class ClearAllPresetService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'clearAllPreset'
        self.name = '删除全部预置位'
        self.type = 'management'
        self.parameters = ClearAllPresetServiceParameters()
        self.output = None


class ClearAllPresetServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelClearAllPresetServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']


class ChannelClearAllPresetServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelClearAllPresetServiceParameterSpecs()
        self.v: int = 0


class ChannelClearAllPresetServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2
        self.max = 2
        self.step = 1


class RemovePresetService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'removePreset'
        self.name = '删除预置位'
        self.type = 'management'
        self.parameters = RemovePresetServiceParameters()
        self.output = None


class RemovePresetServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelRemovePresetServiceParameter()
        self.token = TokenRemovePresetServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v, 'token': self.token.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('token') is not None: self.token.v = value['token']


class TokenRemovePresetServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'token'
        self.name = '预置位token'
        self.type = 'integer'
        self.required = True
        self.specs = TokenRemovePresetServiceParameterSpecs()
        self.v: int = 0


class TokenRemovePresetServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 999
        self.step = 1


class ChannelRemovePresetServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelRemovePresetServiceParameterSpecs()
        self.v: int = 0


class ChannelRemovePresetServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2
        self.max = 2
        self.step = 1


class SetPresetService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setPreset'
        self.name = '设置预置位'
        self.type = 'management'
        self.parameters = SetPresetServiceParameters()
        self.output = [SetPresetServiceOutput()]


class SetPresetServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.token = TokenSetPresetServiceOutput()

    @property
    def v(self):
        return {'token': self.token.v}

    @v.setter
    def v(self, value):
        if value.get('token') is not None: self.token.v = value['token']


class TokenSetPresetServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'token'
        self.name = '新建的预置位token'
        self.type = 'integer'
        self.specs = TokenSetPresetServiceOutputSpecs()
        self.v: int = 0


class TokenSetPresetServiceOutputSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 999
        self.step = 1


class SetPresetServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelSetPresetServiceParameter()
        self.name = NameSetPresetServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v, 'name': self.name.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('name') is not None: self.name.v = value['name']


class NameSetPresetServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'name'
        self.name = '预置位名称'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ChannelSetPresetServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelSetPresetServiceParameterSpecs()
        self.v: int = 0


class ChannelSetPresetServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2
        self.max = 2
        self.step = 1


class MovePtzService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'movePtz'
        self.name = '移动摄像头'
        self.type = 'business'
        self.parameters = MovePtzServiceParameters()
        self.output = None


class MovePtzServiceParameters:
    def __init__(self) -> None:
        self.channel = ChannelMovePtzServiceParameter()
        self.left = LeftMovePtzServiceParameter()
        self.right = RightMovePtzServiceParameter()
        self.up = UpMovePtzServiceParameter()
        self.down = DownMovePtzServiceParameter()

    @property
    def v(self):
        return {'channel': self.channel.v, 'left': self.left.v, 'right': self.right.v, 'up': self.up.v, 'down': self.down.v}

    @v.setter
    def v(self, value):
        if value.get('channel') is not None: self.channel.v = value['channel']
        if value.get('left') is not None: self.left.v = value['left']
        if value.get('right') is not None: self.right.v = value['right']
        if value.get('up') is not None: self.up.v = value['up']
        if value.get('down') is not None: self.down.v = value['down']


class DownMovePtzServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'down'
        self.name = '下移'
        self.type = 'integer'
        self.required = False
        self.specs = DownMovePtzServiceParameterSpecs()
        self.v: int = 0


class DownMovePtzServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10
        self.step = 1


class UpMovePtzServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'up'
        self.name = '上移'
        self.type = 'integer'
        self.required = False
        self.specs = UpMovePtzServiceParameterSpecs()
        self.v: int = 0


class UpMovePtzServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10
        self.step = 1


class RightMovePtzServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'right'
        self.name = '右移'
        self.type = 'integer'
        self.required = False
        self.specs = RightMovePtzServiceParameterSpecs()
        self.v: int = 0


class RightMovePtzServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10
        self.step = 1


class LeftMovePtzServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'left'
        self.name = '左移'
        self.type = 'integer'
        self.required = False
        self.specs = LeftMovePtzServiceParameterSpecs()
        self.v: int = 0


class LeftMovePtzServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 10
        self.step = 1


class ChannelMovePtzServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channel'
        self.name = '通道号'
        self.type = 'integer'
        self.required = True
        self.specs = ChannelMovePtzServiceParameterSpecs()
        self.v: int = 0


class ChannelMovePtzServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 2
        self.max = 2
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
        self.max = 2
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
        self.trafficJunctionMotor = TrafficJunctionMotorEvent()
        self.trafficPedestrain = TrafficPedestrainEvent()
        self.trafficParking = TrafficParkingEvent()


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
        self.presets = PresetsChannelsPropertyColumnComplexStruct()
        self.alarmList = AlarmListChannelsPropertyColumnComplexStruct()
        self.streamCnt = StreamCntChannelsPropertyColumnComplexStruct()
        self.resolutions = ResolutionsChannelsPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'id': self.id.v, 'presets': self.presets.v, 'alarmList': self.alarmList.v, 'streamCnt': self.streamCnt.v, 'resolutions': self.resolutions.v}

    @v.setter
    def v(self, value):
        if value.get('id') is not None: self.id.v = value['id']
        if value.get('presets') is not None: self.presets.v = value['presets']
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
        self.trafficJunctionMotor = TrafficJunctionMotorTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.trafficPedestrain = TrafficPedestrainTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.trafficParking = TrafficParkingTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class TrafficParkingTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficParking'
        self.desc = '违章停车'


class TrafficPedestrainTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficPedestrain'
        self.desc = '交通行人事件'


class TrafficJunctionMotorTypeAlarmListChannelsPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'trafficJunctionMotor'
        self.desc = '交通路口事件----机动车拌线入侵'


class PresetsChannelsPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'presets'
        self.name = '已设置的预置位'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [PresetsChannelsPropertyColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = PresetsChannelsPropertyColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class PresetsChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.token = TokenPresetsChannelsPropertyColumnComplexStructColumnComplexStruct()
        self.name = NamePresetsChannelsPropertyColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'token': self.token.v, 'name': self.name.v}

    @v.setter
    def v(self, value):
        if value.get('token') is not None: self.token.v = value['token']
        if value.get('name') is not None: self.name.v = value['name']


class NamePresetsChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'name'
        self.name = '预置位名称'
        self.type = 'string'
        self.v: str = ''


class TokenPresetsChannelsPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'token'
        self.name = '预置位token'
        self.type = 'integer'
        self.specs = TokenPresetsChannelsPropertyColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class TokenPresetsChannelsPropertyColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 1
        self.max = 999
        self.step = 1


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
        self.max = 2
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
        self.max = 2
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
