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


class Simulator:
    def __init__(self,
                 device: Device,
                 mqtt_client: MQTTClient,
                 is_start: bool = True) -> None:
        """
        MQTT协议控制器基类
        :param device: 设备模型对象
        :param mqtt_client: MQTT客户端
        :param is_start: 自动开始MQTT客户端
        """
        self.device = device
        self.mqtt_client = mqtt_client
        self.check_property_data = None
        if is_start:
            self.start()

    def _config_topic(self,
                      category: str,
                      operation: str = '',
                      id: str = '') -> None:
        """
        配置主题
        :param category: 类别，可以是属性、事件、服务等
        :param operation: 操作，可以是读取、上报、调用等
        :param id: 类别的ID
        """
        topic_prefix = f'/device/{self.device.productId}/{self.device.deviceId}'
        if id:
            pub_topic = f'/{category}/{id}/{operation}'
            sub_topic = f'/{category}/{id}/{operation}_reply'
        elif operation:
            pub_topic = f'/{category}/{operation}'
            sub_topic = f'/{category}/{operation}_reply'
        else:
            pub_topic = f'/{category}'
            sub_topic = f'/{category}_reply'

        self.mqtt_client.pub_topic = topic_prefix + pub_topic
        self.mqtt_client.sub_topic = topic_prefix + sub_topic

    @staticmethod
    def _validate_data(model: Union[BaseProperty, BaseParameter, BaseOutput],
                       data) -> bool:
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
                        logger_error_debug(
                            f'数据{data}超范围，应在({model.specs.min}, {model.specs.max})范围内'
                        )
                        return False
                    if data % model.specs.step != 0:
                        logger_error_debug(
                            f'数据{data}步长错误，应为{model.specs.step}的整数倍')
                        return False
        except AttributeError:
            pass
        # 校验数据选项
        try:
            if model.specs.optional:
                if data not in [
                        optional.value for optional in model.specs.optional
                ]:
                    logger_error_debug(
                        f'数据不属于选项，应在{model.specs.optional}中选择一个value')
                    return False
        except AttributeError:
            pass
        return True

    def parse_msg(self, msg: Dict) -> Tuple[bool, Dict]:
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
                logger.info(f'响应消息数据：{data}')
                return result, data
            elif 'data' in msg.keys():
                data = msg['data']
                logger.info(f'响应消息数据：{data}')
                return True, data
            elif 'params' in msg.keys():
                params = msg['params']
                return True, params
            else:
                raise Exception
        except:
            logger.error(f'消息错误：{msg}')
            return False, msg

    def _send_msg(self, payload: Dict) -> Tuple[bool, Dict]:
        """
        发送消息
        - 解析响应消息后的信息保存在current_response中
        :param msg: 消息内容
        :return: 返回发送结果、响应消息
        """
        r, m = self.mqtt_client.send_msg(payload)
        return r, m

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


class DeviceSimulator(Simulator):
    def __init__(self,
                 device: Device,
                 mqtt_client: MQTTClient,
                 is_start: bool = True) -> None:
        """
        MQTT设备控制器
        :param device: 设备模型对象
        :param mqtt_client: MQTT客户端
        :param is_start: 自动开始MQTT客户端
        """
        super().__init__(device=device,
                         mqtt_client=mqtt_client,
                         is_start=is_start)

    def report(self,
               properties: Dict[BaseProperty, Any],
               is_validate: bool = False) -> Tuple[bool, str]:
        """
        属性上报
        :param properties: 要上报的属性和属性数据
        :param is_validate: 是否需要校验
        :return: 返回属性上报的结果
        """
        self._config_topic('property', 'report')
        params = {}
        for k, v in properties.items():
            if not is_validate:
                params[k.id] = v
            elif self._validate_data(k, v):
                params[k.id] = v
            else:
                msg = f'上报的{k.id}属性，数据校验失败'
                logger_error_debug(msg)
                return False, msg
        payload = {"params": params}
        return self._send_msg(payload)

    def event_report(self,
                     event: BaseEvent,
                     data: Dict,
                     is_validate: bool = False) -> Tuple[bool, str]:
        """
        事件上报
        :param event: 要上报的事件
        :param data: 事件的参数数据
        :param is_validate: 是否需要校验
        :return: 返回事件上报的结果
        """
        self._config_topic('event', 'report', event.id)
        # 不知道事件上报的内容，假设是字典
        params = {}
        for k, v in data.items():
            if not is_validate:
                params[k] = v
            elif self._validate_data(getattr(event.parameters, k), v):
                params[k] = v
            else:
                msg = f'上报的{event.id}事件，参数{k}数据校验失败'
                logger_error_debug(msg)
                return False, msg
        params = {event.name: event.parameters.__dict__}
        payload = {"params": params}
        return self._send_msg(payload)

    def will_set(self) -> Tuple[bool, str]:
        """
        设备遗愿设置
        :return: 返回设置遗愿的结果
        """
        logger.info('设置设备遗愿')
        self._config_topic('lastwill')
        payload = {"msgId": "DEVICE-DISCONNECT", "timestamp": 0, "params": {}}
        return self.mqtt_client.will_set(payload)

    def login(self, salt_len: int = 16) -> Tuple[bool, str]:
        """
        设备登录
        :param salt_len: salt的长度
        :return: 返回设备登录的结果
        """
        if 6 < salt_len < 32:
            salt = random_str(salt_len)
        else:
            msg = f'配置的salt长度错误，应在6-32个字符以内'
            logger_error_debug(msg)
            return False, msg
        md5_str = md5(self.device.productId + salt + self.device.deviceId)
        sha512_str = sha512('7gbox3' + md5_str).hexdigest()
        signature = base64.encodestring(sha512_str)
        self._config_topic('login')
        params = {'salt': salt, 'signature': signature}
        payload = {"params": params}
        return self._send_msg(payload)

    def sys_info_report(self, mode: SysMode, ntp_info: Dict,
                        network_info: Dict,
                        mqtt_info: Dict) -> Tuple[bool, Dict]:
        """
        上报设备信息
        :param mode: 配置的模式
        :param ntp_info: NTP信息，NTP服务器列表
        :param network_info: 网络信息
        :param mqtt_info: MQTT信息
        :return: 返回上报设备信息的结果
        """
        params = {
            'sn': self.device.deviceId,
            'productId': self.device.productId,
            'configureMode': mode,
            'ntpInfo': ntp_info,
            'networkInfo': network_info,
            'mqttInfo': mqtt_info
        }
        payload = {"params": params}
        return self._send_msg(payload)

    def read_listen(self,
                    property: BaseProperty,
                    is_reply: bool = False,
                    code: int = 0,
                    data: Dict = {}) -> Tuple[bool, Dict]:
        """
        监听属性读取
        :param property: 要监听的属性
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :param data: 响应的数据
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听属性读取：{property.id}')
        self._config_topic('property', 'read')
        expr = {}
        expr[property.id] = {}
        r, m = self.mqtt_client.listen(expr)
        logger.info(f'结束监听属性读取：{property.id}')
        if is_reply:
            try:
                self.read_reply(m['msgId'], property, code, data)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        return r, m

    def read_reply(self,
                   msgId: str,
                   property: BaseProperty,
                   code: int = 0,
                   data: Dict = {}) -> None:
        """
        响应属性读取
        :param msgId: 消息ID
        :param property: 需要响应的属性
        :param code: 响应的结果，参见常量const.CODE_INFO
        :param data: 响应的数据
        """
        logger.info(f'响应属性读取：{property.id}')
        self._config_topic('property', 'read')
        self.mqtt_client.send_reply(msgId, code, data)

    def set_listen(self,
                   property: BaseProperty,
                   is_reply: bool = False,
                   code: int = 0) -> Tuple[bool, Dict]:
        """
        监听属性设置
        :param property: 要监听的属性
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听属性设置：{property.id}')
        self._config_topic('property', 'set')
        expr = {}
        expr[property.id] = {}
        r, m = self.mqtt_client.listen(expr)
        logger.info(f'结束监听属性设置：{property.id}')
        if is_reply:
            try:
                self.set_reply(m['msgId'], property, code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        return r, m

    def set_reply(self,
                  msgId: str,
                  property: BaseProperty,
                  code: int = 0) -> None:
        """
        响应属性设置
        :param msgId: 消息ID
        :param property: 需要响应的属性
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应属性设置：{property.id}')
        self._config_topic('property', 'set')
        self.mqtt_client.send_reply(msgId, code)

    def service_invoke_listen(self,
                              service: BaseService,
                              is_reply: bool = False,
                              code: int = 0) -> Tuple[bool, Dict]:
        """
        监听服务调用
        :param service: 要监听的服务
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听服务调用：{service.id}')
        self._config_topic('service', 'invoke')
        expr = {}
        expr[service.id] = {}
        r, m = self.mqtt_client.listen(expr)
        logger.info(f'结束监听服务调用：{service.id}')
        if is_reply:
            try:
                self.service_invoke_reply(m['msgId'], service, code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        return r, m

    def service_invoke_reply(self,
                             msgId: str,
                             service: BaseService,
                             code: int = 0) -> None:
        """
        响应服务调用
        :param msgId: 消息ID
        :param service: 需要响应的服务
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应服务调用：{service.id}')
        self._config_topic('service', 'invoke')
        self.mqtt_client.send_reply(msgId, code)

    def lastwill_listen(self) -> Tuple[bool, Dict]:
        """
        监听平台遗愿
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听平台遗愿')
        self._config_topic('platform', 'lastwill')
        r, m = self.mqtt_client.listen()
        logger.info(f'结束监听平台遗愿')
        return r, m

    def online_listen(self) -> Tuple[bool, Dict]:
        """
        监听平台上线
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听平台上线')
        self._config_topic('platform', 'online')
        r, m = self.mqtt_client.listen()
        logger.info(f'结束监听平台上线')
        return r, m

    def switch_sys_mode_listen(self,
                               is_reply: bool = False,
                               code: int = 0) -> Tuple[bool, Dict]:
        """
        监听切换模式
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听切换模式')
        self._config_topic('config', 'switchSysMode')
        r, m = self.mqtt_client.listen()
        logger.info(f'结束监听切换模式')
        if is_reply:
            try:
                self.switch_sys_mode_reply(m['msgId'], code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        return r, m

    def switch_sys_mode_reply(self, msgId: str, code: int = 0) -> None:
        """
        响应切换模式
        :param msgId: 消息ID
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应切换模式')
        self._config_topic('config', 'switchSysMode')
        self.mqtt_client.send_reply(msgId, code)


class PlatformSimulator(Simulator):
    def __init__(self,
                 target_device: Device,
                 mqtt_client: MQTTClient,
                 is_start: bool = True) -> None:
        """
        MQTT平台控制器
        :param target_device: 目标设备模型对象
        :param mqtt_client: MQTT客户端
        :param is_start: 自动开始MQTT客户端
        """
        super().__init__(device=target_device,
                         mqtt_client=mqtt_client,
                         is_start=is_start)

    def read(self, properties: List[BaseProperty]) -> Tuple[bool, str]:
        """
        读取属性
        :param properties: 要读取的属性列表
        :return: 返回读取属性的结果
        """
        self._config_topic('property', 'read')
        params = {"properties": [property.id for property in properties]}
        payload = {"params": params}
        return self._send_msg(payload)

    def set(self,
            properties: Dict[BaseProperty, Any],
            is_validate: bool = False) -> Tuple[bool, str]:
        """
        属性设置
        :param properties: 要设置的属性
        :param is_validate: 是否需要校验
        :return: 返回属性设置的结果
        """
        self._config_topic('property', 'set')
        params = {}
        for k, v in properties.items():
            if not is_validate:
                params[k.id] = v
            elif self._validate_data(k, v):
                params[k.id] = v
            else:
                msg = f'设置的{k.id}属性，数据校验失败'
                logger_error_debug(msg)
                return False, msg
        payload = {"params": params}
        return self._send_msg(payload)

    def service_invoke(
            self,
            service: BaseService,
            data: Dict,
            is_validate: bool = False,
            check_property: Optional[BaseProperty] = None) -> Tuple[bool, str]:
        """
        服务调用
        :param service: 要调用的服务
        :param data: 服务的参数数据
        :param is_validate: 是否需要校验
        :param check_property: 需要检查的属性上报
        :return: 返回服务调用的结果
        """
        if check_property:
            self._config_topic('property', 'report')
            listen_topic = self.mqtt_client.pub_topic
            self.mqtt_client.subscribe(listen_topic)
        else:
            self.check_property_data = None
            listen_topic = None

        self._config_topic('service', 'invoke', service.id)
        params = {}
        for k, v in data.items():
            if not is_validate:
                params[k] = v
            elif self._validate_data(getattr(service.parameters, k), v):
                params[k] = v
            else:
                msg = f'调用的{service.id}服务，参数{k}数据校验失败'
                logger_error_debug(msg)
                return False, msg
        payload = {"params": params}
        result = self._send_msg(payload)

        if listen_topic:
            expr = {}
            expr[check_property.id] = {}
            data = self.mqtt_client.get_msg(listen_topic, expr)
            if data[0]:
                self.check_property_data = data[1]['params']
            else:
                self.check_property_data = data[1]
        return result

    def will_set(self) -> Tuple[bool, str]:
        """
        平台遗愿设置
        :return: 返回设置遗愿的结果
        """
        logger.info('设置平台遗愿')
        self._config_topic('platform', 'lastwill')
        payload = {"msgId": "PLATFORM-DISCONNECT", "params": {}}
        return self.mqtt_client.will_set(payload)

    def online(self) -> Tuple[bool, str]:
        """
        平台上线
        :return: 返回平台上线的结果
        """
        logger.info('平台上线')
        self._config_topic('platform', 'online')
        payload = {"msgId": "PLATFORM-ONLINE", "params": {}}
        return self.mqtt_client.online(payload)

    def switch_sys_mode(self, mode: SysMode) -> Tuple[bool, str]:
        """
        切换模式
        :param mode: 要切换的模式
        :return: 返回切换模式的结果
        """
        logger.info('切换模式')
        self._config_topic('config', 'switchSysMode')
        payload = {"params": {'configureMode': mode.value}}
        return self.mqtt_client._send_msg(payload)

    def report_listen(self,
                      property: BaseProperty,
                      is_reply: bool = False,
                      code: int = 0) -> Tuple[bool, Dict]:
        """
        监听属性上报
        :param property: 要监听的属性
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听属性：{property.id}')
        self._config_topic('property', 'report')
        expr = {}
        expr[property.id] = {}
        r, m = self.mqtt_client.listen(expr)
        logger.info(f'结束监听属性：{property.id}')
        if is_reply:
            try:
                self.report_reply(m['msgId'], property, code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        return r, m

    def report_reply(self,
                     msgId: str,
                     property: BaseProperty,
                     code: int = 0) -> None:
        """
        响应属性上报
        :param msgId: 消息ID
        :param property: 需要响应的属性
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应属性上报：{property.id}')
        self._config_topic('property', 'report')
        self.mqtt_client.send_reply(msgId, code)

    def event_report_listen(self,
                            event: BaseEvent,
                            is_reply: bool = True,
                            code: int = 0) -> Tuple[bool, Dict]:
        """
        监听事件上报
        :param event: 要监听的事件
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听事件：{event.id}')
        self._config_topic('event', 'report', event.id)
        expr = {}
        expr[event.id] = {}
        r, m = self.mqtt_client.listen(expr)
        logger.info(f'结束监听事件：{event.id}')
        if is_reply:
            try:
                self.event_report_reply(m['msgId'], event, code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        return r, m

    def event_report_reply(self,
                           msgId: str,
                           event: BaseEvent,
                           code: int = 0) -> None:
        """
        响应事件上报
        :param msgId: 消息ID
        :param event: 需要响应的事件
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应事件上报：{event.id}')
        self._config_topic('event', 'report', event.id)
        self.mqtt_client.send_reply(msgId, code)

    def lastwill_listen(self) -> Tuple[bool, Dict]:
        """
        监听设备遗愿
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听设备遗愿')
        self._config_topic('lastwill')
        r, m = self.mqtt_client.listen()
        logger.info(f'结束监听设备遗愿')
        return r, m

    def login_listen(self,
                     is_reply: bool = False,
                     code: int = 0) -> Tuple[bool, Dict]:
        """
        监听设备登录
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听登录：设备{self.device.productId}/{self.device.deviceId}')
        self._config_topic('login')
        r, m = self.mqtt_client.listen()
        logger.info(f'结束监听登录：设备{self.device.productId}/{self.device.deviceId}')
        if is_reply:
            try:
                self.login_reply(m['msgId'], code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        return r, m

    def login_reply(self, msgId: str, code: int = 0) -> None:
        """
        响应设备登录
        :param msgId: 消息ID
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应设备登录：{self.device.productId}/{self.device.deviceId}')
        self._config_topic('login')
        self.mqtt_client.send_reply(msgId, code)

    def sys_info_report_listen(self,
                               is_reply: bool = False,
                               code: int = 0) -> Tuple[bool, Dict]:
        """
        监听上报设备信息
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(
            f'开始监听上报设备信息：设备{self.device.productId}/{self.device.deviceId}')
        self._config_topic('config', 'sysInfoReport')
        r, m = self.mqtt_client.listen()
        logger.info(
            f'结束监听上报设备信息：设备{self.device.productId}/{self.device.deviceId}')
        if is_reply:
            try:
                self.sys_info_report_reply(m['msgId'], code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        return r, m

    def sys_info_report_reply(self, msgId: str, code: int = 0) -> None:
        """
        响应上报设备信息
        :param msgId: 消息ID
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应上报设备信息：{self.device.productId}/{self.device.deviceId}')
        self._config_topic('config', 'sysInfoReport')
        self.mqtt_client.send_reply(msgId, code)
