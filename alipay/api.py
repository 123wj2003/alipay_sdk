#!/usr/bin/python3
# @Time    : 2019-09-12
# @Author  : Kevin Kong (kfx2007@163.com)

from alipay.comm import Comm

SANDBOX_URL = "https://openapi.alipaydev.com/gateway.do"
URL = "https://openapi.alipay.com/gateway.do"


class AliPay(object):

    def __init__(self, appid, public_key, sign_type="rsa", app_cert_sn=None, alipay_root_cert_sn=None, sandbox=False):
        """
        初始化API
        参数：
        appid: 应用id
        public_key: 公钥
        app_cert_sn: 应用公钥证书SN
        alipay_root_cert_sn: 支付宝根证书SN
        sign_type: 签名方式(普通公钥rsa和公钥证书rsa_cert两种)
        """
        self.appid = appid
        self.url = SANDBOX_URL if sandbox else URL
        self.public_key = public_key
        self.sign_type = sign_type
        self.app_cert_sn = app_cert_sn
        self.alipay_root_cert_sn = alipay_root_cert_sn

    comm = Comm()
