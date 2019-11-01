#!/usr/bin/python3
# @Time    : 2019-10-31
# @Author  : Kevin Kong (kfx2007@163.com)

# 支付宝当面付
# 包含 条码支付、扫码支付两个业务场景

from alipay.comm import Comm, isp_args
import inspect


class Pay(Comm):

    @isp_args
    def trade_create(self, out_trade_no, total_amount, subject,
                     body=None, buyer_id=None, discountable_amount=None, seller_id=None,
                     goods_detail=None, product_code=None, operator_id=None, store_id=None, terminal_id=None,
                     extend_params=None, timeout_express=None, settle_info=None, logistics_detail=None, business_params=None,
                     receiver_address_info=None):
        """
        统一收单交易创建接口
        """
        return self.post()

    @isp_args
    def trade_pay(self, out_trade_no, scene, auth_code, subject,
                  product_code=None, buyer_id=None, seller_id=None,
                  total_amount=None, trans_currency=None, settle_currency=None,
                  discountable_amount=None, body=None, goods_detail=None,
                  operator_id=None, store_id=None, terminal_id=None,
                  extend_params=None, timeout_express=None, auth_confirm_mode=None,
                  terminal_params=None, promo_params=None, advance_payment_type=None):
        """
        统一收单交易支付接口
        参数：
            out_trade_no: string 商户订单号 64个字符以内
            scene： string 支付场景 (bar_code,wave_code) 32 
            auth_code: string 支付授权码 32 
            subject: string 订单标题 32
            product_code: string 产品码 32
            buyer_id: string 买家支付宝id 28
            seller_id: string 卖家支付宝id 28
            total_amount: float 订单总金额 11 
            trans_currency: string 币种
            settle_currency: string 商户结算币种
            discountable_amount：float 参与优惠计算的金额，单位为元，精确到小数点后两位
            body: string 订单描述
            goods_detail: list 订单包含的商品列表信息，json格式
            operator_id: string 商户操作员编号
            store_id: string 商户门店编号
            terminal_id: string 商户机具终端编号
            extend_params: dict 业务扩展参数
            timeout_express: string 该笔订单允许的最晚付款时间，逾期将关闭交易。
            auth_confirm_mode: string 预授权确认模式，授权转交易请求中传入，适用于预授权转交易业务使用，目前只支持PRE_AUTH(预授权产品码)
            terminal_params: 商户传入终端设备相关信息，具体值要和支付宝约定
            promo_params: 优惠明细参数，通过此属性补充营销参数
            advance_payment_type: 支付模式类型,若值为ENJOY_PAY_V2表示当前交易允许走先享后付2.0垫资
        """
        return self.post()

    @isp_args
    def trade_close(self, trade_no=None, out_trade_no=None, operator_id=None):
        """
        统一收单交易关闭接口
        参数：
            trade_no： string 64 该交易在支付宝系统中的交易流水号
            out_trade_no: string 64 订单支付时传入的商户订单号,和支付宝交易号不能同时为空
            operator_id: 卖家端自定义的的操作员 ID
        """
        if not trade_no and not out_trade_no:
            raise Exception("交易流水号和商户订单号不能同时为空")
        return self.post()

    @isp_args
    def trade_query(self, out_trade_no=None, trade_no=None, org_pid=None, query_options=None):
        """
        统一收单线下交易查询
        参数：
            out_trade_no：string 订单支付时传入的商户订单号,和支付宝交易号不能同时为空。
            trade_no：string 支付宝交易号，和商户订单号不能同时为空
            org_pid：string 银行间联模式下有用，其它场景请不要使用
            query_options： string 查询选项，商户通过上送该字段来定制查询返回信息
        """
        if not trade_no and not out_trade_no:
            raise Exception("交易流水号和商户订单号不能同时为空")
        return self.post()
