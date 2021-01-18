from .base_controller import *


class DeviceController(BaseController):
    def __init__(self, mqtt_client: MQTTClient, is_start: bool = True) -> None:
        """
        MQTT设备控制器
        :param mqtt_client: MQTT客户端
        :param is_start: 自动开始MQTT客户端
        """
        super().__init__(mqtt_client=mqtt_client, is_start=is_start)

    def report(self,
               device: Device,
               properties: List[BaseProperty],
               is_validate: bool = False,
               is_parsed: bool = False) -> ResultData:
        """
        属性上报
        :param device: 要上报的设备
        :param properties: 要上报的属性列表
        :param is_validate: 是否需要校验
        :return: 返回属性上报的结果
        """
        pub_topic, sub_topic = self.build_topic(device, 'property', 'report')
        params = {}
        for property in properties:
            if not is_validate:
                params[property.id] = property.v
            elif self.validate_data(property, property.v):
                params[property.id] = property.v
            else:
                msg = f'上报的{property.id}属性，数据校验失败'
                logger_error_debug(msg)
                return ResultData(False, msg)
        payload = {"params": params}
        r = self.mqtt_client.send_msg(pub_topic, sub_topic, payload)
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def event_report(self,
                     device: Device,
                     event: BaseEvent,
                     is_validate: bool = False,
                     is_parsed: bool = False) -> ResultData:
        """
        事件上报
        :param device: 要上报的设备
        :param event: 要上报的事件
        :param is_validate: 是否需要校验
        :return: 返回事件上报的结果
        """
        pub_topic, sub_topic = self.build_topic(device, 'event', 'report', event.id)
        params = {}
        for k, v in event.parameters.v.items():
            if not is_validate:
                params[k] = v
            elif self.validate_data(getattr(event.parameters, k), v):
                params[k] = v
            else:
                msg = f'上报的{event.id}事件，参数{k}数据校验失败'
                logger_error_debug(msg)
                return ResultData(False, msg)
        payload = {"params": params}
        r = self.mqtt_client.send_msg(pub_topic, sub_topic, payload)
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def will_set(self, device: Device) -> None:
        """
        设备遗愿设置
        :param device: 要设置遗愿的设备
        """
        logger.info('设置设备遗愿')
        pub_topic, sub_topic = self.build_topic(device, 'lastwill')
        payload = {"msgId": "DEVICE-DISCONNECT", "timestamp": 0, "params": {}}
        self.mqtt_client.will_set(pub_topic, payload)

    def login(self, device: Device, salt_len: int = 16, is_parsed: bool = False) -> ResultData:
        """
        设备登录
        :param device: 要登录的设备
        :param salt_len: salt的长度
        :return: 返回设备登录的结果
        """
        if 6 < salt_len < 32:
            salt = random_str(salt_len)
        else:
            msg = f'配置的salt长度错误，应在6-32个字符以内'
            logger_error_debug(msg)
            return ResultData(False, msg)
        md5_str = md5(device.productId + salt + device.deviceId)
        sha512_str = sha512('7gbox3' + md5_str).hexdigest()
        signature = base64.encodestring(sha512_str)
        pub_topic, sub_topic = self.build_topic(device, 'online')
        params = {'salt': salt, 'signature': signature}
        payload = {"params": params}
        r = self.mqtt_client.online(pub_topic, payload)
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def sys_info_report(self,
                        device: Device,
                        mode: SysMode,
                        ntp_info: Dict,
                        network_info: Dict,
                        mqtt_info: Dict,
                        is_parsed: bool = False) -> ResultData:
        """
        上报设备信息
        :param device: 要上报的设备
        :param mode: 配置的模式
        :param ntp_info: NTP信息，NTP服务器列表
        :param network_info: 网络信息
        :param mqtt_info: MQTT信息
        :return: 返回上报设备信息的结果
        """
        pub_topic, sub_topic = self.build_topic(device, 'config', 'sysInfoReport')
        params = {
            'sn': device.deviceId,
            'productId': device.productId,
            'configureMode': mode,
            'ntpInfo': ntp_info,
            'networkInfo': network_info,
            'mqttInfo': mqtt_info
        }
        payload = {"params": params}
        r = self.mqtt_client.send_msg(pub_topic, sub_topic, payload)
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def read_listen(self,
                    device: Device,
                    properties: Optional[List[BaseProperty]] = None,
                    is_reply: bool = False,
                    code: int = 0,
                    is_parsed: bool = False) -> ResultData:
        """
        监听属性读取
        :param device: 要监听的设备，可监听该设备的任意属性读取
        :param properties: 要监听的属性列表
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        propertie_list = [property.id for property in properties]
        logger.info(f'开始监听属性读取：{propertie_list}')
        pub_topic, sub_topic = self.build_topic(device, 'property', 'read')
        expr = {property: {} for property in propertie_list} if properties else None
        r = self.mqtt_client.listen(pub_topic, expr)
        logger.info(f'结束监听属性读取：{propertie_list}')
        if is_reply and r.result:
            try:
                if not properties:
                    propertie_list = self.parse_msg(r.data_dict).data_dict['properties']
                    properties = [getattr(device.properties, property) for property in propertie_list]
                self.read_reply(device, r.data_dict['msgId'], properties, code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def read_reply(self, device: Device, msgId: str, properties: Optional[List[BaseProperty]], code: int = 0) -> None:
        """
        响应属性读取
        :param device: 要响应的设备
        :param msgId: 消息ID
        :param properties: 需要响应的属性列表
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        propertie_list = [property.id for property in properties]
        logger.info(f'响应属性读取：{propertie_list}')
        pub_topic, sub_topic = self.build_topic(device, 'property', 'read')
        self.mqtt_client.send_reply(sub_topic, msgId, code)

    def set_listen(self,
                   device: Device,
                   properties: Optional[List[BaseProperty]] = None,
                   is_reply: bool = False,
                   code: int = 0,
                   is_parsed: bool = False) -> ResultData:
        """
        监听属性设置
        :param device: 要监听的设备，可监听该设备的任意属性设置
        :param properties: 要监听的属性列表
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        propertie_list = [property.id for property in properties] if properties else None
        logger.info(f'开始监听属性设置：{propertie_list}')
        pub_topic, sub_topic = self.build_topic(device, 'property', 'set')
        expr = {property: {} for property in propertie_list} if properties else None
        r = self.mqtt_client.listen(pub_topic, expr)
        logger.info(f'结束监听属性设置：{propertie_list}')
        if is_reply and r.result:
            try:
                if not properties:
                    propertie_list = self.parse_msg(r.data_dict).data_dict['properties']
                    properties = [getattr(device.properties, property) for property in propertie_list]
                self.set_reply(device, r.data_dict['msgId'], properties, code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def set_reply(self, device: Device, msgId: str, properties: Optional[List[BaseProperty]], code: int = 0) -> None:
        """
        响应属性设置
        :param device: 要响应的设备
        :param msgId: 消息ID
        :param properties: 需要响应的属性列表
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        propertie_list = [property.id for property in properties]
        logger.info(f'响应属性设置：{propertie_list}')
        pub_topic, sub_topic = self.build_topic(device, 'property', 'set')
        self.mqtt_client.send_reply(sub_topic, msgId, code)

    def service_invoke_listen(self,
                              device: Device,
                              service: BaseService,
                              is_reply: bool = False,
                              code: int = 0,
                              is_parsed: bool = False) -> ResultData:
        """
        监听服务调用
        :param device: 要监听的设备
        :param service: 要监听的服务
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听服务调用：{service.id}')
        pub_topic, sub_topic = self.build_topic(device, 'service', 'invoke', service.id)
        expr = {service.id: {}}
        r = self.mqtt_client.listen(pub_topic, expr)
        logger.info(f'结束监听服务调用：{service.id}')
        if is_reply and r.result:
            try:
                self.service_invoke_reply(device, r.data_dict['msgId'], service, code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def service_invoke_reply(self, device: Device, msgId: str, service: BaseService, code: int = 0) -> None:
        """
        响应服务调用
        :param device: 要响应的设备
        :param msgId: 消息ID
        :param service: 需要响应的服务
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应服务调用：{service.id}')
        pub_topic, sub_topic = self.build_topic(device, 'service', 'invoke', service.id)
        self.mqtt_client.send_reply(sub_topic, msgId, code)

    def lastwill_listen(self, device: Device, is_parsed: bool = False) -> ResultData:
        """
        监听平台遗愿
        :param device: 要监听的设备
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听平台遗愿')
        pub_topic, sub_topic = self.build_topic(device, 'platform', 'lastwill')
        r = self.mqtt_client.listen(pub_topic)
        logger.info(f'结束监听平台遗愿')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def online_listen(self, device: Device, is_parsed: bool = False) -> ResultData:
        """
        监听平台上线
        :param device: 要监听的设备
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听平台上线')
        pub_topic, sub_topic = self.build_topic(device, 'platform', 'online')
        r = self.mqtt_client.listen(pub_topic)
        logger.info(f'结束监听平台上线')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def switch_sys_mode_listen(self,
                               device: Device,
                               is_reply: bool = False,
                               code: int = 0,
                               is_parsed: bool = False) -> ResultData:
        """
        监听切换模式
        :param device: 要监听的设备
        :param is_reply: 是否启用响应
        :param code: 响应的结果，参见常量const.CODE_INFO
        :return: 返回监听成功与否, 返回的消息内容
        """
        logger.info(f'开始监听切换模式')
        pub_topic, sub_topic = self.build_topic(device, 'config', 'switchSysMode')
        r = self.mqtt_client.listen(pub_topic)
        logger.info(f'结束监听切换模式')
        if is_reply and r.result:
            try:
                self.switch_sys_mode_reply(device, r.data_dict['msgId'], code)
            except ValueError:
                logger.error('监听到的消息中不包含正确msgId')
        if is_parsed:
            r = self.parse_msg(r.data_dict)
        return r

    def switch_sys_mode_reply(self, device: Device, msgId: str, code: int = 0) -> None:
        """
        响应切换模式
        :param device: 要响应的设备
        :param msgId: 消息ID
        :param code: 响应的结果，参见常量const.CODE_INFO
        """
        logger.info(f'响应切换模式')
        pub_topic, sub_topic = self.build_topic(device, 'config', 'switchSysMode')
        self.mqtt_client.send_reply(sub_topic, msgId, code)
