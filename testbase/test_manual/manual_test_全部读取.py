from library.common import *
from library.mqtt_lib.mqtt_client import MQTTClient
from library.mqtt_lib.mqtt_controller import PlatformController
from library.mqtt_lib.TSL_model.S3_KLT_C4_MODEL import S3_KLT_C4
from library.mqtt_lib.TSL_model.S4_7G_SPEAKER_MODEL import S4_QG_SPEAKER
from library.mqtt_lib.TSL_model.S1_7G_SMARTBOX_MODEL import S1_QG_SMARTBOX
from library.mqtt_lib.TSL_model.S6_YM_1031LRKCT_MODEL import S6_YM_1031LRKCT
from library.mqtt_lib.TSL_model.S9_7G_AI_MODEL import S9_QG_AI
from library.mqtt_lib.TSL_model.S5_DH_SD6A9233XAHNT_MODEL import S5_DH_SD6A9233XAHNT
from library.mqtt_lib.TSL_model.S2_7G_GDH_MODEL import S2_QG_GDH
from library.mqtt_lib.TSL_model.S3_DH_ITSXS170127RGAB_MODEL import S3_DH_ITSXS170127RGAB
from library.mqtt_lib.TSL_model.S8_RLY_RUILONJGS869_MODEL import S8_RLY_RUILONJGS869
from library.mqtt_lib.TSL_model.S3_KLT_A35_MODEL import S3_KLT_A35


def all_read():
    mqtt_client = MQTTClient(host='192.168.49.96', port=1883)
    platform = PlatformController(mqtt_client)

    Inforscreen = S3_KLT_C4('1700002')
    Lamp = S6_YM_1031LRKCT('1700001')
    Speaker = S4_QG_SPEAKER('1700004')
    # SmartBox = S1_QG_SMARTBOX('04132500855')
    SmartBox = S1_QG_SMARTBOX('03846600411')
    AI = S9_QG_AI('1700003')
    IPCOnvif = S5_DH_SD6A9233XAHNT('1700005')
    Power = S2_QG_GDH('1700009')
    Trafficscreen = S3_DH_ITSXS170127RGAB('1700008')
    Inforscreen35 = S3_KLT_A35('1700010')
    Locker = S8_RLY_RUILONJGS869('1700006')

    # 登录
    # platform.will_set()
    # platform.start()
    # thread1 = ThreadWithReturnValue(target=platform.login_listen, args=(SmartBox, True))
    # thread2 = ThreadWithReturnValue(target=platform.login_listen, args=(Inforscreen, True))
    # thread3 = ThreadWithReturnValue(target=platform.login_listen, args=(Lamp, True))
    # thread4 = ThreadWithReturnValue(target=platform.login_listen, args=(Speaker, True))
    # thread5 = ThreadWithReturnValue(target=platform.login_listen, args=(AI, True))
    # thread6 = ThreadWithReturnValue(target=platform.login_listen, args=(IPCOnvif, True))
    # thread7 = ThreadWithReturnValue(target=platform.login_listen, args=(Power, True))
    # thread8 = ThreadWithReturnValue(target=platform.login_listen, args=(Trafficscreen, True))
    # thread9 = ThreadWithReturnValue(target=platform.login_listen, args=(Inforscreen35, True))
    # thread10 = ThreadWithReturnValue(target=platform.login_listen, args=(Locker, True))
    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
    # thread5.start()
    # thread6.start()
    # thread7.start()
    # thread8.start()
    # thread9.start()
    # thread10.start()

    # platform.online()  # 平台上线

    # r1 = thread1.join()
    # r2 = thread2.join()
    # r3 = thread3.join()
    # r4 = thread4.join()
    # r5 = thread5.join()
    # r6 = thread6.join()
    # r7 = thread7.join()
    # r8 = thread8.join()
    # r9 = thread9.join()
    # r10 = thread10.join()

    l = {}
    num = 1

    # # 读取信息屏
    # l['Inforscreen'] = {}
    # # 循环读取全部属性
    # for i in range(num):
    #     l1 = {}
    #     for k, v in vars(Inforscreen.properties).items():
    #         print('-' * 50)
    #         params = [v]
    #         r = platform.read(Inforscreen, params, is_parsed=True)
    #         if r.result:
    #             l1.update(r.data_dict)
    #     l['Inforscreen'][str(i)] = l1
    # # 单条发布读取全部属性
    # r = platform.read(Inforscreen, vars(Inforscreen.properties).values(), is_parsed=True)
    # l['Inforscreen'][str(num)] = r.data_dict

    # # 读取灯控
    # l['Lamp'] = {}
    # # 循环读取全部属性
    # for i in range(num):
    #     l1 = {}
    #     for k, v in vars(Lamp.properties).items():
    #         print('-' * 50)
    #         params = [v]
    #         r = platform.read(Lamp, params, is_parsed=True)
    #         if r.result:
    #             l1.update(r.data_dict)
    #     l['Lamp'][str(i)] = l1
    # # 单条发布读取全部属性
    # r = platform.read(Lamp, vars(Lamp.properties).values(), is_parsed=True)
    # l['Lamp'][str(num)] = r.data_dict

    # # 读取音柱
    # l['Speaker'] = {}
    # # 循环读取全部属性
    # for i in range(num):
    #     l1 = {}
    #     for k, v in vars(Speaker.properties).items():
    #         print('-' * 50)
    #         params = [v]
    #         r = platform.read(Speaker, params, is_parsed=True)
    #         if r.result:
    #             l1.update(r.data_dict)
    #     l['Speaker'][str(i)] = l1
    # # 单条发布读取全部属性
    # r = platform.read(Speaker, vars(Speaker.properties).values(), is_parsed=True)
    # l['Speaker'][str(num)] = r.data_dict

    # 读取智盒
    l['SmartBox'] = {}
    # 循环读取全部属性
    for i in range(num):
        l1 = {}
        for k, v in vars(SmartBox.properties).items():
            print('-' * 50)
            params = [v]
            r = platform.read(SmartBox, params, is_parsed=True)
            if r.result:
                l1.update(r.data_dict)
        l['SmartBox'][str(i)] = l1
    # 单条发布读取全部属性
    r = platform.read(SmartBox, vars(SmartBox.properties).values(), is_parsed=True)
    l['SmartBox'][str(num)] = r.data_dict

    # # 读取AI
    # l['AI'] = {}
    # # 循环读取全部属性
    # for i in range(num):
    #     l1 = {}
    #     for k, v in vars(AI.properties).items():
    #         print('-' * 50)
    #         params = [v]
    #         r = platform.read(AI, params, is_parsed=True)
    #         if r.result:
    #             l1.update(r.data_dict)
    #     l['AI'][str(i)] = l1
    # # 单条发布读取全部属性
    # r = platform.read(AI, vars(AI.properties).values(), is_parsed=True)
    # l['AI'][str(num)] = r.data_dict

    # # 读取摄像头
    # l['IPCOnvif'] = {}
    # # 循环读取全部属性
    # for i in range(num):
    #     l1 = {}
    #     for k, v in vars(IPCOnvif.properties).items():
    #         print('-' * 50)
    #         params = [v]
    #         r = platform.read(IPCOnvif, params, is_parsed=True)
    #         if r.result:
    #             l1.update(r.data_dict)
    #     l['IPCOnvif'][str(i)] = l1
    # # 单条发布读取全部属性
    # r = platform.read(IPCOnvif, vars(IPCOnvif.properties).values(), is_parsed=True)
    # l['IPCOnvif'][str(num)] = r.data_dict

    # # 读取智能电源
    # l['Power'] = {}
    # # 循环读取全部属性
    # for i in range(num):
    #     l1 = {}
    #     for k, v in vars(Power.properties).items():
    #         print('-' * 50)
    #         params = [v]
    #         r = platform.read(Power, params, is_parsed=True)
    #         if r.result:
    #             l1.update(r.data_dict)
    #     l['Power'][str(i)] = l1
    # # 单条发布读取全部属性
    # r = platform.read(Power, vars(Power.properties).values(), is_parsed=True)
    # l['Power'][str(num)] = r.data_dict

    # # 读取交通屏
    # l['Trafficscreen'] = {}
    # # 循环读取全部属性
    # for i in range(num):
    #     l1 = {}
    #     for k, v in vars(Trafficscreen.properties).items():
    #         print('-' * 50)
    #         params = [v]
    #         r = platform.read(Trafficscreen, params, is_parsed=True)
    #         if r.result:
    #             l1.update(r.data_dict)
    #     l['Trafficscreen'][str(i)] = l1
    # # 单条发布读取全部属性
    # r = platform.read(Trafficscreen, vars(Trafficscreen.properties).values(), is_parsed=True)
    # l['Trafficscreen'][str(num)] = r.data_dict

    # # 读取信息屏A35
    # l['Inforscreen35'] = {}
    # # 循环读取全部属性
    # for i in range(num):
    #     l1 = {}
    #     for k, v in vars(Inforscreen35.properties).items():
    #         print('-' * 50)
    #         params = [v]
    #         r = platform.read(Inforscreen35, params, is_parsed=True)
    #         if r.result:
    #             l1.update(r.data_dict)
    #     l['Inforscreen35'][str(i)] = l1
    # # 单条发布读取全部属性
    # r = platform.read(Inforscreen35, vars(Inforscreen35.properties).values(), is_parsed=True)
    # l['Inforscreen35'][str(num)] = r.data_dict

    # # 读取门锁
    # l['Locker'] = {}
    # # 循环读取全部属性
    # for i in range(num):
    #     l1 = {}
    #     for k, v in vars(Locker.properties).items():
    #         print('-' * 50)
    #         params = [v]
    #         r = platform.read(Locker, params, is_parsed=True)
    #         if r.result:
    #             l1.update(r.data_dict)
    #     l['Locker'][str(i)] = l1
    # # 单条发布读取全部属性
    # r = platform.read(Locker, vars(Locker.properties).values(), is_parsed=True)
    # l['Locker'][str(num)] = r.data_dict

    print('*' * 25, '解析数据如下', '*' * 25)
    pprint(l)
    platform.stop()


for i in range(1):
    all_read()