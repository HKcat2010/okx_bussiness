from okx.app import OkxSWAP
from okx.app.utils import eprint
import pandas as pd
import time
import kdj

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
local_time = time.localtime(timestamp)
local_time_str = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
print(f"本地时间: {local_time_str}")
candle = market.update_history_candle(
    instId='BTC-USDT',
    length=50,  # 保留数量
    end=local_time_str,  # end默认为本地计算机时间戳
    bar='15m',
)['data']
df = market.candle_to_df(candle)
print(df.head(1))
candle_arr = df.to_dict()
close_price = candle_arr['c']
high_price = candle_arr['h']
low_price = candle_arr['l']
kdj_data = pd.DataFrame({
    'high': high_price,
    'low': low_price,
    'close': close_price
})
kdj_result = kdj.calculate_kdj(kdj_data, n=9, m1=3, m2=3)
kdj_result['ts'] = candle_arr['ts']
pd.set_option('display.max_rows', None)  # 显示所有行
print(kdj_result)

