#!/usr/bin/python3
# @Time    : 2019-09-12
# @Author  : Kevin Kong (kfx2007@163.com)

from Crypto.PublicKey import RSA
from alipay.comm import Comm
from alipay.api import AliPay
import unittest


class TestComm(unittest.TestCase):    

    def test_sign(self):
        """RSA生成待签名字符"""
        self.api = AliPay("2014072300007148", None, sandbox=True)
        data = {
            "method": "alipay.mobile.public.menu.add",
            "charset": 'GBK',
            "sign_type": 'RSA2',
            "timestamp": '2014-07-24 03:07:50',
            "biz_content": '{"button":[{"actionParam":"ZFB_HFCZ","actionType":"out","name":"话费充值"},{"name":"查询","subButton":[{"actionParam":"ZFB_YECX","actionType":"out","name":"余额查询"},{"actionParam":"ZFB_LLCX","actionType":"out","name":"流量查询"},{"actionParam":"ZFB_HFCX","actionType":"out","name":"话费查询"}]},{"actionParam":"http://m.alipay.com","actionType":"link","name":"最新优惠"}]}',
            "version": "1.0"
        }

        a = self.api.comm.get_signstr(data)
        s = 'app_id=2014072300007148&biz_content={"button":[{"actionParam":"ZFB_HFCZ","actionType":"out","name":"话费充值"},{"name":"查询","subButton":[{"actionParam":"ZFB_YECX","actionType":"out","name":"余额查询"},{"actionParam":"ZFB_LLCX","actionType":"out","name":"流量查询"},{"actionParam":"ZFB_HFCX","actionType":"out","name":"话费查询"}]},{"actionParam":"http://m.alipay.com","actionType":"link","name":"最新优惠"}]}&charset=GBK&method=alipay.mobile.public.menu.add&sign_type=RSA2&timestamp=2014-07-24 03:07:50&version=1.0'
        self.assertEqual(a, s)

    def test_sign_cert(self):
        """RSA证书生成待签名字符"""
        self.api = AliPay("2014072300007148", None, sign_type="rsa_cert", app_cert_sn="50fa7bc5dc305a4fbdbe166689ddc827",
                          alipay_root_cert_sn="6bc29aa3b4d406c43483ffea81e08d22", sandbox=True)
        data = {
            "method": "alipay.mobile.public.menu.add",
            "charset": 'GBK',
            "sign_type": 'RSA2',
            "timestamp": '2014-07-24 03:07:50',
            "biz_content": '{"button":[{"actionParam":"ZFB_HFCZ","actionType":"out","name":"话费充值"},{"name":"查询","subButton":[{"actionParam":"ZFB_YECX","actionType":"out","name":"余额查询"},{"actionParam":"ZFB_LLCX","actionType":"out","name":"流量查询"},{"actionParam":"ZFB_HFCX","actionType":"out","name":"话费查询"}]},{"actionParam":"http://m.alipay.com","actionType":"link","name":"最新优惠"}]}',
            "version": "1.0"
        }
        a = self.api.comm.get_signstr(data)
        s = 'alipay_root_cert_sn=6bc29aa3b4d406c43483ffea81e08d22&app_cert_sn=50fa7bc5dc305a4fbdbe166689ddc827&app_id=2014072300007148&biz_content={"button":[{"actionParam":"ZFB_HFCZ","actionType":"out","name":"话费充值"},{"name":"查询","subButton":[{"actionParam":"ZFB_YECX","actionType":"out","name":"余额查询"},{"actionParam":"ZFB_LLCX","actionType":"out","name":"流量查询"},{"actionParam":"ZFB_HFCX","actionType":"out","name":"话费查询"}]},{"actionParam":"http://m.alipay.com","actionType":"link","name":"最新优惠"}]}&charset=GBK&method=alipay.mobile.public.menu.add&sign_type=RSA2&timestamp=2014-07-24 03:07:50&version=1.0'
        self.assertEqual(a, s)

    def test_sign_rsa(self):
        """验证签名"""
        with open("private.txt", "r") as f:
            private_key = RSA.importKey(f.read())
        api = AliPay("2016101100664659", private_key, sandbox=True)

        data = {
            "method": "alipay.mobile.public.menu.add",
            "charset": 'GBK',
            "sign_type": 'RSA',
            "timestamp": '2014-07-24 03:07:50',
            "biz_content": '123',
            "version": "1.0"
        }

        s = api.comm.get_signstr(data)
        v_s = "UiAfIxH7qr0onTagAiTMMI/vtwI7vCYhY3RKAJk2n/skWSQFrFkjBONgCUaDO4GL8QKFn02MPrBe1nIQXsp48dC0eQ0BzL6SRPVPBlr2MxsWYhmX7Eq+WRl8rn16t9hq+8qYXwv43Q2U66PlaRfq34zU6108Djb0tZIKV9qokSvwFbNVcIrxbYJVkD18rHXyUIItEwAxJ7gCijaVQ66LIZ2xFONOGA4mQi3PDqcExDtpNgI5wouOWZo/BL/Alns5dEMLjuwWu1Qfa+Fc84KCZKSRYrHvfEMIc98Q9DRD0TjIntbeVLMVrADcfpCl6MPVHItUEaoNH9fzGdTEomQY8w=="
        self.assertEqual(api.comm.gen(s),v_s)

    def test_sign_rsa2(self):
        """RSA2签名验证"""
        with open("private.txt", "r") as f:
            private_key = RSA.importKey(f.read())
        api = AliPay("2016101100664659", private_key,sign_type="rsa2",sandbox=True)

        data = {
            "method": "alipay.mobile.public.menu.add",
            "charset": 'GBK',
            "sign_type": 'RSA2',
            "timestamp": '2014-07-24 03:07:50',
            "biz_content": '123',
            "version": "1.0"
        }

        s = api.comm.get_signstr(data)
        v = api.comm.gen(s)
        v_s = "dZ0Zl4UdnqIFRywQCRJFJB5AWnMLjLtKdyyyfa5DX89pZgV/+FlKhDPOiHy0WzI7sXEyk10adyX8JekWtKXEmnrvWbiKM/bNiP+nTKxPH/YsFmW1+p6PSuLG2BUvBmlwX5j3u+CCSoWjAa4DsYqXd275sGoaF933wdrgUzIQMo5zspeAncjLepA6on1ZDYAaRRNfWL58XQKvg05iTSO9IpqQUoDhFPZ2NFahwMSCLsv8e1QHx3bFzqD0MVos12J2ez9WaELrcfz58IUO5utVbCIsFSHZJVmrk/bzcnK9GLDuemL/mD9qlQfzngm4XhyNopemo2naMlntj4OcoisZqA=="
        self.assertEqual(api.comm.gen(s),v_s)


if __name__ == "__main__":
    unittest.main()
