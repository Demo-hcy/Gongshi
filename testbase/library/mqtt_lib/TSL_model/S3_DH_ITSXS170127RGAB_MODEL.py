from .base_model import *


class S3_DH_ITSXS170127RGAB(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S3_DH_ITSXS170127RGAB'
        self.productName = '大华交通屏'
        self.properties = Properties()
        self.events = None
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.setOnOff = SetOnOffService()
        self.setBrightness = SetBrightnessService()
        self.addProgram = AddProgramService()
        self.delProgram = DelProgramService()
        self.renameProgram = RenameProgramService()
        self.playProgram = PlayProgramService()
        self.delCustomizeProgram = DelCustomizeProgramService()
        self.getProgramList = GetProgramListService()
        self.getCustomizeProgramList = GetCustomizeProgramListService()
        self.addCustomizeProgram = AddCustomizeProgramService()
        self.playCustomizeProgram = PlayCustomizeProgramService()
        self.stopProgram = StopProgramService()
        self.switchMode = SwitchModeService()


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
        self.auto = AutoModeSwitchModeServiceParameterSpecsOptional()
        self.manual = ManualModeSwitchModeServiceParameterSpecsOptional()


class ManualModeSwitchModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'manual'
        self.desc = '手动'


class AutoModeSwitchModeServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'auto'
        self.desc = '自动'


class StopProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'stopProgram'
        self.name = '停止播放'
        self.parameters = None


class PlayCustomizeProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'playCustomizeProgram'
        self.name = '播放自定义节目'
        self.parameters = PlayCustomizeProgramServiceParameters()


class PlayCustomizeProgramServiceParameters:
    def __init__(self) -> None:
        self.devId = DevIdPlayCustomizeProgramServiceParameter()
        self.devChannel = DevChannelPlayCustomizeProgramServiceParameter()
        self.alarmType = AlarmTypePlayCustomizeProgramServiceParameter()
        self.alarmSubType = AlarmSubTypePlayCustomizeProgramServiceParameter()
        self.moduleMd5Sum = ModuleMd5SumPlayCustomizeProgramServiceParameter()

    @property
    def v(self):
        return {'devId': self.devId.v, 'devChannel': self.devChannel.v, 'alarmType': self.alarmType.v, 'alarmSubType': self.alarmSubType.v, 'moduleMd5Sum': self.moduleMd5Sum.v}

    @v.setter
    def v(self, value):
        if value.get('devId') is not None: self.devId.v = value['devId']
        if value.get('devChannel') is not None: self.devChannel.v = value['devChannel']
        if value.get('alarmType') is not None: self.alarmType.v = value['alarmType']
        if value.get('alarmSubType') is not None: self.alarmSubType.v = value['alarmSubType']
        if value.get('moduleMd5Sum') is not None: self.moduleMd5Sum.v = value['moduleMd5Sum']


class ModuleMd5SumPlayCustomizeProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'moduleMd5Sum'
        self.name = '模板文件的md5'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class AlarmSubTypePlayCustomizeProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'alarmSubType'
        self.name = '告警文字的来源告警子类型'
        self.required = True
        self.type = 'integer'
        self.v: int = 0


class AlarmTypePlayCustomizeProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'alarmType'
        self.name = '告警文字的来源告警类型'
        self.required = True
        self.type = 'integer'
        self.v: int = 0


class DevChannelPlayCustomizeProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'devChannel'
        self.name = '告警文字的来源设备通道号'
        self.required = True
        self.type = 'integer'
        self.v: int = 0


class DevIdPlayCustomizeProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'devId'
        self.name = '告警文字的来源设备id'
        self.required = True
        self.type = 'integer'
        self.v: int = 0


class AddCustomizeProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'addCustomizeProgram'
        self.name = '添加自定义节目模板'
        self.parameters = AddCustomizeProgramServiceParameters()


class AddCustomizeProgramServiceParameters:
    def __init__(self) -> None:
        self.fileName = FileNameAddCustomizeProgramServiceParameter()
        self.url = UrlAddCustomizeProgramServiceParameter()
        self.md5Sum = Md5SumAddCustomizeProgramServiceParameter()

    @property
    def v(self):
        return {'fileName': self.fileName.v, 'url': self.url.v, 'md5Sum': self.md5Sum.v}

    @v.setter
    def v(self, value):
        if value.get('fileName') is not None: self.fileName.v = value['fileName']
        if value.get('url') is not None: self.url.v = value['url']
        if value.get('md5Sum') is not None: self.md5Sum.v = value['md5Sum']


class Md5SumAddCustomizeProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'md5Sum'
        self.name = '模板文件的MD5'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class UrlAddCustomizeProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'url'
        self.name = '模板文件的url地址'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class FileNameAddCustomizeProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'fileName'
        self.name = '节目名'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class GetCustomizeProgramListService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'getCustomizeProgramList'
        self.name = '查询自定义模板节目'
        self.parameters = None
        self.output = [GetCustomizeProgramListServiceOutput()]


class GetCustomizeProgramListServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.customizeProgramList = CustomizeProgramListGetCustomizeProgramListServiceOutput()

    @property
    def v(self):
        return {'customizeProgramList': self.customizeProgramList.v}

    @v.setter
    def v(self, value):
        if value.get('customizeProgramList') is not None: self.customizeProgramList.v = value['customizeProgramList']


class CustomizeProgramListGetCustomizeProgramListServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'customizeProgramList'
        self.name = '模板文件名和md5列表'
        self.type = 'array'
        self.columnComplex = [CustomizeProgramListGetCustomizeProgramListServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CustomizeProgramListGetCustomizeProgramListServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CustomizeProgramListGetCustomizeProgramListServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.fileName = FileNameCustomizeProgramListGetCustomizeProgramListServiceOutputColumnComplexStruct()
        self.md5 = Md5CustomizeProgramListGetCustomizeProgramListServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'fileName': self.fileName.v, 'md5': self.md5.v}

    @v.setter
    def v(self, value):
        if value.get('fileName') is not None: self.fileName.v = value['fileName']
        if value.get('md5') is not None: self.md5.v = value['md5']


class Md5CustomizeProgramListGetCustomizeProgramListServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'md5'
        self.name = '节目的md5'
        self.type = 'string'
        self.v: str = ''


class FileNameCustomizeProgramListGetCustomizeProgramListServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'fileName'
        self.name = '节目文件名'
        self.type = 'string'
        self.v: str = ''


class GetProgramListService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'getProgramList'
        self.name = '查询节目列表'
        self.parameters = None
        self.output = [GetProgramListServiceOutput()]


class GetProgramListServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.programList = ProgramListGetProgramListServiceOutput()

    @property
    def v(self):
        return {'programList': self.programList.v}

    @v.setter
    def v(self, value):
        if value.get('programList') is not None: self.programList.v = value['programList']


class ProgramListGetProgramListServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'programList'
        self.name = '节目文件名和md5列表'
        self.type = 'array'
        self.columnComplex = [ProgramListGetProgramListServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ProgramListGetProgramListServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ProgramListGetProgramListServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.fileName = FileNameProgramListGetProgramListServiceOutputColumnComplexStruct()
        self.md5 = Md5ProgramListGetProgramListServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'fileName': self.fileName.v, 'md5': self.md5.v}

    @v.setter
    def v(self, value):
        if value.get('fileName') is not None: self.fileName.v = value['fileName']
        if value.get('md5') is not None: self.md5.v = value['md5']


class Md5ProgramListGetProgramListServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'md5'
        self.name = '节目的md5'
        self.type = 'string'
        self.v: str = ''


class FileNameProgramListGetProgramListServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'fileName'
        self.name = '节目文件名'
        self.type = 'string'
        self.v: str = ''


class DelCustomizeProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'delCustomizeProgram'
        self.name = '删除自定义节目模板'
        self.parameters = DelCustomizeProgramServiceParameters()


class DelCustomizeProgramServiceParameters:
    def __init__(self) -> None:
        self.fileName = FileNameDelCustomizeProgramServiceParameter()

    @property
    def v(self):
        return {'fileName': self.fileName.v}

    @v.setter
    def v(self, value):
        if value.get('fileName') is not None: self.fileName.v = value['fileName']


class FileNameDelCustomizeProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'fileName'
        self.name = '节目名'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class PlayProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'playProgram'
        self.name = '播放节目'
        self.parameters = PlayProgramServiceParameters()


class PlayProgramServiceParameters:
    def __init__(self) -> None:
        self.fileName = FileNamePlayProgramServiceParameter()

    @property
    def v(self):
        return {'fileName': self.fileName.v}

    @v.setter
    def v(self, value):
        if value.get('fileName') is not None: self.fileName.v = value['fileName']


class FileNamePlayProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'fileName'
        self.name = '节目名'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class RenameProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'renameProgram'
        self.name = '更改节目名'
        self.parameters = RenameProgramServiceParameters()


class RenameProgramServiceParameters:
    def __init__(self) -> None:
        self.oldProgramName = OldProgramNameRenameProgramServiceParameter()
        self.newProgramName = NewProgramNameRenameProgramServiceParameter()

    @property
    def v(self):
        return {'oldProgramName': self.oldProgramName.v, 'newProgramName': self.newProgramName.v}

    @v.setter
    def v(self, value):
        if value.get('oldProgramName') is not None: self.oldProgramName.v = value['oldProgramName']
        if value.get('newProgramName') is not None: self.newProgramName.v = value['newProgramName']


class NewProgramNameRenameProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'newProgramName'
        self.name = '改动后节目名字'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class OldProgramNameRenameProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'oldProgramName'
        self.name = '改动前节目名字'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class DelProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'delProgram'
        self.name = '删除节目'
        self.parameters = DelProgramServiceParameters()


class DelProgramServiceParameters:
    def __init__(self) -> None:
        self.fileName = FileNameDelProgramServiceParameter()

    @property
    def v(self):
        return {'fileName': self.fileName.v}

    @v.setter
    def v(self, value):
        if value.get('fileName') is not None: self.fileName.v = value['fileName']


class FileNameDelProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'fileName'
        self.name = '节目名'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class AddProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'addProgram'
        self.name = '添加节目'
        self.parameters = AddProgramServiceParameters()


class AddProgramServiceParameters:
    def __init__(self) -> None:
        self.url = UrlAddProgramServiceParameter()
        self.fileName = FileNameAddProgramServiceParameter()
        self.md5Sum = Md5SumAddProgramServiceParameter()

    @property
    def v(self):
        return {'url': self.url.v, 'fileName': self.fileName.v, 'md5Sum': self.md5Sum.v}

    @v.setter
    def v(self, value):
        if value.get('url') is not None: self.url.v = value['url']
        if value.get('fileName') is not None: self.fileName.v = value['fileName']
        if value.get('md5Sum') is not None: self.md5Sum.v = value['md5Sum']


class Md5SumAddProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'md5Sum'
        self.name = '文件MD5'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class FileNameAddProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'fileName'
        self.name = '节目名'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class UrlAddProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'url'
        self.name = '节目url地址'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class SetBrightnessService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setBrightness'
        self.name = '设置亮度'
        self.parameters = SetBrightnessServiceParameters()


class SetBrightnessServiceParameters:
    def __init__(self) -> None:
        self.brightness = BrightnessSetBrightnessServiceParameter()

    @property
    def v(self):
        return {'brightness': self.brightness.v}

    @v.setter
    def v(self, value):
        if value.get('brightness') is not None: self.brightness.v = value['brightness']


class BrightnessSetBrightnessServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'brightness'
        self.name = '亮度'
        self.required = True
        self.type = 'integer'
        self.specs = BrightnessSetBrightnessServiceParameterSpecs()
        self.v: int = 0


class BrightnessSetBrightnessServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 15
        self.step = 1


class SetOnOffService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setOnOff'
        self.name = '开关屏'
        self.parameters = SetOnOffServiceParameters()


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
        self.value0 = Value0OnOffSetOnOffServiceParameterSpecsOptional()
        self.value1 = Value1OnOffSetOnOffServiceParameterSpecsOptional()


class Value1OnOffSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开屏'


class Value0OnOffSetOnOffServiceParameterSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '关屏'


class Properties:
    def __init__(self) -> None:
        self.sn = SnProperty()
        self.model = ModelProperty()
        self.width = WidthProperty()
        self.height = HeightProperty()
        self.ip = IpProperty()
        self.online = OnlineProperty()
        self.playStatus = PlayStatusProperty()
        self.onOff = OnOffProperty()
        self.playingProgram = PlayingProgramProperty()
        self.brightness = BrightnessProperty()
        self.programList = ProgramListProperty()
        self.mode = ModeProperty()

    @property
    def v(self):
        return {'sn': self.sn.v, 'model': self.model.v, 'width': self.width.v, 'height': self.height.v, 'ip': self.ip.v, 'online': self.online.v, 'playStatus': self.playStatus.v, 'onOff': self.onOff.v, 'playingProgram': self.playingProgram.v, 'brightness': self.brightness.v, 'programList': self.programList.v, 'mode': self.mode.v}

    @v.setter
    def v(self, value):
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('width') is not None: self.width.v = value['width']
        if value.get('height') is not None: self.height.v = value['height']
        if value.get('ip') is not None: self.ip.v = value['ip']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('playStatus') is not None: self.playStatus.v = value['playStatus']
        if value.get('onOff') is not None: self.onOff.v = value['onOff']
        if value.get('playingProgram') is not None: self.playingProgram.v = value['playingProgram']
        if value.get('brightness') is not None: self.brightness.v = value['brightness']
        if value.get('programList') is not None: self.programList.v = value['programList']
        if value.get('mode') is not None: self.mode.v = value['mode']


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


class ProgramListProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'programList'
        self.name = '节目列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [ProgramListPropertyColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ProgramListPropertyColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ProgramListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.fileName = FileNameProgramListPropertyColumnComplexStruct()
        self.md5 = Md5ProgramListPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'fileName': self.fileName.v, 'md5': self.md5.v}

    @v.setter
    def v(self, value):
        if value.get('fileName') is not None: self.fileName.v = value['fileName']
        if value.get('md5') is not None: self.md5.v = value['md5']


class Md5ProgramListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'md5'
        self.name = '节目的md5'
        self.type = 'string'
        self.v: str = ''


class FileNameProgramListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'fileName'
        self.name = '节目文件名'
        self.type = 'string'
        self.v: str = ''


class BrightnessProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'brightness'
        self.name = '亮度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = BrightnessPropertySpecs()
        self.v: int = 0


class BrightnessPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 15
        self.step = 1


class PlayingProgramProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'playingProgram'
        self.name = '正在播放的节目'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class OnOffProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'onOff'
        self.name = '屏幕状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = OnOffPropertySpecs()
        self.v: int = 0


class OnOffPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = OnOffPropertySpecsOptional()


class OnOffPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0OnOffPropertySpecsOptional()
        self.value1 = Value1OnOffPropertySpecsOptional()


class Value1OnOffPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开屏'


class Value0OnOffPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '关屏'


class PlayStatusProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'playStatus'
        self.name = '播放状态'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = PlayStatusPropertySpecs()
        self.v: int = 0


class PlayStatusPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = PlayStatusPropertySpecsOptional()


class PlayStatusPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0PlayStatusPropertySpecsOptional()
        self.value1 = Value1PlayStatusPropertySpecsOptional()


class Value1PlayStatusPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '在播'


class Value0PlayStatusPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '空闲'


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


class IpProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'ip'
        self.name = 'ip地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class HeightProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'height'
        self.name = '长度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = HeightPropertySpecs()
        self.v: int = 0


class HeightPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 64
        self.max = 4096
        self.unit = 'px'
        self.unitName = '像素'
        self.step = 32


class WidthProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'width'
        self.name = '宽度'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = WidthPropertySpecs()
        self.v: int = 0


class WidthPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 64
        self.max = 4096
        self.unit = 'px'
        self.unitName = '像素'
        self.step = 32


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
        self.name = '设备sn号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''
