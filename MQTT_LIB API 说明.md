# MQTT_LIB API 说明

### MQTTClient

- 导入方式

  ```python
  from library.mqtt_lib.mqtt_client import MQTTClient
  ```

- API 接口

  1. MQTT客户端

     ```python
     MQTTClient(host: str, 
                port: int, 
                user: str = '', 
                password: str = '', 
             timeout: int = 30) 
     -> None
     ```

     ​    :param host: MQTT服务器地址

     ​    :param port: MQTT服务器端口

     ​    :param user: MQTT服务器认证用户名

     ​    :param password: MQTT服务器认证密码

     ​    :param timeout: 超时时间


### Simulator

**PlatformSimulator 和 DeviceSimulator 的共用接口**

- API 接口

  1. 响应错误码

     ```python
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
     ```

  2. 设备模式

     ```python
     SysMode.factory = 'factory'  # 出厂模式
     SysMode.configure = 'configure'  # 配置模式
     SysMode.networking = 'networking'  # 入网模式
     SysMode.active = 'active'  # 激活模式
     ```

  3. 解析消息

     ```python
     parse_msg(msg: Dict) 
     -> Tuple[bool, Dict]
     ```

     ​    :param msg: 需解析的消息，将读取或监听到的返回数据填入

     ​    :return: 返回响应的结果，解析后的字典

  4. 开始MQTT客户端

     ```python
     start() 
     -> None
     ```

  5. 停止MQTT客户端

     ```python
     stop() 
     -> None
     ```

  6. 销毁MQTT客户端

     ```python
     destroy() 
     -> None
     ```

     

### PlatformSimulator

- 导入方式

  ```python
  from library.mqtt_lib.simulator import PlatformSimulator
  ```

- API 接口

  1. MQTT平台控制器

     ```python
     PlatformSimulator(target_device: Device, 
                       mqtt_client: MQTTClient, 
                       is_start: bool = True) 
     -> None
     ```

     ​    :param target_device: 目标设备模型对象

     ​    :param mqtt_client: MQTT客户端

     ​    :param is_start: 自动开始MQTT客户端

  2. 读取属性

     ```python
     read(properties: List[BaseProperty]) 
     -> Tuple[bool, str]
     ```

     ​    :param properties: 要读取的属性列表

     ​    :return: 返回读取属性的结果

  3. 属性设置

     ```python
     set(properties: Dict[BaseProperty, Any], 
         is_validate: bool = False) 
     -> Tuple[bool, str]
     ```

     ​    :param properties: 要设置的属性

     ​    :param is_validate: 是否需要校验

     ​    :return: 返回属性设置的结果

  4. 服务调用

     ```python
     service_invoke(service: BaseService, 
                    data: Dict, 
                    is_validate: bool = False, 
                    check_property: Optional[BaseProperty] = None) 
     -> Tuple[bool, str]
     ```

     ​    :param service: 要调用的服务

     ​    :param data: 服务的参数数据

     ​    :param is_validate: 是否需要校验

     ​    :param check_property: 需要检查的属性上报

     ​    :return: 返回服务调用的结果

  5. 平台遗愿设置

     ```python
     will_set() 
     -> Tuple[bool, str]
     ```

     ​    :return: 返回设置遗愿的结果

  6. 平台上线

     ```python
     online() 
     -> Tuple[bool, str]
     ```

     ​    :return: 返回平台上线的结果

  7. 切换模式

     ```python
     switch_sys_mode(mode: SysMode) 
     -> Tuple[bool, str]
     ```

     ​    :param mode: 要切换的模式

     ​    :return: 返回切换模式的结果

  8. 监听属性上报

     ```python
     report_listen(property: BaseProperty,
                   is_reply: bool = False,
                   code: int = 0) 
     -> Tuple[bool, Dict]
     ```

     ​    :param property: 要监听的属性

     ​    :param is_reply: 是否启用响应

     ​    :param code: 响应的结果，参见常量const.CODE_INFO

     ​    :return: 返回监听成功与否, 返回的消息内容

  9. 响应属性上报

     ```python
     report_reply(msgId: str,
                  property: BaseProperty,
                  code: int = 0) 
     -> None
     ```

     ​    :param msgId: 消息ID

     ​    :param property: 需要响应的属性

     ​    :param code: 响应的结果，参见常量const.CODE_INFO

  10. 监听事件上报

      ```python
      event_report_listen(event: BaseEvent,
                          is_reply: bool = False,
                          code: int = 0) 
      -> Tuple[bool, Dict]
      ```

      ​    :param event: 要监听的事件

      ​    :param is_reply: 是否启用响应

      ​    :param code: 响应的结果，参见常量const.CODE_INFO

      ​    :return: 返回监听成功与否, 返回的消息内容

  11. 响应事件上报

      ```python
      event_report_reply(msgId: str,
                         event: BaseEvent,
                         code: int = 0) 
      -> None
      ```

      ​    :param msgId: 消息ID

      ​    :param event: 需要响应的事件

      ​    :param code: 响应的结果，参见常量const.CODE_INFO

  12. 监听设备遗愿

      ```python
      lastwill_listen() 
      -> Tuple[bool, Dict]
      ```

      ​    :return: 返回监听成功与否, 返回的消息内容

  13. 监听设备登录

      ```python
      login_listen(is_reply: bool = False,
                   code: int = 0) 
      -> Tuple[bool, Dict]
      ```

      ​    :param is_reply: 是否启用响应

      ​    :param code: 响应的结果，参见常量const.CODE_INFO

      ​    :return: 返回监听成功与否, 返回的消息内容

  14. 响应设备登录

      ```python
      login_reply(msgId: str, 
                  code: int = 0) 
      -> None
      ```

      ​    :param msgId: 消息ID

      ​    :param code: 响应的结果，参见常量const.CODE_INFO

  15. 监听上报设备信息

      ```python
      sys_info_report_listen(is_reply: bool = False,
                             code: int = 0) 
      -> Tuple[bool, Dict]
      ```

      ​    :param is_reply: 是否启用响应

      ​    :param code: 响应的结果，参见常量const.CODE_INFO

      ​    :return: 返回监听成功与否, 返回的消息内容

  16. 响应上报设备信息

      ```python
      sys_info_report_reply(msgId: str, 
                            code: int = 0) 
      -> None
      ```

      ​    :param msgId: 消息ID

      ​    :param code: 响应的结果，参见常量const.CODE_INFO


### DeviceSimulator

- 导入方式

  ```python
  from library.mqtt_lib.simulator import DeviceSimulator
  ```

- API 接口

  1. MQTT设备控制器

     ```python
     PlatformSimulator(device: Device,
                       mqtt_client: MQTTClient, 
                       is_start: bool = True) 
     -> None
     ```

     ​    :param device: 设备模型对象

     ​    :param mqtt_client: MQTT客户端

     ​    :param is_start: 自动开始MQTT客户端

  2. 属性上报

     ```python
     report(properties: Dict[BaseProperty, Any],
            is_validate: bool = False) 
     -> Tuple[bool, str]
     ```

     ​    :param properties: 要上报的属性和属性数据

     ​    :param is_validate: 是否需要校验

     ​    :return: 返回属性上报的结果

  3. 事件上报

     ```python
     event_report(event: BaseEvent,
                  data: Dict,
                  is_validate: bool = False) 
     -> Tuple[bool, str]
     ```

     ​    :param event: 要上报的事件

     ​    :param data: 事件的参数数据

     ​    :param is_validate: 是否需要校验

     ​    :return: 返回事件上报的结果

  4. 设备遗愿设置

     ```python
     will_set() 
     -> Tuple[bool, str]
     ```

     ​    :return: 返回设置遗愿的结果

  5. 设备登录

     ```python
     login(salt_len: int = 16) 
     -> Tuple[bool, str]
     ```

     ​    :param salt_len: salt的长度

     ​    :return: 返回设备登录的结果

  6. 上报设备信息

     ```python
     sys_info_report(mode: SysMode, 
                     ntp_info: Dict,
                     network_info: Dict,
                     mqtt_info: Dict) 
     -> Tuple[bool, Dict]
     ```

     ​    :param mode: 配置的模式

     ​    :param ntp_info: NTP信息，NTP服务器列表

     ​    :param network_info: 网络信息

     ​    :param mqtt_info: MQTT信息

     ​	:return: 返回上报设备信息的结果

  7. 监听属性读取

     ```python
     read_listen(property: BaseProperty,
                 is_reply: bool = False,
                 code: int = 0,
                 data: Dict = {}) 
     -> Tuple[bool, Dict]
     ```

     ​    :param property: 要监听的属性

     ​    :param is_reply: 是否启用响应

     ​    :param code: 响应的结果，参见常量const.CODE_INFO

     ​    :param data: 响应的数据

     ​    :return: 返回监听成功与否, 返回的消息内容

  8. 响应属性读取

     ```python
     read_reply(msgId: str,
                property: BaseProperty,
                code: int = 0,
                data: Dict = {}) 
     -> None
     ```

     ​    :param msgId: 消息ID

     ​    :param property: 需要响应的属性

     ​    :param code: 响应的结果，参见常量const.CODE_INFO

     ​    :param data: 响应的数据

  9. 监听属性设置

     ```python
     set_listen(property: BaseProperty,
                is_reply: bool = False,
                code: int = 0) 
     -> Tuple[bool, Dict]
     ```

     ​    :param property: 要监听的属性

     ​    :param is_reply: 是否启用响应

     ​    :param code: 响应的结果，参见常量const.CODE_INFO

     ​    :return: 返回监听成功与否, 返回的消息内容

  10. 响应属性设置

      ```python
      set_reply(msgId: str,
                property: BaseProperty,
                code: int = 0) 
      -> None
      ```

      ​    :param msgId: 消息ID

      ​    :param property: 需要响应的属性

      ​    :param code: 响应的结果，参见常量const.CODE_INFO

  11. 监听服务调用

      ```python
      service_invoke_listen(service: BaseService,
                            is_reply: bool = False,
                            code: int = 0) 
      -> Tuple[bool, Dict]
      ```

      ​    :param service: 要监听的服务

      ​    :param is_reply: 是否启用响应

      ​    :param code: 响应的结果，参见常量const.CODE_INFO

      ​    :return: 返回监听成功与否, 返回的消息内容

  12. 响应服务调用

      ```python
      service_invoke_reply(msgId: str,
                           service: BaseService,
                           code: int = 0) 
      -> None
      ```

      ​    :param msgId: 消息ID

      ​    :param service: 需要响应的服务

      ​    :param code: 响应的结果，参见常量const.CODE_INFO

  13. 监听平台遗愿

      ```python
      lastwill_listen() 
      -> Tuple[bool, Dict]
      ```

      ​    :return: 返回监听成功与否, 返回的消息内容

  14. 监听平台上线

      ```python
      online_listen() 
      -> Tuple[bool, Dict]
      ```

      ​    :return: 返回监听成功与否, 返回的消息内容

  15. 监听切换模式

      ```python
      switch_sys_mode_listen(is_reply: bool = False,
                             code: int = 0) 
      -> Tuple[bool, Dict]
      ```

      ​    :param is_reply: 是否启用响应

      ​    :param code: 响应的结果，参见常量const.CODE_INFO

      ​    :return: 返回监听成功与否, 返回的消息内容

  16. 响应切换模式

      ```python
      switch_sys_mode_reply(msgId: str, 
                            code: int = 0) 
      -> None
      ```

      ​    :param msgId: 消息ID

      ​    :param code: 响应的结果，参见常量const.CODE_INFO

