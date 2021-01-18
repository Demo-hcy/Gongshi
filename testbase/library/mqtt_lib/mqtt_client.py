from json.decoder import JSONDecodeError
from ..common import *
import paho.mqtt.client as mqtt
from queue import Empty, Queue
import json
import time


def _cmp_dict(expr: Dict, data: Dict) -> bool:
    """
    判断data是否包含expr
    expr中的k,v都是data中对应k,v的子集
    :param expr: 表达式字典
    :param data: 数据字典
    :return: 返回满足条件返回True，反之返回False
    """
    result = False
    for k, v in expr.items():
        if v == {}:
            if 'params' not in data.keys():
                break
            if k in data['params'].keys():
                continue
        # 为字典时递归调用
        elif isinstance(v, dict):
            res = _cmp_dict(v, data.get(k))
            if res is False:
                break
        # 为list时，转为集合比较
        elif isinstance(v, list) and isinstance(data.get(k), list):
            if set(v) < set(data.get(k)):  # 是否为子集
                continue
            else:
                break
        else:
            if v == data.get(k):
                continue
            elif data.get('params') and v == data['params'].get(k):
                continue
            else:
                break
    else:
        result = True
    return result


class MQTTClient:
    def __init__(self, host: str, port: int, user: str = '', password: str = '', timeout: int = 30) -> None:
        """
        MQTT客户端
        :param host: MQTT服务器地址
        :param port: MQTT服务器端口
        :param user: MQTT服务器认证用户名
        :param password: MQTT服务器认证密码
        :param timeout: 超时时间
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.timeout = timeout
        self.queue = Queue()
        # self.connect_status = None
        self.client = None
        self.pub_topic = None
        self.sub_topic = None
        # 注册回调函数
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        # 设置认证信息
        self.client.username_pw_set(self.user, self.password)

    def on_message(self, client, userdata, msg: mqtt.MQTTMessage) -> None:
        """
        消息接收事件
        :param client: MQTT客户端
        :param userdata: 用户数据
        :param msg: MQTT消息
        """
        m = msg.payload.decode('utf-8')
        logger.info(f'获取消息：{m}')
        try:
            m_dict = json.loads(m)
            m_dict['rsp_time'] = time.time()
            m = json.dumps(m_dict)
        except Exception as e:
            logger_error_debug(f'数据json序列化失败：{e}')
            raise
        msg = (msg.topic, m)
        self.queue.put(msg)

    def on_connect(self, client, userdata, flags, rc: int) -> None:
        """
        连接事件
        :param client: MQTT客户端
        :param userdata: 用户数据
        :param flags: 标志
        :param rc: 结果码
        """
        rc_dict = {
            0: '连接成功',
            1: '连接失败 - 不正确的协议版本',
            2: '连接失败 - 无效的客户端标识符',
            3: '连接失败 - 服务器不可用',
            4: '连接失败 - 错误的用户名或密码',
            5: '连接失败 - 未经授权'
        }
        if rc in rc_dict.keys():
            msg = rc_dict[rc]
        else:
            msg = '保留'
        logger.info(f'连接结果：{msg}')
        # if rc == 0:
        #     self.connect_status = True

    def on_disconnect(self, client, userdata, rc: int) -> None:
        """
        断开事件
        :param client: MQTT客户端
        :param userdata: 用户数据
        :param rc: 结果码
        """
        if rc == 0:
            msg = '断开成功'
            # self.connect_status = False
        else:
            msg = '断开失败'
        logger.info(f'断开结果：{msg}')

    def connect_server(self) -> None:
        """
        连接服务器
        """
        try:
            self.client.connect(self.host, self.port, self.timeout)
        except Exception as e:
            logger_error_debug(f'连接服务器出错：{e}')
            raise

    def will_set(self, pub_topic: str, payload: Dict, qos: int = 2) -> None:
        """
        设置遗愿
        :param pub_topic: 发布的主题
        :param payload: 消息内容
        :param qos: 服务质量
        - level 0：最多一次的传输
        - level 1：至少一次的传输
        - level 2：只有一次的传输
        """
        try:
            self.client.will_set(pub_topic, json.dumps(payload), qos)
        except Exception as e:
            logger_error_debug(f'设置遗愿出错:{e}')
            raise

    def online(self, pub_topic: str, payload: Dict, qos: int = 2) -> None:
        """
        上线消息
        :param pub_topic: 发布的主题
        :param payload: 消息内容
        :param qos: 服务质量
        - level 0：最多一次的传输
        - level 1：至少一次的传输
        - level 2：只有一次的传输
        """
        try:
            self.client.publish(pub_topic, json.dumps(payload), qos)
        except Exception as e:
            logger_error_debug(f'上线消息出错:{e}')
            raise

    def destroy(self) -> None:
        """
        销毁MQTT客户端
        """
        if not self.client:
            return
        self.client.loop_stop()
        self.client = None
        # self.connect_status = False

    def loop_start(self) -> None:
        """
        启动MQTT客户端
        """
        if self.client.is_connected():
            return
        # 建立连接
        self.connect_server()
        self.client.loop_start()
        time.sleep(0.1)

    def loop_stop(self) -> None:
        """
        停止MQTT客户端
        """
        if not self.client.is_connected():
            return
        self.client.disconnect()
        self.client.loop_stop()
        # self.connect_status = False

    def publish(self, pub_topic: str, payload: Dict, qos: int = 2) -> None:
        """
        发布
        :param pub_topic: 发布的主题
        :param payload: 消息内容
        :param qos: 服务质量
        - level 0：最多一次的传输
        - level 1：至少一次的传输
        - level 2：只有一次的传输
        """
        self.client.publish(pub_topic, json.dumps(payload), qos)
        logger.info(f'发布的主题：{pub_topic}')
        logger.info(f'发布的payload：{payload}')

    def subscribe(self, sub_topic: str, qos: int = 2) -> None:
        """
        订阅
        :param sub_topic: 订阅的主题
        :param qos: 服务质量
        - level 0：最多一次的传输
        - level 1：至少一次的传输
        - level 2：只有一次的传输
        """
        self.client.subscribe(sub_topic, qos)
        logger.info(f'订阅的主题：{sub_topic}')

    def unsubscribe(self, sub_topic: str) -> None:
        """
        取消订阅
        :param sub_topic: 要取消订阅的主题
        """
        self.client.unsubscribe(sub_topic)
        logger.info(f'取消订阅的主题：{sub_topic}')

    def receive_msg(self) -> Tuple[str, str]:
        """
        接收消息
        :return: 返回接收到的消息
        """
        if not self.client.is_connected():
            return ''
        msg = self.queue.get_nowait()
        return msg

    def send_msg(self, pub_topic: str, sub_topic: str, payload: Dict, is_build_seq: bool = True) -> ResultData:
        """
        发送MQTT消息，并获取对应的响应消息
        :param pub_topic: 发布的主题
        :param sub_topic: 订阅的主题
        :param payload: 消息字典
        :param is_build_seq: 响应超时时间
        :return: 返回发送成功与否, 返回的消息内容
        """
        if not isinstance(payload, dict):
            msg = 'payload必须是字典类型'
            logger_error_debug(msg)
            return ResultData(False, msg)
        # 添加随机序列号
        if is_build_seq:
            seq = str(random_int(10**6, 10**8))
            payload['msgId'] = seq
        else:
            seq = payload['msgId']
        # 添加时间戳
        payload['timestamp'] = int(round(time.time() * 1000))
        # 发布消息
        self.subscribe(sub_topic)
        self.publish(pub_topic, payload)
        # 处理遗愿消息
        if 'lastwill' in pub_topic:
            msg = '遗愿发布完成'
            logger.info(msg)
            return ResultData(True, msg)
        # 根据序列号获取响应消息
        r = self.get_msg(sub_topic, expr={'msgId': seq})
        return r

    def send_reply(self, reply_topic: str, msgId: str, code: int = 0, data: Optional[Dict] = None):
        """
        发送MQTT响应消息
        :param reply_topic: 响应的主题
        :param msgId: 消息ID
        :param code: 响应的错误码
        :param data: 响应的数据
        """
        payload = {}
        payload['msgId'] = msgId
        payload['timestamp'] = int(round(time.time() * 1000))
        payload['code'] = code
        payload['message'] = 'AutoTester'
        payload['data'] = data
        self.publish(reply_topic, payload)

    def get_msg(self, sub_topic: str, expr: Optional[Dict] = None) -> ResultData:
        """
        获取MQTT消息
        :param sub_topic: 订阅的主题
        :param expr: 期望包含的字典
        :return: 返回获取消息成功与否, 返回的消息内容
        """
        try:
            stime = time.time()
            result = ResultData(False, '')
            m = ''
            while time.time() - stime < self.timeout:
                try:
                    time.sleep(0.1)
                    msg = self.receive_msg()
                    topic, m = msg
                    if topic != sub_topic:
                        self.queue.put(msg)
                        continue
                    m = json.loads(m)
                    if expr:
                        if _cmp_dict(expr, m):
                            result = ResultData(True, m)
                            break
                        else:
                            m = json.dumps(m)
                            msg = (topic, m)
                            self.queue.put(msg)
                            continue
                    else:
                        result = ResultData(True, m)
                        break
                except JSONDecodeError:
                    raise JSONDecodeError(f'消息不是JSON格式：{str(m)}')
                except Empty:
                    continue
            if m == '':
                raise ValueError(f'消息为空')
        except Exception as e:
            logger.error(f'获取消息异常：{e}')
            result = ResultData(False, e)
        self.unsubscribe(sub_topic)
        return result

    def listen(self, listen_topic: str, expr: Optional[Dict] = None) -> ResultData:
        """
        监听MQTT消息
        :param listen_topic: 监听的主题
        :param expr: 期望包含的字典
        :return: 返回监听成功与否, 返回的消息内容
        """
        self.subscribe(listen_topic)
        r = self.get_msg(listen_topic, expr)
        return r
