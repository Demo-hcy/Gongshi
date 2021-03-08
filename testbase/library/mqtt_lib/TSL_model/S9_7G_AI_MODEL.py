from .base_model import *


class S9_QG_AI(Device):
    def __init__(self, deviceId: str) -> None:
        super().__init__(deviceId)
        self.productId = 'S9_7G_AI'
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
        self.deleteCameraSub = DeleteCameraSubService()
        self.modifyCamera = ModifyCameraService()
        self.queryCameraByCameraId = QueryCameraByCameraIdService()
        self.queryCameraByCameraIdAndModelId = QueryCameraByCameraIdAndModelIdService()
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
        self.name = '查询所有摄像头AI应用'
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
        self.name = '摄像头AI应用列表'
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
        self.name = '模型ID列表'
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
        self.name = '模型实现功能'
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
        self.name = '摄像头url'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListQueryCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class ChannelIdCameraAIListQueryCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelId'
        self.name = '通道id'
        self.type = 'string'
        self.v: str = ''


class QueryCamerAIByCameraIdAndModelIdService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryCamerAIByCameraIdAndModelId'
        self.name = '查询摄像头AI应用模型'
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
        self.name = '摄像头AI应用列表'
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
        self.name = '模型ID列表'
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
        self.name = '模型实现功能'
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
        self.name = '摄像头url'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class ChannelIdCameraAIListQueryCamerAIByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelId'
        self.name = '通道id'
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
        self.name = '摄像头AI应用列表'
        self.type = 'array'
        self.required = True
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
        self.name = '模型ID列表'
        self.type = 'array'
        self.required = True
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
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class QueryCameraAIByCameraIdService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryCameraAIByCameraId'
        self.name = '查询摄像头AI应用'
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
        self.name = '摄像头AI应用列表'
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
        self.name = '模型信息列表'
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
        self.name = '模型实现功能'
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
        self.name = '摄像头url'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class ChannelIdCameraAIListQueryCameraAIByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelId'
        self.name = '通道id'
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
        self.name = '摄像头ID列表'
        self.type = 'array'
        self.required = True
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
        self.name = '删除摄像头AI应用模型'
        self.type = 'management'
        self.parameters = DeleteCameraAISubServiceParameters()
        self.output = [DeleteCameraAISubServiceOutput()]


class DeleteCameraAISubServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraAIList = CameraAIListDeleteCameraAISubServiceOutput()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListDeleteCameraAISubServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraAIList'
        self.name = '摄像头应用信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListDeleteCameraAISubServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListDeleteCameraAISubServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListDeleteCameraAISubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeCameraAIListDeleteCameraAISubServiceOutputColumnComplexStruct()
        self.message = MessageCameraAIListDeleteCameraAISubServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructColumnComplexStruct()
        self.message = MessageModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class CodeModelInfoListCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class MessageCameraAIListDeleteCameraAISubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeCameraAIListDeleteCameraAISubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeCameraAIListDeleteCameraAISubServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.name = '摄像头AI应用列表'
        self.type = 'array'
        self.required = True
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
        self.name = '模型ID列表'
        self.type = 'array'
        self.required = True
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
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class DeleteCameraAIService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'deleteCameraAI'
        self.name = '删除摄像头AI应用'
        self.type = 'management'
        self.parameters = DeleteCameraAIServiceParameters()
        self.output = [DeleteCameraAIServiceOutput()]


class DeleteCameraAIServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraAIList = CameraAIListDeleteCameraAIServiceOutput()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListDeleteCameraAIServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraAIList'
        self.name = '摄像头应用信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListDeleteCameraAIServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListDeleteCameraAIServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListDeleteCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeCameraAIListDeleteCameraAIServiceOutputColumnComplexStruct()
        self.message = MessageCameraAIListDeleteCameraAIServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageCameraAIListDeleteCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeCameraAIListDeleteCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeCameraAIListDeleteCameraAIServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeCameraAIListDeleteCameraAIServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.name = '摄像头ID列表'
        self.type = 'array'
        self.required = True
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
        self.name = '关闭摄像头AI应用模型'
        self.type = 'management'
        self.parameters = CloseCameraAISubServiceParameters()
        self.output = [CloseCameraAISubServiceOutput()]


class CloseCameraAISubServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraAIList = CameraAIListCloseCameraAISubServiceOutput()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListCloseCameraAISubServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraAIList'
        self.name = '摄像头应用信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListCloseCameraAISubServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListCloseCameraAISubServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListCloseCameraAISubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeCameraAIListCloseCameraAISubServiceOutputColumnComplexStruct()
        self.message = MessageCameraAIListCloseCameraAISubServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStructColumnComplexStruct()
        self.message = MessageModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class CodeModelInfoListCameraAIListCloseCameraAISubServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class MessageCameraAIListCloseCameraAISubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeCameraAIListCloseCameraAISubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeCameraAIListCloseCameraAISubServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeCameraAIListCloseCameraAISubServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.name = '摄像头AI应用列表'
        self.type = 'array'
        self.required = True
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
        self.name = '模型ID列表'
        self.type = 'array'
        self.required = True
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
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CloseCameraAIService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'closeCameraAI'
        self.name = '关闭摄像头AI应用'
        self.type = 'management'
        self.parameters = CloseCameraAIServiceParameters()
        self.output = [CloseCameraAIServiceOutput()]


class CloseCameraAIServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraAIList = CameraAIListCloseCameraAIServiceOutput()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListCloseCameraAIServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraAIList'
        self.name = '摄像头应用信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListCloseCameraAIServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListCloseCameraAIServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListCloseCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeCameraAIListCloseCameraAIServiceOutputColumnComplexStruct()
        self.message = MessageCameraAIListCloseCameraAIServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageCameraAIListCloseCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeCameraAIListCloseCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeCameraAIListCloseCameraAIServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeCameraAIListCloseCameraAIServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.name = '摄像头ID列表'
        self.type = 'array'
        self.required = True
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
        self.name = '开启摄像头AI应用'
        self.type = 'management'
        self.parameters = OpenCameraAIServiceParameters()
        self.output = [OpenCameraAIServiceOutput()]


class OpenCameraAIServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraAIList = CameraAIListOpenCameraAIServiceOutput()

    @property
    def v(self):
        return {'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraAIList') is not None: self.cameraAIList.v = value['cameraAIList']


class CameraAIListOpenCameraAIServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraAIList'
        self.name = '摄像头应用信息列表'
        self.type = 'array'
        self.columnComplex = [CameraAIListOpenCameraAIServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraAIListOpenCameraAIServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraAIListOpenCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeCameraAIListOpenCameraAIServiceOutputColumnComplexStruct()
        self.message = MessageCameraAIListOpenCameraAIServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStructColumnComplexStruct()
        self.message = MessageModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class CodeModelInfoListCameraAIListOpenCameraAIServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class MessageCameraAIListOpenCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeCameraAIListOpenCameraAIServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeCameraAIListOpenCameraAIServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeCameraAIListOpenCameraAIServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.name = '摄像头AI应用列表'
        self.type = 'array'
        self.required = True
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
        self.name = '模型信息列表'
        self.type = 'array'
        self.required = True
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
        self.name = '模型实现功能'
        self.type = 'string'
        self.required = True
        self.specs = FunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructSpecs()
        self.v: str = ''


class FunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = FunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructSpecsOptional()


class FunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.Detection = DetectionFunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructSpecsOptional()
        self.Collection = CollectionFunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructSpecsOptional()
        self.DetectandCollect = DetectandCollectFunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructSpecsOptional()


class DetectandCollectFunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'DetectandCollect'
        self.desc = '检测采集'


class CollectionFunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Collection'
        self.desc = '采集'


class DetectionFunctionModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Detection'
        self.desc = '检测'


class DetectionAreaIdListModelInfoListCameraAIListOpenCameraAIServiceParameterColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaIdList'
        self.name = '检测区域ID列表'
        self.type = 'array'
        self.required = True
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
        self.required = True
        self.v: str = ''


class CameraIdCameraAIListOpenCameraAIServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
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
        self.name = '模型信息列表'
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
        self.objList = ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objList': self.objList.v, 'objThreshList': self.objThreshList.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标采集阈值'
        self.type = 'array'
        self.columnSimple = [ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.columnSimple = [ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


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
        self.alarmIntervalList = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfoList = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmIntervalList': self.alarmIntervalList.v, 'objThreshList': self.objThreshList.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfoList': self.detectionAreaInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmIntervalList') is not None: self.alarmIntervalList.v = value['alarmIntervalList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']
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


class ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标上报阈值'
        self.type = 'array'
        self.columnSimple = [ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmIntervalList'
        self.name = '告警间隔'
        self.type = 'array'
        self.columnSimple = [AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'integer'
        self.specs = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: int = 0


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
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


class QueryCameraByCameraIdAndModelIdService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryCameraByCameraIdAndModelId'
        self.name = '查询指定摄像头ID下关联的指定模型配置'
        self.type = 'management'
        self.parameters = QueryCameraByCameraIdAndModelIdServiceParameters()
        self.output = [QueryCameraByCameraIdAndModelIdServiceOutput()]


class QueryCameraByCameraIdAndModelIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraInfoList = CameraInfoListQueryCameraByCameraIdAndModelIdServiceOutput()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListQueryCameraByCameraIdAndModelIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头列表'
        self.type = 'array'
        self.columnComplex = [CameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct()
        self.cameraUrl = CameraUrlCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct()
        self.pushRtsp = PushRtspCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'pushRtsp': self.pushRtsp.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('pushRtsp') is not None: self.pushRtsp.v = value['pushRtsp']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.detectionInfo = DetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.imageCollectInfo = ImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionInfo': self.detectionInfo.v, 'imageCollectInfo': self.imageCollectInfo.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionInfo') is not None: self.detectionInfo.v = value['detectionInfo']
        if value.get('imageCollectInfo') is not None: self.imageCollectInfo.v = value['imageCollectInfo']


class ImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'imageCollectInfo'
        self.name = '图片采集信息'
        self.type = 'struct'
        self.struct = ImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.pushImageAddress = PushImageAddressImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.startTime = StartTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.endTime = EndTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.circulationTime = CirculationTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objList = ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objList': self.objList.v, 'objThreshList': self.objThreshList.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标采集阈值'
        self.type = 'array'
        self.columnSimple = [ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.columnSimple = [ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CirculationTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'circulationTime'
        self.name = '采集时间是否循环'
        self.type = 'boolean'
        self.v: bool = True


class EndTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '采集结束时间'
        self.type = 'string'
        self.v: str = ''


class StartTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '采集开始时间'
        self.type = 'string'
        self.v: str = ''


class PushImageAddressImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageAddress'
        self.name = '图片推送地址'
        self.type = 'string'
        self.v: str = ''


class DetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionInfo'
        self.name = '检测区域检测信息'
        self.type = 'struct'
        self.struct = DetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class DetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.objList = ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.alarmIntervalList = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfoList = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmIntervalList': self.alarmIntervalList.v, 'objThreshList': self.objThreshList.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfoList': self.detectionAreaInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmIntervalList') is not None: self.alarmIntervalList.v = value['alarmIntervalList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']
        if value.get('pushImageFile') is not None: self.pushImageFile.v = value['pushImageFile']
        if value.get('detectionAreaInfoList') is not None: self.detectionAreaInfoList.v = value['detectionAreaInfoList']


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaInfoList'
        self.name = '检测区域信息'
        self.type = 'array'
        self.columnComplex = [DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.regionId = RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()
        self.regionArea = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()

    @property
    def v(self):
        return {'regionId': self.regionId.v, 'regionArea': self.regionArea.v}

    @v.setter
    def v(self, value):
        if value.get('regionId') is not None: self.regionId.v = value['regionId']
        if value.get('regionArea') is not None: self.regionArea.v = value['regionArea']


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionArea'
        self.name = '检测区域面积信息'
        self.type = 'struct'
        self.struct = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.x = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.y = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.w = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.h = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'x': self.x.v, 'y': self.y.v, 'w': self.w.v, 'h': self.h.v}

    @v.setter
    def v(self, value):
        if value.get('x') is not None: self.x.v = value['x']
        if value.get('y') is not None: self.y.v = value['y']
        if value.get('w') is not None: self.w.v = value['w']
        if value.get('h') is not None: self.h.v = value['h']


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'h'
        self.name = '检测区域h'
        self.type = 'number'
        self.specs = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'w'
        self.name = '检测区域w'
        self.type = 'number'
        self.specs = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'y'
        self.name = '检测区域y'
        self.type = 'number'
        self.specs = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'x'
        self.name = '检测区域x'
        self.type = 'number'
        self.specs = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionId'
        self.name = '区域ID'
        self.type = 'string'
        self.v: str = ''


class PushImageFileDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageFile'
        self.name = '识别推送图片地址'
        self.type = 'string'
        self.v: str = ''


class ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标上报阈值'
        self.type = 'array'
        self.columnSimple = [ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmIntervalList'
        self.name = '告警间隔'
        self.type = 'array'
        self.columnSimple = [AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'integer'
        self.specs = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: int = 0


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.columnSimple = [ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class PushRtspCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pushRtsp'
        self.name = '识别推送视频流地址'
        self.type = 'string'
        self.v: str = ''


class CameraUrlCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流URL'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraInfoListQueryCameraByCameraIdAndModelIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class QueryCameraByCameraIdAndModelIdServiceParameters:
    def __init__(self) -> None:
        self.cameraInfoList = CameraInfoListQueryCameraByCameraIdAndModelIdServiceParameter()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListQueryCameraByCameraIdAndModelIdServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头列表'
        self.type = 'array'
        self.required = True
        self.columnComplex = [CameraInfoListQueryCameraByCameraIdAndModelIdServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListQueryCameraByCameraIdAndModelIdServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListQueryCameraByCameraIdAndModelIdServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraInfoListQueryCameraByCameraIdAndModelIdServiceParameterColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '模型ID列表'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceParameterColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceParameterColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ModelInfoListCameraInfoListQueryCameraByCameraIdAndModelIdServiceParameterColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraInfoListQueryCameraByCameraIdAndModelIdServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class QueryCameraByCameraIdService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'queryCameraByCameraId'
        self.name = '根据ID查询摄像头'
        self.type = 'management'
        self.parameters = QueryCameraByCameraIdServiceParameters()
        self.output = [QueryCameraByCameraIdServiceOutput()]


class QueryCameraByCameraIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraInfoList = CameraInfoListQueryCameraByCameraIdServiceOutput()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListQueryCameraByCameraIdServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头列表'
        self.type = 'array'
        self.columnComplex = [CameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct()
        self.cameraUrl = CameraUrlCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct()
        self.pushRtsp = PushRtspCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'cameraUrl': self.cameraUrl.v, 'pushRtsp': self.pushRtsp.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('cameraUrl') is not None: self.cameraUrl.v = value['cameraUrl']
        if value.get('pushRtsp') is not None: self.pushRtsp.v = value['pushRtsp']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.modelId = ModelIdModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.detectionInfo = DetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()
        self.imageCollectInfo = ImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'modelId': self.modelId.v, 'detectionInfo': self.detectionInfo.v, 'imageCollectInfo': self.imageCollectInfo.v}

    @v.setter
    def v(self, value):
        if value.get('modelId') is not None: self.modelId.v = value['modelId']
        if value.get('detectionInfo') is not None: self.detectionInfo.v = value['detectionInfo']
        if value.get('imageCollectInfo') is not None: self.imageCollectInfo.v = value['imageCollectInfo']


class ImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'imageCollectInfo'
        self.name = '图片采集信息'
        self.type = 'struct'
        self.struct = ImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class ImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.pushImageAddress = PushImageAddressImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.startTime = StartTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.endTime = EndTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.circulationTime = CirculationTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objList = ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objList': self.objList.v, 'objThreshList': self.objThreshList.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标采集阈值'
        self.type = 'array'
        self.columnSimple = [ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.columnSimple = [ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CirculationTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'circulationTime'
        self.name = '采集时间是否循环'
        self.type = 'boolean'
        self.v: bool = True


class EndTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '采集结束时间'
        self.type = 'string'
        self.v: str = ''


class StartTimeImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '采集开始时间'
        self.type = 'string'
        self.v: str = ''


class PushImageAddressImageCollectInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageAddress'
        self.name = '图片推送地址'
        self.type = 'string'
        self.v: str = ''


class DetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionInfo'
        self.name = '检测区域检测信息'
        self.type = 'struct'
        self.struct = DetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class DetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.objList = ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.alarmIntervalList = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfoList = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmIntervalList': self.alarmIntervalList.v, 'objThreshList': self.objThreshList.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfoList': self.detectionAreaInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmIntervalList') is not None: self.alarmIntervalList.v = value['alarmIntervalList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']
        if value.get('pushImageFile') is not None: self.pushImageFile.v = value['pushImageFile']
        if value.get('detectionAreaInfoList') is not None: self.detectionAreaInfoList.v = value['detectionAreaInfoList']


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaInfoList'
        self.name = '检测区域信息'
        self.type = 'array'
        self.columnComplex = [DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.regionId = RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()
        self.regionArea = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct()

    @property
    def v(self):
        return {'regionId': self.regionId.v, 'regionArea': self.regionArea.v}

    @v.setter
    def v(self, value):
        if value.get('regionId') is not None: self.regionId.v = value['regionId']
        if value.get('regionArea') is not None: self.regionArea.v = value['regionArea']


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionArea'
        self.name = '检测区域面积信息'
        self.type = 'struct'
        self.struct = RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return self.struct.v

    @v.setter
    def v(self, value):
        self.struct.v = value


class RegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.x = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.y = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.w = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()
        self.h = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'x': self.x.v, 'y': self.y.v, 'w': self.w.v, 'h': self.h.v}

    @v.setter
    def v(self, value):
        if value.get('x') is not None: self.x.v = value['x']
        if value.get('y') is not None: self.y.v = value['y']
        if value.get('w') is not None: self.w.v = value['w']
        if value.get('h') is not None: self.h.v = value['h']


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'h'
        self.name = '检测区域h'
        self.type = 'number'
        self.specs = HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class HRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'w'
        self.name = '检测区域w'
        self.type = 'number'
        self.specs = WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class WRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'y'
        self.name = '检测区域y'
        self.type = 'number'
        self.specs = YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class YRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'x'
        self.name = '检测区域x'
        self.type = 'number'
        self.specs = XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs()
        self.v: float = 0.0


class XRegionAreaDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStructStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class RegionIdDetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'regionId'
        self.name = '区域ID'
        self.type = 'string'
        self.v: str = ''


class PushImageFileDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageFile'
        self.name = '识别推送图片地址'
        self.type = 'string'
        self.v: str = ''


class ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标上报阈值'
        self.type = 'array'
        self.columnSimple = [ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmIntervalList'
        self.name = '告警间隔'
        self.type = 'array'
        self.columnSimple = [AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'integer'
        self.specs = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: int = 0


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.columnSimple = [ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListDetectionInfoModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class ModelIdModelInfoListCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型id'
        self.type = 'string'
        self.v: str = ''


class PushRtspCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pushRtsp'
        self.name = '识别推送视频流地址'
        self.type = 'string'
        self.v: str = ''


class CameraUrlCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流URL'
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraInfoListQueryCameraByCameraIdServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.v: str = ''


class QueryCameraByCameraIdServiceParameters:
    def __init__(self) -> None:
        self.cameraIdList = CameraIdListQueryCameraByCameraIdServiceParameter()

    @property
    def v(self):
        return {'cameraIdList': self.cameraIdList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraIdList') is not None: self.cameraIdList.v = value['cameraIdList']


class CameraIdListQueryCameraByCameraIdServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraIdList'
        self.name = '摄像头ID列表'
        self.type = 'array'
        self.required = True
        self.columnSimple = [CameraIdListQueryCameraByCameraIdServiceParameterColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = CameraIdListQueryCameraByCameraIdServiceParameterColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class CameraIdListQueryCameraByCameraIdServiceParameterColumnSimpleStruct:
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
        self.output = [ModifyCameraServiceOutput()]


class ModifyCameraServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraInfoList = CameraInfoListModifyCameraServiceOutput()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListModifyCameraServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头信息列表'
        self.type = 'array'
        self.columnComplex = [CameraInfoListModifyCameraServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListModifyCameraServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListModifyCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeCameraInfoListModifyCameraServiceOutputColumnComplexStruct()
        self.message = MessageCameraInfoListModifyCameraServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStructColumnComplexStruct()
        self.message = MessageModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class CodeModelInfoListCameraInfoListModifyCameraServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class MessageCameraInfoListModifyCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeCameraInfoListModifyCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeCameraInfoListModifyCameraServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeCameraInfoListModifyCameraServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.required = True
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
        self.name = '模型信息列表'
        self.type = 'array'
        self.required = True
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
        self.objList = ObjListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objList': self.objList.v, 'objThreshList': self.objThreshList.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标采集阈值'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ObjThreshListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class ObjListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ObjListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CirculationTimeImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'circulationTime'
        self.name = '采集时间是否循环'
        self.type = 'boolean'
        self.required = True
        self.v: bool = True


class EndTimeImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '采集结束时间'
        self.type = 'string'
        self.required = True
        self.format = 'date-time'
        self.v: str = ''


class StartTimeImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '采集开始时间'
        self.type = 'string'
        self.required = True
        self.format = 'date-time'
        self.v: str = ''


class PushImageAddressImageCollectInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageAddress'
        self.name = '图片推送地址'
        self.type = 'string'
        self.required = True
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
        self.alarmIntervalList = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfoList = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmIntervalList': self.alarmIntervalList.v, 'objThreshList': self.objThreshList.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfoList': self.detectionAreaInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmIntervalList') is not None: self.alarmIntervalList.v = value['alarmIntervalList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']
        if value.get('pushImageFile') is not None: self.pushImageFile.v = value['pushImageFile']
        if value.get('detectionAreaInfoList') is not None: self.detectionAreaInfoList.v = value['detectionAreaInfoList']


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaInfoList'
        self.name = '检测区域信息'
        self.type = 'array'
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
        self.v: str = ''


class PushImageFileDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageFile'
        self.name = '识别推送图片地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ObjThreshListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标上报阈值'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ObjThreshListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmIntervalList'
        self.name = '告警间隔'
        self.type = 'array'
        self.required = True
        self.columnSimple = [AlarmIntervalListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'integer'
        self.specs = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: int = 0


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjListDetectionInfoModelInfoListCameraInfoListModifyCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.required = True
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
        self.required = True
        self.v: str = ''


class PushRtspCameraInfoListModifyCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pushRtsp'
        self.name = '识别推送视频流地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraIdCameraInfoListModifyCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class DeleteCameraSubService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'deleteCameraSub'
        self.name = '删除摄像头下关联的模型'
        self.type = 'management'
        self.parameters = DeleteCameraSubServiceParameters()
        self.output = [DeleteCameraSubServiceOutput()]


class DeleteCameraSubServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraInfoList = CameraInfoListDeleteCameraSubServiceOutput()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListDeleteCameraSubServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头信息列表'
        self.type = 'array'
        self.columnComplex = [CameraInfoListDeleteCameraSubServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListDeleteCameraSubServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListDeleteCameraSubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeCameraInfoListDeleteCameraSubServiceOutputColumnComplexStruct()
        self.message = MessageCameraInfoListDeleteCameraSubServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructColumnComplexStruct()
        self.message = MessageModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class CodeModelInfoListCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class MessageCameraInfoListDeleteCameraSubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeCameraInfoListDeleteCameraSubServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeCameraInfoListDeleteCameraSubServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class DeleteCameraSubServiceParameters:
    def __init__(self) -> None:
        self.cameraInfoList = CameraInfoListDeleteCameraSubServiceParameter()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListDeleteCameraSubServiceParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头列表'
        self.type = 'array'
        self.required = True
        self.columnComplex = [CameraInfoListDeleteCameraSubServiceParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListDeleteCameraSubServiceParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListDeleteCameraSubServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.cameraId = CameraIdCameraInfoListDeleteCameraSubServiceParameterColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListDeleteCameraSubServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'cameraId': self.cameraId.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraId') is not None: self.cameraId.v = value['cameraId']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListDeleteCameraSubServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '模型ID列表'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ModelInfoListCameraInfoListDeleteCameraSubServiceParameterColumnComplexStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ModelInfoListCameraInfoListDeleteCameraSubServiceParameterColumnComplexStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ModelInfoListCameraInfoListDeleteCameraSubServiceParameterColumnComplexStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CameraIdCameraInfoListDeleteCameraSubServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class DeleteCameraService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'deleteCamera'
        self.name = '删除摄像头'
        self.type = 'management'
        self.parameters = DeleteCameraServiceParameters()
        self.output = [DeleteCameraServiceOutput()]


class DeleteCameraServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraInfoList = CameraInfoListDeleteCameraServiceOutput()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListDeleteCameraServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头信息列表'
        self.type = 'array'
        self.columnComplex = [CameraInfoListDeleteCameraServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListDeleteCameraServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListDeleteCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeCameraInfoListDeleteCameraServiceOutputColumnComplexStruct()
        self.message = MessageCameraInfoListDeleteCameraServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageCameraInfoListDeleteCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeCameraInfoListDeleteCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeCameraInfoListDeleteCameraServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeCameraInfoListDeleteCameraServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.required = True
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
        self.output = [AddCameraServiceOutput()]


class AddCameraServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.cameraInfoList = CameraInfoListAddCameraServiceOutput()

    @property
    def v(self):
        return {'cameraInfoList': self.cameraInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('cameraInfoList') is not None: self.cameraInfoList.v = value['cameraInfoList']


class CameraInfoListAddCameraServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'cameraInfoList'
        self.name = '摄像头信息列表'
        self.type = 'array'
        self.columnComplex = [CameraInfoListAddCameraServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = CameraInfoListAddCameraServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class CameraInfoListAddCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeCameraInfoListAddCameraServiceOutputColumnComplexStruct()
        self.message = MessageCameraInfoListAddCameraServiceOutputColumnComplexStruct()
        self.modelInfoList = ModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v, 'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStructColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStructColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStructColumnComplexStruct()
        self.message = MessageModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStructColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStructColumnComplexStructSpecs()
        self.v: int = 0


class CodeModelInfoListCameraInfoListAddCameraServiceOutputColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class MessageCameraInfoListAddCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeCameraInfoListAddCameraServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeCameraInfoListAddCameraServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeCameraInfoListAddCameraServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.required = True
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
        self.name = '模型信息列表'
        self.type = 'array'
        self.required = True
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
        self.objList = ObjListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objList': self.objList.v, 'objThreshList': self.objThreshList.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标采集阈值'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ObjThreshListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class ObjListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ObjListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CirculationTimeImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'circulationTime'
        self.name = '采集时间是否循环'
        self.type = 'boolean'
        self.required = True
        self.v: bool = True


class EndTimeImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '采集结束时间'
        self.type = 'string'
        self.required = True
        self.format = 'date-time'
        self.v: str = ''


class StartTimeImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '采集开始时间'
        self.type = 'string'
        self.required = True
        self.format = 'date-time'
        self.v: str = ''


class PushImageAddressImageCollectInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageAddress'
        self.name = '图片推送地址'
        self.type = 'string'
        self.required = True
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
        self.alarmIntervalList = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfoList = DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmIntervalList': self.alarmIntervalList.v, 'objThreshList': self.objThreshList.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfoList': self.detectionAreaInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmIntervalList') is not None: self.alarmIntervalList.v = value['alarmIntervalList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']
        if value.get('pushImageFile') is not None: self.pushImageFile.v = value['pushImageFile']
        if value.get('detectionAreaInfoList') is not None: self.detectionAreaInfoList.v = value['detectionAreaInfoList']


class DetectionAreaInfoListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaInfoList'
        self.name = '检测区域信息'
        self.type = 'array'
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
        self.v: str = ''


class PushImageFileDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageFile'
        self.name = '识别推送图片地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ObjThreshListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标上报阈值'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ObjThreshListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmIntervalList'
        self.name = '告警间隔'
        self.type = 'array'
        self.required = True
        self.columnSimple = [AlarmIntervalListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'integer'
        self.specs = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: int = 0


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjListDetectionInfoModelInfoListCameraInfoListAddCameraServiceParameterColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.required = True
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
        self.required = True
        self.v: str = ''


class PushRtspCameraInfoListAddCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pushRtsp'
        self.name = '识别推送视频流地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraUrlCameraInfoListAddCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流URL'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraIdCameraInfoListAddCameraServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
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
        self.name = '模型信息列表'
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
        self.name = '模型信息列表'
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
        self.required = True
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
        self.output = [UpdateModelServiceOutput()]


class UpdateModelServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.modelInfoList = ModelInfoListUpdateModelServiceOutput()

    @property
    def v(self):
        return {'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListUpdateModelServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListUpdateModelServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListUpdateModelServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListUpdateModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeModelInfoListUpdateModelServiceOutputColumnComplexStruct()
        self.message = MessageModelInfoListUpdateModelServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageModelInfoListUpdateModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeModelInfoListUpdateModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeModelInfoListUpdateModelServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeModelInfoListUpdateModelServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.modelSrcId = ModelSrcIdModelInfoListUpdateModelServiceParameterColumnComplexStruct()
        self.modelId = ModelIdModelInfoListUpdateModelServiceParameterColumnComplexStruct()
        self.modelName = ModelNameModelInfoListUpdateModelServiceParameterColumnComplexStruct()
        self.modelUrl = ModelUrlModelInfoListUpdateModelServiceParameterColumnComplexStruct()
        self.modelMd5 = ModelMd5ModelInfoListUpdateModelServiceParameterColumnComplexStruct()
        self.updateTime = UpdateTimeModelInfoListUpdateModelServiceParameterColumnComplexStruct()

    @property
    def v(self):
        return {'modelSrcId': self.modelSrcId.v, 'modelId': self.modelId.v, 'modelName': self.modelName.v, 'modelUrl': self.modelUrl.v, 'modelMd5': self.modelMd5.v, 'updateTime': self.updateTime.v}

    @v.setter
    def v(self, value):
        if value.get('modelSrcId') is not None: self.modelSrcId.v = value['modelSrcId']
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
        self.required = True
        self.format = 'date-time'
        self.v: str = ''


class ModelMd5ModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelMd5'
        self.name = '模型md5值'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelUrlModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelUrl'
        self.name = '模型url地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelNameModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelName'
        self.name = '模型名称'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelIdModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型ID'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelSrcIdModelInfoListUpdateModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelSrcId'
        self.name = '模型原始Id'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class DeleteModelService(BaseService):
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        super().__init__(id, name, parameters, outputs)
        self.id = 'deleteModel'
        self.name = '删除模型'
        self.type = 'management'
        self.parameters = DeleteModelServiceParameters()
        self.output = [DeleteModelServiceOutput()]


class DeleteModelServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.modelInfoList = ModelInfoListDeleteModelServiceOutput()

    @property
    def v(self):
        return {'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListDeleteModelServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListDeleteModelServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListDeleteModelServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListDeleteModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeModelInfoListDeleteModelServiceOutputColumnComplexStruct()
        self.message = MessageModelInfoListDeleteModelServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageModelInfoListDeleteModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeModelInfoListDeleteModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeModelInfoListDeleteModelServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeModelInfoListDeleteModelServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.required = True
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
        self.output = [AddModelServiceOutput()]


class AddModelServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.modelInfoList = ModelInfoListAddModelServiceOutput()

    @property
    def v(self):
        return {'modelInfoList': self.modelInfoList.v}

    @v.setter
    def v(self, value):
        if value.get('modelInfoList') is not None: self.modelInfoList.v = value['modelInfoList']


class ModelInfoListAddModelServiceOutput(BaseOutput):
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        super().__init__(id, name, type, specs)
        self.id = 'modelInfoList'
        self.name = '模型信息列表'
        self.type = 'array'
        self.columnComplex = [ModelInfoListAddModelServiceOutputColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = ModelInfoListAddModelServiceOutputColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class ModelInfoListAddModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.code = CodeModelInfoListAddModelServiceOutputColumnComplexStruct()
        self.message = MessageModelInfoListAddModelServiceOutputColumnComplexStruct()

    @property
    def v(self):
        return {'code': self.code.v, 'message': self.message.v}

    @v.setter
    def v(self, value):
        if value.get('code') is not None: self.code.v = value['code']
        if value.get('message') is not None: self.message.v = value['message']


class MessageModelInfoListAddModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'message'
        self.name = '状态描述'
        self.type = 'string'
        self.v: str = ''


class CodeModelInfoListAddModelServiceOutputColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'code'
        self.name = '返回状态码'
        self.type = 'integer'
        self.specs = CodeModelInfoListAddModelServiceOutputColumnComplexStructSpecs()
        self.v: int = 0


class CodeModelInfoListAddModelServiceOutputColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


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
        self.required = True
        self.format = 'date-time'
        self.v: str = ''


class ModelMd5ModelInfoListAddModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelMd5'
        self.name = '模型md5值'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelUrlModelInfoListAddModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelUrl'
        self.name = '模型url地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelNameModelInfoListAddModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelName'
        self.name = '模型名称'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelIdModelInfoListAddModelServiceParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型ID'
        self.type = 'string'
        self.required = True
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
        self.targetDetetctAlarm = TargetDetetctAlarmEvent()
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
        self.required = True
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
        self.required = True
        self.v: str = ''


class CameraIdCamerIdListCameraAbnormalEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
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
        self.required = True
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
        self.required = True
        self.specs = SimilarityAlarmListTargetIdentifyAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class SimilarityAlarmListTargetIdentifyAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class TargetUuidAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetUuid'
        self.name = '样本特征值对应的uuid'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class TargetEigenvaluesAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetEigenvalues'
        self.name = '识别目标特征值'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ClassNameAlarmListTargetIdentifyAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'className'
        self.name = '识别类型名称'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelFunctionTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelFunction'
        self.name = '模型功能'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelIdTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelId'
        self.name = '模型Id'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ImagePathTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '告警图片智盒路径'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class StorageUrlTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'storageUrl'
        self.name = '告警视频存储URL'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraUrlTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraUrl'
        self.name = '摄像头url'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraIdTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraId'
        self.name = '摄像头Id'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ChannelIdTargetIdentifyAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channelId'
        self.name = '通道id'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class TargetDetetctAlarmEvent(BaseEvent):
    def __init__(self, id=None, name=None, parameters=None) -> None:
        super().__init__(id, name, parameters)
        self.id = 'targetDetetctAlarm'
        self.name = '目标检测告警'
        self.parameters = TargetDetetctAlarmEventParameters()


class TargetDetetctAlarmEventParameters:
    def __init__(self) -> None:
        self.channelId = ChannelIdTargetDetetctAlarmEventParameter()
        self.cameraId = CameraIdTargetDetetctAlarmEventParameter()
        self.cameraUrl = CameraUrlTargetDetetctAlarmEventParameter()
        self.storageUrl = StorageUrlTargetDetetctAlarmEventParameter()
        self.imagePath = ImagePathTargetDetetctAlarmEventParameter()
        self.modelId = ModelIdTargetDetetctAlarmEventParameter()
        self.modelFunction = ModelFunctionTargetDetetctAlarmEventParameter()
        self.alarmList = AlarmListTargetDetetctAlarmEventParameter()

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


class AlarmListTargetDetetctAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'alarmList'
        self.name = '告警列表信息'
        self.type = 'array'
        self.required = True
        self.columnComplex = [AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnComplex]

    @v.setter
    def v(self, value):
        self.columnComplex = []
        for val in value:
            x = AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()
            x.v = val
            self.columnComplex.append(x)


class AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.className = ClassNameAlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()
        self.objectId = ObjectIdAlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()
        self.X1 = X1AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()
        self.Y1 = Y1AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()
        self.X2 = X2AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()
        self.Y2 = Y2AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()
        self.targetEigenvalues = TargetEigenvaluesAlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()
        self.targetUuid = TargetUuidAlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()
        self.similarity = SimilarityAlarmListTargetDetetctAlarmEventParameterColumnComplexStruct()

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


class SimilarityAlarmListTargetDetetctAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'similarity'
        self.name = '目标相似度'
        self.type = 'number'
        self.required = True
        self.specs = SimilarityAlarmListTargetDetetctAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class SimilarityAlarmListTargetDetetctAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class TargetUuidAlarmListTargetDetetctAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetUuid'
        self.name = '样本特征值对应的uuid'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class TargetEigenvaluesAlarmListTargetDetetctAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetEigenvalues'
        self.name = '识别目标特征值'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class Y2AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'Y2'
        self.name = '目标右下角Y坐标'
        self.type = 'number'
        self.required = True
        self.specs = Y2AlarmListTargetDetetctAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class Y2AlarmListTargetDetetctAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class X2AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'X2'
        self.name = '目标右下角X坐标'
        self.type = 'number'
        self.required = True
        self.specs = X2AlarmListTargetDetetctAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class X2AlarmListTargetDetetctAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class Y1AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'Y1'
        self.name = '目标左上角Y坐标'
        self.type = 'number'
        self.required = True
        self.specs = Y1AlarmListTargetDetetctAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class Y1AlarmListTargetDetetctAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class X1AlarmListTargetDetetctAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'X1'
        self.name = '目标左上角X坐标'
        self.type = 'number'
        self.required = True
        self.specs = X1AlarmListTargetDetetctAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class X1AlarmListTargetDetetctAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjectIdAlarmListTargetDetetctAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'objectId'
        self.name = '目标跟踪Id'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ClassNameAlarmListTargetDetetctAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'className'
        self.name = '识别类型名称'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelFunctionTargetDetetctAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelFunction'
        self.name = '模型功能'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelIdTargetDetetctAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelId'
        self.name = '模型Id'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ImagePathTargetDetetctAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '告警图片智盒路径'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class StorageUrlTargetDetetctAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'storageUrl'
        self.name = '告警视频存储URL'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraUrlTargetDetetctAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraUrl'
        self.name = '摄像头url'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraIdTargetDetetctAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraId'
        self.name = '摄像头Id'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ChannelIdTargetDetetctAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channelId'
        self.name = '通道id'
        self.type = 'string'
        self.required = True
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
        self.required = True
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
        self.required = True
        self.specs = SimilarityAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStructSpecs()
        self.v: float = 0.0


class SimilarityAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class EndTimeAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '行为结束时间'
        self.type = 'string'
        self.required = True
        self.format = 'date-time'
        self.v: str = ''


class StartTimeAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '行为开始时间'
        self.type = 'string'
        self.required = True
        self.format = 'date-time'
        self.v: str = ''


class ClassNameAlarmListBehaviorDetetcAlarmEventParameterColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'className'
        self.name = '识别类型名称'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelFunctionBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelFunction'
        self.name = '模型功能'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelIdBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'modelId'
        self.name = '模型Id'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ImagePathBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'imagePath'
        self.name = '告警图片地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class StorageUrlBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'storageUrl'
        self.name = '告警视频存储URL'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraUrlBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraUrl'
        self.name = '摄像头url'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraIdBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'cameraId'
        self.name = '摄像头Id'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ChannelIdBehaviorDetetcAlarmEventParameter(BaseParameter):
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, type, required, specs)
        self.id = 'channelId'
        self.name = '通道id'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class Properties:
    def __init__(self) -> None:
        self.sn = SnProperty()
        self.model = ModelProperty()
        self.productId = ProductIdProperty()
        self.online = OnlineProperty()
        self.mode = ModeProperty()
        self.modelInfoList = ModelInfoListProperty()
        self.cameraInfoList = CameraInfoListProperty()
        self.cameraAIList = CameraAIListProperty()

    @property
    def v(self):
        return {'sn': self.sn.v, 'model': self.model.v, 'productId': self.productId.v, 'online': self.online.v, 'mode': self.mode.v, 'modelInfoList': self.modelInfoList.v, 'cameraInfoList': self.cameraInfoList.v, 'cameraAIList': self.cameraAIList.v}

    @v.setter
    def v(self, value):
        if value.get('sn') is not None: self.sn.v = value['sn']
        if value.get('model') is not None: self.model.v = value['model']
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
        self.name = '摄像头AI应用列表'
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
        self.name = '模型信息列表'
        self.type = 'array'
        self.required = True
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
        self.required = True
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
        self.name = '模型实现功能'
        self.type = 'string'
        self.required = True
        self.specs = FunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecs()
        self.v: str = ''


class FunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = FunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class FunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.Detection = DetectionFunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.Collection = CollectionFunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional()
        self.DetectandCollect = DetectandCollectFunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional()


class DetectandCollectFunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'DetectandCollect'
        self.desc = '检测采集'


class CollectionFunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Collection'
        self.desc = '采集'


class DetectionFunctionModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'Detection'
        self.desc = '检测'


class DetectionAreaIdListModelInfoListCameraAIListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaIdList'
        self.name = '检测区域ID列表'
        self.type = 'array'
        self.required = True
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
        self.required = True
        self.v: str = ''


class CameraUrlCameraAIListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头URL'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraIdCameraAIListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ChannelIdCameraAIListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'channelId'
        self.name = '通道id'
        self.type = 'string'
        self.required = True
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
        self.name = '模型信息列表'
        self.type = 'array'
        self.required = True
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
        self.required = True
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
        self.objList = ObjListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'pushImageAddress': self.pushImageAddress.v, 'startTime': self.startTime.v, 'endTime': self.endTime.v, 'circulationTime': self.circulationTime.v, 'objList': self.objList.v, 'objThreshList': self.objThreshList.v}

    @v.setter
    def v(self, value):
        if value.get('pushImageAddress') is not None: self.pushImageAddress.v = value['pushImageAddress']
        if value.get('startTime') is not None: self.startTime.v = value['startTime']
        if value.get('endTime') is not None: self.endTime.v = value['endTime']
        if value.get('circulationTime') is not None: self.circulationTime.v = value['circulationTime']
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标上报阈值'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ObjThreshListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class ObjListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ObjListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjListImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'string'
        self.v: str = ''


class CirculationTimeImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'circulationTime'
        self.name = '采集时间是否循环'
        self.type = 'boolean'
        self.required = True
        self.v: bool = True


class EndTimeImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'endTime'
        self.name = '采集结束时间'
        self.type = 'string'
        self.required = True
        self.format = 'date-time'
        self.v: str = ''


class StartTimeImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'startTime'
        self.name = '采集开始时间'
        self.type = 'string'
        self.required = True
        self.format = 'date-time'
        self.v: str = ''


class PushImageAddressImageCollectInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageAddress'
        self.name = '图片推送地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class DetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'detectionInfo'
        self.name = '检测区域检测信息'
        self.type = 'struct'
        self.required = True
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
        self.alarmIntervalList = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.objThreshList = ObjThreshListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.pushImageFile = PushImageFileDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()
        self.detectionAreaInfo = DetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct()

    @property
    def v(self):
        return {'objList': self.objList.v, 'alarmIntervalList': self.alarmIntervalList.v, 'objThreshList': self.objThreshList.v, 'pushImageFile': self.pushImageFile.v, 'detectionAreaInfo': self.detectionAreaInfo.v}

    @v.setter
    def v(self, value):
        if value.get('objList') is not None: self.objList.v = value['objList']
        if value.get('alarmIntervalList') is not None: self.alarmIntervalList.v = value['alarmIntervalList']
        if value.get('objThreshList') is not None: self.objThreshList.v = value['objThreshList']
        if value.get('pushImageFile') is not None: self.pushImageFile.v = value['pushImageFile']
        if value.get('detectionAreaInfo') is not None: self.detectionAreaInfo.v = value['detectionAreaInfo']


class DetectionAreaInfoDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'detectionAreaInfo'
        self.name = '检测区域信息'
        self.type = 'array'
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
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
        self.required = True
        self.v: str = ''


class PushImageFileDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'pushImageFile'
        self.name = '识别推送图片地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ObjThreshListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objThreshList'
        self.name = '目标上报阈值'
        self.type = 'array'
        self.required = True
        self.columnSimple = [ObjThreshListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = ObjThreshListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class ObjThreshListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'number'
        self.specs = ObjThreshListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: float = 0.0


class ObjThreshListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 100


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'alarmIntervalList'
        self.name = '告警间隔'
        self.type = 'array'
        self.required = True
        self.columnSimple = [AlarmIntervalListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct()]

    @property
    def v(self):
        return [complex_data.v for complex_data in self.columnSimple]

    @v.setter
    def v(self, value):
        self.columnSimple = []
        for val in value:
            x = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct()
            x.v = val
            self.columnSimple.append(x)


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStruct:
    def __init__(self) -> None:
        self.type = 'integer'
        self.specs = AlarmIntervalListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs()
        self.v: int = 0


class AlarmIntervalListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStructColumnSimpleStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.min = 0
        self.max = 999999


class ObjListDetectionInfoModelInfoListCameraInfoListPropertyColumnComplexStructColumnComplexStructStruct:
    def __init__(self) -> None:
        self.id = 'objList'
        self.name = '目标列表'
        self.type = 'array'
        self.required = True
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
        self.required = True
        self.v: str = ''


class PushRtspCameraInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'pushRtsp'
        self.name = '识别推送视频流地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraUrlCameraInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraUrl'
        self.name = '摄像头视频流URL'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class CameraIdCameraInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'cameraId'
        self.name = '摄像头ID'
        self.type = 'string'
        self.required = True
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
        self.format = 'date-time'
        self.required = True
        self.v: str = ''


class TargetNameListModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'targetNameList'
        self.name = '识别能力列表'
        self.type = 'array'
        self.required = True
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
        self.required = True
        self.v: str = ''


class ModelFunctionModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelFunction'
        self.name = '模型功能(行为识别、目标检测、目标分类)'
        self.type = 'string'
        self.required = True
        self.specs = ModelFunctionModelInfoListPropertyColumnComplexStructSpecs()
        self.v: str = ''


class ModelFunctionModelInfoListPropertyColumnComplexStructSpecs(BaseSpecs):
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        super().__init__(min, max, unit, unitName, step, optional)
        self.optional = ModelFunctionModelInfoListPropertyColumnComplexStructSpecsOptional()


class ModelFunctionModelInfoListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.behaviorDetetct = BehaviorDetetctModelFunctionModelInfoListPropertyColumnComplexStructSpecsOptional()
        self.targetDetetct = TargetDetetctModelFunctionModelInfoListPropertyColumnComplexStructSpecsOptional()
        self.targetIdentify = TargetIdentifyModelFunctionModelInfoListPropertyColumnComplexStructSpecsOptional()


class TargetIdentifyModelFunctionModelInfoListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'targetIdentify'
        self.desc = '目标分类'


class TargetDetetctModelFunctionModelInfoListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'targetDetetct'
        self.desc = '目标检测'


class BehaviorDetetctModelFunctionModelInfoListPropertyColumnComplexStructSpecsOptional(BaseOptional):
    def __init__(self, value=None, desc=None) -> None:
        super().__init__(value, desc)
        self.value = 'behaviorDetetct'
        self.desc = '行为识别'


class ModelMd5ModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelMd5'
        self.name = '模型md5值'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelFileModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelFile'
        self.name = '模型存储地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelUrlModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelUrl'
        self.name = '模型url地址'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelNameModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelName'
        self.name = '模型名称'
        self.type = 'string'
        self.required = True
        self.v: str = ''


class ModelIdModelInfoListPropertyColumnComplexStruct:
    def __init__(self) -> None:
        self.id = 'modelId'
        self.name = '模型ID'
        self.type = 'string'
        self.required = True
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


class ModelProperty(BaseProperty):
    def __init__(self, id=None, name=None, accessMode=None, type=None, required=None, specs=None) -> None:
        super().__init__(id, name, accessMode, type, required, specs)
        self.id = 'model'
        self.name = 'AI设备型号'
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
