#!/usr/bin/python3
# @Time    : 2019-09-12
# @Author  : Kevin Kong (kfx2007@163.com)

from alipay.comm import Comm

SANDBOX_URL = "https://openapi.alipaydev.com/gateway.do"
URL = "https://openapi.alipay.com/gateway.do"


class AliPay(object):

    def __init__(self, appid, public_key, sandbox=False):
        self.appid = appid
        self.url = SANDBOX_URL if sandbox else URL
        self.public_key = public_key

    comm = Comm()
