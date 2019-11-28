#!/usr/bin/python3
# @Time    : 2019-11-27
# @Author  : Kevin Kong (kfx2007@163.com)

# 口碑相关接口

from functools import partial
from alipay.comm import Comm, isp_args
from autils import String

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

    @koubei
    def trade_itemorder_buy(self, out_order_no, subject, biz_product,
                            biz_scene, shop_id, buyer_id, total_amount,
                            timeout=None, promo_params=None, item_order_details=None):
        """
        口碑商品交易购买接口

        :param out_order_no: 商户订单号,64个字符以内、只能包含字母、数字、下划线；需保证在商户端不重复
        :param subject: 订单标题
        :param biz_product: 业务产品
        :param biz_scene: 业务场景
        :param shop_id: 门店ID
        :param buyer_id: 买家支付宝ID
        :param total_amount: 订单总金额，单位为元，精确到小数点后两位，必须等于费用之和
        :param promo_params: 商户传入营销信息，具体值要和口碑约定，格式为json格式
        :param item_order_details: 购买商品信息	
        :return: 返回数据
        """
        return self.post()

    @koubei
    def trade_itemorder_refund(self, order_no, out_request_no, refund_infos, reason=None):
        """
        口碑商品交易退货接口

        :param order_no: 口碑订单号		
        :param out_request_no: 标识一次退款请求，同一笔订单多次退款需要保证唯一	
        :param refund_infos: 退货明细信息	
        :param reason: 退款原因描述	
        :return: 返回数据
        """
        return self.post()

    @koubei
    def trade_ticket_ticketcode_send(self, isv_ma_list, send_order_no, send_token, order_no, request_id=String.generate_digits(32)):
        """
        码商发码成功回调接口

        :param isv_ma_list: 需要发送的码列表，其中code表示串码码值，num表示码的可核销份数
        :param send_order_no: 口碑商品发货单号
        :param send_token: 口碑发码通知透传码商，码商需要跟发码通知获取到的参数一致
        :param order_no: 口碑订单号
        :param request_id: 请求id，唯一标识一次请求，不传则由SDK自动生成
        :return: 返回数据
        """
        return self.post()

    @koubei
    def trade_ticket_ticketcode_delay(self, end_date, ticket_code, order_no, code_type='INTERNAL_CODE', request_id=String.generate_digits(32)):
        """
        口碑凭证延期接口

        :param end_date: 延至日期
        :param ticket_code: 凭证码
        :param order_no: 口碑订单号
        :param code_type: INTERNAL_CODE(券码),EXTERNAL_CODE(外部券码)
        :param request_id: 请求id，唯一标识一次请求，不传则由SDK自动生成
        :return: 返回数据
        """
        return self.post()
