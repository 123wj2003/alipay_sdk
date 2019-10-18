from alipay.comm import Comm
from alipay.api import AliPay
import unittest

from Crypto.PublicKey import RSA


class TestSign(unittest.TestCase):

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
