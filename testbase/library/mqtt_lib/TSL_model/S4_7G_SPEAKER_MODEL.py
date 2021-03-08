from .base_model import *


class S4_QG_SPEAKER(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S4_7G_SPEAKER'
        self.productName = '音柱'
        self.properties = Properties()
        self.events = None
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.setVolume = SetVolumeService()
        self.addProgram = AddProgramService()
        self.renameProgram = RenameProgramService()
        self.delProgram = DelProgramService()
        self.getPrograms = GetProgramsService()
        self.playProgram = PlayProgramService()
        self.pauseProgram = PauseProgramService()
        self.resumeProgram = ResumeProgramService()
        self.stopProgram = StopProgramService()
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


class StopProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'stopProgram'
        self.name = '停止播放'
        self.type = 'business'
        self.parameters = None
        self.output = None


class ResumeProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'resumeProgram'
        self.name = '继续播放'
        self.type = 'business'
        self.parameters = None
        self.output = None


class PauseProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'pauseProgram'
        self.name = '暂停播放'
        self.type = 'business'
        self.parameters = None
        self.output = None


class PlayProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'playProgram'
        self.name = '播放节目'
        self.type = 'business'
        self.parameters = PlayProgramServiceParameters()
        self.output = None


class PlayProgramServiceParameters:
    def __init__(self) -> None:
        self.program = ProgramPlayProgramServiceParameter()

    @property
    def v(self):
        return {'program': self.program.v}

    @v.setter
    def v(self, value):
        if value.get('program') is not None: self.program.v = value['program']


class ProgramPlayProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'program'
        self.name = '节目名字'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = ProgramPlayProgramServiceParameterSpecs()
        self.v: str = ''


class ProgramPlayProgramServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class GetProgramsService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'getPrograms'
        self.name = '查询节目'
        self.type = 'management'
        self.parameters = None
        self.output = [GetProgramsServiceOutput()]


class GetProgramsServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.files = FilesGetProgramsServiceOutput()

    @property
    def v(self):
        return {'files': self.files.v}

    @v.setter
    def v(self, value):
        if value.get('files') is not None: self.files.v = value['files']


class FilesGetProgramsServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'files'
        self.name = '节目列表'
        self.type = 'array'
        self.columnComplex = [FilesGetProgramsServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = FilesGetProgramsServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class FilesGetProgramsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.fileName = FileNameFilesGetProgramsServiceOutputColumnComplexStruct()
        self.md5 = Md5FilesGetProgramsServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'fileName': self.fileName.v, 'md5': self.md5.v}

    @v.setter
    def v(self, value):
        if value.get('fileName') is not None: self.fileName.v = value['fileName']
        if value.get('md5') is not None: self.md5.v = value['md5']


class Md5FilesGetProgramsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'md5'
        self.name = 'md5列表'
        self.type = 'string'
        self.v: str = ''


class FileNameFilesGetProgramsServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'fileName'
        self.name = '节目名列表'
        self.type = 'string'
        self.v: str = ''


class DelProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'delProgram'
        self.name = '删除节目'
        self.type = 'management'
        self.parameters = DelProgramServiceParameters()
        self.output = None


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
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class RenameProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'renameProgram'
        self.name = '更改节目名'
        self.type = 'management'
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


class AddProgramService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'addProgram'
        self.name = '添加节目'
        self.type = 'management'
        self.parameters = AddProgramServiceParameters()
        self.output = None


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
        self.name = 'md5校验值'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class FileNameAddProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'fileName'
        self.name = '节目名'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class UrlAddProgramServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'url'
        self.name = '下载地址'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class SetVolumeService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'setVolume'
        self.name = '设置音量'
        self.type = 'business'
        self.parameters = SetVolumeServiceParameters()
        self.output = None


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
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = VolumeSetVolumeServiceParameterSpecs()
        self.v: int = 0


class VolumeSetVolumeServiceParameterSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class Properties:
    def __init__(self) -> None:
        self.volume = VolumeProperty()
        self.model = ModelProperty()
        self.sn = SnProperty()
        self.playingProgram = PlayingProgramProperty()
        self.online = OnlineProperty()
        self.playStatus = PlayStatusProperty()
        self.mode = ModeProperty()
        self.fileNameList = FileNameListProperty()

    @property
    def v(self):
        return {'volume': self.volume.v, 'model': self.model.v, 'sn': self.sn.v, 'playingProgram': self.playingProgram.v, 'online': self.online.v, 'playStatus': self.playStatus.v, 'mode': self.mode.v, 'fileNameList': self.fileNameList.v}

    @v.setter
    def v(self, value):
        if value.get('volume') is not None: self.volume.v = value['volume']
        if value.get('model') is not None: self.model.v = value['model']
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('playingProgram') is not None: self.playingProgram.v = value['playingProgram']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('playStatus') is not None: self.playStatus.v = value['playStatus']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('fileNameList') is not None: self.fileNameList.v = value['fileNameList']


class FileNameListProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'fileNameList'
        self.name = '节目列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnSimple = [FileNameListPropertyColumnSimpleStruct()]
        self.specs = FileNameListPropertySpecs()

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = FileNameListPropertyColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class FileNameListPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

class FileNameListPropertyColumnSimpleStruct:
    def __init__(self) -> None:
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


class PlayStatusProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'playStatus'
        self.name = '当前播放状态'
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
        self.value2 = Value2PlayStatusPropertySpecsOptional()


class Value2PlayStatusPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '空闲状态'


class Value1PlayStatusPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '播放暂停状态'


class Value0PlayStatusPropertySpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '正在播放'


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


class PlayingProgramProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'playingProgram'
        self.name = '当前播放歌曲'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.specs = PlayingProgramPropertySpecs()
        self.v: str = ''


class PlayingProgramPropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        pass

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

class VolumeProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'volume'
        self.name = '音量'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'integer'
        self.specs = VolumePropertySpecs()
        self.v: int = 0


class VolumePropertySpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100
