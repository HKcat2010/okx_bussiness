from okx.app import OkxSWAP
from okx.app.utils import eprint
import time 

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
#history_candle_latest = market.get_history_candle_latest(
#    instId='BTC-USDT-SWAP',
#    length=10,
#    bar='1m'
#)
timestamp = time.time()
local_start_time = time.localtime(timestamp)
local_end_time = time.localtime(timestamp-10)
local_start_time_str = time.strftime('%Y-%m-%d %H:%M:%S', local_start_time)
local_end_time_str = time.strftime('%Y-%m-%d %H:%M:%S', local_end_time)
print(f"本地时间: {local_start_time_str} => {local_end_time_str}")
candle = market.get_history_candle(
    instId='BTC-USDT-SWAP',
    start=local_start_time_str,
    end=local_end_time_str,
    bar='1m',
)['data']
df = market.candle_to_df(candle)
print(df.head())