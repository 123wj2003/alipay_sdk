#!/usr/bin/python3
# @Time    : 2019-09-12
# @Author  : Kevin Kong (kfx2007@163.com)


class Comm(object):

    def __get__(self, instance, type):
        self.appid = instance.appid
        self.public_key = instance.public_key
        self.sign_type = instance.sign_type
        self.alipay_root_cert_sn = instance.alipay_root_cert_sn
        self.app_cert_sn = instance.app_cert_sn
        return self

    def gen(self, data, cert=False):
        """
        生成签名
        参数：
        data: 要签名的数据
        cert: 是否使用公钥证书的方式，默认普通公钥方式
        """
        data["app_id"] = self.appid
        if self.sign_type == "rsa_cert":
            data["alipay_root_cert_sn"] = self.alipay_root_cert_sn
            data["app_cert_sn"] = self.app_cert_sn
            return f"{'&'.join([f'{key}={data[key]}' for key in sorted(data) if data[key]])}"
        else:
            return f"{'&'.join([f'{key}={data[key]}' for key in sorted(data) if data[key]])}"
