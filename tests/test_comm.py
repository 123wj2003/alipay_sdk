#!/usr/bin/python3
# @Time    : 2019-09-12
# @Author  : Kevin Kong (kfx2007@163.com)

from alipay.comm import Comm
from alipay.api import AliPay
import unittest


class TestComm(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.api = AliPay("2014072300007148", None, True)
        super(TestComm, self).__init__(*args, **kwargs)

    def test_sign(self):
        data = {
            "method":"alipay.mobile.public.menu.add",
            "charset": 'GBK',
            "sign_type": 'RSA2',
            "timestamp": '2014-07-24 03:07:50',
            "biz_content": '{"button":[{"actionParam":"ZFB_HFCZ","actionType":"out","name":"话费充值"},{"name":"查询","subButton":[{"actionParam":"ZFB_YECX","actionType":"out","name":"余额查询"},{"actionParam":"ZFB_LLCX","actionType":"out","name":"流量查询"},{"actionParam":"ZFB_HFCX","actionType":"out","name":"话费查询"}]},{"actionParam":"http://m.alipay.com","actionType":"link","name":"最新优惠"}]}',
            "version": "1.0"
        }

        a = self.api.comm.gen(data)
        s = 'app_id=2014072300007148&biz_content={"button":[{"actionParam":"ZFB_HFCZ","actionType":"out","name":"话费充值"},{"name":"查询","subButton":[{"actionParam":"ZFB_YECX","actionType":"out","name":"余额查询"},{"actionParam":"ZFB_LLCX","actionType":"out","name":"流量查询"},{"actionParam":"ZFB_HFCX","actionType":"out","name":"话费查询"}]},{"actionParam":"http://m.alipay.com","actionType":"link","name":"最新优惠"}]}&charset=GBK&method=alipay.mobile.public.menu.add&sign_type=RSA2&timestamp=2014-07-24 03:07:50&version=1.0'
        self.assertEqual(a, s)


if __name__ == "__main__":
    unittest.main()
