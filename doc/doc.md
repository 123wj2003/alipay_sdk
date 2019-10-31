# 支付宝SDK 文档

## 签名方式

支付宝支持的两种验签方式RSA和RSA2

### RSA

普通公钥，不需要证书， 只需要AppId和Private Key即可。

### RSA2 

公钥证书方式，需要用户上传CSR文件生成商户公钥证书和应用私钥，具体参看[官方文档](https://docs.open.alipay.com/291/105971)

