from okx.app import OkxSWAP
from okx.app.utils import eprint
# 永续合约行情不需要秘钥

# 使用http和https代理，proxies={'http':'xxxxx','https:':'xxxxx'}，与requests中的proxies参数规则相同
proxies = {}
# 转发：需搭建转发服务器，可参考：https://github.com/pyted/okx_resender
proxy_host = None

# okxSPOT.market 等同于 marketSPOT
okxSWAP = OkxSWAP(
    key=key, secret=secret, passphrase=passphrase, proxies=proxies, proxy_host=proxy_host,
)
market = okxSWAP.market
# 如果有挂单或持仓，会提示“设置持仓方式为双向持仓失败”，如果你的持仓模式已经是双向持仓，可以忽略这个警告ticker_result = market.get_ticker(instId='BTC-USDT-SWAP')
ticker_result = market.get_ticker(instId='BTC-USDT-SWAP')
eprint(ticker_result)