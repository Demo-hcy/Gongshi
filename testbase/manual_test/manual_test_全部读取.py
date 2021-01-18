from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.INFORSCREEN_COLORLIGHT_MODEL import Colorlight
from library.mqtt_lib.TSL_model.LAMP_YM103_1_L_R_KCT_MODEL import YM103_1_L_R_KCT
from library.mqtt_lib.TSL_model.SPEAKER_MODEL import Speaker
from library.mqtt_lib.TSL_model.SMARTBOX_MODEL import SmartBox


def all_read():
    mqtt_client = MQTTClient(host='192.168.49.68', port=1883)
    platform = PlatformController(mqtt_client)

    # inforscreen = Colorlight('1700002')
    inforscreen = Colorlight('3500002')
    # lamp = YM103_1_L_R_KCT('1700001')
    # speaker = Speaker('1700004')
    speaker = Speaker('3500004')
    # smartbox = SmartBox('03846600411')
    smartbox = SmartBox('03846600084')

    # 登录
    platform.will_set()
    platform.start()
    thread1 = ThreadWithReturnValue(target=platform.login_listen, args=(smartbox, True))
    thread2 = ThreadWithReturnValue(target=platform.login_listen, args=(inforscreen, True))
    # thread3 = ThreadWithReturnValue(target=platform.login_listen, args=(lamp, True))
    thread4 = ThreadWithReturnValue(target=platform.login_listen, args=(speaker, True))
    thread1.start()
    thread2.start()
    # thread3.start()
    thread4.start()

    platform.online()  # 平台上线

    r1 = thread1.join()
    r2 = thread2.join()
    # r3 = thread3.join()
    r4 = thread4.join()

    l = {}
    num = 1

    # 读取信息屏
    l['Colorlight'] = {}
    # 循环读取全部属性
    for i in range(num):
        l1 = {}
        for k, v in vars(inforscreen.properties).items():
            print('-' * 50)
            params = [v]
            r = platform.read(inforscreen, params, is_parsed=True)
            if r.result:
                l1.update(r.data_dict)
        l['Colorlight'][i] = l1
    # 单条发布读取全部属性
    r = platform.read(inforscreen, vars(inforscreen.properties).values(), is_parsed=True)
    l['Colorlight'][num] = r.data_dict

    # # 读取灯控
    # l['YM103_1_L_R_KCT'] = {}
    # # 循环读取全部属性
    # for i in range(num):
    #     l1 = {}
    #     for k, v in vars(lamp.properties).items():
    #         print('-' * 50)
    #         params = [v]
    #         r = platform.read(lamp, params, is_parsed=True)
    #         if r.result:
    #             l1.update(r.data_dict)
    #     l['YM103_1_L_R_KCT'][i] = l1
    # # 单条发布读取全部属性
    # r = platform.read(lamp, vars(lamp.properties).values(), is_parsed=True)
    # l['YM103_1_L_R_KCT'][num] = r.data_dict

    # 读取音柱
    l['Speaker'] = {}
    # 循环读取全部属性
    for i in range(num):
        l1 = {}
        for k, v in vars(speaker.properties).items():
            print('-' * 50)
            params = [v]
            r = platform.read(speaker, params, is_parsed=True)
            if r.result:
                l1.update(r.data_dict)
        l['Speaker'][i] = l1
    # 单条发布读取全部属性
    r = platform.read(speaker, vars(speaker.properties).values(), is_parsed=True)
    l['Speaker'][num] = r.data_dict

    ## 读取智盒
    l['SmartBox'] = {}
    # 循环读取全部属性
    for i in range(num):
        l1 = {}
        for k, v in vars(smartbox.properties).items():
            print('-' * 50)
            params = [v]
            r = platform.read(smartbox, params, is_parsed=True)
            if r.result:
                l1.update(r.data_dict)
        l['SmartBox'][i] = l1
    # 单条发布读取全部属性
    r = platform.read(smartbox, vars(smartbox.properties).values(), is_parsed=True)
    l['SmartBox'][num] = r.data_dict

    print('*' * 25, '解析数据如下', '*' * 25)
    pprint(l)
    platform.stop()


for i in range(100):
    all_read()