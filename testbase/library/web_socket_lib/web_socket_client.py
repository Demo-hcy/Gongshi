from ..common import *
import time
import random
import string


class WebSocketClient:
    def __init__(self, box_id: str, ws_url: str) -> None:
        self.box_id = box_id
        self.ws_url = ws_url
        self.console_id = 'console4'

    @staticmethod
    def build_msg_seq():
        time_str = time.strftime("%Y%m%d%H%M%S", time.localtime())
        rand_str_list = random.sample(string.ascii_lowercase, 4)
        return time_str + '_' + "".join(rand_str_list)

    async def send_method(self, send_dict, assert_func, recv_time=60, *args):
        # 通过websocket发送数据到iot_server
        pass

    async def api_result(self, msg_id, timeout=15):
        # 下发命令后获取对应msg_id的响应消息,最大响应时间timeoutm,默认超时15s
        pass

    async def dev_upload_msg(self, dev_id, time_out=15, before_times=2):
        # 从send_dict获取设备id在指定时间内的上报信息
        pass

    def websocket_rsp(self, msg_id=None, dev_id=None, timeout=15, send_task=None):
        # 获取websockt的响应和反推的消息
        pass

    def websockt_send_msg(self, data, dev_id=None, timeout=15):
        # 向指定的盒子发送websockt请求,并打印对应的响应信息
        pass
