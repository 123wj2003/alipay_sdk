#!/usr/bin/python3
# @Time    : 2019-10-31
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from Crypto.PublicKey import RSA
from alipay.api import AliPay


class TestPay(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestPay, cls).setUpClass()
        with open("private.txt", "r") as f:
            private_key = RSA.importKey(f.read())
        cls.alipay = AliPay("2016101100664659", private_key, sandbox=True)

    def test_trade_create(self):
        """测试统一下单"""
        res = self.alipay.pay.trade_create("1572515083020","10","test")
        print(res)

    # def test_trade_pay(self):
    #     """测试同一下单接口"""
    #     res = self.alipay.pay.trade_pay(
    #         "5887941a66988732489", "bar_code", "q212312", "48797", product_code="ABC")
    #     print(res)


if __name__ == "__main__":
    unittest.main()
