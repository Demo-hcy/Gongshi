from .base_model import *


class AIHub001(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'AIHub001'
        self.productName = 'AI微服务'
        self.properties = Properties()
        self.events = Events()
        self.services = Services()


class Services:
    def __init__(self) -> None:
        self.reboot = RebootService()
        self.addModel = AddModelService()
        self.deleteModel = DeleteModelService()
        self.updateModel = UpdateModelService()
        self.queryModelById = QueryModelByIdService()
        self.queryModel = QueryModelService()
        self.addCamera = AddCameraService()
        self.deleteCamera = DeleteCameraService()
        self.modifyCamera = ModifyCameraService()
        self.queryCameraById = QueryCameraByIdService()
        self.queryCamera = QueryCameraService()
        self.openCameraAI = OpenCameraAIService()
        self.closeCameraAI = CloseCameraAIService()
        self.closeCameraAISub = CloseCameraAISubService()
        self.deleteCameraAI = DeleteCameraAIService()
        self.deleteCameraAISub = DeleteCameraAISubService()
        self.queryCameraAIByCameraId = QueryCameraAIByCameraIdService()
        self.queryCamerAIByCameraIdAndModelId = QueryCamerAIByCameraIdAndModelIdService()
        self.queryCameraAI = QueryCameraAIService()


class QueryCameraAIService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryCameraAI'
        self.name = '通道信息查询'
        self.type = 'management'
        self.parameters = None
        self.output = [QueryCameraAIServiceOutput()]


class QueryCameraAIServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraAIList = CameraAIListQueryCameraAIServiceOutput()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListQueryCameraAIServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraAIList'
        self.name = '通道信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListQueryCameraAIServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListQueryCameraAIServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListQueryCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.channelId = ChannelIdCameraAIListQueryCameraAIServiceOutputColumnComplexStruct()
        self.cameraId = CameraIdCameraAIListQueryCameraAIServiceOutputColumnComplexStruct()
        self.cameraUrl = CameraUrlCameraAIListQueryCameraAIServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'channelId': self.channelId.v, 'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('channelId') is not None: self.channelId.v = value['channelId']
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '子通道信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct()
        self.detectionAreaIdList = DetectionAreaIdListModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct()
        self.function = FunctionModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct()
        self.status = StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionAreaIdList': self.detectionAreaIdList.v, 'function': self.function.v, 'status': self.status.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionAreaIdList') is not None: self.detectionAreaIdList.v = value['detectionAreaIdList']
        if value.get('function') is not None: self.function.v = value['function']
        if value.get('status') is not None: self.status.v = value['status']


class StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'status'
        self.name = '运行状态'
        self.type = 'integer'
        self.specs = StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()
        self.value1 = Value1StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()
        self.value2 = Value2StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class Value2StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '开启异常'


class Value1StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开启'


class Value0StatusModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未开启'


class FunctionModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'function'
        self.name = '子通道功能'
        self.type = 'string'
        self.v: str = ''


class DetectionAreaIdListModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaIdList'
        self.name = '检测区域ID列表'
        self.type = 'array'
        self.columnSimple = [DetectionAreaIdListModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = DetectionAreaIdListModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class DetectionAreaIdListModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraAIListQueryCameraAIServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class CameraUrlCameraAIListQueryCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流url'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListQueryCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '检测摄像头ID'
        self.type = 'string'
        self.v: str = ''


class ChannelIdCameraAIListQueryCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelId'
        self.name = '通道编号'
        self.type = 'string'
        self.v: str = ''


class QueryCamerAIByCameraIdAndModelIdService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryCamerAIByCameraIdAndModelId'
        self.name = '根据通道ID子通道ID查询子检测通道'
        self.type = 'management'
        self.parameters = QueryCamerAIByCameraIdAndModelIdServiceParameters()
        self.output = [QueryCamerAIByCameraIdAndModelIdServiceOutput()]


class QueryCamerAIByCameraIdAndModelIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraAIList = CameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutput()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraAIList'
        self.name = '通道信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.channelId = ChannelIdCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct()
        self.cameraId = CameraIdCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct()
        self.cameraUrl = CameraUrlCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'channelId': self.channelId.v, 'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('channelId') is not None: self.channelId.v = value['channelId']
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '子通道信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.detectionAreaIdList = DetectionAreaIdListModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.function = FunctionModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.status = StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionAreaIdList': self.detectionAreaIdList.v, 'function': self.function.v, 'status': self.status.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionAreaIdList') is not None: self.detectionAreaIdList.v = value['detectionAreaIdList']
        if value.get('function') is not None: self.function.v = value['function']
        if value.get('status') is not None: self.status.v = value['status']


class StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'status'
        self.name = '运行状态'
        self.type = 'integer'
        self.specs = StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()
        self.value1 = Value1StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()
        self.value2 = Value2StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class Value2StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '开启异常'


class Value1StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开启'


class Value0StatusModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未开启'


class FunctionModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'function'
        self.name = '子通道功能'
        self.type = 'string'
        self.v: str = ''


class DetectionAreaIdListModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaIdList'
        self.name = '检测区域ID列表'
        self.type = 'array'
        self.columnSimple = [DetectionAreaIdListModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = DetectionAreaIdListModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class DetectionAreaIdListModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class CameraUrlCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流url'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '检测摄像头ID'
        self.type = 'string'
        self.v: str = ''


class ChannelIdCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelId'
        self.name = '通道编号'
        self.type = 'string'
        self.v: str = ''


class QueryCamerAIByCameraIdAndModelIdServiceParameters:
    def __init__(self) -> None:
        self.cameraAIList = CameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameter()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraAIList'
        self.name = '摄像头信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameterColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '子通道信息'
        self.type = 'array'
        self.columnSimple = [ModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameterColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameterColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ModelInfoListCameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameterColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListQueryCamerAIByCameraIdAndModelIdServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '检测摄像头ID'
        self.type = 'string'
        self.v: str = ''


class QueryCameraAIByCameraIdService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryCameraAIByCameraId'
        self.name = '根据通道ID查询检测通道'
        self.type = 'management'
        self.parameters = QueryCameraAIByCameraIdServiceParameters()
        self.output = [QueryCameraAIByCameraIdServiceOutput()]


class QueryCameraAIByCameraIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraAIList = CameraAIListQueryCameraAIByCameraIdServiceOutput()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListQueryCameraAIByCameraIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraAIList'
        self.name = '通道信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.channelId = ChannelIdCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct()
        self.cameraId = CameraIdCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct()
        self.cameraUrl = CameraUrlCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'channelId': self.channelId.v, 'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('channelId') is not None: self.channelId.v = value['channelId']
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '子通道信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.detectionAreaIdList = DetectionAreaIdListModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.function = FunctionModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.status = StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionAreaIdList': self.detectionAreaIdList.v, 'function': self.function.v, 'status': self.status.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionAreaIdList') is not None: self.detectionAreaIdList.v = value['detectionAreaIdList']
        if value.get('function') is not None: self.function.v = value['function']
        if value.get('status') is not None: self.status.v = value['status']


class StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'status'
        self.name = '运行状态'
        self.type = 'integer'
        self.specs = StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()
        self.value1 = Value1StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()
        self.value2 = Value2StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional()


class Value2StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '开启异常'


class Value1StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开启'


class Value0StatusModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未开启'


class FunctionModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'function'
        self.name = '子通道功能'
        self.type = 'string'
        self.v: str = ''


class DetectionAreaIdListModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaIdList'
        self.name = '检测区域ID列表'
        self.type = 'array'
        self.columnSimple = [DetectionAreaIdListModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = DetectionAreaIdListModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class DetectionAreaIdListModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class CameraUrlCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流url'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '检测摄像头ID'
        self.type = 'string'
        self.v: str = ''


class ChannelIdCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelId'
        self.name = '通道编号'
        self.type = 'string'
        self.v: str = ''


class QueryCameraAIByCameraIdServiceParameters:
    def __init__(self) -> None:
        self.cameraIdList = CameraIdListQueryCameraAIByCameraIdServiceParameter()

    @property
    def v(self):
        return {'cameraIdList': self.cameraIdList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraIdList') is not None: self.cameraIdList.v = value['cameraIdList']


class CameraIdListQueryCameraAIByCameraIdServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraIdList'
        self.name = '通道id列表'
        self.type = 'array'
        self.columnSimple = [CameraIdListQueryCameraAIByCameraIdServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = CameraIdListQueryCameraAIByCameraIdServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class CameraIdListQueryCameraAIByCameraIdServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class DeleteCameraAISubService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'deleteCameraAISub'
        self.name = '删除检测通道子通道'
        self.type = 'management'
        self.parameters = DeleteCameraAISubServiceParameters()
        self.output = None


class DeleteCameraAISubServiceParameters:
    def __init__(self) -> None:
        self.cameraAIList = CameraAIListDeleteCameraAISubServiceParameter()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListDeleteCameraAISubServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraAIList'
        self.name = '通道id列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListDeleteCameraAISubServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListDeleteCameraAISubServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListDeleteCameraAISubServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraAIListDeleteCameraAISubServiceParameterColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListDeleteCameraAISubServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListDeleteCameraAISubServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '子通道信息'
        self.type = 'array'
        self.columnSimple = [ModelInfoListCameraAIListDeleteCameraAISubServiceParameterColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ModelInfoListCameraAIListDeleteCameraAISubServiceParameterColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ModelInfoListCameraAIListDeleteCameraAISubServiceParameterColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListDeleteCameraAISubServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '通道编号'
        self.type = 'string'
        self.v: str = ''


class DeleteCameraAIService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'deleteCameraAI'
        self.name = '删除检测通道'
        self.type = 'management'
        self.parameters = DeleteCameraAIServiceParameters()
        self.output = None


class DeleteCameraAIServiceParameters:
    def __init__(self) -> None:
        self.cameraIdList = CameraIdListDeleteCameraAIServiceParameter()

    @property
    def v(self):
        return {'cameraIdList': self.cameraIdList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraIdList') is not None: self.cameraIdList.v = value['cameraIdList']


class CameraIdListDeleteCameraAIServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraIdList'
        self.name = '通道id列表'
        self.type = 'array'
        self.columnSimple = [CameraIdListDeleteCameraAIServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = CameraIdListDeleteCameraAIServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class CameraIdListDeleteCameraAIServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CloseCameraAISubService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'closeCameraAISub'
        self.name = '关闭检测通道模型'
        self.type = 'management'
        self.parameters = CloseCameraAISubServiceParameters()
        self.output = None


class CloseCameraAISubServiceParameters:
    def __init__(self) -> None:
        self.cameraAIList = CameraAIListCloseCameraAISubServiceParameter()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListCloseCameraAISubServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraAIList'
        self.name = '通道信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListCloseCameraAISubServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListCloseCameraAISubServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListCloseCameraAISubServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraAIListCloseCameraAISubServiceParameterColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListCloseCameraAISubServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListCloseCameraAISubServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '子通道信息'
        self.type = 'array'
        self.columnSimple = [ModelInfoListCameraAIListCloseCameraAISubServiceParameterColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ModelInfoListCameraAIListCloseCameraAISubServiceParameterColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ModelInfoListCameraAIListCloseCameraAISubServiceParameterColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListCloseCameraAISubServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '检测摄像头ID'
        self.type = 'string'
        self.v: str = ''


class CloseCameraAIService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'closeCameraAI'
        self.name = '关闭检测通道'
        self.type = 'management'
        self.parameters = CloseCameraAIServiceParameters()
        self.output = None


class CloseCameraAIServiceParameters:
    def __init__(self) -> None:
        self.cameraIdList = CameraIdListCloseCameraAIServiceParameter()

    @property
    def v(self):
        return {'cameraIdList': self.cameraIdList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraIdList') is not None: self.cameraIdList.v = value['cameraIdList']


class CameraIdListCloseCameraAIServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraIdList'
        self.name = '通道id列表'
        self.type = 'array'
        self.columnSimple = [CameraIdListCloseCameraAIServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = CameraIdListCloseCameraAIServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class CameraIdListCloseCameraAIServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class OpenCameraAIService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'openCameraAI'
        self.name = '添加检测通道'
        self.type = 'management'
        self.parameters = OpenCameraAIServiceParameters()
        self.output = None


class OpenCameraAIServiceParameters:
    def __init__(self) -> None:
        self.cameraAIList = CameraAIListOpenCameraAIServiceParameter()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListOpenCameraAIServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraAIList'
        self.name = '通道信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListOpenCameraAIServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListOpenCameraAIServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListOpenCameraAIServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraAIListOpenCameraAIServiceParameterColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '子通道信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStruct()
        self.detectionAreaIdList = DetectionAreaIdListModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStruct()
        self.function = FunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionAreaIdList': self.detectionAreaIdList.v, 'function': self.function.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionAreaIdList') is not None: self.detectionAreaIdList.v = value['detectionAreaIdList']
        if value.get('function') is not None: self.function.v = value['function']


class FunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'function'
        self.name = '子通道功能'
        self.type = 'string'
        self.v: str = ''


class DetectionAreaIdListModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaIdList'
        self.name = '检测区域ID列表'
        self.type = 'array'
        self.columnSimple = [DetectionAreaIdListModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = DetectionAreaIdListModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class DetectionAreaIdListModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListOpenCameraAIServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '检测摄像头ID'
        self.type = 'string'
        self.v: str = ''


class QueryCameraService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryCamera'
        self.name = '查询摄像头'
        self.type = 'management'
        self.parameters = None
        self.output = [QueryCameraServiceOutput()]


class QueryCameraServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraInfoList = CameraInfoListQueryCameraServiceOutput()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListQueryCameraServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头列表'
        self.type = 'array'
        self.columnComplex = [CameraInfoListQueryCameraServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListQueryCameraServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListQueryCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraInfoListQueryCameraServiceOutputColumnComplexStruct()
        self.cameraUrl = CameraUrlCameraInfoListQueryCameraServiceOutputColumnComplexStruct()
        self.pushRtsp = PushRtspCameraInfoListQueryCameraServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'pushRtsp': self.pushRtsp.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('pushRtsp') is not None: self.pushRtsp.v = value['pushRtsp']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '应用模型信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStruct()
        self.detectionInfo = DetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStruct()
        self.imageCollectInfo = ImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionInfo': self.detectionInfo.v, 'imageCollectInfo': self.imageCollectInfo.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionInfo') is not None: self.detectionInfo.v = value['detectionInfo']
        if value.get('imageCollectInfo') is not None: self.imageCollectInfo.v = value['imageCollectInfo']


class ImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'imageCollectInfo'
        self.name = '图片采集信息'
        self.type = 'struct'
        self.struct = ImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.pushImageAddress = PushImageAddressImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.startTime = StartTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.endTime = EndTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.circulationTime = CirculationTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objThresh = ObjThreshImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objThresh': self.objThresh.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objThresh') is not None: self.objThresh.v = value['objThresh']


class ObjThreshImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThresh'
        self.name = '目标采集阈值'
        self.type = 'number'
        self.specs = ObjThreshImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class ObjThreshImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class CirculationTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'circulationTime'
        self.name = '采集时间是否循环'
        self.type = 'boolean'
        self.v: bool = True


class EndTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '采集结束时间'
        self.type = 'string'
        self.v: str = ''


class StartTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '采集开始时间'
        self.type = 'string'
        self.v: str = ''


class PushImageAddressImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageAddress'
        self.name = '图片推送地址'
        self.type = 'string'
        self.v: str = ''


class DetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionInfo'
        self.name = '检测区域检测信息'
        self.type = 'struct'
        self.struct = DetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class DetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.objList = ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.alarmInterval = AlarmIntervalDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objThresh = ObjThreshDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfoList = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmInterval': self.alarmInterval.v, 'objThresh': self.objThresh.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfoList': self.detectionAreaInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmInterval') is not None: self.alarmInterval.v = value['alarmInterval']
        if value.get('objThresh') is not None: self.objThresh.v = value['objThresh']
        if value.get('pushImageFile') is not None: self.pushImageFile.v = value['pushImageFile']
        if value.get('detectionAreaInfoList') is not None: self.detectionAreaInfoList.v = value['detectionAreaInfoList']


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaInfoList'
        self.name = '检测区域信息'
        self.type = 'array'
        self.columnComplex = [DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.regionId = RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()
        self.regionArea = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()

    @property
    def v(self):
        return {'regionId': self.regionId.v, 'regionArea': self.regionArea.v}

    @v.setter
    def v(self, value):
        if value.get('regionId') is not None: self.regionId.v = value['regionId']
        if value.get('regionArea') is not None: self.regionArea.v = value['regionArea']


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionArea'
        self.name = '检测区域面积信息'
        self.type = 'struct'
        self.struct = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.x = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.y = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.w = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.h = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'x': self.x.v, 'y': self.y.v, 'w': self.w.v, 'h': self.h.v}

    @v.setter
    def v(self, value):
        if value.get('x') is not None: self.x.v = value['x']
        if value.get('y') is not None: self.y.v = value['y']
        if value.get('w') is not None: self.w.v = value['w']
        if value.get('h') is not None: self.h.v = value['h']


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'h'
        self.name = '检测区域h'
        self.type = 'number'
        self.specs = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'w'
        self.name = '检测区域w'
        self.type = 'number'
        self.specs = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'y'
        self.name = '检测区域y'
        self.type = 'number'
        self.specs = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'x'
        self.name = '检测区域x'
        self.type = 'number'
        self.specs = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionId'
        self.name = '区域ID'
        self.type = 'string'
        self.v: str = ''


class PushImageFileDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageFile'
        self.name = '识别推送图片地址'
        self.type = 'string'
        self.v: str = ''


class ObjThreshDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThresh'
        self.name = '目标上报阈值'
        self.type = 'number'
        self.specs = ObjThreshDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class ObjThreshDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class AlarmIntervalDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmInterval'
        self.name = '告警间隔'
        self.type = 'integer'
        self.specs = AlarmIntervalDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructSpecs()
        self.v: int = 0


class AlarmIntervalDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.columnSimple = [ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class PushRtspCameraInfoListQueryCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pushRtsp'
        self.name = '识别推送视频流地址'
        self.type = 'string'
        self.v: str = ''


class CameraUrlCameraInfoListQueryCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流URL'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraInfoListQueryCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class QueryCameraByIdService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryCameraById'
        self.name = '根据ID查询摄像头'
        self.type = 'management'
        self.parameters = QueryCameraByIdServiceParameters()
        self.output = [QueryCameraByIdServiceOutput()]


class QueryCameraByIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraInfoList = CameraInfoListQueryCameraByIdServiceOutput()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListQueryCameraByIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头列表'
        self.type = 'array'
        self.columnComplex = [CameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct()
        self.cameraUrl = CameraUrlCameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct()
        self.pushRtsp = PushRtspCameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'pushRtsp': self.pushRtsp.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('pushRtsp') is not None: self.pushRtsp.v = value['pushRtsp']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '应用模型信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.detectionInfo = DetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.imageCollectInfo = ImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionInfo': self.detectionInfo.v, 'imageCollectInfo': self.imageCollectInfo.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionInfo') is not None: self.detectionInfo.v = value['detectionInfo']
        if value.get('imageCollectInfo') is not None: self.imageCollectInfo.v = value['imageCollectInfo']


class ImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'imageCollectInfo'
        self.name = '图片采集信息'
        self.type = 'struct'
        self.struct = ImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.pushImageAddress = PushImageAddressImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.startTime = StartTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.endTime = EndTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.circulationTime = CirculationTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objThresh = ObjThreshImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objThresh': self.objThresh.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objThresh') is not None: self.objThresh.v = value['objThresh']


class ObjThreshImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThresh'
        self.name = '目标采集阈值'
        self.type = 'number'
        self.specs = ObjThreshImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class ObjThreshImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class CirculationTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'circulationTime'
        self.name = '采集时间是否循环'
        self.type = 'boolean'
        self.v: bool = True


class EndTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '采集结束时间'
        self.type = 'string'
        self.v: str = ''


class StartTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '采集开始时间'
        self.type = 'string'
        self.v: str = ''


class PushImageAddressImageCollectInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageAddress'
        self.name = '图片推送地址'
        self.type = 'string'
        self.v: str = ''


class DetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionInfo'
        self.name = '检测区域检测信息'
        self.type = 'struct'
        self.struct = DetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class DetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.objList = ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.alarmInterval = AlarmIntervalDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objThresh = ObjThreshDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfoList = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmInterval': self.alarmInterval.v, 'objThresh': self.objThresh.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfoList': self.detectionAreaInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmInterval') is not None: self.alarmInterval.v = value['alarmInterval']
        if value.get('objThresh') is not None: self.objThresh.v = value['objThresh']
        if value.get('pushImageFile') is not None: self.pushImageFile.v = value['pushImageFile']
        if value.get('detectionAreaInfoList') is not None: self.detectionAreaInfoList.v = value['detectionAreaInfoList']


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaInfoList'
        self.name = '检测区域信息'
        self.type = 'array'
        self.columnComplex = [DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.regionId = RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()
        self.regionArea = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()

    @property
    def v(self):
        return {'regionId': self.regionId.v, 'regionArea': self.regionArea.v}

    @v.setter
    def v(self, value):
        if value.get('regionId') is not None: self.regionId.v = value['regionId']
        if value.get('regionArea') is not None: self.regionArea.v = value['regionArea']


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionArea'
        self.name = '检测区域面积信息'
        self.type = 'struct'
        self.struct = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.x = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.y = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.w = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.h = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'x': self.x.v, 'y': self.y.v, 'w': self.w.v, 'h': self.h.v}

    @v.setter
    def v(self, value):
        if value.get('x') is not None: self.x.v = value['x']
        if value.get('y') is not None: self.y.v = value['y']
        if value.get('w') is not None: self.w.v = value['w']
        if value.get('h') is not None: self.h.v = value['h']


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'h'
        self.name = '检测区域h'
        self.type = 'number'
        self.specs = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'w'
        self.name = '检测区域w'
        self.type = 'number'
        self.specs = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'y'
        self.name = '检测区域y'
        self.type = 'number'
        self.specs = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'x'
        self.name = '检测区域x'
        self.type = 'number'
        self.specs = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionId'
        self.name = '区域ID'
        self.type = 'string'
        self.v: str = ''


class PushImageFileDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageFile'
        self.name = '识别推送图片地址'
        self.type = 'string'
        self.v: str = ''


class ObjThreshDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThresh'
        self.name = '目标上报阈值'
        self.type = 'number'
        self.specs = ObjThreshDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class ObjThreshDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class AlarmIntervalDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmInterval'
        self.name = '告警间隔'
        self.type = 'integer'
        self.specs = AlarmIntervalDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructSpecs()
        self.v: int = 0


class AlarmIntervalDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.columnSimple = [ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraInfoListQueryCameraByIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class PushRtspCameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pushRtsp'
        self.name = '识别推送视频流地址'
        self.type = 'string'
        self.v: str = ''


class CameraUrlCameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流URL'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraInfoListQueryCameraByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class QueryCameraByIdServiceParameters:
    def __init__(self) -> None:
        self.cameraIdList = CameraIdListQueryCameraByIdServiceParameter()

    @property
    def v(self):
        return {'cameraIdList': self.cameraIdList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraIdList') is not None: self.cameraIdList.v = value['cameraIdList']


class CameraIdListQueryCameraByIdServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraIdList'
        self.name = '摄像头ID列表'
        self.type = 'array'
        self.columnSimple = [CameraIdListQueryCameraByIdServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = CameraIdListQueryCameraByIdServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class CameraIdListQueryCameraByIdServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModifyCameraService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'modifyCamera'
        self.name = '修改摄像头信息'
        self.type = 'management'
        self.parameters = ModifyCameraServiceParameters()
        self.output = None


class ModifyCameraServiceParameters:
    def __init__(self) -> None:
        self.cameraInfoList = CameraInfoListModifyCameraServiceParameter()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListModifyCameraServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头列表'
        self.type = 'array'
        self.columnComplex = [CameraInfoListModifyCameraServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListModifyCameraServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListModifyCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraInfoListModifyCameraServiceParameterColumnComplexStruct()
        self.pushRtsp = PushRtspCameraInfoListModifyCameraServiceParameterColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'pushRtsp': self.pushRtsp.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('pushRtsp') is not None: self.pushRtsp.v = value['pushRtsp']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '应用模型信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStruct()
        self.detectionInfo = DetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStruct()
        self.imageCollectInfo = ImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionInfo': self.detectionInfo.v, 'imageCollectInfo': self.imageCollectInfo.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionInfo') is not None: self.detectionInfo.v = value['detectionInfo']
        if value.get('imageCollectInfo') is not None: self.imageCollectInfo.v = value['imageCollectInfo']


class ImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'imageCollectInfo'
        self.name = '图片采集信息'
        self.type = 'struct'
        self.struct = ImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.pushImageAddress = PushImageAddressImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.startTime = StartTimeImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.endTime = EndTimeImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.circulationTime = CirculationTimeImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.objThresh = ObjThreshImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objThresh': self.objThresh.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objThresh') is not None: self.objThresh.v = value['objThresh']


class ObjThreshImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThresh'
        self.name = '目标采集阈值'
        self.type = 'number'
        self.specs = ObjThreshImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class ObjThreshImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class CirculationTimeImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'circulationTime'
        self.name = '采集时间是否循环'
        self.type = 'boolean'
        self.v: bool = True


class EndTimeImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '采集结束时间'
        self.type = 'string'
        self.v: str = ''


class StartTimeImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '采集开始时间'
        self.type = 'string'
        self.v: str = ''


class PushImageAddressImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageAddress'
        self.name = '图片推送地址'
        self.type = 'string'
        self.v: str = ''


class DetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionInfo'
        self.name = '检测区域检测信息'
        self.type = 'struct'
        self.struct = DetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class DetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.objList = ObjListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.alarmInterval = AlarmIntervalDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.objThresh = ObjThreshDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfoList = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmInterval': self.alarmInterval.v, 'objThresh': self.objThresh.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfoList': self.detectionAreaInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmInterval') is not None: self.alarmInterval.v = value['alarmInterval']
        if value.get('objThresh') is not None: self.objThresh.v = value['objThresh']
        if value.get('pushImageFile') is not None: self.pushImageFile.v = value['pushImageFile']
        if value.get('detectionAreaInfoList') is not None: self.detectionAreaInfoList.v = value['detectionAreaInfoList']


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaInfoList'
        self.name = '检测区域信息'
        self.type = 'array'
        self.columnComplex = [DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.regionId = RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct()
        self.regionArea = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct()

    @property
    def v(self):
        return {'regionId': self.regionId.v, 'regionArea': self.regionArea.v}

    @v.setter
    def v(self, value):
        if value.get('regionId') is not None: self.regionId.v = value['regionId']
        if value.get('regionArea') is not None: self.regionArea.v = value['regionArea']


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionArea'
        self.name = '检测区域面积信息'
        self.type = 'struct'
        self.struct = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.x = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.y = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.w = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.h = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'x': self.x.v, 'y': self.y.v, 'w': self.w.v, 'h': self.h.v}

    @v.setter
    def v(self, value):
        if value.get('x') is not None: self.x.v = value['x']
        if value.get('y') is not None: self.y.v = value['y']
        if value.get('w') is not None: self.w.v = value['w']
        if value.get('h') is not None: self.h.v = value['h']


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'h'
        self.name = '检测区域h'
        self.type = 'number'
        self.specs = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'w'
        self.name = '检测区域w'
        self.type = 'number'
        self.specs = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'y'
        self.name = '检测区域y'
        self.type = 'number'
        self.specs = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'x'
        self.name = '检测区域x'
        self.type = 'number'
        self.specs = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionId'
        self.name = '区域ID'
        self.type = 'string'
        self.v: str = ''


class PushImageFileDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageFile'
        self.name = '识别推送图片地址'
        self.type = 'string'
        self.v: str = ''


class ObjThreshDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThresh'
        self.name = '目标上报阈值'
        self.type = 'number'
        self.specs = ObjThreshDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class ObjThreshDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class AlarmIntervalDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmInterval'
        self.name = '告警间隔'
        self.type = 'integer'
        self.specs = AlarmIntervalDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs()
        self.v: int = 0


class AlarmIntervalDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.columnSimple = [ObjListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class PushRtspCameraInfoListModifyCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pushRtsp'
        self.name = '识别推送视频流地址'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraInfoListModifyCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class DeleteCameraService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'deleteCamera'
        self.name = '删除摄像头'
        self.type = 'management'
        self.parameters = DeleteCameraServiceParameters()
        self.output = None


class DeleteCameraServiceParameters:
    def __init__(self) -> None:
        self.cameraIdList = CameraIdListDeleteCameraServiceParameter()

    @property
    def v(self):
        return {'cameraIdList': self.cameraIdList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraIdList') is not None: self.cameraIdList.v = value['cameraIdList']


class CameraIdListDeleteCameraServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraIdList'
        self.name = '摄像头列表'
        self.type = 'array'
        self.columnSimple = [CameraIdListDeleteCameraServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = CameraIdListDeleteCameraServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class CameraIdListDeleteCameraServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class AddCameraService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'addCamera'
        self.name = '增加摄像头'
        self.type = 'management'
        self.parameters = AddCameraServiceParameters()
        self.output = None


class AddCameraServiceParameters:
    def __init__(self) -> None:
        self.cameraInfoList = CameraInfoListAddCameraServiceParameter()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListAddCameraServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头列表'
        self.type = 'array'
        self.columnComplex = [CameraInfoListAddCameraServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListAddCameraServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListAddCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraInfoListAddCameraServiceParameterColumnComplexStruct()
        self.cameraUrl = CameraUrlCameraInfoListAddCameraServiceParameterColumnComplexStruct()
        self.pushRtsp = PushRtspCameraInfoListAddCameraServiceParameterColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'pushRtsp': self.pushRtsp.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('pushRtsp') is not None: self.pushRtsp.v = value['pushRtsp']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '应用模型信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStruct()
        self.detectionInfo = DetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStruct()
        self.imageCollectInfo = ImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionInfo': self.detectionInfo.v, 'imageCollectInfo': self.imageCollectInfo.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionInfo') is not None: self.detectionInfo.v = value['detectionInfo']
        if value.get('imageCollectInfo') is not None: self.imageCollectInfo.v = value['imageCollectInfo']


class ImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'imageCollectInfo'
        self.name = '图片采集信息'
        self.type = 'struct'
        self.struct = ImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.pushImageAddress = PushImageAddressImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.startTime = StartTimeImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.endTime = EndTimeImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.circulationTime = CirculationTimeImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.objThresh = ObjThreshImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objThresh': self.objThresh.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objThresh') is not None: self.objThresh.v = value['objThresh']


class ObjThreshImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThresh'
        self.name = '目标采集阈值'
        self.type = 'number'
        self.specs = ObjThreshImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class ObjThreshImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class CirculationTimeImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'circulationTime'
        self.name = '采集时间是否循环'
        self.type = 'boolean'
        self.v: bool = True


class EndTimeImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '采集结束时间'
        self.type = 'string'
        self.v: str = ''


class StartTimeImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '采集开始时间'
        self.type = 'string'
        self.v: str = ''


class PushImageAddressImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageAddress'
        self.name = '图片推送地址'
        self.type = 'string'
        self.v: str = ''


class DetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionInfo'
        self.name = '检测区域检测信息'
        self.type = 'struct'
        self.struct = DetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class DetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.objList = ObjListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.alarmInterval = AlarmIntervalDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.objThresh = ObjThreshDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfoList = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmInterval': self.alarmInterval.v, 'objThresh': self.objThresh.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfoList': self.detectionAreaInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmInterval') is not None: self.alarmInterval.v = value['alarmInterval']
        if value.get('objThresh') is not None: self.objThresh.v = value['objThresh']
        if value.get('pushImageFile') is not None: self.pushImageFile.v = value['pushImageFile']
        if value.get('detectionAreaInfoList') is not None: self.detectionAreaInfoList.v = value['detectionAreaInfoList']


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaInfoList'
        self.name = '检测区域信息'
        self.type = 'array'
        self.columnComplex = [DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.regionId = RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct()
        self.regionArea = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct()

    @property
    def v(self):
        return {'regionId': self.regionId.v, 'regionArea': self.regionArea.v}

    @v.setter
    def v(self, value):
        if value.get('regionId') is not None: self.regionId.v = value['regionId']
        if value.get('regionArea') is not None: self.regionArea.v = value['regionArea']


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionArea'
        self.name = '检测区域面积信息'
        self.type = 'struct'
        self.struct = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.x = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.y = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.w = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.h = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'x': self.x.v, 'y': self.y.v, 'w': self.w.v, 'h': self.h.v}

    @v.setter
    def v(self, value):
        if value.get('x') is not None: self.x.v = value['x']
        if value.get('y') is not None: self.y.v = value['y']
        if value.get('w') is not None: self.w.v = value['w']
        if value.get('h') is not None: self.h.v = value['h']


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'h'
        self.name = '检测区域h'
        self.type = 'number'
        self.specs = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'w'
        self.name = '检测区域w'
        self.type = 'number'
        self.specs = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'y'
        self.name = '检测区域y'
        self.type = 'number'
        self.specs = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'x'
        self.name = '检测区域x'
        self.type = 'number'
        self.specs = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionId'
        self.name = '区域ID'
        self.type = 'string'
        self.v: str = ''


class PushImageFileDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageFile'
        self.name = '识别推送图片地址'
        self.type = 'string'
        self.v: str = ''


class ObjThreshDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThresh'
        self.name = '目标上报阈值'
        self.type = 'number'
        self.specs = ObjThreshDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class ObjThreshDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class AlarmIntervalDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmInterval'
        self.name = '告警间隔'
        self.type = 'integer'
        self.specs = AlarmIntervalDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs()
        self.v: int = 0


class AlarmIntervalDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.columnSimple = [ObjListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class PushRtspCameraInfoListAddCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pushRtsp'
        self.name = '识别推送视频流地址'
        self.type = 'string'
        self.v: str = ''


class CameraUrlCameraInfoListAddCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流URL'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraInfoListAddCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class QueryModelService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryModel'
        self.name = '模型查询'
        self.type = 'management'
        self.parameters = None
        self.output = [QueryModelServiceOutput()]


class QueryModelServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.modelInfoList = ModelInfoListQueryModelServiceOutput()

    @property
    def v(self):
        return {'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListQueryModelServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'modelInfoList'
        self.name = '模型信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListQueryModelServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListQueryModelServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListQueryModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListQueryModelServiceOutputColumnComplexStruct()
        self.modelName = ModelNameModelInfoListQueryModelServiceOutputColumnComplexStruct()
        self.modelUrl = ModelUrlModelInfoListQueryModelServiceOutputColumnComplexStruct()
        self.modelFile = ModelFileModelInfoListQueryModelServiceOutputColumnComplexStruct()
        self.modelMd5 = ModelMd5ModelInfoListQueryModelServiceOutputColumnComplexStruct()
        self.modelFunction = ModelFunctionModelInfoListQueryModelServiceOutputColumnComplexStruct()
        self.modelAlgType = ModelAlgTypeModelInfoListQueryModelServiceOutputColumnComplexStruct()
        self.targetNameList = TargetNameListModelInfoListQueryModelServiceOutputColumnComplexStruct()
        self.updateTime = UpdateTimeModelInfoListQueryModelServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'modelName': self.modelName.v, 'modelUrl': self.modelUrl.v, 'modelFile': self.modelFile.v, 'modelMd5': self.modelMd5.v, 'modelFunction': self.modelFunction.v, 'modelAlgType': self.modelAlgType.v, 'targetNameList': self.targetNameList.v, 'updateTime': self.updateTime.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('modelName') is not None: self.modelName.v = value['modelName']
        if value.get('modelUrl') is not None: self.modelUrl.v = value['modelUrl']
        if value.get('modelFile') is not None: self.modelFile.v = value['modelFile']
        if value.get('modelMd5') is not None: self.modelMd5.v = value['modelMd5']
        if value.get('modelFunction') is not None: self.modelFunction.v = value['modelFunction']
        if value.get('modelAlgType') is not None: self.modelAlgType.v = value['modelAlgType']
        if value.get('targetNameList') is not None: self.targetNameList.v = value['targetNameList']
        if value.get('updateTime') is not None: self.updateTime.v = value['updateTime']


class UpdateTimeModelInfoListQueryModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'updateTime'
        self.name = '模型更新时间'
        self.type = 'string'
        self.v: str = ''


class TargetNameListModelInfoListQueryModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetNameList'
        self.name = '识别能力列表'
        self.type = 'array'
        self.columnSimple = [TargetNameListModelInfoListQueryModelServiceOutputColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = TargetNameListModelInfoListQueryModelServiceOutputColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class TargetNameListModelInfoListQueryModelServiceOutputColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelAlgTypeModelInfoListQueryModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelAlgType'
        self.name = '模型类别(ssd、yolo、built-in)'
        self.type = 'string'
        self.v: str = ''


class ModelFunctionModelInfoListQueryModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelFunction'
        self.name = '模型功能(分类、检测)'
        self.type = 'string'
        self.v: str = ''


class ModelMd5ModelInfoListQueryModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelMd5'
        self.name = '模型md5值'
        self.type = 'string'
        self.v: str = ''


class ModelFileModelInfoListQueryModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelFile'
        self.name = '模型文件地址'
        self.type = 'string'
        self.v: str = ''


class ModelUrlModelInfoListQueryModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelUrl'
        self.name = '模型url地址'
        self.type = 'string'
        self.v: str = ''


class ModelNameModelInfoListQueryModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelName'
        self.name = '模型名称'
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListQueryModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型ID'
        self.type = 'string'
        self.v: str = ''


class QueryModelByIdService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryModelById'
        self.name = '根据ID查询模型'
        self.type = 'management'
        self.parameters = QueryModelByIdServiceParameters()
        self.output = [QueryModelByIdServiceOutput()]


class QueryModelByIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.modelInfoList = ModelInfoListQueryModelByIdServiceOutput()

    @property
    def v(self):
        return {'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListQueryModelByIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'modelInfoList'
        self.name = '模型信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListQueryModelByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()
        self.modelName = ModelNameModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()
        self.modelUrl = ModelUrlModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()
        self.modelFile = ModelFileModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()
        self.modelMd5 = ModelMd5ModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()
        self.modelFunction = ModelFunctionModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()
        self.modelAlgType = ModelAlgTypeModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()
        self.targetNameList = TargetNameListModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()
        self.updateTime = UpdateTimeModelInfoListQueryModelByIdServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'modelName': self.modelName.v, 'modelUrl': self.modelUrl.v, 'modelFile': self.modelFile.v, 'modelMd5': self.modelMd5.v, 'modelFunction': self.modelFunction.v, 'modelAlgType': self.modelAlgType.v, 'targetNameList': self.targetNameList.v, 'updateTime': self.updateTime.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('modelName') is not None: self.modelName.v = value['modelName']
        if value.get('modelUrl') is not None: self.modelUrl.v = value['modelUrl']
        if value.get('modelFile') is not None: self.modelFile.v = value['modelFile']
        if value.get('modelMd5') is not None: self.modelMd5.v = value['modelMd5']
        if value.get('modelFunction') is not None: self.modelFunction.v = value['modelFunction']
        if value.get('modelAlgType') is not None: self.modelAlgType.v = value['modelAlgType']
        if value.get('targetNameList') is not None: self.targetNameList.v = value['targetNameList']
        if value.get('updateTime') is not None: self.updateTime.v = value['updateTime']


class UpdateTimeModelInfoListQueryModelByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'updateTime'
        self.name = '模型更新时间'
        self.type = 'string'
        self.v: str = ''


class TargetNameListModelInfoListQueryModelByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetNameList'
        self.name = '识别能力列表'
        self.type = 'array'
        self.columnSimple = [TargetNameListModelInfoListQueryModelByIdServiceOutputColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = TargetNameListModelInfoListQueryModelByIdServiceOutputColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class TargetNameListModelInfoListQueryModelByIdServiceOutputColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelAlgTypeModelInfoListQueryModelByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelAlgType'
        self.name = '模型类别(ssd、yolo、built-in)'
        self.type = 'string'
        self.v: str = ''


class ModelFunctionModelInfoListQueryModelByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelFunction'
        self.name = '模型功能(分类、检测)'
        self.type = 'string'
        self.v: str = ''


class ModelMd5ModelInfoListQueryModelByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelMd5'
        self.name = '模型md5值'
        self.type = 'string'
        self.v: str = ''


class ModelFileModelInfoListQueryModelByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelFile'
        self.name = '模型文件地址'
        self.type = 'string'
        self.v: str = ''


class ModelUrlModelInfoListQueryModelByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelUrl'
        self.name = '模型url地址'
        self.type = 'string'
        self.v: str = ''


class ModelNameModelInfoListQueryModelByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelName'
        self.name = '模型名称'
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListQueryModelByIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型ID'
        self.type = 'string'
        self.v: str = ''


class QueryModelByIdServiceParameters:
    def __init__(self) -> None:
        self.modelIdList = ModelIdListQueryModelByIdServiceParameter()

    @property
    def v(self):
        return {'modelIdList': self.modelIdList.v}

    @v.setter
    def v(self, value):
        if value.get('modelIdList') is not None: self.modelIdList.v = value['modelIdList']


class ModelIdListQueryModelByIdServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelIdList'
        self.name = '模型ID'
        self.type = 'array'
        self.columnSimple = [ModelIdListQueryModelByIdServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ModelIdListQueryModelByIdServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ModelIdListQueryModelByIdServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class UpdateModelService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'updateModel'
        self.name = '模型更新'
        self.type = 'management'
        self.parameters = UpdateModelServiceParameters()
        self.output = None


class UpdateModelServiceParameters:
    def __init__(self) -> None:
        self.modelInfoList = ModelInfoListUpdateModelServiceParameter()

    @property
    def v(self):
        return {'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListUpdateModelServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListUpdateModelServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListUpdateModelServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListUpdateModelServiceParameterColumnComplexStruct()
        self.modelName = ModelNameModelInfoListUpdateModelServiceParameterColumnComplexStruct()
        self.modelUrl = ModelUrlModelInfoListUpdateModelServiceParameterColumnComplexStruct()
        self.modelMd5 = ModelMd5ModelInfoListUpdateModelServiceParameterColumnComplexStruct()
        self.updateTime = UpdateTimeModelInfoListUpdateModelServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'modelName': self.modelName.v, 'modelUrl': self.modelUrl.v, 'modelMd5': self.modelMd5.v, 'updateTime': self.updateTime.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('modelName') is not None: self.modelName.v = value['modelName']
        if value.get('modelUrl') is not None: self.modelUrl.v = value['modelUrl']
        if value.get('modelMd5') is not None: self.modelMd5.v = value['modelMd5']
        if value.get('updateTime') is not None: self.updateTime.v = value['updateTime']


class UpdateTimeModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'updateTime'
        self.name = '模型更新时间'
        self.type = 'string'
        self.v: str = ''


class ModelMd5ModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelMd5'
        self.name = '模型md5值'
        self.type = 'string'
        self.v: str = ''


class ModelUrlModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelUrl'
        self.name = '模型url地址'
        self.type = 'string'
        self.v: str = ''


class ModelNameModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelName'
        self.name = '模型名称'
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型ID'
        self.type = 'string'
        self.v: str = ''


class DeleteModelService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'deleteModel'
        self.name = '删除模型'
        self.type = 'management'
        self.parameters = DeleteModelServiceParameters()
        self.output = None


class DeleteModelServiceParameters:
    def __init__(self) -> None:
        self.modelIdList = ModelIdListDeleteModelServiceParameter()

    @property
    def v(self):
        return {'modelIdList': self.modelIdList.v}

    @v.setter
    def v(self, value):
        if value.get('modelIdList') is not None: self.modelIdList.v = value['modelIdList']


class ModelIdListDeleteModelServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelIdList'
        self.name = '删除模型ID列表'
        self.type = 'array'
        self.columnSimple = [ModelIdListDeleteModelServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ModelIdListDeleteModelServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ModelIdListDeleteModelServiceParameterColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class AddModelService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'addModel'
        self.name = '模型增加'
        self.type = 'management'
        self.parameters = AddModelServiceParameters()
        self.output = None


class AddModelServiceParameters:
    def __init__(self) -> None:
        self.modelInfoList = ModelInfoListAddModelServiceParameter()

    @property
    def v(self):
        return {'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListAddModelServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListAddModelServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListAddModelServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListAddModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListAddModelServiceParameterColumnComplexStruct()
        self.modelName = ModelNameModelInfoListAddModelServiceParameterColumnComplexStruct()
        self.modelUrl = ModelUrlModelInfoListAddModelServiceParameterColumnComplexStruct()
        self.modelMd5 = ModelMd5ModelInfoListAddModelServiceParameterColumnComplexStruct()
        self.updateTime = UpdateTimeModelInfoListAddModelServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'modelName': self.modelName.v, 'modelUrl': self.modelUrl.v, 'modelMd5': self.modelMd5.v, 'updateTime': self.updateTime.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('modelName') is not None: self.modelName.v = value['modelName']
        if value.get('modelUrl') is not None: self.modelUrl.v = value['modelUrl']
        if value.get('modelMd5') is not None: self.modelMd5.v = value['modelMd5']
        if value.get('updateTime') is not None: self.updateTime.v = value['updateTime']


class UpdateTimeModelInfoListAddModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'updateTime'
        self.name = '模型更新时间'
        self.type = 'string'
        self.v: str = ''


class ModelMd5ModelInfoListAddModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelMd5'
        self.name = '模型md5值'
        self.type = 'string'
        self.v: str = ''


class ModelUrlModelInfoListAddModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelUrl'
        self.name = '模型url地址'
        self.type = 'string'
        self.v: str = ''


class ModelNameModelInfoListAddModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelName'
        self.name = '模型名称'
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListAddModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型ID'
        self.type = 'string'
        self.v: str = ''


class RebootService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'reboot'
        self.name = '重启'
        self.type = 'management'
        self.parameters = None
        self.output = None


class Events:
    def __init__(self) -> None:
        self.behaviorDetetcAlarm = BehaviorDetetcAlarmEvent()
        self.targetDetetcAlarm = TargetDetetcAlarmEvent()
        self.targetIdentifyAlarm = TargetIdentifyAlarmEvent()
        self.cameraAbnormal = CameraAbnormalEvent()


class CameraAbnormalEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'cameraAbnormal'
        self.name = '视频异常事件'
        self.parameters = CameraAbnormalEventParameters()


class CameraAbnormalEventParameters:
    def __init__(self) -> None:
        self.camerIdList = CamerIdListCameraAbnormalEventParameter()

    @property
    def v(self):
        return {'camerIdList': self.camerIdList.v}

    @v.setter
    def v(self, value):
        if value.get('camerIdList') is not None: self.camerIdList.v = value['camerIdList']


class CamerIdListCameraAbnormalEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'camerIdList'
        self.name = '异常摄像头列表'
        self.type = 'array'
        self.columnComplex = [CamerIdListCameraAbnormalEventParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CamerIdListCameraAbnormalEventParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CamerIdListCameraAbnormalEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCamerIdListCameraAbnormalEventParameterColumnComplexStruct()
        self.cameraUrl = CameraUrlCamerIdListCameraAbnormalEventParameterColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']


class CameraUrlCamerIdListCameraAbnormalEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流URL'
        self.type = 'string'
        self.v: str = ''


class CameraIdCamerIdListCameraAbnormalEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class TargetIdentifyAlarmEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'targetIdentifyAlarm'
        self.name = '目标分类告警'
        self.parameters = TargetIdentifyAlarmEventParameters()


class TargetIdentifyAlarmEventParameters:
    def __init__(self) -> None:
        self.channelId = ChannelIdTargetIdentifyAlarmEventParameter()
        self.cameraId = CameraIdTargetIdentifyAlarmEventParameter()
        self.cameraUrl = CameraUrlTargetIdentifyAlarmEventParameter()
        self.storageUrl = StorageUrlTargetIdentifyAlarmEventParameter()
        self.imagePath = ImagePathTargetIdentifyAlarmEventParameter()
        self.modelId = ModelIdTargetIdentifyAlarmEventParameter()
        self.modelFunction = ModelFunctionTargetIdentifyAlarmEventParameter()
        self.alarmList = AlarmListTargetIdentifyAlarmEventParameter()

    @property
    def v(self):
        return {'channelId': self.channelId.v, 'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'storageUrl': self.storageUrl.v, 'imagePath': self.imagePath.v, 'modelId': self.modelId.v, 'modelFunction': self.modelFunction.v, 'alarmList': self.alarmList.v}

    @v.setter
    def v(self, value):
        if value.get('channelId') is not None: self.channelId.v = value['channelId']
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('storageUrl') is not None: self.storageUrl.v = value['storageUrl']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('modelFunction') is not None: self.modelFunction.v = value['modelFunction']
        if value.get('alarmList') is not None: self.alarmList.v = value['alarmList']


class AlarmListTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'alarmList'
        self.name = '告警列表信息'
        self.type = 'array'
        self.columnComplex = [AlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = AlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class AlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.className = ClassNameAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct()
        self.targetEigenvalues = TargetEigenvaluesAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct()
        self.targetUuid = TargetUuidAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct()
        self.similarity = SimilarityAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct()

    @property
    def v(self):
        return {'className': self.className.v, 'targetEigenvalues': self.targetEigenvalues.v, 'targetUuid': self.targetUuid.v, 'similarity': self.similarity.v}

    @v.setter
    def v(self, value):
        if value.get('className') is not None: self.className.v = value['className']
        if value.get('targetEigenvalues') is not None: self.targetEigenvalues.v = value['targetEigenvalues']
        if value.get('targetUuid') is not None: self.targetUuid.v = value['targetUuid']
        if value.get('similarity') is not None: self.similarity.v = value['similarity']


class SimilarityAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'similarity'
        self.name = '相似度'
        self.type = 'number'
        self.specs = SimilarityAlarmListTargetIdentifyAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class SimilarityAlarmListTargetIdentifyAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class TargetUuidAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetUuid'
        self.name = '样本特征值对应的uuid'
        self.type = 'string'
        self.v: str = ''


class TargetEigenvaluesAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetEigenvalues'
        self.name = '识别目标特征值'
        self.type = 'string'
        self.v: str = ''


class ClassNameAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'className'
        self.name = '识别类型名称'
        self.type = 'string'
        self.v: str = ''


class ModelFunctionTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelFunction'
        self.name = '模型功能'
        self.type = 'string'
        self.v: str = ''


class ModelIdTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelId'
        self.name = '模型Id'
        self.type = 'string'
        self.v: str = ''


class ImagePathTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '告警图片智盒路径'
        self.type = 'string'
        self.v: str = ''


class StorageUrlTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'storageUrl'
        self.name = '告警视频存储URL'
        self.type = 'string'
        self.v: str = ''


class CameraUrlTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraUrl'
        self.name = '摄像头url'
        self.type = 'string'
        self.v: str = ''


class CameraIdTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraId'
        self.name = '摄像头Id'
        self.type = 'string'
        self.v: str = ''


class ChannelIdTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channelId'
        self.name = '通道id'
        self.type = 'string'
        self.v: str = ''


class TargetDetetcAlarmEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'targetDetetcAlarm'
        self.name = '目标检测告警'
        self.parameters = TargetDetetcAlarmEventParameters()


class TargetDetetcAlarmEventParameters:
    def __init__(self) -> None:
        self.channelId = ChannelIdTargetDetetcAlarmEventParameter()
        self.cameraId = CameraIdTargetDetetcAlarmEventParameter()
        self.cameraUrl = CameraUrlTargetDetetcAlarmEventParameter()
        self.storageUrl = StorageUrlTargetDetetcAlarmEventParameter()
        self.imagePath = ImagePathTargetDetetcAlarmEventParameter()
        self.modelId = ModelIdTargetDetetcAlarmEventParameter()
        self.modelFunction = ModelFunctionTargetDetetcAlarmEventParameter()
        self.alarmList = AlarmListTargetDetetcAlarmEventParameter()

    @property
    def v(self):
        return {'channelId': self.channelId.v, 'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'storageUrl': self.storageUrl.v, 'imagePath': self.imagePath.v, 'modelId': self.modelId.v, 'modelFunction': self.modelFunction.v, 'alarmList': self.alarmList.v}

    @v.setter
    def v(self, value):
        if value.get('channelId') is not None: self.channelId.v = value['channelId']
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('storageUrl') is not None: self.storageUrl.v = value['storageUrl']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('modelFunction') is not None: self.modelFunction.v = value['modelFunction']
        if value.get('alarmList') is not None: self.alarmList.v = value['alarmList']


class AlarmListTargetDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'alarmList'
        self.name = '告警列表信息'
        self.type = 'array'
        self.columnComplex = [AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.className = ClassNameAlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()
        self.objectId = ObjectIdAlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()
        self.X1 = X1AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()
        self.Y1 = Y1AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()
        self.X2 = X2AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()
        self.Y2 = Y2AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()
        self.targetEigenvalues = TargetEigenvaluesAlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()
        self.targetUuid = TargetUuidAlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()
        self.similarity = SimilarityAlarmListTargetDetetcAlarmEventParameterColumnComplexStruct()

    @property
    def v(self):
        return {'className': self.className.v, 'objectId': self.objectId.v, 'X1': self.X1.v, 'Y1': self.Y1.v, 'X2': self.X2.v, 'Y2': self.Y2.v, 'targetEigenvalues': self.targetEigenvalues.v, 'targetUuid': self.targetUuid.v, 'similarity': self.similarity.v}

    @v.setter
    def v(self, value):
        if value.get('className') is not None: self.className.v = value['className']
        if value.get('objectId') is not None: self.objectId.v = value['objectId']
        if value.get('X1') is not None: self.X1.v = value['X1']
        if value.get('Y1') is not None: self.Y1.v = value['Y1']
        if value.get('X2') is not None: self.X2.v = value['X2']
        if value.get('Y2') is not None: self.Y2.v = value['Y2']
        if value.get('targetEigenvalues') is not None: self.targetEigenvalues.v = value['targetEigenvalues']
        if value.get('targetUuid') is not None: self.targetUuid.v = value['targetUuid']
        if value.get('similarity') is not None: self.similarity.v = value['similarity']


class SimilarityAlarmListTargetDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'similarity'
        self.name = '目标相似度'
        self.type = 'number'
        self.specs = SimilarityAlarmListTargetDetetcAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class SimilarityAlarmListTargetDetetcAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class TargetUuidAlarmListTargetDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetUuid'
        self.name = '样本特征值对应的uuid'
        self.type = 'string'
        self.v: str = ''


class TargetEigenvaluesAlarmListTargetDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetEigenvalues'
        self.name = '识别目标特征值'
        self.type = 'string'
        self.v: str = ''


class Y2AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'Y2'
        self.name = '目标右下角Y坐标'
        self.type = 'number'
        self.specs = Y2AlarmListTargetDetetcAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class Y2AlarmListTargetDetetcAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class X2AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'X2'
        self.name = '目标右下角X坐标'
        self.type = 'number'
        self.specs = X2AlarmListTargetDetetcAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class X2AlarmListTargetDetetcAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class Y1AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'Y1'
        self.name = '目标左上角Y坐标'
        self.type = 'number'
        self.specs = Y1AlarmListTargetDetetcAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class Y1AlarmListTargetDetetcAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class X1AlarmListTargetDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'X1'
        self.name = '目标左上角X坐标'
        self.type = 'number'
        self.specs = X1AlarmListTargetDetetcAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class X1AlarmListTargetDetetcAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjectIdAlarmListTargetDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'objectId'
        self.name = '目标跟踪Id'
        self.type = 'string'
        self.v: str = ''


class ClassNameAlarmListTargetDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'className'
        self.name = '识别类型名称'
        self.type = 'string'
        self.v: str = ''


class ModelFunctionTargetDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelFunction'
        self.name = '模型功能'
        self.type = 'string'
        self.v: str = ''


class ModelIdTargetDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelId'
        self.name = '模型Id'
        self.type = 'string'
        self.v: str = ''


class ImagePathTargetDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '告警图片智盒路径'
        self.type = 'string'
        self.v: str = ''


class StorageUrlTargetDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'storageUrl'
        self.name = '告警视频存储URL'
        self.type = 'string'
        self.v: str = ''


class CameraUrlTargetDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraUrl'
        self.name = '摄像头url'
        self.type = 'string'
        self.v: str = ''


class CameraIdTargetDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraId'
        self.name = '摄像头Id'
        self.type = 'string'
        self.v: str = ''


class ChannelIdTargetDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channelId'
        self.name = '通道id'
        self.type = 'string'
        self.v: str = ''


class BehaviorDetetcAlarmEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'behaviorDetetcAlarm'
        self.name = '行为识别告警'
        self.parameters = BehaviorDetetcAlarmEventParameters()


class BehaviorDetetcAlarmEventParameters:
    def __init__(self) -> None:
        self.channelId = ChannelIdBehaviorDetetcAlarmEventParameter()
        self.cameraId = CameraIdBehaviorDetetcAlarmEventParameter()
        self.cameraUrl = CameraUrlBehaviorDetetcAlarmEventParameter()
        self.storageUrl = StorageUrlBehaviorDetetcAlarmEventParameter()
        self.imagePath = ImagePathBehaviorDetetcAlarmEventParameter()
        self.modelId = ModelIdBehaviorDetetcAlarmEventParameter()
        self.modelFunction = ModelFunctionBehaviorDetetcAlarmEventParameter()
        self.alarmList = AlarmListBehaviorDetetcAlarmEventParameter()

    @property
    def v(self):
        return {'channelId': self.channelId.v, 'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'storageUrl': self.storageUrl.v, 'imagePath': self.imagePath.v, 'modelId': self.modelId.v, 'modelFunction': self.modelFunction.v, 'alarmList': self.alarmList.v}

    @v.setter
    def v(self, value):
        if value.get('channelId') is not None: self.channelId.v = value['channelId']
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('storageUrl') is not None: self.storageUrl.v = value['storageUrl']
        if value.get('imagePath') is not None: self.imagePath.v = value['imagePath']
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('modelFunction') is not None: self.modelFunction.v = value['modelFunction']
        if value.get('alarmList') is not None: self.alarmList.v = value['alarmList']


class AlarmListBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'alarmList'
        self.name = '告警列表信息'
        self.type = 'array'
        self.columnComplex = [AlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = AlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class AlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.className = ClassNameAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct()
        self.startTime = StartTimeAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct()
        self.endTime = EndTimeAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct()
        self.similarity = SimilarityAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct()

    @property
    def v(self):
        return {'className': self.className.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'similarity': self.similarity.v}

    @v.setter
    def v(self, value):
        if value.get('className') is not None: self.className.v = value['className']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('similarity') is not None: self.similarity.v = value['similarity']


class SimilarityAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'similarity'
        self.name = '行为相似度'
        self.type = 'number'
        self.specs = SimilarityAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class SimilarityAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class EndTimeAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '行为结束时间'
        self.type = 'string'
        self.v: str = ''


class StartTimeAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '行为开始时间'
        self.type = 'string'
        self.v: str = ''


class ClassNameAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'className'
        self.name = '识别类型名称'
        self.type = 'string'
        self.v: str = ''


class ModelFunctionBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelFunction'
        self.name = '模型功能'
        self.type = 'string'
        self.v: str = ''


class ModelIdBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelId'
        self.name = '模型Id'
        self.type = 'string'
        self.v: str = ''


class ImagePathBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '告警图片地址'
        self.type = 'string'
        self.v: str = ''


class StorageUrlBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'storageUrl'
        self.name = '告警视频存储URL'
        self.type = 'string'
        self.v: str = ''


class CameraUrlBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraUrl'
        self.name = '摄像头url'
        self.type = 'string'
        self.v: str = ''


class CameraIdBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraId'
        self.name = '摄像头Id'
        self.type = 'string'
        self.v: str = ''


class ChannelIdBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channelId'
        self.name = '通道id'
        self.type = 'string'
        self.v: str = ''


class Properties:
    def __init__(self) -> None:
        self.sn = SnProperty()
        self.productId = ProductIdProperty()
        self.online = OnlineProperty()
        self.mode = ModeProperty()
        self.modelInfoList = ModelInfoListProperty()
        self.cameraInfoList = CameraInfoListProperty()
        self.cameraAIList = CameraAIListProperty()

    @property
    def v(self):
        return {'sn': self.sn.v, 'productId': self.productId.v, 'online': self.online.v, 'mode': self.mode.v, 'modelInfoList': self.modelInfoList.v, 'cameraInfoList': self.cameraInfoList.v, 'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('productId') is not None: self.productId.v = value['productId']
        if value.get('online') is not None: self.online.v = value['online']
        if value.get('mode') is not None: self.mode.v = value['mode']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'cameraAIList'
        self.name = '通道信息列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [CameraAIListPropertyColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListPropertyColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.channelId = ChannelIdCameraAIListPropertyColumnComplexStruct()
        self.cameraId = CameraIdCameraAIListPropertyColumnComplexStruct()
        self.cameraUrl = CameraUrlCameraAIListPropertyColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'channelId': self.channelId.v, 'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('channelId') is not None: self.channelId.v = value['channelId']
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '子通道信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct()
        self.detectionAreaIdList = DetectionAreaIdListModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct()
        self.function = FunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct()
        self.status = StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionAreaIdList': self.detectionAreaIdList.v, 'function': self.function.v, 'status': self.status.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionAreaIdList') is not None: self.detectionAreaIdList.v = value['detectionAreaIdList']
        if value.get('function') is not None: self.function.v = value['function']
        if value.get('status') is not None: self.status.v = value['status']


class StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'status'
        self.name = '模型检测状态'
        self.type = 'integer'
        self.specs = StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value0 = Value0StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.value1 = Value1StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.value2 = Value2StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class Value2StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 2
        self.desc = '开启异常'


class Value1StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 1
        self.desc = '开启'


class Value0StatusModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 0
        self.desc = '未开启'


class FunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'function'
        self.name = '子通道功能'
        self.type = 'string'
        self.v: str = ''


class DetectionAreaIdListModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaIdList'
        self.name = '检测区域ID列表'
        self.type = 'array'
        self.columnSimple = [DetectionAreaIdListModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = DetectionAreaIdListModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class DetectionAreaIdListModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class CameraUrlCameraAIListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流URL'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '检测摄像头ID'
        self.type = 'string'
        self.v: str = ''


class ChannelIdCameraAIListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelId'
        self.name = '通道编号'
        self.type = 'string'
        self.v: str = ''


class CameraInfoListProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [CameraInfoListPropertyColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListPropertyColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraInfoListPropertyColumnComplexStruct()
        self.cameraUrl = CameraUrlCameraInfoListPropertyColumnComplexStruct()
        self.pushRtsp = PushRtspCameraInfoListPropertyColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'pushRtsp': self.pushRtsp.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('pushRtsp') is not None: self.pushRtsp.v = value['pushRtsp']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '应用模型信息'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStruct()
        self.detectionInfo = DetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStruct()
        self.imageCollectInfo = ImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionInfo': self.detectionInfo.v, 'imageCollectInfo': self.imageCollectInfo.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionInfo') is not None: self.detectionInfo.v = value['detectionInfo']
        if value.get('imageCollectInfo') is not None: self.imageCollectInfo.v = value['imageCollectInfo']


class ImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'imageCollectInfo'
        self.name = '图片采集信息'
        self.type = 'struct'
        self.struct = ImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.pushImageAddress = PushImageAddressImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.startTime = StartTimeImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.endTime = EndTimeImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.circulationTime = CirculationTimeImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.objhresh = ObjhreshImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objhresh': self.objhresh.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objhresh') is not None: self.objhresh.v = value['objhresh']


class ObjhreshImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objhresh'
        self.name = '目标采集阈值'
        self.type = 'number'
        self.specs = ObjhreshImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class ObjhreshImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class CirculationTimeImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'circulationTime'
        self.name = '采集时间是否循环'
        self.type = 'boolean'
        self.v: bool = True


class EndTimeImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '采集结束时间'
        self.type = 'string'
        self.v: str = ''


class StartTimeImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '采集开始时间'
        self.type = 'string'
        self.v: str = ''


class PushImageAddressImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageAddress'
        self.name = '图片推送地址'
        self.type = 'string'
        self.v: str = ''


class DetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionInfo'
        self.name = '检测区域检测信息'
        self.type = 'struct'
        self.struct = DetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class DetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.objList = ObjListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.alarmInterval = AlarmIntervalDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.objThresh = ObjThreshDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfo = DetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmInterval': self.alarmInterval.v, 'objThresh': self.objThresh.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfo': self.detectionAreaInfo.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmInterval') is not None: self.alarmInterval.v = value['alarmInterval']
        if value.get('objThresh') is not None: self.objThresh.v = value['objThresh']
        if value.get('pushImageFile') is not None: self.pushImageFile.v = value['pushImageFile']
        if value.get('detectionAreaInfo') is not None: self.detectionAreaInfo.v = value['detectionAreaInfo']


class DetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaInfo'
        self.name = '检测区域信息'
        self.type = 'array'
        self.columnComplex = [DetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.regionId = RegionIdDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStruct()
        self.regionArea = RegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStruct()

    @property
    def v(self):
        return {'regionId': self.regionId.v, 'regionArea': self.regionArea.v}

    @v.setter
    def v(self, value):
        if value.get('regionId') is not None: self.regionId.v = value['regionId']
        if value.get('regionArea') is not None: self.regionArea.v = value['regionArea']


class RegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionArea'
        self.name = '检测区域面积信息'
        self.type = 'struct'
        self.struct = RegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class RegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.x = XRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.y = YRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.w = WRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.h = HRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'x': self.x.v, 'y': self.y.v, 'w': self.w.v, 'h': self.h.v}

    @v.setter
    def v(self, value):
        if value.get('x') is not None: self.x.v = value['x']
        if value.get('y') is not None: self.y.v = value['y']
        if value.get('w') is not None: self.w.v = value['w']
        if value.get('h') is not None: self.h.v = value['h']


class HRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'h'
        self.name = '检测区域h'
        self.type = 'number'
        self.specs = HRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class HRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class WRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'w'
        self.name = '检测区域w'
        self.type = 'number'
        self.specs = WRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class WRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class YRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'y'
        self.name = '检测区域y'
        self.type = 'number'
        self.specs = YRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class YRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class XRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'x'
        self.name = '检测区域x'
        self.type = 'number'
        self.specs = XRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class XRegionAreaDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class RegionIdDetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionId'
        self.name = '区域ID'
        self.type = 'string'
        self.v: str = ''


class PushImageFileDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageFile'
        self.name = '识别推送图片地址'
        self.type = 'string'
        self.v: str = ''


class ObjThreshDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThresh'
        self.name = '目标上报阈值'
        self.type = 'number'
        self.specs = ObjThreshDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class ObjThreshDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 1


class AlarmIntervalDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmInterval'
        self.name = '告警间隔'
        self.type = 'integer'
        self.specs = AlarmIntervalDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructSpecs()
        self.v: int = 0


class AlarmIntervalDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.columnSimple = [ObjListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class PushRtspCameraInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pushRtsp'
        self.name = '识别推送视频流地址'
        self.type = 'string'
        self.v: str = ''


class CameraUrlCameraInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流URL'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class ModelInfoListProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'array'
        self.columnComplex = [ModelInfoListPropertyColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListPropertyColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListPropertyColumnComplexStruct()
        self.modelName = ModelNameModelInfoListPropertyColumnComplexStruct()
        self.modelUrl = ModelUrlModelInfoListPropertyColumnComplexStruct()
        self.modelFile = ModelFileModelInfoListPropertyColumnComplexStruct()
        self.modelMd5 = ModelMd5ModelInfoListPropertyColumnComplexStruct()
        self.modelFunction = ModelFunctionModelInfoListPropertyColumnComplexStruct()
        self.modelAlgType = ModelAlgTypeModelInfoListPropertyColumnComplexStruct()
        self.targetNameList = TargetNameListModelInfoListPropertyColumnComplexStruct()
        self.updateTime = UpdateTimeModelInfoListPropertyColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'modelName': self.modelName.v, 'modelUrl': self.modelUrl.v, 'modelFile': self.modelFile.v, 'modelMd5': self.modelMd5.v, 'modelFunction': self.modelFunction.v, 'modelAlgType': self.modelAlgType.v, 'targetNameList': self.targetNameList.v, 'updateTime': self.updateTime.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('modelName') is not None: self.modelName.v = value['modelName']
        if value.get('modelUrl') is not None: self.modelUrl.v = value['modelUrl']
        if value.get('modelFile') is not None: self.modelFile.v = value['modelFile']
        if value.get('modelMd5') is not None: self.modelMd5.v = value['modelMd5']
        if value.get('modelFunction') is not None: self.modelFunction.v = value['modelFunction']
        if value.get('modelAlgType') is not None: self.modelAlgType.v = value['modelAlgType']
        if value.get('targetNameList') is not None: self.targetNameList.v = value['targetNameList']
        if value.get('updateTime') is not None: self.updateTime.v = value['updateTime']


class UpdateTimeModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'updateTime'
        self.name = '模型更新时间'
        self.type = 'string'
        self.v: str = ''


class TargetNameListModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetNameList'
        self.name = '识别能力列表'
        self.type = 'array'
        self.columnSimple = [TargetNameListModelInfoListPropertyColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = TargetNameListModelInfoListPropertyColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class TargetNameListModelInfoListPropertyColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelAlgTypeModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelAlgType'
        self.name = '模型类别(ssd、yolo、built-in)'
        self.type = 'string'
        self.v: str = ''


class ModelFunctionModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelFunction'
        self.name = '模型功能(行为识别、目标检测、目标分类)'
        self.type = 'string'
        self.v: str = ''


class ModelMd5ModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelMd5'
        self.name = '模型md5值'
        self.type = 'string'
        self.v: str = ''


class ModelFileModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelFile'
        self.name = '模型存储地址'
        self.type = 'string'
        self.v: str = ''


class ModelUrlModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelUrl'
        self.name = '模型url地址'
        self.type = 'string'
        self.v: str = ''


class ModelNameModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelName'
        self.name = '模型名称'
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型ID'
        self.type = 'string'
        self.v: str = ''


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
        self.name = '状态'
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


class ProductIdProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'productId'
        self.name = '产品ID'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''


class SnProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'sn'
        self.name = '序列号'
        self.accessMode = 'ro'
        self.required = True
        self.type = 'string'
        self.v: str = ''
