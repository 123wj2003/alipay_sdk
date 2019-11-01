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
        v_s = "b5UyLbGui7uUSK5bNZrxQO+wjI4XySnjpT9ODpPx0L45886RsPSfFWfTjXYzAkuRKADJrRYpkk41TBsUhhp4dLPJwU6H/R90NZgQ8hIxKn1in0+GK3hDEJOaiO+bEPLGSNAC2iiyAoEBz1llNkP6EQBgBi7JaiNaASBXrh0gFpZ7X8dKlTSsx7jeDYULlxKbS3EXaIZnx3Jnv/LDBjXuaWNjUoc7v8bLHF8LNDsOQ5MxuGdijVY/rOAnNocCCxYCuftErxhGtqCfxuhKdkLJc4+T5+5VejwR8wcUZLk1PYkU6sF7qs6+YfjLUyFFakLVCXx+BpzXrNDbQU49L1vXgA=="
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
        v_s = "N/ZcddFYAgPCkHQE5GcvK0vqaxYJhTsAvP9E54Kd4iYcGWY6eWwS56UOyHFelCI7ONOhmHKz/vRTndBQngXoQYNq+U+/e/9wrS4uT/4VMWpnivegvooaVYnGgrdWBIseE33G41xlEZZLXnaA0KShC9H6n2vIrP9Jgx93g4mU2S+ExJttY4rtgQJoJXKlXV1a8DHMoXY5flLF6hbLOUzonLpCnwbdU7L2DV5pHkNwkP38iACqbbTqDy6SQyoFrOhkmZAk1J6m79oTB1lmekO56c+FjYPZ+hegEWVwYqM1cpB3JYUDVZ+EBTIUewOq3U+f8CreJkkf3OjI32d3mGFWCg=="
        self.assertEqual(api.comm.gen(s),v_s)


if __name__ == "__main__":
    unittest.main()
