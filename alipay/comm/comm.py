#!/usr/bin/python3
# @Time    : 2019-09-12
# @Author  : Kevin Kong (kfx2007@163.com)

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256, SHA
import base64


class Comm(object):

    def __get__(self, instance, type):
        self.appid = instance.appid
        self.app_private_key = instance.app_private_key
        self.sign_type = instance.sign_type
        self.alipay_root_cert_sn = instance.alipay_root_cert_sn
        self.app_cert_sn = instance.app_cert_sn
        return self

    def get_signstr(self, data):
        """
        生成签名
        参数：
        data: 要签名的数据
        """
        data["app_id"] = self.appid
        if self.alipay_root_cert_sn and self.app_cert_sn:
            data["alipay_root_cert_sn"] = self.alipay_root_cert_sn
            data["app_cert_sn"] = self.app_cert_sn
            return f"{'&'.join([f'{key}={data[key]}' for key in sorted(data) if data[key]])}"
        else:
            return f"{'&'.join([f'{key}={data[key]}' for key in sorted(data) if data[key]])}"

    def gen(self, str):
        """
        签名
        """
        if self.sign_type == "RSA":
            to_sign = SHA.new(str.encode('utf-8'))
        else:
            to_sign = SHA256.new(str.encode('utf-8'))
        return base64.b64encode(PKCS1_v1_5.new(self.app_private_key).sign(to_sign)).decode("utf-8")
