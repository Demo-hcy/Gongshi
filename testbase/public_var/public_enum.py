from library.common import *


# 示例1
@unique
class DevType(Enum):
    """
    设备类型
    """
    lamp = 'Lamp'  # 灯控
    screen = 'InfoScreen'  # 信息屏
    speaker = 'Speaker'  # 广播
    camera = 'IPC-Onvif'  # 摄像头


# 示例2
@unique
class WlRespCode(Enum):
    """
    物联平台响应码
    code	说明
    000	操作成功
    001	操作失败
    002	认证无效或已过期
    003	系统错误
    004	账号过期或禁用
    005	参数异常
    006	参数无效
    007	参数不能为空
    008	设备不存在
    009	设备编号重复
    """
    sucess_code = '000'
    fail_code = '001'
    auto_fial = '002'
    sys_eror = '003'
    token_error = '004'
    param_error = '005'
    param_invalid = '006'
    param_miss = '007'
    dev_non_exists = '008'
    dev_duplicate = '009'


if __name__ == '__main__':
    print(DevType.lamp.value)
    print(enum_to_dict(WlRespCode))