from builtins import str as str15, int as int20, RuntimeError as RuntimeError49
from typing import Union as Union18
from concurrent.futures import Future as Future78
from abc import ABCMeta as ABCMeta48, abstractmethod as abstractmethod51
from temper_core import std_net_send as std_net_send77
std_net_send_2636 = std_net_send77
class NetRequest:
    '*NetRequest* is a builder class for an HTTP send.\nNone of the methods except *send* actually initiate anything.'
    url_17: 'str15'
    method_18: 'str15'
    body_content_19: 'Union18[str15, None]'
    body_mime_type_20: 'Union18[str15, None]'
    __slots__ = ('url_17', 'method_18', 'body_content_19', 'body_mime_type_20')
    def post(this_0, content_22: 'str15', mime_type_23: 'str15') -> 'None':
        '*Post* switches the HTTP method to "POST" and makes sure that\na body with the given textual content and mime-type will be sent\nalong.\n\nthis__0: NetRequest\n\ncontent__22: String\n\nmimeType__23: String\n'
        this_0.method_18 = 'POST'
        this_0.body_content_19 = content_22
        t_50: 'Union18[str15, None]' = this_0.body_mime_type_20
        this_0.body_mime_type_20 = t_50
    def send(this_1) -> 'Future78[NetResponse]':
        '*Send* makes a best effort to actual send an HTTP method.\nBackends may or may not support all request features in which\ncase, send should return a broken promise.\n\nthis__1: NetRequest\n'
        return std_net_send_2636(this_1.url_17, this_1.method_18, this_1.body_content_19, this_1.body_mime_type_20)
    def __init__(this_5, url_28: 'str15') -> None:
        this_5.url_17 = url_28
        this_5.method_18 = 'GET'
        this_5.body_content_19 = None
        this_5.body_mime_type_20 = None
class NetResponse(metaclass = ABCMeta48):
    @property
    @abstractmethod51
    def status(self) -> 'int20':
        pass
    @property
    @abstractmethod51
    def content_type(self) -> 'Union18[str15, None]':
        pass
    @property
    @abstractmethod51
    def body_content(self) -> 'Future78[(Union18[str15, None])]':
        pass
def send_request_16(url_35: 'str15', method_36: 'str15', body_content_37: 'Union18[str15, None]', body_mime_type_38: 'Union18[str15, None]') -> 'Future78[NetResponse]':
    raise RuntimeError49()
