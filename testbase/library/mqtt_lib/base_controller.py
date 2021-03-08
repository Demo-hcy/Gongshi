from ..common import *
from .mqtt_client import MQTTClient
from .TSL_model.base_model import *
from hashlib import md5, sha512
import base64

const.CODE_INFO = {
    0: '成功',
    1: '未知错误',
    2: '参数错误',
    3: '不支持',
    4: '超时',
    5: '访问失败',
    6: '创建错误',
    7: '打开失败(文件、设备)',
    8: '数据无效',
    9: '未就绪',
    10: '命令错误',
    11: '链接失败',
    12: '请求不支持',
    13: '网络忙',
    14: '设备忙',
    15: '服务未启动',
    16: '路径不存在',
    17: '校验失败',
    18: '加载配置失败',
    20: '关闭设备失败',
    21: '未初始化',
    22: '没有足够空间',
    23: '保存配置失败',
    24: '注册失败',
    25: '版本错误',
    26: '系统初始化失败',
    27: '设备拒绝访问',
    28: '访问不存在',
    29: '数据格式错误',
    30: '没有权限',
    31: '程序捕获异常',
    32: '设备处于自动模式',
    33: '设备处于手动模式',
    34: '解压失败',
    35: '设备未认证',
    36: '只读',
    37: '设备返回执行失败',
    50: '链接数据库失败',
    51: '操作数据库失败',
    52: '无效链接',
    60: '本地IP无效',
    61: '远程IP无效',
    62: 'ssl不支持',
    70: 'topic不支持',
    71: 'topic不存在',
    72: 'mqtt未连接',
    901: '开锁失败',
    902: '关锁失败',
    1301: '备份网络信息失败',
    1302: '备份数据库失败',
    1501: '下载失败',
    1502: '下载开始',
    1503: '下载中',
    1504: '下载成功',
    1505: '文件已经存在',
    1506: '文件不存在',
    1517: '上传开始',
    1518: '上传中',
    1519: '上传失败',
    1520: '上传完成',
    1600: '串口资源被独占',
    1601: '串口资源被占用',
    1602: '无效的Token',
    1700: '模型信息中keys错误',
    1701: '摄像头信息中keys错误',
    1702: '检测区域keys错误',
    1703: '采集信息keys错误',
    1704: '摄像头应用信息中keys错误',
    1705: '模型id已存在',
    1706: '模型id不存在',
    1707: '摄像头id已存在',
    1708: '摄像头id不存在',
    1709: '模型下载路径不是.zip',
    1710: '模型下载失败',
    1711: '从模型文件中获取模型信息失败',
    1712: '删除模型文件失败',
    1713: '模型已关联摄像头',
    1714: '模型没有关联摄像头',
    1715: '要更新的原始模型id不存在',
    1716: '摄像头url错误',
    1717: '摄像头url已存在',
    1718: '模型检测区域没有关联摄像头',
    1719: '摄像头正在被应用',
    1720: '模型没有被应用',
    1721: '模型正在被应用',
    1722: '摄像头AI没有应用',
    1723: '摄像头AI有应用'
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
            if msg == '':
                logger.error(f'可能是未获取到对应的消息ID')
            return ResultData(False, msg)

    @staticmethod
    def gen_signature(device: Device, salt: str) -> str:
        s = (device.productId + salt + device.deviceId).encode('utf8')
        md5_str = md5(s).hexdigest()
        s = ('7gbox3' + md5_str).encode('utf8')
        sha512_str = sha512(s).digest()
        signature_bytes = base64.b64encode(sha512_str)
        signature = signature_bytes.decode('utf8')
        return signature

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
