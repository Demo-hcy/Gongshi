from ...common import *


class Product:
    def __init__(self, productId=None, productName=None, properties=None, events=None, services=None) -> None:
        self.productId = productId
        self.productName = productName
        self.properties = properties
        self.events = events
        self.services = services


class Device(Product):
    def __init__(self, deviceId=None) -> None:
        self.deviceId = deviceId


class BaseEvent:
    def __init__(self, id=None, name=None, parameters=None) -> None:
        self.id = id
        self.name = name
        self.parameters = parameters


class BaseService:
    def __init__(self, id=None, name=None, parameters=None, outputs=None) -> None:
        self.id = id
        self.name = name
        self.parameters = parameters
        self.outputs = outputs


class BaseParameter:
    def __init__(self, id=None, name=None, type=None, required=None, specs=None) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.required = required
        self.specs = specs
        self.v: Any

    def build_value(self) -> Any:
        """
        生成符合规则的值
        - 目前支持integer、number、string、boolean类型
        - 暂时不支持struct、array类型
        :return: 返回生成的值
        """
        if self.type in ('integer', 'number'):
            if hasattr(self.specs, 'min'):
                min_val = self.specs.min
            else:
                min_val = 0
            if hasattr(self.specs, 'step'):
                step_val = self.specs.step
            else:
                step_val = 1
            result = min_val + step_val
            if hasattr(self.specs, 'optional'):
                o_list = dir(self.specs.optional)
                result = getattr(o_list[0]).value
            return result
        elif self.type == 'string':
            if hasattr(self.specs, 'optional'):
                o_list = dir(self.specs.optional)
                result = getattr(o_list[0]).value
            else:
                result = ''
            return result
        elif self.type == 'boolean':
            if hasattr(self.specs, 'optional'):
                o_list = dir(self.specs.optional)
                result = getattr(o_list[0]).value
            else:
                result = True
            return result
        else:
            raise ValueError('暂未支持结构体和数组类型')


class BaseOutput():
    def __init__(self, id=None, name=None, type=None, specs=None) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.specs = specs


class BaseSpecs:
    def __init__(self, min=None, max=None, unit=None, unitName=None, step=None, optional=None) -> None:
        self.min = min
        self.max = max
        self.unit = unit
        self.unitName = unitName
        self.step = step
        self.optional = optional


class BaseOptional:
    def __init__(self, value=None, desc=None) -> None:
        self.value = value
        self.desc = desc


class BaseProperty():
    def __init__(self, id=None, name=None, accessMode=None, required=None, type=None, specs=None) -> None:
        self.id = id
        self.name = name
        self.accessMode = accessMode
        self.type = type
        self.required = required
        self.specs = specs
        self.v: Any
