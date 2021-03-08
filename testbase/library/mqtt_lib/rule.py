from ..common import *
from .TSL_model.base_model import *


class DeviceInfo:
    def __init__(self, device: Device) -> None:
        """
        设备信息的基类，包含产品ID和设备ID
        :param device: 设备的物模型
        """
        self.productId = device.productId
        self.devId = device.deviceId

    def __repr__(self) -> str:
        return f'{self.productId}.{self.devId}'


class RefProperty(DeviceInfo):
    def __init__(self, device: Device, property: str, more_str: str = None) -> None:
        """
        对属性取值，基于设备信息类
        :param device: 设备的物模型
        :param property: 需提前由get_var_name()获取到属性物模型名称再传入
        :param more_str: 前置额外字符串
        """
        super().__init__(device)
        self.more_str = more_str
        self.property = property.split('.properties.')[1]
        self.property = self.property.replace('.columnComplex', '')
        self.property = self.property.replace('.columnSimple', '')

    def __repr__(self) -> str:
        device_info = super().__repr__()
        if self.more_str:
            s = f'\'{self.more_str}\' + #ref("{device_info}.properties.{self.property}")'
        else:
            s = f'#ref("{device_info}.properties.{self.property}")'
        return s


class RefEvent(DeviceInfo):
    def __init__(self, device: Device, event: str, more_str: str = None) -> None:
        """
        对事件取值，基于设备信息类
        :param device: 设备的物模型
        :param event: 需提前由get_var_name()获取到事件物模型名称再传入
        :param more_str: 前置额外字符串
        """
        super().__init__(device)
        self.more_str = more_str
        self.event = event.split('.events.')[1]
        self.event = self.event.replace('.parameters.', '.')

    def __repr__(self) -> str:
        device_info = super().__repr__()
        if self.more_str:
            s = f'\'{self.more_str}\' + #ref("{device_info}.events.{self.event}")'
        else:
            s = f'#ref("{device_info}.events.{self.event}")'
        return s


class CallService(DeviceInfo):
    def __init__(self, device: Device, service: str, duration: int, param: Dict) -> None:
        """
        调用服务，基于设备信息类
        :param device: 设备的物模型
        :param service: 需提前由get_var_name()获取到服务物模型名称再传入
        :param duration: 服务调用持续时长，单位：秒，0表示持续执行
        :param param: 服务的参数字典，
        简单类型：key为参数物模型，value为对应数据类型的值，
        复杂类型：暂未处理
        """
        super().__init__(device)
        self.service = service.split('.services.')[1]
        self.duration = duration
        self.param = param

    def __repr__(self) -> str:
        device_info = super().__repr__()
        l = []
        for k, v in self.param.items():
            if isinstance(k, (BaseParameter, BaseProperty, BaseOutput)):
                k = k.id
            l.append(f'{k}={self.val_handler(v)}')
        param = ', '.join(l)
        return f'#call_service("{device_info}.services.{self.service}", duration={self.duration}, {param});\n'

    @staticmethod
    def val_handler(val):
        """
        值处理函数，将字符串类型的值添加"号
        :param val: 初始值
        :return: 返回处理后的值
        """
        if isinstance(val, str):
            return '"' + val + '"'
        else:
            return val


class Src(DeviceInfo):
    def __init__(self, device: Device) -> None:
        """
        源设备，基于设备信息类
        :param device: 设备的物模型
        """
        super().__init__(device)

    def __repr__(self) -> str:
        return '{' + f'\\"productId\\": \\"{self.productId}\\", \\"deviceId\\": \\"{self.devId}\\"' + '}'


class RaiseEvent:
    def __init__(self, event: str, srcList: List[Src]) -> None:
        """
        产生事件
        :param event: 此事件ID为平台自定义事件ID，非设备物模型中定义的事件ID
        :param srcList: 源设备列表
        """
        self.event = event
        self.srcList = srcList

    def __repr__(self) -> str:
        srcList = ', '.join([src.__repr__() for src in self.srcList])
        return f'#raise_event("{self.event}", srcList="[{srcList}]");\n'


class Duration(DeviceInfo):
    def __init__(self, device: Device, event: str) -> None:
        """
        某事件触发持续时间，单位：秒，基于设备信息类
        :param device: 设备的物模型
        :param event: 需提前由get_var_name()获取到事件物模型名称再传入
        """
        super().__init__(device)
        self.event = event.split('.events.')[1]

    def __repr__(self) -> str:
        device_info = super().__repr__()
        return f'#duration("{device_info}.events.{self.event}")'


class Condition:
    def __init__(self, param1: Union[RefProperty, RefEvent, Duration], operator: str, param2) -> None:
        """
        条件
        :param param1: 某个属性或事件的取值
        :param operator: 比较运算符
        :param param2: 比较的值
        """
        self.param1 = param1
        self.operator = operator
        self.param2 = param2

    def __repr__(self) -> str:
        return f'{str(self.param1)} {self.operator} {self.val_handler(self.param2)}'

    @staticmethod
    def val_handler(val):
        """
        值处理函数，将字符串类型的值添加"号
        :param val: 初始值
        :return: 返回处理后的值
        """
        if isinstance(val, str):
            return f'"{val}"'
        else:
            return val


class Script:
    def __init__(self, conditions: List = None, if_block: List = None, else_block: List = None) -> None:
        """
        策略
        :param conditions: 条件列表
        :param if_block: *不可为空*，满足条件后的动作，包括调用服务和产生事件
        :param else_block: 不满足条件后的动作，包括调用服务和产生事件
        """
        if not if_block:
            raise ValueError('if_block不可为空')
        self.conditions = conditions
        self.if_block = if_block
        self.else_block = else_block

    def __repr__(self) -> str:
        if self.conditions:
            conditions = ' '.join([f'{x}' for x in self.conditions])
        else:
            conditions = ''
        if self.if_block:
            if_block = '    '.join([f'{x}' for x in self.if_block])
        else:
            if_block = ''
        if self.else_block:
            else_block = '    '.join([f'{x}' for x in self.else_block])
            else_str = f' else {{\n    {else_block}}}'
        else:
            else_str = ''
        if conditions:
            result = f'if ({conditions}) {{\n    {if_block}}}{else_str}'
        else:
            result = ''.join([f'{x}' for x in self.if_block])
        return result


class RuleDate(Dict):
    def __init__(self, start: str, end: str) -> None:
        super().__init__()
        self['startDate'] = start
        self['endDate'] = end


class RuleTime(Dict):
    def __init__(self, start: str, end: str) -> None:
        super().__init__()
        self['startTime'] = start
        self['endTime'] = end


class _Rule(Dict):
    def __init__(self, uuid: str, enable: bool, priority: int, date: List[RuleDate], time: List[RuleTime],
                 src: List[Device], dst: List[Device], script: Script) -> None:
        super().__init__()
        self['uuid'] = uuid
        self['enable'] = enable
        self['type'] = 'linkage'
        self['priority'] = priority
        self['date'] = date
        self['time'] = time
        self['srcDevice'] = [x.deviceId for x in src]
        self['dstDevice'] = [x.deviceId for x in dst]
        self['script'] = str(script)


class LinkageRule(_Rule):
    def __init__(self, uuid: str, enable: bool, priority: int, date: List[RuleDate], time: List[RuleTime],
                 src: List[Device], dst: List[Device], script: Script) -> None:
        super().__init__(uuid, enable, priority, date, time, src, dst, script)
        self['type'] = 'linkage'


class TimerRule(_Rule):
    def __init__(self, uuid: str, enable: bool, priority: int, date: List[RuleDate], time: List[RuleTime],
                 src: List[Device], dst: List[Device], script: Script) -> None:
        super().__init__(uuid, enable, priority, date, time, src, dst, script)
        self['type'] = 'timer'


class Rules(Dict):
    def __init__(self, rule_list: List) -> None:
        super().__init__()
        self['rules'] = rule_list


class OutsideLinkageService(Dict):
    def __init__(self, uuid: str, priority: int, script: Script) -> None:
        super().__init__()
        self['uuid'] = uuid
        self['priority'] = priority
        self['script'] = str(script)


class OutsideLinkageServices(Dict):
    def __init__(self, outside_linkage_service_list: List) -> None:
        super().__init__()
        self['services'] = outside_linkage_service_list


class ManualControlService(Dict):
    def __init__(self, priority: int, script: Script) -> None:
        super().__init__()
        self['priority'] = priority
        self['script'] = str(script)


class ManualControlServices(Dict):
    def __init__(self, manual_control_service_list: List) -> None:
        super().__init__()
        self['services'] = manual_control_service_list