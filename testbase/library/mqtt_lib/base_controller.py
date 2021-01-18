from ..common import *
from .mqtt_client import MQTTClient
from .TSL_model.base_model import *
from hashlib import md5, sha512
import base64

const.CODE_INFO = {
    0: '成功',
    100: '消息格式错误，解析出错',
    101: '重复消息，消息ID重复',
    102: '消息过期，超过处理时限',
    103: '操作超时',
    200: '指定属性不存在',
    201: '属性不可读',
    202: '属性不可写',
    210: '属性值不合法，值类型不对、或超出规定范围'
}


@unique
class SysMode(Enum):
    """
    设备模式
    """
    factory = 'factory'  # 出厂模式
    configure = 'configure'  # 配置模式
    networking = 'networking'  # 入网模式
    active = 'active'  # 激活模式


class BaseController:
    def __init__(self, mqtt_client: MQTTClient, is_start: bool = True) -> None:
        """
        MQTT协议控制器基类
        :param mqtt_client: MQTT客户端
        :param is_start: 自动开始MQTT客户端
        """
        self.mqtt_client = mqtt_client
        self.check_property_data = None
        if is_start:
            self.start()

    @staticmethod
    def build_topic(device: Device, category: str, operation: str = '', id: str = '') -> Tuple[str, str]:
        """
        生成主题
        :param device: 设备
        :param category: 类别，可以是属性、事件、服务等
        :param operation: 操作，可以是读取、上报、调用等
        :param id: 类别的ID
        :return: 返回发布的主题，订阅的主题
        """
        topic_prefix = f'/device/{device.productId}/{device.deviceId}'
        if id:
            pub_topic = f'/{category}/{id}/{operation}'
            sub_topic = f'/{category}/{id}/{operation}_reply'
        elif operation:
            pub_topic = f'/{category}/{operation}'
            sub_topic = f'/{category}/{operation}_reply'
        else:
            pub_topic = f'/{category}'
            sub_topic = f'/{category}_reply'
        pub_topic = topic_prefix + pub_topic
        sub_topic = topic_prefix + sub_topic
        return pub_topic, sub_topic

    @staticmethod
    def validate_data(model: Union[BaseProperty, BaseParameter, BaseOutput], data) -> bool:
        """
        数据校验
        :param model: 数据的模型对象
        :param data: 待校验的数据
        :return: 返回是否校验通过
        """
        # 校验数据类型
        if model.type:
            if model.type == 'string' and not isinstance(data, str):
                logger_error_debug(f'数据{data}类型错误，应为str类型')
                return False
            elif model.type == 'number' and not isinstance(data, (int, float)):
                logger_error_debug(f'数据{data}类型错误，应为int或float类型')
                return False
            elif model.type == 'integer' and not isinstance(data, int):
                logger_error_debug(f'数据{data}类型错误，应为int类型')
                return False
            elif model.type == 'boolean' and not isinstance(data, bool):
                logger_error_debug(f'数据{data}类型错误，应为bool类型')
                return False
            elif model.type == 'array' and not isinstance(data, list):
                logger_error_debug(f'数据{data}类型错误，应为list类型')
                return False
            elif model.type == 'struct' and not isinstance(data, dict):
                logger_error_debug(f'数据{data}类型错误，应为dict类型')
                return False
            elif model.type == 'null' and not data:
                logger_error_debug(f'数据{data}类型错误，应为None类型')
                return False
        # 校验数据范围
        try:
            if model.specs.min:
                if isinstance(data, (int, float)):
                    if not (model.specs.min < data < model.specs.max):
                        logger_error_debug(f'数据{data}超范围，应在({model.specs.min}, {model.specs.max})范围内')
                        return False
                    if data % model.specs.step != 0:
                        logger_error_debug(f'数据{data}步长错误，应为{model.specs.step}的整数倍')
                        return False
        except AttributeError:
            pass
        # 校验数据选项
        try:
            if model.specs.optional:
                if data not in [optional.value for optional in model.specs.optional]:
                    logger_error_debug(f'数据不属于选项，应在{model.specs.optional}中选择一个value')
                    return False
        except AttributeError:
            pass
        return True

    @staticmethod
    def parse_msg(msg: Dict) -> ResultData:
        """
        解析消息
        :param msg: 需解析的消息，将读取或监听到的返回数据填入
        :return: 返回响应的结果，解析后的字典
        """
        try:
            if 'code' in msg.keys():
                code = msg['code']
                message = msg['message']
                data = msg['data']
                if code == 0:
                    logger.info(f'响应消息状态：{const.CODE_INFO[code]} {message}')
                    result = True
                elif code in const.CODE_INFO.keys():
                    logger.warning(f'响应消息状态：{const.CODE_INFO[code]} {message}')
                    result = False
                else:
                    logger.warning(f'响应消息状态：响应异常 {message}')
                    result = False
                # logger.info(f'响应消息数据：{data}')
                return ResultData(result, data)
            elif 'data' in msg.keys():
                data = msg['data']
                # logger.info(f'响应消息数据：{data}')
                return ResultData(True, data)
            elif 'params' in msg.keys():
                params = msg['params']
                return ResultData(True, params)
            else:
                raise Exception
        except:
            logger.error(f'消息错误：{msg}')
            return ResultData(False, msg)

    def start(self) -> None:
        """
        开始MQTT客户端
        """
        self.mqtt_client.loop_start()

    def stop(self) -> None:
        """
        停止MQTT客户端
        """
        self.mqtt_client.loop_stop()

    def destroy(self) -> None:
        """
        销毁MQTT客户端
        """
        self.mqtt_client.destroy()
