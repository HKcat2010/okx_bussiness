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
ticker_result = market.get_ticker(instId='BTC-USDT-SWAP')
eprint(ticker_result)