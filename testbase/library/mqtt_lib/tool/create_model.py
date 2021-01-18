from library.common import *
from jsonschema import validate, draft7_format_checker
from jsonschema.exceptions import SchemaError, ValidationError
from library.mqtt_lib.TSL_model import base_model
import json

_sub_classes = {}


def json_validate(schema_file: Path, json_file: Path) -> bool:
    """
    通过schema.json对json文件进行校验
    :param schema_file: 用于校验的json模板文件
    :param json_file: 需要校验的json文件
    :return: 返回是否校验通过
    """
    try:
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema = json.load(f)
        with open(json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        validate(instance=json_data, schema=schema, format_checker=draft7_format_checker)
    except SchemaError as e:
        error_path = ' --> '.join([i for i in e.path])
        logger_error_debug(f'{json_file.name} 验证模式schema出错：\n出错位置：{error_path}\n提示信息：{e.message}')
        return False
    except ValidationError as e:
        error_path = ' --> '.join([i for i in e.path])
        logger_error_debug(f'{json_file.name} 不符合schema规定：\n出错字段：{error_path}\n提示信息：{e.message}')
        return False
    else:
        logger.info(f'{json_file.name} 验证成功！')
        return True


def create_model(src: Dict) -> str:
    """
    由各个设备物模型json文件转换的dict生成对应的class模型字符串
    可以再保存到py文件中，方便调用
    :param src: 物模型json文件转换的dict
    :return: 返回模型字符串
    """
    result = 'from .base_model import *\n'
    result += create_class(class_name=str_format(src['productId']),
                           attrs=src,
                           parent_name='Device',
                           init_param='deviceId: str')
    while True:
        if not _sub_classes:
            break
        sub_class = _sub_classes.popitem()
        result += create_class(class_name=sub_class[0], attrs=sub_class[1])
    return result


def create_class(class_name: str, attrs: Union[Dict, List], parent_name: str = '', init_param: str = '') -> str:
    """
    由dict或list内容生成class，每个元素是class中的一个对象属性
    :param class_name: 要生成的class的名称
    :param attrs: 需生成的属性内容
    :param parent_name: 来源的名称
    :param init_param: 初始化参数
    :return: 返回生成的class的字符串
    """
    base = ('Property', 'Service', 'Event', 'Parameter', 'Output', 'Specs', 'Optional')
    base_model_name = ''
    if parent_name and init_param:
        base_model_name = parent_name
        result = f'\n\nclass {class_name}({base_model_name}):\n'
        super_init_param = init_param[:init_param.rfind(':')]
        init_param = f'self, {init_param}'
        super_str = f'        super().__init__({super_init_param})\n'
    elif class_name.endswith(base):
        base_model_name = 'Base' + get_ends(class_name, base)
        result = f'\n\nclass {class_name}({base_model_name}):\n'
        base_cls = getattr(base_model, base_model_name)
        params = vars(base_cls())
        init_param_str = ', '.join([x + '=None' for x in params])
        init_param = f'self, {init_param_str}'
        super_param = ', '.join(params)
        super_str = f'        super().__init__({super_param})\n'
    else:
        result = f'\n\nclass {class_name}:\n'
        init_param = 'self'
        super_str = ''
    result += f'    def __init__({init_param}) -> None:\n'
    result += super_str
    if attrs:
        attr_list = create_attr_list(attrs, class_name)
        self_v_get = '\n'
        self_v_get += '    @property\n'
        self_v_get += '    def v(self):\n'
        self_v_set = '\n'
        self_v_set += '    @v.setter\n'
        self_v_set += '    def v(self, value):\n'

        self_v = ''
        for attr in attr_list:
            if 'self.columnSimple' in attr:
                self_v += self_v_get
                self_v += '        return [complex_data.v for complex_data in self.columnSimple]\n'
                self_v += self_v_set
                self_v += '        self.columnSimple = []\n'
                self_v += '        for val in value:\n'
                self_v += f'            x = {attr[attr.find("[")+1:-1]}\n'
                self_v += '            x.v = val\n'
                self_v += '            self.columnSimple.append(x)\n'
            elif 'self.columnComplex' in attr:
                self_v += self_v_get
                self_v += '        return [complex_data.v for complex_data in self.columnComplex]\n'
                self_v += self_v_set
                self_v += '        self.columnComplex = []\n'
                self_v += '        for val in value:\n'
                self_v += f'            x = {attr[attr.find("[")+1:-1]}\n'
                self_v += '            x.v = val\n'
                self_v += '            self.columnComplex.append(x)\n'
            elif "self.type = 'struct'" in attr:
                self_v += self_v_get
                self_v += '        return self.struct.v\n'
                self_v += self_v_set
                self_v += '        self.struct.v = value\n'
            elif "self.type = 'boolean'" in attr:
                self_v = '        self.v: bool = True\n'
            elif "self.type = 'integer'" in attr:
                self_v = '        self.v: int = 0\n'
            elif "self.type = 'number'" in attr:
                self_v = '        self.v: float = 0.0\n'
            elif "self.type = 'string'" in attr:
                self_v = "        self.v: str = ''\n"
        c1 = base_model_name not in ('BaseSpecs', 'BaseOptional', 'BaseService', 'BaseEvent', 'Device')
        c2 = class_name not in ('Services', 'Events')
        if not self_v and c1 and c2:
            attrs_name = [attr[attr.find('.') + 1:attr.find(' =')] for attr in attr_list]
            attrs_v = [f"'{attr_name}': self.{attr_name}.v" for attr_name in attrs_name]
            attrs_v = ', '.join(attrs_v)
            attrs_v = '{%s}' % attrs_v
            self_v += self_v_get
            self_v += f'        return {attrs_v}\n'
            self_v += self_v_set
            attrs_v = [
                f"        if value.get('{attr_name}') is not None: self.{attr_name}.v = value['{attr_name}']\n"
                for attr_name in attrs_name
            ]
            attrs_v = ''.join(attrs_v)
            self_v += attrs_v
        attr_list.append(self_v)
        result += '\n'.join(attr_list)
    else:
        result += '        pass'
    return result


def create_attr_list(attrs: Union[Dict, List], class_name: str) -> List:
    """
    由dict或list生成对象属性列表
    :param attrs: 需生成的属性内容
    :param class_name: 所属的class名称
    :return: 返回生成的对象属性列表字符串
    """
    result = []
    if isinstance(attrs, dict):
        for k, v in attrs.items():
            attr_name = str_format(k, False)
            if isinstance(v, list):
                if v == [{}] or len(v) == 0:
                    result.append(f'        self.{attr_name} = None')
                    continue
                if k in ('properties', 'events', 'services'):
                    sub_class_name = str_format(attr_name)
                    attr_val = f'{sub_class_name}()'
                elif k in ('parameters', 'outputs', 'struct', 'optional'):
                    sub_class_name = class_name
                    sub_class_name += str_format(attr_name)
                    attr_val = f'{sub_class_name}()'
                elif k == 'columnComplex':
                    sub_class_name = class_name
                    sub_class_name += str_format(attr_name)
                    sub_class_name += 'Struct'
                    attr_val = f'[{sub_class_name}()]'
                else:
                    sub_class_name = class_name
                    sub_class_name += str_format(attr_name)
                    attr_val = f'[{sub_class_name}()]'
                _sub_classes[sub_class_name] = v
            elif isinstance(v, dict):
                if k == 'columnSimple':
                    sub_class_name = class_name
                    sub_class_name += str_format(attr_name)
                    sub_class_name += 'Struct'
                    attr_val = f'[{sub_class_name}()]'
                else:
                    sub_class_name = class_name
                    sub_class_name += str_format(attr_name)
                    attr_val = f'{sub_class_name}()'
                _sub_classes[sub_class_name] = v
            elif isinstance(v, str):
                attr_val = f"'{v.strip()}'"
            else:
                attr_val = v
            result.append(f'        self.{attr_name} = {attr_val}')
    elif isinstance(attrs, list):
        for attr in attrs:
            sub_class_name = ''
            attr_name = ''
            if 'id' in attr:
                if attr['id'][0].isdigit():
                    attr_name = 'id' + attr['id']
                else:
                    attr_name = attr['id']
                sub_class_name = attr_name
            elif 'value' in attr:
                if isinstance(attr['value'], int) or attr['value'][0].isdigit():
                    attr_name = f"value{attr['value']}"
                else:
                    attr_name = attr['value']
                sub_class_name = attr_name
            if class_name[-3:] == 'ies':
                sub_class_name += class_name[:-3] + 'y'
            elif class_name[-1] == 's':
                sub_class_name += class_name[:-1]
            else:
                sub_class_name += class_name
            sub_class_name = str_format(sub_class_name)
            attr_val = f'{sub_class_name}()'
            _sub_classes[sub_class_name] = attr
            attr_name = str_format(attr_name, False)
            result.append(f'        self.{attr_name} = {attr_val}')
    return result


if __name__ == "__main__":
    json_path = Path.cwd().joinpath('E:/AutoTester/testbase/library/mqtt_lib/TSL_json')
    model_path = Path.cwd().joinpath('E:/AutoTester/testbase/library/mqtt_lib/TSL_model')
    schema_path = json_path.joinpath('_SCHEMA.json')
    for j in json_path.iterdir():
        if j.name == '_SCHEMA.json':
            continue
        m = j.name[:-5] + '_MODEL.py'
        m = m.replace('-', '_')
        if json_validate(schema_path, j):
            with open(j, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            s = create_model(json_data)
            with open(model_path.joinpath(m), 'w', encoding='utf-8') as f:
                f.write(s)
            logger.info(f'{m} 生成成功！')
        else:
            logger.error(f'{m} 生成失败！')
