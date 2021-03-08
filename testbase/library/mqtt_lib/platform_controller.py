from .base_controller import *


class PlatformController(BaseController):
    def __init__(self, mqtt_client: MQTTClient, is_start: bool = True) -> None:
        """
        MQTT平台控制器
        :param mqtt_client: MQTT客户端
        :param is_start: 自动开始MQTT客户端
        """
        super().__init__(mqtt_client=mqtt_client, is_start=is_start)

    def read(self, device: Device, properties: List[BaseProperty], is_parsed: bool = False) -> ResultData:
        """
        读取属性
        :param device: 要读取的设备
        :param properties: 要读取的属性列表
        :return: 返回读取属性的结果
        """
        pub_topic, sub_topic = self.build_topic(device, 'property', 'read')
        params = {"properties": [x.id for x in properties]}
        payload = {"params": params}
        r = self.mqtt_client.send_msg(pub_topic, sub_topic, payload)
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def set(self,
            device: Device,
            properties: List[BaseProperty],
            is_validate: bool = False,
            is_parsed: bool = False) -> ResultData:
        """
        属性设置
        :param device: 要设置的设备
        :param properties: 要设置的属性列表
        :param is_validate: 是否需要校验
        :return: 返回属性设置的结果
        """
        pub_topic, sub_topic = self.build_topic(device, 'property', 'set')
        params = {}
        for x in properties:
            if not is_validate:
                params[x.id] = x.v
            elif self.validate_data(x, x.v):
                params[x.id] = x.v
            else:
                msg = f'设置的{x.id}属性，数据校验失败'
                logger_error_debug(msg)
                return False, msg
        payload = {"params": params}
        r = self.mqtt_client.send_msg(pub_topic, sub_topic, payload)
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def service_invoke(self,
                       device: Device,
                       service: BaseService,
                       data: Dict = None,
                       is_validate: bool = False,
                       check_property: BaseProperty = None,
                       is_parsed: bool = False) -> ResultData:
        """
        服务调用
        :param device: 要调用的设备
        :param service: 要调用的服务
        :param data: 服务的参数数据
        :param is_validate: 是否需要校验
        :param check_property: 需要检查的属性上报
        :return: 返回服务调用的结果
        """
        if check_property:
            pub_topic, sub_topic = self.build_topic(device, 'property', 'report')
            listen_topic = pub_topic
            self.mqtt_client.subscribe(listen_topic)
        else:
            self.check_property_data = None
            listen_topic = None

        pub_topic, sub_topic = self.build_topic(device, 'service', 'invoke', service.id)
        params = {}
        if data or data == {}:
            params_dict = data
        else:
            if service.parameters == None:
                params_dict = {}
            else:
                params_dict = service.parameters.v
        for k, v in params_dict.items():
            if not is_validate:
                params[k] = v
            elif self.validate_data(getattr(service.parameters, k), v):
                params[k] = v
            else:
                msg = f'调用的{service.id}服务，参数{k}数据校验失败'
                logger_error_debug(msg)
                return ResultData(False, msg)
        payload = {"params": params}
        r = self.mqtt_client.send_msg(pub_topic, sub_topic, payload)

        if listen_topic:
            expr = {check_property.id: {}}
            listen_r = self.mqtt_client.get_msg(listen_topic, expr)
            if listen_r:
                self.check_property_data = listen_r.data_dict['params']
            else:
                self.check_property_data = listen_r.data_dict
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def will_set(self) -> None:
        """
        平台遗愿设置
        """
        logger.info('设置平台遗愿')
        pub_topic = '/platform/lastwill'
        payload = {"msgId": "PLATFORM-DISCONNECT", "params": {}}
        self.mqtt_client.will_set(pub_topic, payload)

    def online(self, is_parsed: bool = False) -> ResultData:
        """
        平台上线
        :return: 返回平台上线的结果
        """
        logger.info('平台上线')
        pub_topic = '/platform/online'
        payload = {"msgId": "PLATFORM-ONLINE", "params": {}}
        r = self.mqtt_client.online(pub_topic, payload)
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def switch_sys_mode(self, device: Device, mode: SysMode, is_parsed: bool = False) -> ResultData:
        """
        切换模式
        :param device: 要切换模式的设备
        :param mode: 要切换的模式
        :return: 返回切换模式的结果
        """
        logger.info('切换模式')
        pub_topic, sub_topic = self.build_topic(device, 'config', 'switchSysMode')
        payload = {"params": {'configureMode': mode.value}}
        r = self.mqtt_client.send_msg(pub_topic, sub_topic, payload)
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def report_listen(self,
                      device: Device,
                      properties: List[BaseProperty] = None,
                      is_reply: bool = False,
                      code: int = 0,
                      is_parsed: bool = False) -> ResultData:
        """
        监听属性上报
        :param device: 要监听的设备，可监听该设备的任意属性上报
        :param properties: 要监听的属性列表
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        if not properties:
            property_list = '全部属性'
        else:
            property_list = [x.id for x in properties] if properties else None
        logger.info(f'开始监听属性上报：{property_list}')
        pub_topic, sub_topic = self.build_topic(device, 'property', 'report')
        expr = {x: {} for x in property_list} if properties else None
        r = self.mqtt_client.listen(pub_topic, expr)
        logger.info(f'结束监听属性上报：{property_list}')
        if is_reply and r.result:
            try:
                if not properties:
                    property_list = self.parse_msg(r.data_dict).data_dict['properties']
                    properties = [getattr(device.properties, x) for x in property_list]
                self.report_reply(device, r.data_dict['msgId'], properties, code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def report_reply(self,
                     device: Device,
                     msgId: str,
                     properties: List[BaseProperty],
                     code: int = 0) -> None:
        """
        响应属性上报
        :param device: 要响应的设备
        :param msgId: 消息ID
        :param properties: 需要响应的属性列表
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        property_list = [x.id for x in properties]
        logger.info(f'响应属性上报：{property_list}')
        pub_topic, sub_topic = self.build_topic(device, 'property', 'report')
        self.mqtt_client.send_reply(sub_topic, msgId, code)

    def event_report_listen(self,
                            device: Device,
                            event: BaseEvent,
                            is_reply: bool = False,
                            code: int = 0,
                            is_parsed: bool = False) -> ResultData:
        """
        监听事件上报
        :param device: 要监听的设备
        :param event: 要监听的事件
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听事件上报：{event.id}')
        pub_topic, sub_topic = self.build_topic(device, 'event', 'report', event.id)
        expr = {event.id: {}}
        r = self.mqtt_client.listen(pub_topic, expr)
        logger.info(f'结束监听事件上报：{event.id}')
        if is_reply and r.result:
            try:
                self.event_report_reply(device, r.data_dict['msgId'], event, code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def event_report_reply(self, device: Device, msgId: str, event: BaseEvent, code: int = 0) -> None:
        """
        响应事件上报
        :param device: 要响应的设备
        :param msgId: 消息ID
        :param event: 需要响应的事件
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应事件上报：{event.id}')
        pub_topic, sub_topic = self.build_topic(device, 'event', 'report', event.id)
        self.mqtt_client.send_reply(sub_topic, msgId, code)

    def lastwill_listen(self, device: Device, is_parsed: bool = False) -> ResultData:
        """
        监听设备遗愿
        :param device: 要监听的设备
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听设备遗愿：设备{device.productId}/{device.deviceId}')
        pub_topic, sub_topic = self.build_topic(device, 'lastwill')
        r = self.mqtt_client.listen(pub_topic)
        logger.info(f'结束监听设备遗愿：设备{device.productId}/{device.deviceId}')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def login_listen(self,
                     device: Device,
                     is_reply: bool = False,
                     code: int = 0,
                     is_parsed: bool = False) -> ResultData:
        """
        监听设备登录
        :param device: 要监听的设备
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听登录：设备{device.productId}/{device.deviceId}')
        pub_topic, sub_topic = self.build_topic(device, 'login')
        r = self.mqtt_client.listen(pub_topic)
        logger.info(f'结束监听登录：设备{device.productId}/{device.deviceId}')
        if is_reply and r.result:
            try:
                self.login_reply(device, r.data_dict['msgId'], code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def login_reply(self, device: Device, msgId: str, code: int = 0) -> None:
        """
        响应设备登录
        :param device: 要响应的设备
        :param msgId: 消息ID
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应设备登录：{device.productId}/{device.deviceId}')
        pub_topic, sub_topic = self.build_topic(device, 'login')
        self.mqtt_client.send_reply(sub_topic, msgId, code)

    def sys_info_report_listen(self,
                               device: Device,
                               is_reply: bool = False,
                               code: int = 0,
                               is_parsed: bool = False) -> ResultData:
        """
        监听上报设备信息
        :param device: 要监听的设备
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听上报设备信息：设备{device.productId}/{device.deviceId}')
        pub_topic, sub_topic = self.build_topic(device, 'config', 'sysInfoReport')
        r = self.mqtt_client.listen(pub_topic)
        logger.info(f'结束监听上报设备信息：设备{device.productId}/{device.deviceId}')
        if is_reply and r.result:
            try:
                self.sys_info_report_reply(device, r.data_dict['msgId'], code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def sys_info_report_reply(self, device: Device, msgId: str, code: int = 0) -> None:
        """
        响应上报设备信息
        :param device: 要响应的设备
        :param msgId: 消息ID
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应上报设备信息：{device.productId}/{device.deviceId}')
        pub_topic, sub_topic = self.build_topic(device, 'config', 'sysInfoReport')
        self.mqtt_client.send_reply(sub_topic, msgId, code)
