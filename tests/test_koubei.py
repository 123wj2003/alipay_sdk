#!/usr/bin/python3
# @Time    : 2019-11-27
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from Crypto.PublicKey import RSA
from alipay.api import AliPay


class KoubeiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(KoubeiTest, cls).setUpClass()
        with open("private.txt", "r") as f:
            private_key = RSA.importKey(f.read())
        cls.alipay = AliPay("2016101100664659", private_key,
                            sign_type="rsa2", sandbox=True)
        cls.buyer_id = "2088102179514385"

    def test_koubei_trade_itemorder_query(self):
        """
        测试口碑商品交易查询接口
        """
        res = self.alipay.koubei.trade_itemorder_query("123456")
        self.assertIn(res['code'], ['40006'], msg=res)

    def test_koubei_trade_itemorder_buy(self):
        """
        测试口碑商品交易购买接口
        """
        res = self.alipay.koubei.trade_itemorder_buy(
            "11223344", "测试口碑购买", "ABC", "测试场景", "1", "abcde", 20)
        self.assertIn(res['code'], ['40006'], msg=res)

    def test_koubei_trade_itemorder_refund(self):
        """
        测试口碑商品交易退货接口
        """
        res = self.alipay.koubei.trade_itemorder_refund(
            "11223344", "00000", {"item_order_no": "12312", "amount": 10})
        self.assertIn(res['code'], ['40006'], msg=res)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(KoubeiTest("test_koubei_trade_itemorder_query"))
    suite.addTest(KoubeiTest("test_koubei_trade_itemorder_buy"))
    suite.addTest(KoubeiTest("test_koubei_trade_itemorder_refund"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
