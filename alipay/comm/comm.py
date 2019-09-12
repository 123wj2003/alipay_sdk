#!/usr/bin/python3
# @Time    : 2019-09-12
# @Author  : Kevin Kong (kfx2007@163.com)


class Comm(object):

    def __get__(self, instance, type):
        self.appid = instance.appid
        self.public_key = instance.public_key
        return self

    def gen(self, data, cert=False):
        """
        生成签名
        参数：
        data: 要签名的数据
        cert: 是否使用公钥证书的方式，默认公钥
        """
        if cert:
            pass
        else:
            tosign = "&".join(
                [f"{key}={data[key]}" for key in sorted(data) if data[key]])
            tosign = f"app_id={self.appid}&{tosign}"
        return tosign
