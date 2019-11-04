#!/usr/bin/python3
# @Time    : 2019-09-12
# @Author  : Kevin Kong (kfx2007@163.com)

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256, SHA
import base64
from itertools import zip_longest
from datetime import datetime
import requests
import inspect
from urllib.parse import quote_plus, urlencode, quote
import json
import traceback


def isp_args(func):

    def inner(self, *args, **kwarg):
        """
        提交方法的装饰器
        封装参数
        """
        print(args, kwarg)
        ags = inspect.getfullargspec(func).args
        print(ags)
        ags.pop(0)
        data = dict(zip_longest(ags, args))
        data.update(kwarg)
        data = {key: value for key, value in data.items() if value}
        self.method = f"alipay.{func.__name__.replace('_','.')}"
        self.data = data
        return func(self, *args, **kwarg)
    return inner


class Comm(object):

    def __get__(self, instance, type):
        self.url = instance.url
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

    def _get_comm_args(self):
        """
        获取公共请求参数
        """
        data = {
            "app_id": self.appid,
            "format": "JSON",
            "charset": "utf-8",
            "sign_type": self.sign_type,
            "timestamp": datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
            "version": "1.0",
            "notify_url": None,
            "app_auth_token": None,
            "method": self.method
        }

        return data

    def _pre_response(self, response):
        """
        处理响应报文
        """
        if type(response) is not dict:
            raise TypeError("服务器响应异常")

        prefix = f"{self.method.replace('.','_')}_response"
        return response.get(prefix)

    def _get_request_url(self):
        """
        生成请求地址
        """
        data = self._get_comm_args()
        # 过滤参数为None的参数
        data = {key: value for key, value in data.items() if value}
        data["biz_content"] = json.dumps(self.data)
        data["sign"] = self.gen(self.get_signstr(data))
        return f"{self.url}?{urlencode(data)}"

    def post(self):
        """
        提交请求的方法
        参数：
            data: 接口的参数数据
        """
        try:
            response = requests.get(self._get_request_url())
            print(response.content)
            return self._pre_response(response.json())
        except Exception as err:
            raise Exception(f"接口请求错误：{traceback.format_exc()}")
