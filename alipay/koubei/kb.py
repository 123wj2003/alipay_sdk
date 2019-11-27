#!/usr/bin/python3
# @Time    : 2019-11-27
# @Author  : Kevin Kong (kfx2007@163.com)

# 口碑相关接口

from functools import partial
from alipay.comm import Comm, isp_args

koubei = partial(isp_args, method="koubei")

class KouBei(Comm):

    @koubei
    def trade_itemorder_query(self, order_no):
        """
        口碑商品交易查询接口
        参数：
            order_no: string 64 口碑订单号
        """
        return self.post()
