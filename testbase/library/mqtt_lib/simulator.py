from .device_controller import *
from .platform_controller import *


class PlatformSimulator(PlatformController):
    def __init__(self, device: Device, mqtt_client: MQTTClient, is_start: bool = True) -> None:
        super().__init__(mqtt_client, is_start=is_start)
        self.device = device

    def read(self, properties: List[BaseProperty], is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().read(self.device, properties, is_parsed)
        return r.result, r.data_dict

    def set(self,
            properties: List[BaseProperty],
            is_validate: bool = False,
            is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().set(self.device, properties, is_validate, is_parsed)
        return r.result, r.data_dict

    def service_invoke(self,
                       service: BaseService,
                       data: Dict = None,
                       is_validate: bool = False,
                       check_property: BaseProperty = None,
                       is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().service_invoke(self.device, service, data, is_validate, check_property, is_parsed)
        return r.result, r.data_dict

    def switch_sys_mode(self, mode: SysMode, is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().switch_sys_mode(self.device, mode, is_parsed)
        return r.result, r.data_dict

    def report_listen(self,
                      properties: List[BaseProperty] = None,
                      is_reply: bool = False,
                      code: int = 0,
                      is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().report_listen(self.device, properties, is_reply, code, is_parsed)
        return r.result, r.data_dict

    def report_reply(self, msgId: str, properties: List[BaseProperty], code: int = 0) -> None:
        super().report_reply(self.device, msgId, properties, code)

    def event_report_listen(self,
                            event: BaseEvent,
                            is_reply: bool = False,
                            code: int = 0,
                            is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().event_report_listen(self.device, event, is_reply, code, is_parsed)
        return r.result, r.data_dict

    def event_report_reply(self, msgId: str, event: BaseEvent, code: int = 0) -> None:
        super().event_report_reply(self.device, msgId, event, code)

    def lastwill_listen(self, is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().lastwill_listen(self.device, is_parsed)
        return r.result, r.data_dict

    def login_listen(self, is_reply: bool = False, code: int = 0, is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().login_listen(self.device, is_reply, code, is_parsed)
        return r.result, r.data_dict

    def login_reply(self, msgId: str, code: int = 0) -> None:
        super().login_reply(self.device, msgId, code)

    def sys_info_report_listen(self,
                               is_reply: bool = False,
                               code: int = 0,
                               is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().sys_info_report_listen(self.device, is_reply, code, is_parsed)
        return r.result, r.data_dict

    def sys_info_report_reply(self, msgId: str, code: int = 0) -> None:
        super().sys_info_report_reply(self.device, msgId, code)


class DeviceSimulator(DeviceController):
    def __init__(self, device: Device, mqtt_client: MQTTClient, is_start: bool = True) -> None:
        super().__init__(mqtt_client, is_start=is_start)
        self.device = device

    def report(self,
               properties: List[BaseProperty],
               is_validate: bool = False,
               is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().report(self.device, properties, is_validate, is_parsed)
        return r.result, r.data_dict

    def event_report(self, event: BaseEvent, is_validate: bool = False, is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().event_report(self.device, event, is_validate, is_parsed)
        return r.result, r.data_dict

    def will_set(self) -> None:
        super().will_set(self.device)

    def login(self, salt_len: int = 16, is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().login(self.device, salt_len, is_parsed)
        return r.result, r.data_dict

    def sys_info_report(self,
                        mode: SysMode,
                        ntp_info: Dict,
                        network_info: Dict,
                        mqtt_info: Dict,
                        is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().sys_info_report(self.device, mode, ntp_info, network_info, mqtt_info, is_parsed)
        return r.result, r.data_dict

    def read_listen(self,
                    properties: List[BaseProperty] = None,
                    is_reply: bool = False,
                    code: int = 0,
                    is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().read_listen(self.device, properties, is_reply, code, is_parsed)
        return r.result, r.data_dict

    def read_reply(self, msgId: str, properties: List[BaseProperty], code: int = 0) -> None:
        super().read_reply(self.device, msgId, properties, code)

    def set_listen(self,
                   properties: List[BaseProperty] = None,
                   is_reply: bool = False,
                   code: int = 0,
                   is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().set_listen(self.device, properties, is_reply, code, is_parsed)
        return r.result, r.data_dict

    def set_reply(self, msgId: str, properties: List[BaseProperty], code: int = 0) -> None:
        super().set_reply(self.device, msgId, properties, code)

    def service_invoke_listen(self,
                              service: BaseService,
                              is_reply: bool = False,
                              code: int = 0,
                              is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().service_invoke_listen(self.device, service, is_reply, code, is_parsed)
        return r.result, r.data_dict

    def service_invoke_reply(self, msgId: str, service: BaseService, code: int = 0) -> None:
        super().service_invoke_reply(self.device, msgId, service, code)

    def lastwill_listen(self, is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().lastwill_listen(self.device, is_parsed)
        return r.result, r.data_dict

    def online_listen(self, is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().online_listen(self.device, is_parsed)
        return r.result, r.data_dict

    def switch_sys_mode_listen(self,
                               is_reply: bool = False,
                               code: int = 0,
                               is_parsed: bool = False) -> Tuple[bool, dict]:
        r = super().switch_sys_mode_listen(self.device, is_reply, code, is_parsed)
        return r.result, r.data_dict

    def switch_sys_mode_reply(self, msgId: str, code: int = 0) -> None:
        super().switch_sys_mode_reply(self.device, msgId, code)
